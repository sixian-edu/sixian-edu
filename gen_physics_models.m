% gen_physics_models.m
% Generate physics model SVGs using precise MATLAB computation
% Each model saved as separate SVG file in gen_svg_out/

function gen_physics_models()
    out = fullfile(fileparts(mfilename('fullpath')), 'gen_svg_out');
    if ~exist(out, 'dir'), mkdir(out); end

    W = 480; H = 300;
    models = {
        @()model_free_body(out, W, H);       % 1
        @()model_lever(out, W, H);            % 2
        @()model_pulley(out, W, H);           % 3
        @()model_buoyancy(out, W, H);         % 4
        @()model_reflection(out, W, H);       % 5
        @()model_refraction(out, W, H);       % 6
        @()model_lens(out, W, H);             % 7
        @()model_motion_graph(out, W, H);     % 8
        @()model_melting_curve(out, W, H);    % 9
        @()model_boiling_curve(out, W, H);    % 10
        @()model_ohm_graph(out, W, H);        % 11
        @()model_force_decomp(out, W, H);     % 12
    };
    names = {
        'phy_01_free_body.svg';
        'phy_02_lever.svg';
        'phy_03_pulley.svg';
        'phy_04_buoyancy.svg';
        'phy_05_reflection.svg';
        'phy_06_refraction.svg';
        'phy_07_lens.svg';
        'phy_08_motion_graph.svg';
        'phy_09_melting_curve.svg';
        'phy_10_boiling_curve.svg';
        'phy_11_ohm_graph.svg';
        'phy_12_force_decomp.svg';
    };

    for i = 1:numel(models)
        fprintf('Generating %s ... ', names{i});
        models{i}();
        fprintf('OK\n');
    end
    fprintf('All %d physics models generated in %s\n', numel(models), out);
end

%% ===================== Helper =====================
function [fig, ax] = setup_fig(W, H)
    fig = figure('Visible', 'off', 'Position', [0, 0, W, H], 'Color', 'none');
    set(fig, 'PaperPositionMode', 'auto');
    ax = axes('Position', [0, 0, 1, 1]);
    axis off; axis equal; hold on;
    xlim([0, W]); ylim([0, H]);
end

function save_svg(fig, filename)
    print(fig, '-dsvg', '-painters', filename);
    close(fig);
end

function h = draw_line(ax, x1, y1, x2, y2, color, style, width)
    if nargin < 6, color = '#333333'; end
    if nargin < 7, style = '-'; end
    if nargin < 8, width = 1.5; end
    h = plot(ax, [x1, x2], [y1, y2], style, 'Color', color, 'LineWidth', width);
end

function h = draw_dashed(ax, x1, y1, x2, y2, color)
    h = draw_line(ax, x1, y1, x2, y2, color, '--', 1.5);
end

function draw_arrow(ax, x1, y1, x2, y2, color, width)
    % Draw line with arrowhead at (x2,y2)
    if nargin < 7, width = 2; end
    draw_line(ax, x1, y1, x2, y2, color, '-', width);
    % Arrowhead
    ang = atan2(y2-y1, x2-x1);
    hs = 10; ha = pi/6;
    head_x = [x2, x2 - hs*cos(ang-ha), x2 - hs*cos(ang+ha)];
    head_y = [y2, y2 - hs*sin(ang-ha), y2 - hs*sin(ang+ha)];
    c = hex2rgb(color);
    fill(ax, head_x, head_y, c, 'EdgeColor', 'none');
end

function draw_point(ax, x, y, color, radius)
    if nargin < 5, radius = 3; end
    if nargin < 4, color = '#333333'; end
    plot(ax, x, y, 'o', 'MarkerSize', radius*2, ...
        'MarkerFaceColor', color, 'MarkerEdgeColor', 'none');
end

function draw_label(ax, x, y, txt, color, sz)
    if nargin < 6, sz = 14; end
    if nargin < 5, color = '#333333'; end
    text(ax, x, y, txt, 'FontSize', sz, 'Color', color, ...
        'FontName', 'sans-serif', 'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle');
end

function draw_right_angle_mark(ax, x, y, size, color)
    if nargin < 5, color = '#e74c3c'; end
    plot(ax, [x, x+size, x+size], [y, y, y-size], 'Color', color, 'LineWidth', 1.5);
end

function draw_arc(ax, cx, cy, r, theta1, theta2, color)
    if nargin < 7, color = '#e74c3c'; end
    th = linspace(theta1, theta2, 50);
    plot(ax, cx + r*cos(th), cy + r*sin(th), 'Color', color, 'LineWidth', 1.5);
end

function draw_double_arrow(ax, x1, y1, x2, y2, color, label, side)
    % Draw dimension line with arrows at both ends
    if nargin < 7, label = ''; end
    if nargin < 8, side = 'right'; end
    draw_line(ax, x1, y1, x2, y2, color, '-', 1);
    % Arrowheads
    ang = atan2(y2-y1, x2-x1);
    hs = 6; ha = pi/6;
    for dir = [0, 1]
        if dir == 0
            px = x1; py = y1; s = 1;
        else
            px = x2; py = y2; s = -1;
        end
        head_x = [px, px + s*hs*cos(ang-ha), px + s*hs*cos(ang+ha)];
        head_y = [py, py + s*hs*sin(ang-ha), py + s*hs*sin(ang+ha)];
        fill(head_x, head_y, hex2rgb(color), 'EdgeColor', 'none');
    end
    if ~isempty(label)
        mid = (x1+x2)/2; midy = (y1+y2)/2;
        if strcmp(side, 'right')
            off = 16;
            draw_label(ax, mid + off*cos(ang+pi/2), midy + off*sin(ang+pi/2), label, color, 12);
        else
            off = 16;
            draw_label(ax, mid - off*cos(ang+pi/2), midy - off*sin(ang+pi/2), label, color, 12);
        end
    end
end

%% ===================== Model 01: 受力分析 =====================
function model_free_body(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Block on horizontal surface with forces
    % Box centered in figure
    bx = W/2; by = H/2;
    bw = 80; bh = 60;

    % Surface line
    draw_line(ax, 30, by-bh/2, W-30, by-bh/2, '#999999', '-', 1.5);

    % Block (rectangle)
    rx = bx - bw/2; ry = by - bh/2;
    plot(ax, [rx, rx+bw, rx+bw, rx, rx], [ry, ry, ry+bh, ry+bh, ry], ...
        'Color', '#333333', 'LineWidth', 2);
    % Light fill
    hf = fill([rx, rx+bw, rx+bw, rx], [ry, ry, ry+bh, ry+bh], [0.95, 0.97, 1]);
    set(hf, 'EdgeColor', 'none', 'FaceAlpha', 0.5);

    % Gravity G (down from center)
    draw_arrow(ax, bx, by, bx, by+90, '#e74c3c', 2.5);
    draw_label(ax, bx+18, by+55, 'G = mg', '#e74c3c');

    % Support N (up from center)
    draw_arrow(ax, bx, by, bx, by-90, '#2ecc71', 2.5);
    draw_label(ax, bx+18, by-55, 'N', '#2ecc71');

    % Applied force F (right from center)
    draw_arrow(ax, bx, by, bx+100, by, '#3498db', 2.5);
    draw_label(ax, bx+65, by-15, 'F', '#3498db');

    % Friction f (left from bottom)
    draw_arrow(ax, bx, by+10, bx-80, by+10, '#e67e22', 2.5);
    draw_label(ax, bx-50, by+25, 'f', '#e67e22');

    % Title
    draw_label(ax, W/2, H-18, '受力分析（水平面）', '#333333', 14);

    fname = fullfile(out, 'phy_01_free_body.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 02: 杠杆平衡 =====================
function model_lever(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Lever: seesaw with fulcrum, force F₁ on left, F₂ on right
    cx = W/2; cy = H/2;

    % Lever bar (thick line)
    L = 160;
    x1 = cx - L; x2 = cx + L;
    y_bar = cy + 20;
    draw_line(ax, x1, y_bar, x2, y_bar, '#333333', '-', 4);

    % Fulcrum (triangle)
    tri_h = 20; tri_w = 14;
    fill(ax, [cx, cx-tri_w/2, cx+tri_w/2], [y_bar, y_bar-tri_h, y_bar-tri_h], ...
        [0.4, 0.4, 0.4], 'EdgeColor', 'none');
    % Ground line below fulcrum
    draw_line(ax, cx-30, y_bar-tri_h, cx+30, y_bar-tri_h, '#666666', '-', 1.5);

    % Force F₁ down on left (at L₁ from fulcrum, smaller force since longer arm)
    L1 = 100;
    f1_x = cx - L1;
    draw_arrow(ax, f1_x, y_bar, f1_x, y_bar+50, '#e74c3c', 2.5);
    draw_label(ax, f1_x-16, y_bar+30, 'F₁', '#e74c3c', 13);

    % Force F₂ down on right (at L₂ from fulcrum, larger force since shorter arm)
    L2 = 60;
    f2_x = cx + L2;
    draw_arrow(ax, f2_x, y_bar, f2_x, y_bar+70, '#2ecc71', 2.5);
    draw_label(ax, f2_x+16, y_bar+45, 'F₂', '#2ecc71', 13);

    % Dimension lines for L₁ and L₂
    dim_y = y_bar + 90;
    draw_double_arrow(ax, cx, dim_y, cx-L1, dim_y, '#999999', 'L₁', 'above');
    draw_double_arrow(ax, cx, dim_y-18, cx+L2, dim_y-18, '#999999', 'L₂', 'above');

    % Formula
    draw_label(ax, W/2, dim_y+30, 'F₁ · L₁ = F₂ · L₂', '#e74c3c', 15);

    fname = fullfile(out, 'phy_02_lever.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 03: 滑轮组 =====================
function model_pulley(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Simple pulley system with 2 fixed + 1 moving pulley
    % Wall on left
    wall_x = 60;
    draw_line(ax, wall_x, 20, wall_x, H-20, '#666666', '-', 3);
    % Wall hatching
    for y = 30:20:H-30
        draw_line(ax, wall_x-8, y, wall_x, y-6, '#999999', '-', 0.5);
    end

    % Fixed pulley at top
    cx1 = 140; cy1 = 60; r1 = 20;
    th = linspace(0, 2*pi, 40);
    plot(ax, cx1 + r1*cos(th), cy1 + r1*sin(th), 'Color', '#333333', 'LineWidth', 2);
    draw_point(ax, cx1, cy1, '#333333', 2);
    % Connect to wall
    draw_line(ax, wall_x, cy1, cx1-r1, cy1, '#333333', '-', 2);

    % Moving pulley (lower)
    cx2 = 140; cy2 = 180; r2 = 20;
    plot(ax, cx2 + r2*cos(th), cx2 + r2*sin(th), 'Color', '#333333', 'LineWidth', 2);
    draw_point(ax, cx2, cy2, '#333333', 2);

    % Rope: from fixed pulley left side, down around moving pulley, up to fixed
    draw_line(ax, cx1-r1, cy1, cx2-r2, cy2+r2, '#8B4513', '-', 1.5);
    draw_line(ax, cx2+r2, cy2, cx1+r1, cy1, '#8B4513', '-', 1.5);

    % Rope from moving pulley down to load
    draw_line(ax, cx2+r2, cy2, cx2+r2, cy2+40, '#8B4513', '-', 1.5);

    % Load (box)
    lx = cx2+r2 - 20; ly = cy2+40;
    plot(ax, [lx, lx+40, lx+40, lx, lx], [ly, ly, ly+25, ly+25, ly], ...
        'Color', '#333333', 'LineWidth', 2);
    draw_label(ax, cx2+r2, ly+13, 'G', '#e74c3c', 12);

    % Force F pulling down on rope
    draw_arrow(ax, cx1+r1, cy1-r1, cx1+r1, cy1-r1-50, '#3498db', 2.5);
    draw_label(ax, cx1+r1+18, cy1-r1-25, 'F', '#3498db', 13);

    % Annotation
    draw_label(ax, cx2, cy2-r2-18, '动滑轮', '#333333', 11);
    draw_label(ax, cx1, cy1+r1+15, '定滑轮', '#333333', 11);

    fname = fullfile(out, 'phy_03_pulley.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 04: 浮力模型 =====================
function model_buoyancy(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Object submerged in liquid, showing buoyancy forces

    % Container
    cx = W/2; cy = H/2;
    % Container width/height
    cw = 160; ch = 180;
    lx = cx - cw/2; ly = cy - ch/2;

    % Container walls
    draw_line(ax, lx, ly+ch, lx, ly-10, '#666666', '-', 2.5);
    draw_line(ax, lx+20, ly-10, lx+cw-20, ly-10, '#666666', '-', 2.5);
    draw_line(ax, lx+cw, ly+ch, lx+cw, ly-10, '#666666', '-', 2.5);
    draw_line(ax, lx, ly+ch, lx+cw, ly+ch, '#666666', '-', 2.5);

    % Liquid surface (wave line)
    liq_y = ly + 40;
    draw_line(ax, lx+2, liq_y, lx+cw-2, liq_y, '#3498db', '-', 2);

    % Liquid fill (light blue)
    hf = fill([lx+2, lx+cw-2, lx+cw-2, lx+2], [liq_y, liq_y, ly+ch-2, ly+ch-2], ...
        [0.8, 0.9, 1]);
    set(hf, 'EdgeColor', 'none', 'FaceAlpha', 0.3);

    % Submerged block
    bw = 50; bh = 40;
    bx = cx; by = (liq_y + ly+ch)/2 - bh/2 + 10;
    rx = bx - bw/2; ry = by - bh/2;
    plot(ax, [rx, rx+bw, rx+bw, rx, rx], [ry, ry, ry+bh, ry+bh, ry], ...
        'Color', '#333333', 'LineWidth', 2);
    hf2 = fill([rx, rx+bw, rx+bw, rx], [ry, ry, ry+bh, ry+bh], [0.95, 0.95, 0.95]);
    set(hf2, 'EdgeColor', 'none', 'FaceAlpha', 0.6);

    % Gravity G (down from center of block)
    draw_arrow(ax, bx, by+bh/2, bx, by+bh/2+60, '#e74c3c', 2.5);
    draw_label(ax, bx+18, by+bh/2+35, 'G', '#e74c3c');

    % Buoyancy F浮 (up from center of block)
    draw_arrow(ax, bx, by+bh/2, bx, by+bh/2-60, '#2ecc71', 2.5);
    draw_label(ax, bx+18, by+bh/2-35, 'F浮', '#2ecc71');

    % Liquid label
    draw_label(ax, lx+cw/2, ly+ch-12, '液体（ρ液）', '#888888', 12);

    % Formula
    draw_label(ax, W/2, 20, 'F浮 = ρ液 g V排', '#e74c3c', 15);

    fname = fullfile(out, 'phy_04_buoyancy.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 05: 光的反射 =====================
function model_reflection(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Reflection: incident ray → mirror, reflected ray off
    cx = W/2; cy = H/2 + 20;

    % Mirror (horizontal thick line)
    draw_line(ax, 40, cy, W-40, cy, '#999999', '-', 4);
    % Mirror hatching (short diagonal lines below)
    for x = 60:20:W-60
        plot(ax, x, cy, x+6, cy+8, 'Color', '#999999', 'LineWidth', 0.8);
    end

    % Normal line (dashed, vertical)
    draw_dashed(ax, cx, cy-30, cx, cy+30, '#888888');

    % Incident ray (from upper-left to O)
    ang_i = -30 * pi/180;  % 30° from normal
    len = 120;
    ix = cx + len * sin(ang_i);
    iy = cy + len * cos(ang_i);  % going up
    draw_arrow(ax, ix, iy, cx, cy, '#e74c3c', 2.5);
    draw_label(ax, ix-18, iy+12, '入射光线', '#e74c3c', 12);

    % Reflected ray (to upper-right)
    ang_r = ang_i;  % angle of reflection = angle of incidence
    rx = cx + len * sin(-ang_i);  % mirror side (positive angle)
    ry = cy + len * cos(ang_i);
    draw_line(ax, cx, cy, rx, ry, '#2ecc71', '-', 2.5);

    % Arrowhead for reflected ray
    ang_draw = atan2(ry-cy, rx-cx);
    hs = 10; ha = pi/6;
    head_x = [rx, rx - hs*cos(ang_draw-ha), rx - hs*cos(ang_draw+ha)];
    head_y = [ry, ry - hs*sin(ang_draw-ha), ry - hs*sin(ang_draw+ha)];
    c_green = hex2rgb('#2ecc71');
    fill(ax, head_x, head_y, c_green, 'EdgeColor', 'none');
    draw_label(ax, rx+18, ry+12, '反射光线', '#2ecc71', 12);

    % Angle arcs
    ar = 30;
    draw_arc(ax, cx, cy, ar, -pi/2+ang_i, -pi/2, '#e74c3c');
    draw_arc(ax, cx, cy, ar, -pi/2, -pi/2-ang_i, '#2ecc71');

    % Angle labels
    draw_label(ax, cx+ar*cos(-pi/2+ang_i/2)+10, cy+ar*sin(-pi/2+ang_i/2), 'θ₁', '#e74c3c', 12);
    draw_label(ax, cx+ar*cos(-pi/2-ang_i/2)-10, cy+ar*sin(-pi/2-ang_i/2), 'θ₂', '#2ecc71', 12);

    % Law label
    draw_label(ax, W/2, 20, '反射定律：θ₁ = θ₂', '#333333', 15);

    fname = fullfile(out, 'phy_05_reflection.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 06: 光的折射 =====================
function model_refraction(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Refraction: light entering water from air
    cx = W/2; cy = H/2;

    % Interface (water surface)
    draw_line(ax, 40, cy, W-40, cy, '#3498db', '-', 2.5);

    % Air label (above)
    draw_label(ax, W-30, cy-20, '空气', '#888888', 12);
    % Water label (below)
    draw_label(ax, W-30, cy+20, '水', '#3498db', 12);

    % Normal (dashed, vertical)
    draw_dashed(ax, cx, cy-90, cx, cy+80, '#888888');

    % Incident ray (from upper-left)
    ang_i = 40 * pi/180;  % 40° from normal
    len1 = 100;
    ix = cx - len1 * sin(ang_i);
    iy = cy - len1 * cos(ang_i);
    draw_arrow(ax, ix, iy, cx, cy, '#e74c3c', 2.5);

    % Refracted ray (bent toward normal, in water)
    ang_r = 28 * pi/180;  % refraction angle < incident (water is denser)
    len2 = 120;
    rx = cx + len2 * sin(ang_r);
    ry = cy + len2 * cos(ang_r);
    draw_line(ax, cx, cy, rx, ry, '#2ecc71', '-', 2.5);
    % Arrowhead for refracted
    ang_draw = atan2(ry-cy, rx-cx);
    hs = 10; ha = pi/6;
    head_x = [rx, rx - hs*cos(ang_draw-ha), rx - hs*cos(ang_draw+ha)];
    head_y = [ry, ry - hs*sin(ang_draw-ha), ry - hs*sin(ang_draw+ha)];
    c_green = hex2rgb('#2ecc71');
    fill(ax, head_x, head_y, c_green, 'EdgeColor', 'none');

    % Angle arcs
    ar = 30;
    draw_arc(ax, cx, cy, ar, -pi/2, -pi/2+ang_i, '#e74c3c');
    draw_arc(ax, cx, cy, ar, -pi/2, -pi/2-ang_r, '#2ecc71');

    % Labels
    draw_label(ax, cx+ar*cos(-pi/2+ang_i/2)-16, cy+ar*sin(-pi/2+ang_i/2), '入射角', '#e74c3c', 11);
    draw_label(ax, cx+ar*cos(-pi/2-ang_r/2)+18, cy+ar*sin(-pi/2-ang_r/2), '折射角', '#2ecc71', 11);

    fname = fullfile(out, 'phy_06_refraction.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 07: 凸透镜成像 =====================
function model_lens(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Convex lens ray diagram showing imaging
    cx = W/2; cy = H/2;

    % Principal axis (horizontal line)
    draw_line(ax, 30, cy, W-30, cy, '#999999', '-', 1);

    % Convex lens (double arc)
    lens_h = 100;
    % Draw as two arcs meeting at center
    th_l = linspace(-pi/2, pi/2, 30);
    r_lens = 120;
    lens_x = cx + (r_lens - sqrt(r_lens^2 - (lens_h/2)^2));
    plot(ax, cx + lens_x*cos(th_l), cy + (lens_h/2)*sin(th_l), ...
        'Color', '#333333', 'LineWidth', 2.5);
    % Actually simpler: draw a lens symbol
    % Two facing parentheses
    x_l = cx - 8; x_r = cx + 8;
    y_t = cy - lens_h/2; y_b = cy + lens_h/2;
    plot(ax, [x_l, x_l], [y_t, y_b], 'Color', '#333333', 'LineWidth', 2.5);
    % Arrow heads on lens (convex symbol)
    draw_line(ax, x_l, y_t, x_l+8, cy, '#333333', '-', 1.5);
    draw_line(ax, x_l, y_b, x_l+8, cy, '#333333', '-', 1.5);

    % Focal points (both sides)
    f = 60;
    draw_point(ax, cx-f, cy, '#e74c3c', 4);
    draw_point(ax, cx+f, cy, '#e74c3c', 4);
    draw_label(ax, cx-f, cy+18, 'F', '#e74c3c', 12);
    draw_label(ax, cx+f, cy+18, 'F', '#e74c3c', 12);
    % 2F points
    draw_point(ax, cx-2*f, cy, '#888888', 3);
    draw_point(ax, cx+2*f, cy, '#888888', 3);
    draw_label(ax, cx-2*f, cy+18, '2F', '#888888', 11);
    draw_label(ax, cx+2*f, cy+18, '2F', '#888888', 11);

    % Object (arrow pointing up, placed at u > 2f)
    obj_x = cx - 2*f - 20;
    obj_h = 40;
    draw_arrow(ax, obj_x, cy, obj_x, cy+obj_h, '#e74c3c', 2.5);
    draw_label(ax, obj_x-12, cy+obj_h/2, '物体', '#e74c3c', 11);

    % Image (real, inverted, between F and 2F)
    % For u = 2f+20, 1/f = 1/u + 1/v → v = uf/(u-f)
    u = 2*f + 20;
    v = u*f / (u - f);
    img_h = obj_h * v / u;
    img_x = cx + v;
    draw_arrow(ax, img_x, cy, img_x, cy-img_h, '#2ecc71', 2.5);
    draw_label(ax, img_x+12, cy-img_h/2, '实像', '#2ecc71', 11);

    % Rays from object top
    obj_top_y = cy + obj_h;
    % Ray 1: parallel to axis → through F after lens
    draw_line(ax, obj_x, obj_top_y, cx, obj_top_y, '#999999', '-', 1);
    draw_line(ax, cx, obj_top_y, cx+r_lens, cy-img_h, '#999999', '-', 1);
    % Small arrow
    ang_draw = atan2(cy-img_h-obj_top_y, cx+r_lens-cx);
    hs = 8; ha = pi/6;
    head_x = [cx+r_lens, cx+r_lens - hs*cos(ang_draw-ha), cx+r_lens - hs*cos(ang_draw+ha)];
    head_y = [cy-img_h, cy-img_h - hs*sin(ang_draw-ha), cy-img_h - hs*sin(ang_draw+ha)];
    c_gray = hex2rgb('#999999');
    fill(ax, head_x, head_y, c_gray, 'EdgeColor', 'none');

    % Ray 2: through center of lens (straight)
    draw_line(ax, obj_x, obj_top_y, img_x, cy-img_h, '#888888', '-', 1);

    fname = fullfile(out, 'phy_07_lens.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 08: 速度图像（运动模型） =====================
function model_motion_graph(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Speed-time graph for motion models

    % Draw coordinate axes
    margin = 50;
    ax_w = W - 2*margin;
    ax_h = H - 2*margin;
    ox = margin; oy = margin + ax_h;

    % Axes
    draw_arrow(ax, ox, oy, ox+ax_w, oy, '#333333', 1.5);
    draw_arrow(ax, ox, oy, ox, oy-ax_h, '#333333', 1.5);

    % Labels
    draw_label(ax, ox+ax_w+10, oy, 't', '#333333', 13);
    draw_label(ax, ox-10, oy-ax_h-5, 'v', '#333333', 13);
    draw_label(ax, ox-12, oy+12, 'O', '#333333', 11);

    % Tick marks
    for t = 1:4
        tx = ox + t*(ax_w/5);
        plot(ax, [tx, tx], [oy, oy+4], 'Color', '#333333', 'LineWidth', 1);
    end
    for v = 1:4
        vy = oy - v*(ax_h/5);
        plot(ax, [ox, ox+4], [vy, vy], 'Color', '#333333', 'LineWidth', 1);
    end

    % Line 1: uniform motion (constant v)
    v_uniform = oy - ax_h*0.45;
    draw_line(ax, ox+ax_w*0.05, v_uniform, ox+ax_w*0.85, v_uniform, '#3498db', '-', 2.5);
    draw_label(ax, ox+ax_w*0.92, v_uniform, '匀速', '#3498db', 11);

    % Line 2: accelerated motion (increasing v)
    x1 = ox + ax_w*0.10; y1 = oy;
    x2 = ox + ax_w*0.65; y2 = oy - ax_h*0.6;
    draw_line(ax, x1, y1, x2, y2, '#e74c3c', '-', 2.5);
    draw_label(ax, x2+5, y2+4, '加速', '#e74c3c', 11);

    % Line 3: decelerated motion (decreasing v)
    x3 = ox + ax_w*0.15; y3 = oy - ax_h*0.6;
    x4 = ox + ax_w*0.70; y4 = oy;
    draw_line(ax, x3, y3, x4, y4, '#2ecc71', '-', 2.5);
    draw_label(ax, x4+5, y4-4, '减速', '#2ecc71', 11);

    fname = fullfile(out, 'phy_08_motion_graph.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 09: 晶体熔化曲线 =====================
function model_melting_curve(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Crystal melting: temperature vs time
    % Three segments: solid heating → melting (plateau) → liquid heating
    margin = 55;
    ox = margin; oy = H - margin;
    ax_w = W - 2*margin;
    ax_h = H - 2*margin - 10;

    % Axes
    draw_arrow(ax, ox, oy, ox+ax_w, oy, '#333333', 1.5);
    draw_arrow(ax, ox, oy, ox, oy-ax_h, '#333333', 1.5);

    % Labels
    draw_label(ax, ox+ax_w+10, oy, '时间/min', '#333333', 12);
    draw_label(ax, ox-10, oy-ax_h-5, '温度/℃', '#333333', 12);
    draw_label(ax, ox-10, oy+12, 'O', '#333333', 11);

    % Segment 1: solid heating (sloped up)
    s1 = [ox+15, oy-15];
    s2 = [ox+ax_w*0.30, oy-ax_h*0.40];
    draw_line(ax, s1(1), s1(2), s2(1), s2(2), '#e74c3c', '-', 2.5);

    % Segment 2: melting plateau (horizontal)
    s3 = [ox+ax_w*0.55, oy-ax_h*0.40];
    draw_line(ax, s2(1), s2(2), s3(1), s3(2), '#e74c3c', '-', 2.5);

    % Segment 3: liquid heating (sloped up)
    s4 = [ox+ax_w*0.85, oy-ax_h*0.83];
    draw_line(ax, s3(1), s3(2), s4(1), s4(2), '#e74c3c', '-', 2.5);

    % Melting point dashed line
    mp_y = oy - ax_h*0.40;
    draw_dashed(ax, ox+5, mp_y, ox+ax_w*0.6, mp_y, '#888888');
    draw_label(ax, ox-14, mp_y, '熔点', '#888888', 11);

    % Region labels
    draw_label(ax, ox+ax_w*0.14, oy-20, '固态', '#e74c3c', 11);
    draw_label(ax, (s2(1)+s3(1))/2, mp_y-14, '熔化', '#e74c3c', 11);
    draw_label(ax, ox+ax_w*0.70, oy-20, '液态', '#e74c3c', 11);

    fname = fullfile(out, 'phy_09_melting_curve.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 10: 水的沸腾曲线 =====================
function model_boiling_curve(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Water boiling: temperature vs time, plateau at 100°C
    margin = 55;
    ox = margin; oy = H - margin;
    ax_w = W - 2*margin;
    ax_h = H - 2*margin - 10;

    % Axes
    draw_arrow(ax, ox, oy, ox+ax_w, oy, '#333333', 1.5);
    draw_arrow(ax, ox, oy, ox, oy-ax_h, '#333333', 1.5);

    % Labels
    draw_label(ax, ox+ax_w+10, oy, '时间/min', '#333333', 12);
    draw_label(ax, ox-10, oy-ax_h-5, '温度/℃', '#333333', 12);
    draw_label(ax, ox-10, oy+12, 'O', '#333333', 11);

    % Segment 1: heating (sloped up)
    s1 = [ox+15, oy-15];
    s2 = [ox+ax_w*0.35, oy-ax_h*0.70];
    draw_line(ax, s1(1), s1(2), s2(1), s2(2), '#3498db', '-', 2.5);

    % Segment 2: boiling plateau (horizontal, at 100°C)
    bp_y = oy - ax_h*0.70;
    s3 = [ox+ax_w*0.85, bp_y];
    draw_line(ax, s2(1), s2(2), s3(1), s3(2), '#3498db', '-', 2.5);

    % 100°C dashed line
    draw_dashed(ax, ox+5, bp_y, ox+ax_w*0.9, bp_y, '#888888');
    draw_label(ax, ox-14, bp_y, '100℃', '#e74c3c', 11);

    % Labels
    draw_label(ax, ox+ax_w*0.15, oy-20, '加热', '#3498db', 11);
    draw_label(ax, (s2(1)+s3(1))/2, bp_y-15, '沸腾', '#e74c3c', 11);

    fname = fullfile(out, 'phy_10_boiling_curve.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 11: 欧姆定律 I-U 图像 =====================
function model_ohm_graph(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Ohm's law: I = U/R, three resistors with different slopes
    margin = 55;
    ox = margin; oy = H - margin;
    ax_w = W - 2*margin;
    ax_h = H - 2*margin - 10;

    % Axes
    draw_arrow(ax, ox, oy, ox+ax_w, oy, '#333333', 1.5);
    draw_arrow(ax, ox, oy, ox, oy-ax_h, '#333333', 1.5);

    % Labels
    draw_label(ax, ox+ax_w+10, oy, 'U/V', '#333333', 12);
    draw_label(ax, ox-10, oy-ax_h-5, 'I/A', '#333333', 12);
    draw_label(ax, ox-10, oy+12, 'O', '#333333', 11);

    scale = ax_h / 2.5;  % current scaling (A per pixel)
    Rs = [5, 10, 20];
    colors = {'#e74c3c', '#3498db', '#2ecc71'};
    labels = {'R=5Ω', 'R=10Ω', 'R=20Ω'};

    for i = 1:3
        R = Rs(i);
        x_end = ox + ax_w * 0.78;
        U_max = 8;
        I_max = U_max / R;
        y_end = oy - I_max * scale;
        draw_line(ax, ox+10, oy, x_end, y_end, colors{i}, '-', 2.5);
        draw_label(ax, x_end+8, y_end, labels{i}, colors{i}, 10);
    end

    fname = fullfile(out, 'phy_11_ohm_graph.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 12: 力的合成（平行四边形法则） =====================
function model_force_decomp(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Force composition: parallelogram law
    cx = W/2; cy = H/2;

    % Origin O
    draw_point(ax, cx, cy, '#333333', 4);

    % Force F1 (horizontal, right)
    f1_len = 110;
    f1_end = [cx+f1_len, cy];
    draw_arrow(ax, cx, cy, f1_end(1), f1_end(2), '#e74c3c', 2.5);
    draw_label(ax, f1_end(1), f1_end(2)+20, 'F₁', '#e74c3c', 13);

    % Force F2 (diagonal, up-right)
    f2_len = 80;
    f2_ang = 50 * pi/180;
    f2_end = [cx+f2_len*cos(f2_ang), cy-f2_len*sin(f2_ang)];
    draw_arrow(ax, cx, cy, f2_end(1), f2_end(2), '#3498db', 2.5);
    draw_label(ax, f2_end(1)+12, f2_end(2)-10, 'F₂', '#3498db', 13);

    % Parallelogram completion (dashed)
    f3_end = f1_end + f2_end - [cx, cy];
    draw_dashed(ax, f1_end(1), f1_end(2), f3_end(1), f3_end(2), '#999999');
    draw_dashed(ax, f2_end(1), f2_end(2), f3_end(1), f3_end(2), '#999999');

    % Resultant R (diagonal, bold)
    draw_arrow(ax, cx, cy, f3_end(1), f3_end(2), '#e67e22', 3.5);
    draw_label(ax, f3_end(1)+14, f3_end(2)-12, '合力 R', '#e67e22', 13);

    fname = fullfile(out, 'phy_12_force_decomp.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Utility =====================
function c = hex2rgb(hex)
    h = hex(2:end);
    c = [hex2dec(h(1:2)), hex2dec(h(3:4)), hex2dec(h(5:6))] / 255;
end

function clean_svg(fname)
    % Placeholder, actual cleanup done by clean_svgs.py
end
