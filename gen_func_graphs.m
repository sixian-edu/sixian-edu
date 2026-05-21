% gen_func_graphs.m
% Generate all junior-high math function graphs as SVGs

function gen_func_graphs()
    out = fullfile(fileparts(mfilename('fullpath')), 'gen_svg_out');
    if ~exist(out, 'dir'), mkdir(out); end

    W = 480; H = 300;
    models = {
        @()func_linear(out, W, H);         % 1
        @()func_proportional(out, W, H);   % 2
        @()func_inverse(out, W, H);        % 3
        @()func_quadratic(out, W, H);      % 4
        @()func_vertex(out, W, H);         % 5
        @()func_intersect(out, W, H);      % 6
        @()func_discriminant(out, W, H);   % 7
        @()func_translate(out, W, H);      % 8
        @()func_linear_k(out, W, H);       % 9
        @()func_inverse_k(out, W, H);      % 10
    };
    names = {
        'func_01_linear.svg';
        'func_02_proportional.svg';
        'func_03_inverse.svg';
        'func_04_quadratic.svg';
        'func_05_vertex.svg';
        'func_06_intersect.svg';
        'func_07_discriminant.svg';
        'func_08_translate.svg';
        'func_09_linear_k.svg';
        'func_10_inverse_k.svg';
    };

    for i = 1:numel(models)
        fprintf('Generating %s ... ', names{i});
        models{i}();
        fprintf('OK\n');
    end
    fprintf('All %d function graphs generated.\n', numel(models));
end

%% ===================== Helpers =====================
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

function draw_axes(ax, W, H)
    % Draw coordinate axes centered in figure
    cx = W/2; cy = H/2;
    % x-axis
    plot(ax, [20, W-20], [cy, cy], 'Color', '#333333', 'LineWidth', 1);
    % y-axis
    plot(ax, [cx, cx], [20, H-20], 'Color', '#333333', 'LineWidth', 1);
    % Arrows
    plot(ax, [W-25, W-20, W-25], [cy-4, cy, cy+4], 'Color', '#333333', 'LineWidth', 1);
    plot(ax, [cx-4, cx, cx+4], [25, 20, 25], 'Color', '#333333', 'LineWidth', 1);
    % Labels
    text(ax, W-18, cy-8, 'x', 'FontSize', 12, 'Color', '#333333', ...
        'FontName', 'sans-serif');
    text(ax, cx+8, 18, 'y', 'FontSize', 12, 'Color', '#333333', ...
        'FontName', 'sans-serif');
    text(ax, cx-10, cy+10, 'O', 'FontSize', 11, 'Color', '#888888', ...
        'FontName', 'sans-serif');
end

function h = draw_line(ax, x1, y1, x2, y2, color, style, width)
    if nargin < 6, color = '#333333'; end
    if nargin < 7, style = '-'; end
    if nargin < 8, width = 2; end
    h = plot(ax, [x1, x2], [y1, y2], style, 'Color', color, 'LineWidth', width);
end

function draw_func(ax, x1, x2, f, color, width)
    % Draw a function f(x) from x1 to x2
    xx = linspace(x1, x2, 200);
    yy = arrayfun(f, xx);
    plot(ax, xx, yy, 'Color', color, 'LineWidth', width);
end

function draw_dashed(ax, x1, y1, x2, y2, color)
    draw_line(ax, x1, y1, x2, y2, color, '--', 1);
end

function draw_label(ax, x, y, txt, color, sz)
    if nargin < 6, sz = 13; end
    if nargin < 5, color = '#333333'; end
    text(ax, x, y, txt, 'FontSize', sz, 'Color', color, ...
        'FontName', 'sans-serif', 'HorizontalAlignment', 'center', 'VerticalAlignment', 'middle');
end

function draw_point(ax, x, y, color, radius)
    if nargin < 5, radius = 3; end
    if nargin < 4, color = '#e74c3c'; end
    plot(ax, x, y, 'o', 'MarkerSize', radius*2, ...
        'MarkerFaceColor', color, 'MarkerEdgeColor', 'none');
end

function c = h2r(hex)
    h = hex(2:end);
    c = [hex2dec(h(1:2)), hex2dec(h(3:4)), hex2dec(h(5:6))] / 255;
end

%% ===================== 1. 一次函数综合 =====================
function func_linear(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2;
    s = 28; % pixels per math unit

    % y = 0.8x + 1 (k>0, b=1 — 不经过原点)
    x_m = linspace(-5, 5, 100);
    y1 = 0.8*x_m + 1;
    plot(ax, cx + x_m*s, cy - y1*s, 'Color', '#e74c3c', 'LineWidth', 2.5);
    draw_label(ax, cx + 4.5*s, cy - (0.8*4.5+1)*s - 14, 'y = 0.8x+1', '#e74c3c', 11);

    % y = -0.6x + 2 (k<0, b=2)
    y2 = -0.6*x_m + 2;
    plot(ax, cx + x_m*s, cy - y2*s, 'Color', '#2ecc71', 'LineWidth', 2.5);
    draw_label(ax, cx + 4.5*s, cy - (-0.6*4.5+2)*s + 16, 'y = -0.6x+2', '#2ecc71', 11);

    % 标记 y 轴截距点 (0,b) 证明 b≠0
    draw_point(ax, cx, cy - 1*s, '#e74c3c', 4);
    draw_point(ax, cx, cy - 2*s, '#2ecc71', 4);
    draw_label(ax, cx + 12, cy - 1*s + 12, 'b=1', '#e74c3c', 10);
    draw_label(ax, cx + 12, cy - 2*s + 12, 'b=2', '#2ecc71', 10);

    draw_label(ax, cx, 20, '一次函数 y = kx + b', '#333333', 14);
    fname = fullfile(out, 'func_01_linear.svg');
    save_svg(fig, fname);
end

%% ===================== 2. 正比例函数 =====================
function func_proportional(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2; s = 28;

    x_m = linspace(-5, 5, 100);

    y1 = 1.2*x_m;
    plot(ax, cx + x_m*s, cy - y1*s, 'Color', '#e74c3c', 'LineWidth', 2.5);
    draw_label(ax, cx + 5*s + 10, cy - 1.2*5*s, 'y = 1.2x', '#e74c3c', 11);

    y2 = 0.5*x_m;
    plot(ax, cx + x_m*s, cy - y2*s, 'Color', '#3498db', 'LineWidth', 2.5);
    draw_label(ax, cx + 5*s + 10, cy - 0.5*5*s, 'y = 0.5x', '#3498db', 11);

    y3 = -0.8*x_m;
    plot(ax, cx + x_m*s, cy - y3*s, 'Color', '#2ecc71', 'LineWidth', 2.5);
    draw_label(ax, cx - 5*s - 50, cy + 0.8*5*s, 'y = -0.8x', '#2ecc71', 11);

    draw_label(ax, cx, 20, '正比例函数 y = kx (k≠0)', '#333333', 14);
    fname = fullfile(out, 'func_02_proportional.svg');
    save_svg(fig, fname);
end

%% ===================== 3. 反比例函数 =====================
function func_inverse(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2; s = 25;

    % y = 6/x (k>0) — 一三象限
    x_p = linspace(0.8, 7, 200);
    x_n = linspace(-7, -0.8, 200);
    y_p = 6 ./ x_p;
    y_n = 6 ./ x_n;
    plot(ax, cx + x_p*s, cy - y_p*s, 'Color', '#e74c3c', 'LineWidth', 2.5);
    plot(ax, cx + x_n*s, cy - y_n*s, 'Color', '#e74c3c', 'LineWidth', 2.5);
    draw_label(ax, cx + 4*s + 12, cy - (6/4)*s, 'y = ⁶⁄ₓ (k>0)', '#e74c3c', 11);

    % y = -4/x (k<0) — 二四象限
    y_p2 = -4 ./ x_p;
    y_n2 = -4 ./ x_n;
    plot(ax, cx + x_p*s, cy - y_p2*s, 'Color', '#2ecc71', 'LineWidth', 2.5);
    plot(ax, cx + x_n*s, cy - y_n2*s, 'Color', '#2ecc71', 'LineWidth', 2.5);
    draw_label(ax, cx - 5*s - 60, cy + (4/5)*s, 'y = -⁴⁄ₓ (k<0)', '#2ecc71', 11);

    draw_label(ax, cx, 20, '反比例函数 y = k/x (k≠0)', '#333333', 14);
    fname = fullfile(out, 'func_03_inverse.svg');
    save_svg(fig, fname);
end

%% ===================== 4. 二次函数基础 =====================
function func_quadratic(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2; s = 16;

    x_m = linspace(-3, 3, 200);

    % y = x² (开口向上)
    y1 = x_m.^2;
    plot(ax, cx + x_m*s, cy - y1*s, 'Color', '#e74c3c', 'LineWidth', 2.5);
    draw_label(ax, cx + 2.8*s, cy - (2.8^2)*s - 14, 'y = x² (a>0)', '#e74c3c', 11);

    % y = -x² + 2 (开口向下)
    y2 = -x_m.^2 + 2;
    plot(ax, cx + x_m*s, cy - y2*s, 'Color', '#2ecc71', 'LineWidth', 2.5);
    draw_label(ax, cx - 2.8*s, cy - (-2.8^2+2)*s + 16, 'y = -x²+2 (a<0)', '#2ecc71', 11);

    draw_label(ax, cx, 20, '二次函数 y = ax²+bx+c', '#333333', 14);
    fname = fullfile(out, 'func_04_quadratic.svg');
    save_svg(fig, fname);
end

%% ===================== 5. 二次函数顶点式 =====================
function func_vertex(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2; s = 12;

    % y = (x-2)² + 3  顶点 (2,3)
    x_m = linspace(-1, 5, 200);
    y_m = (x_m-2).^2 + 3;
    plot(ax, cx + x_m*s, cy - y_m*s, 'Color', '#e74c3c', 'LineWidth', 2.5);
    draw_label(ax, cx + 4.8*s, cy - ((4.8-2)^2+3)*s - 14, 'y = (x-2)²+3', '#e74c3c', 11);

    % 标记顶点 (2,3)
    vx = cx + 2*s; vy = cy - 3*s;
    draw_point(ax, vx, vy, '#e74c3c', 5);
    draw_label(ax, vx + 16, vy - 10, '顶点 (2,3)', '#e74c3c', 11);

    % 对称轴 (虚线)
    draw_dashed(ax, vx, 20, vx, H-20, '#e74c3c');

    draw_label(ax, cx, 20, '顶点式 y = a(x-h)² + k', '#333333', 14);
    fname = fullfile(out, 'func_05_vertex.svg');
    save_svg(fig, fname);
end

%% ===================== 6. 一次函数与二次函数交点 =====================
function func_intersect(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2; s = 18;

    % 抛物线: y = x² - 2x - 3
    x_m = linspace(-2.5, 4.5, 200);
    y_q = x_m.^2 - 2*x_m - 3;
    plot(ax, cx + x_m*s, cy - y_q*s, 'Color', '#e74c3c', 'LineWidth', 2.5);
    draw_label(ax, cx + 4.3*s, cy - (4.3^2-2*4.3-3)*s - 14, 'y = x²-2x-3', '#e74c3c', 11);

    % 直线: y = x - 1
    y_l = x_m - 1;
    plot(ax, cx + x_m*s, cy - y_l*s, 'Color', '#2ecc71', 'LineWidth', 2.5);
    draw_label(ax, cx + 4.3*s, cy - (4.3-1)*s + 16, 'y = x-1', '#2ecc71', 11);

    % 交点: x²-2x-3 = x-1 → x²-3x-2=0 → x = (3±√17)/2
    x1 = (3-sqrt(17))/2; x2 = (3+sqrt(17))/2;
    y1 = x1-1; y2 = x2-1;
    draw_point(ax, cx + x1*s, cy - y1*s, '#333333', 5);
    draw_point(ax, cx + x2*s, cy - y2*s, '#333333', 5);

    draw_label(ax, cx, 18, '函数交点问题', '#333333', 14);
    fname = fullfile(out, 'func_06_intersect.svg');
    save_svg(fig, fname);
end

%% ===================== 7. 判别式与根 =====================
function func_discriminant(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2; s = 18;

    % Δ > 0: y = x² - 2x - 3 (两个交点 x=-1, x=3)
    x1 = linspace(-2, 4, 200);
    y1 = x1.^2 - 2*x1 - 3;
    plot(ax, cx + x1*s, cy - y1*s, 'Color', '#e74c3c', 'LineWidth', 2);
    draw_label(ax, cx + x1(end)*s, cy - y1(end)*s - 12, 'Δ>0 两交点', '#e74c3c', 10);

    % Δ = 0: y = x² - 4x + 4 = (x-2)² (相切)
    x2 = linspace(0, 4, 200);
    y2 = x2.^2 - 4*x2 + 4;
    plot(ax, cx + x2*s, cy - y2*s, 'Color', '#2ecc71', 'LineWidth', 2);
    draw_label(ax, cx + x2(end)*s, cy - y2(end)*s + 14, 'Δ=0 相切', '#2ecc71', 10);

    % Δ < 0: y = x² + 2x + 3 (无交点)
    x3 = linspace(-3, 1, 200);
    y3 = x3.^2 + 2*x3 + 3;
    plot(ax, cx + x3*s, cy - y3*s, 'Color', '#3498db', 'LineWidth', 2);
    draw_label(ax, cx + x3(1)*s, cy - y3(1)*s - 12, 'Δ<0 无交点', '#3498db', 10);

    draw_label(ax, cx, 18, '判别式 Δ = b²-4ac', '#333333', 14);
    fname = fullfile(out, 'func_07_discriminant.svg');
    save_svg(fig, fname);
end

%% ===================== 8. 函数图像平移 =====================
function func_translate(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2; s = 14;

    x_m = linspace(-1.5, 5.5, 200);

    % y = x² (参考线，虚线)
    y0 = x_m.^2;
    plot(ax, cx + x_m*s, cy - y0*s, 'Color', '#999999', 'LineWidth', 1.5, 'LineStyle', '--');
    draw_label(ax, cx + 4.5*s, cy - (4.5^2)*s - 14, 'y=x²', '#999999', 10);

    % y = (x-2)² + 1 (向右2，向上1)
    y1 = (x_m-2).^2 + 1;
    plot(ax, cx + x_m*s, cy - y1*s, 'Color', '#e74c3c', 'LineWidth', 2.5);
    draw_label(ax, cx + 5.2*s, cy - ((5.2-2)^2+1)*s - 14, 'y=(x-2)²+1', '#e74c3c', 11);

    % 平移箭头: 从 (0,0) → (2,1)
    ax_s = cx + 0*s; ay_s = cy - 0*s;
    ax_e = cx + 2*s; ay_e = cy - 1*s;
    draw_arrow2(ax, ax_s, ay_s, ax_e, ay_e, '#e74c3c');

    draw_label(ax, cx, 18, '二次函数图像平移', '#333333', 14);
    fname = fullfile(out, 'func_08_translate.svg');
    save_svg(fig, fname);
end

%% Arrow helper (像素坐标)
function draw_arrow2(ax, x1, y1, x2, y2, color)
    plot(ax, [x1, x2], [y1, y2], 'Color', color, 'LineWidth', 1.5);
    ang = atan2(y2-y1, x2-x1);
    hs = 8; ha = pi/6;
    c = h2r(color);
    fill(ax, [x2, x2-hs*cos(ang-ha), x2-hs*cos(ang+ha)], ...
              [y2, y2-hs*sin(ang-ha), y2-hs*sin(ang+ha)], c, 'EdgeColor', 'none');
end

%% ===================== 9. k的几何意义（一次函数） =====================
function func_linear_k(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2; s = 28;

    x_m = linspace(-5, 5, 100);
    ks = [1.5, 0.8, 0.3, -0.4, -1.2];
    colors = {'#e74c3c', '#e67e22', '#3498db', '#2ecc71', '#9b59b6'};
    labels = {'k=1.5', 'k=0.8', 'k=0.3', 'k=-0.4', 'k=-1.2'};

    for i = 1:numel(ks)
        y_m = ks(i) * x_m;
        plot(ax, cx + x_m*s, cy - y_m*s, 'Color', colors{i}, 'LineWidth', 2);
        % label 在 x=5 处
        draw_label(ax, cx + 5*s + 12, cy - ks(i)*5*s, labels{i}, colors{i}, 10);
    end

    draw_label(ax, cx, 20, 'k决定直线的倾斜程度', '#333333', 14);
    fname = fullfile(out, 'func_09_linear_k.svg');
    save_svg(fig, fname);
end

%% ===================== 10. 反比例函数k的几何意义 =====================
function func_inverse_k(out, W, H)
    [fig, ax] = setup_fig(W, H);
    draw_axes(ax, W, H);
    cx = W/2; cy = H/2; s = 25;

    x_m = linspace(0.6, 6, 200);

    % y = 4/x, y = 8/x, y = 1/x
    y4 = 4 ./ x_m;
    y8 = 8 ./ x_m;
    y1 = 1 ./ x_m;

    plot(ax, cx + x_m*s, cy - y4*s, 'Color', '#e74c3c', 'LineWidth', 2.5);
    draw_label(ax, cx + 4*s + 12, cy - (4/4)*s, 'k=4', '#e74c3c', 11);

    plot(ax, cx + x_m*s, cy - y8*s, 'Color', '#3498db', 'LineWidth', 2.5);
    draw_label(ax, cx + 3*s + 12, cy - (8/3)*s, 'k=8', '#3498db', 11);

    plot(ax, cx + x_m*s, cy - y1*s, 'Color', '#888888', 'LineWidth', 1.5, 'LineStyle', '--');
    draw_label(ax, cx + 5*s + 12, cy - (1/5)*s, 'k=1', '#888888', 10);

    % 矩形区域: y=4/x 在 x=2 处的面积 = |k| = 4
    rx = cx + 2*s; ry = cy;
    rw = (4.5-2)*s; rh = (4/2)*s;
    hf = fill([rx, rx+rw, rx+rw, rx], [ry, ry, ry-rh, ry-rh], [0.9, 0.95, 1]);
    set(hf, 'EdgeColor', [0.906, 0.298, 0.235], 'LineStyle', '--', 'FaceAlpha', 0.2);
    draw_label(ax, rx + rw/2, cy + 16, '矩形面积 = |k|', '#e74c3c', 11);

    draw_label(ax, cx, 20, '反比例函数 |k| 的几何意义', '#333333', 14);
    fname = fullfile(out, 'func_10_inverse_k.svg');
    save_svg(fig, fname);
end
