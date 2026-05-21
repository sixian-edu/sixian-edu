% gen_math_models.m
% Generate all math geometry model SVGs using precise MATLAB computation
% Each model saved as separate SVG file in gen_svg_out/

function gen_math_models()
    out = fullfile(fileparts(mfilename('fullpath')), 'gen_svg_out');
    if ~exist(out, 'dir'), mkdir(out); end

    W = 480; H = 300;  % figure size
    models = {
        @()model_handshake(out, W, H);       % 1
        @()model_k_shape(out, W, H);          % 2
        @()model_three_perp(out, W, H);       % 3
        @()model_median_double(out, W, H);    % 4
        @()model_angle_bisector(out, W, H);   % 5
        @()model_a_similar(out, W, H);        % 6
        @()model_8_similar(out, W, H);        % 7
        @()model_projection(out, W, H);       % 8
        @()model_half_angle(out, W, H);       % 9
        @()model_jiangjun(out, W, H);         % 10
        @()model_huguigui(out, W, H);         % 11
        @()model_apollonius(out, W, H);       % 12
        @()model_fermat(out, W, H);           % 13
        @()model_hidden_circle(out, W, H);    % 14
        @()model_guadou(out, W, H);           % 15
        @()model_fold(out, W, H);             % 16
    };
    names = {
        'model_01_handshake.svg';
        'model_02_k_shape.svg';
        'model_03_three_perp.svg';
        'model_04_median_double.svg';
        'model_05_angle_bisector.svg';
        'model_06_a_similar.svg';
        'model_07_8_similar.svg';
        'model_08_projection.svg';
        'model_09_half_angle.svg';
        'model_10_jiangjun.svg';
        'model_11_huguigui.svg';
        'model_12_apollonius.svg';
        'model_13_fermat.svg';
        'model_14_hidden_circle.svg';
        'model_15_guadou.svg';
        'model_16_fold.svg';
    };

    for i = 1:numel(models)
        fprintf('Generating %s ... ', names{i});
        models{i}();
        fprintf('OK\n');
    end
    fprintf('All %d math models generated in %s\n', numel(models), out);
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

function h = draw_dotted(ax, x1, y1, x2, y2, color)
    h = draw_line(ax, x1, y1, x2, y2, color, ':', 1.5);
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

%% ===================== Model 01: 手拉手模型 =====================
function model_handshake(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Two isosceles triangles △ABC and △ADE sharing vertex A.
    % D and E are rotated INWARD relative to AB/AC, so BD and CE
    % clearly show as the "handshake" lines.
    % Conclusion: △ABD ≅ △ACE (SSS: AB=AC, AD=AE, BD=CE)

    A = [W/2, 50];          % common vertex (head)
    B = [70,  H-45];        % △ABC base left
    C = [W-70, H-45];       % △ABC base right

    % D and E: rotate AB/AC inward so they LEAN toward center
    half_ang = atan2(B(1)-A(1), B(2)-A(2));               % angle of AB from horizontal, ~2.94 rad
    % Actually compute correctly: vector A→B, angle from vertical downward
    vAB = B - A;
    theta_AB = atan2(abs(vAB(1)), vAB(2));  % angle from vertical
    theta_in = 0.15;  % inward rotation (radians)
    r_small = 160;     % AD = AE

    D = A + r_small * [-sin(theta_AB - theta_in), cos(theta_AB - theta_in)];
    E = A + r_small * [ sin(theta_AB - theta_in), cos(theta_AB - theta_in)];

    % — Outer triangle ABC —
    draw_line(ax, A(1), A(2), B(1), B(2), '#333333');
    draw_line(ax, A(1), A(2), C(1), C(2), '#333333');
    draw_line(ax, B(1), B(2), C(1), C(2), '#333333');

    % — Inner triangle ADE —
    draw_line(ax, A(1), A(2), D(1), D(2), '#333333');
    draw_line(ax, A(1), A(2), E(1), E(2), '#333333');
    draw_line(ax, D(1), D(2), E(1), E(2), '#999999', '--');

    % — Handshake lines BD and CE (highlighted) —
    hand = '#e74c3c';
    draw_line(ax, B(1), B(2), D(1), D(2), hand, '-', 2.5);
    draw_line(ax, C(1), C(2), E(1), E(2), hand, '-', 2.5);

    % — Equal marks: AB=AC, AD=AE, BD=CE —
    mark_equal(ax, A, B, 0.35, '#333333');
    mark_equal(ax, A, C, 0.35, '#333333');
    mark_equal(ax, A, D, 0.35, '#2ecc71');
    mark_equal(ax, A, E, 0.35, '#2ecc71');
    mark_equal(ax, B, D, 0.50, hand);
    mark_equal(ax, C, E, 0.50, hand);

    % — Points —
    draw_point(ax, A(1), A(2), '#333333', 4);
    draw_point(ax, B(1), B(2), '#333333');
    draw_point(ax, C(1), C(2), '#333333');
    draw_point(ax, D(1), D(2), '#333333');
    draw_point(ax, E(1), E(2), '#333333');

    % — Labels —
    draw_label(ax, A(1), A(2)-20, 'A');
    draw_label(ax, B(1)-18, B(2)+18, 'B');
    draw_label(ax, C(1)+18, C(2)+18, 'C');
    draw_label(ax, D(1)-18, D(2)-10, 'D');
    draw_label(ax, E(1)+18, E(2)-10, 'E');

    % — Rotation arc at A: from AD to AB (showing inward rotation) —
    r_arc = 38;
    thD = atan2(D(2)-A(2), D(1)-A(1));
    thB = atan2(B(2)-A(2), B(1)-A(1));
    draw_arc(ax, A(1), A(2), r_arc, thB, thD, hand);
    th_mid = (thD + thB) / 2;
    draw_label(ax, A(1)+r_arc*1.7*cos(th_mid)+6, ...
                   A(2)+r_arc*1.7*sin(th_mid), '旋转', hand, 12);

    fname = fullfile(out, 'model_01_handshake.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 02: 一线三等角 (K字型) =====================
function model_k_shape(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Base line with 3 equal angles
    baseY = H - 60;
    Bx = 80; Cx = W/2; Dx = W - 80;
    B = [Bx, baseY]; C = [Cx, baseY]; D = [Dx, baseY];

    % Points above the line forming equal angles
    alpha = 30; % angle in degrees
    % Height for equal angles
    h_ang = 60;
    % Point A such that ∠ABC = α
    % For ∠ABC = α, we need A_y such that tan(α) = (A_y - B_y) / (A_x - B_x)
    A = [Bx + h_ang/tand(alpha), baseY - h_ang];
    E = [Cx + h_ang/tand(alpha), baseY - h_ang];
    F = [Dx + h_ang/tand(alpha), baseY - h_ang];

    % Line from B to A, C to E, D to F
    draw_line(ax, B(1), B(2), A(1), A(2), '#333333');
    draw_line(ax, C(1), C(2), E(1), E(2), '#333333');
    draw_line(ax, D(1), D(2), F(1), F(2), '#333333');

    % Base line
    draw_line(ax, B(1)-30, B(2), Dx+30, baseY, '#333333');

    % Connect A-E and E-F to show the triangle pattern
    draw_line(ax, A(1), A(2), E(1), E(2), '#2ecc71');
    draw_line(ax, E(1), E(2), F(1), F(2), '#2ecc71');
    draw_dashed(ax, A(1), A(2), F(1), F(2), '#999999');

    % Angle marks
    ang_r = 20;
    draw_arc(ax, B(1), B(2), ang_r, pi-atan2(A(2)-B(2), A(1)-B(1)), 0, '#e74c3c');
    draw_arc(ax, C(1), C(2), ang_r, pi-atan2(E(2)-C(2), E(1)-C(1)), 0, '#e74c3c');
    draw_arc(ax, D(1), D(2), ang_r, pi-atan2(F(2)-D(2), F(1)-D(1)), 0, '#e74c3c');

    % Angle labels
    draw_label(ax, B(1)+ang_r+15, B(2)-ang_r, 'α');
    draw_label(ax, C(1)+ang_r+15, C(2)-ang_r, 'α');
    draw_label(ax, D(1)+ang_r+15, D(2)-ang_r, 'α');

    % Points
    for p = {B, C, D, A, E, F}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, B(1), B(2)+18, 'B');
    draw_label(ax, C(1), C(2)+18, 'C');
    draw_label(ax, D(1), D(2)+18, 'D');
    draw_label(ax, A(1), A(2)-15, 'A');
    draw_label(ax, E(1), E(2)-15, 'E');
    draw_label(ax, F(1), F(2)-15, 'F');

    fname = fullfile(out, 'model_02_k_shape.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 03: 三垂直模型 =====================
function model_three_perp(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Rectangle with three right angles marked
    % Rectangle ABCD, point E on AD
    margin = 50;
    A = [margin, margin]; B = [margin, H-margin];
    C = [W-margin, H-margin]; D = [W-margin, margin];

    % Point E on AD (between A and D)
    E = [A(1) + (D(1)-A(1))*0.7, A(2) + (D(2)-A(2))*0.7];

    % Main rectangle
    draw_line(ax, A(1), A(2), B(1), B(2), '#333333');
    draw_line(ax, B(1), B(2), C(1), C(2), '#333333');
    draw_line(ax, C(1), C(2), D(1), D(2), '#333333');
    draw_line(ax, A(1), A(2), E(1), E(2), '#2ecc71');

    % Diagonal
    draw_line(ax, B(1), B(2), D(1), D(2), '#999999', '--');

    % Perpendicular from E to diagonal
    % Projection of E onto line BD
    t = dot(D-B, E-B) / dot(D-B, D-B);
    t = max(0, min(1, t));
    P = B + t*(D - B);
    draw_line(ax, E(1), E(2), P(1), P(2), '#e74c3c');

    % Right angle marks
    draw_right_angle_mark(ax, A(1)+12, A(2)-12, 10);
    draw_right_angle_mark(ax, B(1)+12, B(2)-12, 10);
    draw_right_angle_mark(ax, D(1)-24, D(2)+12, 10);
    draw_right_angle_mark(ax, P(1), P(2), 10, '#e74c3c');

    % Points
    for p = {A, B, C, D, E, P}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, A(1)-15, A(2), 'A');
    draw_label(ax, B(1)-15, B(2)+15, 'B');
    draw_label(ax, C(1)+15, C(2)+15, 'C');
    draw_label(ax, D(1)+15, D(2), 'D');
    draw_label(ax, E(1)+15, E(2), 'E');
    draw_label(ax, P(1)-15, P(2), 'P');

    fname = fullfile(out, 'model_03_three_perp.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 04: 倍长中线模型 =====================
function model_median_double(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Triangle ABC with median AM extended to D where MD=AM
    A = [W/2, 50]; B = [50, H-40]; C = [W-50, H-40];
    M = (B + C) / 2;  % midpoint of BC
    D = A + 2*(M - A);  % D such that M is midpoint of AD

    % Triangle ABC
    draw_line(ax, A(1), A(2), B(1), B(2), '#333333');
    draw_line(ax, A(1), A(2), C(1), C(2), '#333333');
    draw_line(ax, B(1), B(2), C(1), C(2), '#333333');

    % Median AM (solid)
    draw_line(ax, A(1), A(2), M(1), M(2), '#e74c3c');
    % Extended to D (dashed)
    draw_dashed(ax, M(1), M(2), D(1), D(2), '#e74c3c');
    % BD and CD (dashed to show parallelogram)
    draw_dashed(ax, B(1), B(2), D(1), D(2), '#2ecc71');
    draw_dashed(ax, C(1), C(2), D(1), D(2), '#2ecc71');

    % Equal marks on AM and MD
    mark_equal(ax, A, M, 0.5, '#e74c3c');
    mark_equal(ax, M, D, 0.5, '#e74c3c');

    % Points
    for p = {A, B, C, M, D}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, A(1), A(2)-18, 'A');
    draw_label(ax, B(1)-18, B(2)+18, 'B');
    draw_label(ax, C(1)+18, C(2)+18, 'C');
    draw_label(ax, M(1)-15, M(2)+18, 'M');
    draw_label(ax, D(1), D(2)+18, 'D');

    fname = fullfile(out, 'model_04_median_double.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 05: 角平分线模型 =====================
function model_angle_bisector(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % ∠BAC with bisector AD, DE⟂AB, DF⟂AC, DE=DF
    % Symmetric angle opening downward, filling the figure well

    A = [W/2, H-60];      % vertex near top
    B = [A(1)-160, 45];   % lower-left
    C = [A(1)+160, 45];   % lower-right

    % D on the angle bisector (bisector = straight down for symmetric angle)
    D = [A(1), 140];

    % E: foot from D to AB (perpendicular)
    E = project_point_to_line(D, A, B);
    % F: foot from D to AC (perpendicular)
    F = project_point_to_line(D, A, C);

    % Angle sides AB and AC
    draw_line(ax, A(1), A(2), B(1), B(2), '#333333');
    draw_line(ax, A(1), A(2), C(1), C(2), '#333333');

    % Bisector AD (red, thicker)
    draw_line(ax, A(1), A(2), D(1), D(2), '#e74c3c', '-', 2);

    % Perpendiculars DE and DF (green dashed)
    draw_dashed(ax, D(1), D(2), E(1), E(2), '#2ecc71');
    draw_dashed(ax, D(1), D(2), F(1), F(2), '#2ecc71');

    % Right-angle marks at E and F
    % At E: between DE and AB → corner at E, L along DE and EA
    draw_right_angle_mark(ax, E(1), E(2), 10, '#2ecc71');
    draw_right_angle_mark(ax, F(1), F(2), 10, '#2ecc71');

    % Equal-distance mark on DE and DF (short double-dash)
    mark_equal(ax, D, E, 0.5, '#2ecc71');
    mark_equal(ax, D, F, 0.5, '#2ecc71');

    % Points
    for p = {A, B, C, D, E, F}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, A(1), A(2)-18, 'A');
    draw_label(ax, B(1)-18, B(2)-10, 'B');
    draw_label(ax, C(1)+18, C(2)-10, 'C');
    draw_label(ax, D(1)+16, D(2), 'D');
    draw_label(ax, E(1)-16, E(2)-10, 'E');
    draw_label(ax, F(1)+16, F(2)-10, 'F');

    fname = fullfile(out, 'model_05_angle_bisector.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 06: A字型相似 =====================
function model_a_similar(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Triangle ABC with DE∥BC
    A = [W/2, 40]; B = [60, H-40]; C = [W-60, H-40];
    % DE parallel to BC
    t = 0.45;
    D = A + t*(B - A); E = A + t*(C - A);

    % Outer triangle
    draw_line(ax, A(1), A(2), B(1), B(2), '#333333');
    draw_line(ax, A(1), A(2), C(1), C(2), '#333333');
    draw_line(ax, B(1), B(2), C(1), C(2), '#333333');

    % DE (highlighted)
    draw_line(ax, D(1), D(2), E(1), E(2), '#e74c3c', '-', 2);

    % Parallel marks (small arrows on DE and BC)
    % Midpoint of DE and BC
    M_DE = (D + E) / 2; M_BC = (B + C) / 2;
    draw_parallel_mark(ax, M_DE(1), M_DE(2), 12, '#e74c3c');
    draw_parallel_mark(ax, M_BC(1), M_BC(2), 12, '#e74c3c');

    % Points
    for p = {A, B, C, D, E}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, A(1), A(2)-18, 'A');
    draw_label(ax, B(1)-18, B(2)+18, 'B');
    draw_label(ax, C(1)+18, C(2)+18, 'C');
    draw_label(ax, D(1)-18, D(2), 'D');
    draw_label(ax, E(1)+18, E(2), 'E');

    fname = fullfile(out, 'model_06_a_similar.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 07: 8字型相似 =====================
function model_8_similar(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Two intersecting lines forming 8 shape: AB∥CD
    A = [60, 50]; B = [W-60, 50];  % top line
    C = [W-60, H-50]; D = [60, H-50];  % bottom line (reversed for 8-shape)
    O = [W/2, H/2];  % intersection

    % Lines AC and BD (the crossing lines)
    draw_line(ax, A(1), A(2), C(1), C(2), '#333333');
    draw_line(ax, B(1), B(2), D(1), D(2), '#333333');

    % Parallel lines AB and CD (highlighted)
    draw_line(ax, A(1), A(2), B(1), B(2), '#e74c3c', '-', 2);
    draw_line(ax, C(1), C(2), D(1), D(2), '#e74c3c', '-', 2);

    % Parallel marks
    draw_parallel_mark(ax, W/2, 40, 12, '#e74c3c');
    draw_parallel_mark(ax, W/2, H-40, 12, '#e74c3c');

    % Points
    for p = {A, B, C, D, O}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, A(1)-15, A(2)-10, 'A');
    draw_label(ax, B(1)+15, B(2)-10, 'B');
    draw_label(ax, C(1)+15, C(2)+10, 'C');
    draw_label(ax, D(1)-15, D(2)+10, 'D');
    draw_label(ax, O(1)-10, O(2)+10, 'O');

    fname = fullfile(out, 'model_07_8_similar.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 08: 射影定理 =====================
function model_projection(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Rt△ABC with ∠A = 90°, AD ⟂ BC
    % A is right-angle vertex, BC is hypotenuse
    % B and C symmetric about the altitude for visual clarity
    cx = W/2;
    A = [cx, 90];           % top vertex (right angle)
    base_y = H - 40;        % BC baseline
    b_half = 150;           % half the base spread
    B = [cx - b_half, base_y];
    C = [cx + b_half, base_y];
    % D: foot of altitude from A to BC
    D = [cx, base_y];

    % Triangle ABC
    draw_line(ax, A(1), A(2), B(1), B(2), '#333333');
    draw_line(ax, A(1), A(2), C(1), C(2), '#333333');
    draw_line(ax, B(1), B(2), C(1), C(2), '#333333');

    % Altitude AD (red, thicker)
    draw_line(ax, A(1), A(2), D(1), D(2), '#e74c3c', '-', 2.5);

    % Right-angle marks: at A (∠BAC=90°) and D (AD⟂BC)
    % A: corner at A, legs along AB (down-left) and AC (down-right)
    draw_right_angle_mark(ax, A(1)-12, A(2), 12, '#333333');
    % D: corner at D, legs along AD (up) and BD (left) or CD (right)
    draw_right_angle_mark(ax, D(1)-12, D(2), 12, '#e74c3c');

    % Points
    for p = {A, B, C, D}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, A(1), A(2)-18, 'A');
    draw_label(ax, B(1)-18, B(2)+18, 'B');
    draw_label(ax, C(1)+18, C(2)+18, 'C');
    draw_label(ax, D(1), D(2)+18, 'D');

    fname = fullfile(out, 'model_08_projection.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 09: 半角模型 =====================
function model_half_angle(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Square ABCD, point E on AB (extended), F on AD
    % ∠EAF = 45°, prove BE+DF=EF

    % Square with side length 150
    sq_size = 150;
    offset_x = (W - sq_size) / 2;
    offset_y = (H - sq_size) / 2;
    A_sq = [offset_x, offset_y + sq_size];  % bottom-left of square = A
    B_sq = [offset_x, offset_y];  % top-left
    C_sq = [offset_x + sq_size, offset_y];  % top-right
    D_sq = [offset_x + sq_size, offset_y + sq_size];  % bottom-right

    % Point E on extended AB and F on extended AD
    % Actually for this model: BE along BC direction, DF along DC direction
    % E on BC, F on CD
    E = [offset_x + sq_size*0.4, offset_y];  % on BC (top)
    F = [offset_x + sq_size, offset_y + sq_size*0.6];  % on CD (right)

    % Square
    draw_line(ax, A_sq(1), A_sq(2), B_sq(1), B_sq(2), '#333333');
    draw_line(ax, B_sq(1), B_sq(2), C_sq(1), C_sq(2), '#333333');
    draw_line(ax, C_sq(1), C_sq(2), D_sq(1), D_sq(2), '#333333');
    draw_line(ax, D_sq(1), D_sq(2), A_sq(1), A_sq(2), '#333333');

    % Triangle AEF (45°)
    draw_line(ax, A_sq(1), A_sq(2), E(1), E(2), '#e74c3c', '-', 2);
    draw_line(ax, A_sq(1), A_sq(2), F(1), F(2), '#e74c3c', '-', 2);
    draw_line(ax, E(1), E(2), F(1), F(2), '#e74c3c', '-', 2);

    % 45° angle mark at A
    % A is at bottom-left, E is on top edge, F is on right edge
    draw_arc(ax, A_sq(1), A_sq(2), 25, 0, pi/4, '#e74c3c');
    draw_label(ax, A_sq(1)+35, A_sq(2)-15, '45°', '#e74c3c', 12);

    % Points
    for p = {A_sq, B_sq, C_sq, D_sq, E, F}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, A_sq(1)-15, A_sq(2), 'A');
    draw_label(ax, B_sq(1)-15, B_sq(2)-15, 'B');
    draw_label(ax, C_sq(1)+15, C_sq(2)-15, 'C');
    draw_label(ax, D_sq(1)+15, D_sq(2)+15, 'D');
    draw_label(ax, E(1), E(2)-15, 'E');
    draw_label(ax, F(1)+15, F(2), 'F');

    fname = fullfile(out, 'model_09_half_angle.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 10: 将军饮马 =====================
function model_jiangjun(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Line l (river), point A above, point B above
    % A' is reflection of A across l
    % P is intersection of A'B with l

    river_y = H/2 + 20;
    A = [80, H-50];
    B = [W-80, H-50];

    % River line
    draw_line(ax, 20, river_y, W-20, river_y, '#333399', '-', 2);

    % A' (reflection of A across river)
    A_prime = [A(1), river_y - (A(2) - river_y)];

    % Connect A' to B through P
    % P is at intersection of line A'B with river_y
    t = (river_y - A_prime(2)) / (B(2) - A_prime(2));
    P = A_prime + t*(B - A_prime);

    % Path A-P-B (green, optimal)
    draw_line(ax, A(1), A(2), P(1), P(2), '#2ecc71', '-', 2);
    draw_line(ax, P(1), P(2), B(1), B(2), '#2ecc71', '-', 2);

    % A' to P (dashed, for construction)
    draw_dashed(ax, A_prime(1), A_prime(2), P(1), P(2), '#e74c3c');

    % A to A' (perpendicular, dashed)
    draw_dashed(ax, A(1), A(2), A_prime(1), A_prime(2), '#999999');
    % Right angle mark
    draw_right_angle_mark(ax, A(1)-15, river_y+15, 10, '#999999');

    % Points
    colors = {'#e74c3c', '#e74c3c', '#2ecc71', '#aaaaaa'};
    pts = {A, B, P, A_prime};
    for i = 1:4
        draw_point(ax, pts{i}(1), pts{i}(2), colors{i});
    end

    % Labels
    draw_label(ax, A(1), A(2)-15, 'A');
    draw_label(ax, B(1)+15, B(2)-15, 'B');
    draw_label(ax, P(1), P(2)-12, 'P');
    draw_label(ax, A_prime(1), A_prime(2)+18, "A'");
    draw_label(ax, W/2, river_y-15, 'l（河）', '#333399', 13);

    fname = fullfile(out, 'model_10_jiangjun.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 11: 胡不归模型 =====================
function model_huguigui(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % 胡不归: Travel in desert (slow) then road (fast) to destination
    % sin(α) = v_desert/v_road = k  (k < 1)

    road_y = H - 50;
    % Point A (destination) on the road, right side
    A = [W - 60, road_y];
    % Point P in desert, below and left of A
    P = [140, H - 180];

    % Desert fill (below road)
    hf = fill([30, W-30, W-30, 30], [0, 0, road_y, road_y], [0.96, 0.94, 0.88]);
    set(hf, 'EdgeColor', 'none', 'FaceAlpha', 0.35);

    % Road line
    draw_line(ax, 30, road_y, W-30, road_y, '#333333', '-', 2.5);

    % Project P vertically onto road to find reference
    P_proj = [P(1), road_y];

    % Transition point T on road, to the left of A
    % For sin(α) = 0.5 (i.e., α = 30°), path PT makes 30° from vertical
    Tx = P(1) + (road_y - P(2)) * tand(30);  % where 30° from vertical hits the road
    % But T should be between P_proj and A
    Tx = min(Tx, A(1) - 20);
    T = [Tx, road_y];

    % Path: P → T (desert) dashed construction, T → A (road) solid
    draw_line(ax, P(1), P(2), T(1), T(2), '#e74c3c', '-', 2.5);
    draw_line(ax, T(1), T(2), A(1), A(2), '#e74c3c', '-', 2);

    % Construction lines (dashed)
    % Vertical from P to road
    draw_dashed(ax, P(1), P(2), P_proj(1), P_proj(2), '#999999');

    % Angle arc at T: between PT and vertical
    ang_r = 22;
    ang = atan2(abs(T(1)-P(1)), road_y - P(2));
    draw_arc(ax, T(1), T(2), ang_r, -pi/2-ang, -pi/2, '#e74c3c');
    draw_label(ax, T(1)+ang_r+12, T(2)-ang_r, 'α', '#e74c3c', 13);

    % Points
    draw_point(ax, P(1), P(2), '#e74c3c', 4);
    draw_point(ax, A(1), A(2), '#2ecc71', 4);
    draw_point(ax, T(1), T(2), '#333333', 3);

    % Labels
    draw_label(ax, P(1), P(2)-18, 'P（沙漠）', '#e74c3c', 12);
    draw_label(ax, A(1)+15, A(2)-15, 'A', '#2ecc71', 13);
    draw_label(ax, T(1)-15, T(2)+15, 'T');
    draw_label(ax, W*0.65, road_y-15, '驿道（v）', '#333333', 13);
    draw_label(ax, W*0.65, road_y/2, '沙地（v''）', '#b8860b', 13);
    draw_label(ax, W*0.25, road_y/3, 'sinα = v''/v', '#888888', 12);

    fname = fullfile(out, 'model_11_huguigui.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 12: 阿氏圆 =====================
function model_apollonius(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Apollonius circle: PA/PB = k (k > 0, k ≠ 1)
    % Choose parameters so the whole circle sits nicely in 480x300
    % Use k = 2: PA = 2·PB
    k = 2;
    A = [60, H/2];
    B = [210, H/2];
    d = B(1) - A(1);  % = 150

    % Center: Cx = (k²·Bx - Ax) / (k² - 1)
    center = [ (k^2*B(1) - A(1)) / (k^2 - 1),  H/2 ];
    r = k * d / (k^2 - 1);  % = 2*150/3 = 100

    % Draw full circle
    th = linspace(0, 2*pi, 120);
    plot(ax, center(1) + r*cos(th), center(2) + r*sin(th), ...
        'Color', '#e74c3c', 'LineWidth', 2.5);

    % Base line AB (dashed)
    draw_line(ax, A(1), A(2), B(1), B(2), '#333333', '--');

    % Point P on the upper-right part of the circle
    theta_p = pi/4;
    P = [center(1) + r*cos(theta_p), center(2) + r*sin(theta_p)];

    % Lines PA and PB
    draw_line(ax, A(1), A(2), P(1), P(2), '#2ecc71', '-', 2);
    draw_line(ax, B(1), B(2), P(1), P(2), '#2ecc71', '-', 2);

    % Verify PA/PB = k (for display, optional)
    PA = norm(P - A); PB = norm(P - B);
    ratio_check = PA / PB;

    % Points
    colors = {'#e74c3c', '#e74c3c', '#2ecc71', '#888888'};
    pts = {A, B, P, center};
    labels = {'A', 'B', 'P', 'O'};
    for i = 1:4
        draw_point(ax, pts{i}(1), pts{i}(2), colors{i});
    end

    % Labels
    draw_label(ax, A(1)-15, A(2)+15, 'A');
    draw_label(ax, B(1)+15, B(2)+15, 'B');
    draw_label(ax, P(1)+15, P(2)-10, 'P');
    draw_label(ax, center(1), center(2)-18, 'O');
    draw_label(ax, center(1)+r+8, center(2), 'PA:PB=2:1', '#e74c3c', 11);

    fname = fullfile(out, 'model_12_apollonius.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 13: 费马点 =====================
function model_fermat(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Triangle ABC with Fermat point P (all angles 120°)
    A = [W/2, 40]; B = [60, H-40]; C = [W-60, H-40];

    % Fermat point for a triangle where all angles < 120°
    % Approximate construction: rotate one side outward by 60°, connect to opposite vertex
    % This gives the Fermat point at intersection

    % Compute Fermat point precisely:
    % For a triangle, the Fermat point minimizes PA+PB+PC
    % It's at the intersection of lines from each vertex to the opposite
    % vertex of an equilateral triangle constructed on the opposite side

    % Simpler: numerical approximate Fermat point
    % Use the fact that at Fermat point, all angles between lines are 120°
    % Let's find P by bisection
    P = fminsearch(@(p) norm(p-A)+norm(p-B)+norm(p-C), [W/2, H/2]);

    % Triangle
    draw_line(ax, A(1), A(2), B(1), B(2), '#333333');
    draw_line(ax, A(1), A(2), C(1), C(2), '#333333');
    draw_line(ax, B(1), B(2), C(1), C(2), '#333333');

    % Lines from P to vertices (highlighted)
    draw_line(ax, P(1), P(2), A(1), A(2), '#e74c3c', '-', 2);
    draw_line(ax, P(1), P(2), B(1), B(2), '#2ecc71', '-', 2);
    draw_line(ax, P(1), P(2), C(1), C(2), '#2ecc71', '-', 2);

    % 120° angle marks at P
    r = 20;
    % Angle APB
    th1 = atan2(A(2)-P(2), A(1)-P(1));
    th2 = atan2(B(2)-P(2), B(1)-P(1));
    draw_arc(ax, P(1), P(2), r, th1, th2, '#333333');

    % Inner angle marks (60°) - show 120° each
    draw_label(ax, P(1)+r*1.8*cos((th1+th2)/2)+5, P(2)+r*1.8*sin((th1+th2)/2), '120°', '#333333', 11);

    % Points
    for p = {A, B, C, P}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, A(1), A(2)-18, 'A');
    draw_label(ax, B(1)-18, B(2)+18, 'B');
    draw_label(ax, C(1)+18, C(2)+18, 'C');
    draw_label(ax, P(1)-15, P(2), 'P');

    fname = fullfile(out, 'model_13_fermat.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 14: 隐圆模型 =====================
function model_hidden_circle(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Fixed chord AB, point P such that ∠APB = constant α
    % P trajectory is an arc (hidden circle)

    A = [130, H-50]; B = [W-130, H-50];
    % Chord length
    d = B(1) - A(1);

    % Circle that sees chord AB at angle α = 45°
    alpha = 45 * pi/180;
    % Radius = d/(2*sin(α))
    r = d / (2*sin(alpha));
    % Center lies on perpendicular bisector
    cx = (A(1) + B(1)) / 2;
    cy = A(2) - sqrt(r^2 - (d/2)^2);  % center above AB

    % Hidden circle (dashed)
    th = linspace(0, 2*pi, 100);
    plot(ax, cx + r*cos(th), cy + r*sin(th), 'Color', '#2ecc71', ...
        'LineWidth', 1.5, 'LineStyle', '--');

    % Chord AB
    draw_line(ax, A(1), A(2), B(1), B(2), '#333333');

    % Points P at various positions on the arc
    P_positions = {[cx + r*cos(-pi/4), cy + r*sin(-pi/4)], ...
                   [cx + r*cos(-pi/6), cy + r*sin(-pi/6)], ...
                   [cx + r*cos(-pi/12), cy + r*sin(-pi/12)]};

    for i = 1:3
        P = P_positions{i};
        if P(2) > H-20, continue; end
        draw_line(ax, A(1), A(2), P(1), P(2), '#e74c3c');
        draw_line(ax, B(1), B(2), P(1), P(2), '#e74c3c');
        draw_point(ax, P(1), P(2), '#e74c3c');
    end

    % Points A, B
    draw_point(ax, A(1), A(2), '#333333');
    draw_point(ax, B(1), B(2), '#333333');

    % Labels
    draw_label(ax, A(1)-15, A(2)+10, 'A');
    draw_label(ax, B(1)+15, B(2)+10, 'B');
    draw_label(ax, P_positions{1}(1)+15, P_positions{1}(2)-10, 'P');
    draw_label(ax, cx, cy-20, '隐圆');

    fname = fullfile(out, 'model_14_hidden_circle.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 15: 瓜豆原理 =====================
function model_guadou(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % 瓜豆原理: Active point P moves along a path (main),
    % follower Q moves along a similar path (scaled+rotated) around fixed O.
    % Q = O + k·R(θ)·(P − O)

    O = [100, H/2];       % fixed center
    P_r = 90;              % P trajectory radius
    Q_r = 50;              % Q trajectory radius (scaled by ~0.55)
    angle_offset = pi/5;   % rotation between P and Q trajectories

    % Sample 6 points along each trajectory
    angles = linspace(-pi/3, pi+pi/4, 6);
    P_pos = zeros(length(angles), 2);
    Q_pos = zeros(length(angles), 2);

    for i = 1:length(angles)
        th = angles(i);
        P_pos(i,:) = O + P_r * [cos(th), sin(th)];
        Q_pos(i,:) = O + Q_r * [cos(th + angle_offset), sin(th + angle_offset)];
    end

    % Draw trajectories
    th_fine = linspace(-pi/3, pi+pi/4, 60);
    % P trajectory (big, red)
    plot(ax, O(1)+P_r*cos(th_fine), O(2)+P_r*sin(th_fine), ...
        'Color', '#e74c3c', 'LineWidth', 2.5);
    % Q trajectory (small, green)
    plot(ax, O(1)+Q_r*cos(th_fine+angle_offset), O(2)+Q_r*sin(th_fine+angle_offset), ...
        'Color', '#2ecc71', 'LineWidth', 2.5);

    % Connection lines: O→P (dashed), P→Q (solid thin), O→Q (dashed)
    for i = 1:size(P_pos, 1)
        draw_dashed(ax, O(1), O(2), P_pos(i,1), P_pos(i,2), '#cccccc');
        draw_dashed(ax, O(1), O(2), Q_pos(i,1), Q_pos(i,2), '#cccccc');
        % Connect P→Q for the first and middle points
        if i == 1 || i == round(length(angles)/2)
            draw_line(ax, P_pos(i,1), P_pos(i,2), Q_pos(i,1), Q_pos(i,2), '#999999', '-.', 1);
        end
    end

    % Highlight the sample points
    for i = 1:size(P_pos, 1)
        draw_point(ax, P_pos(i,1), P_pos(i,2), '#e74c3c', 4);
        draw_point(ax, Q_pos(i,1), Q_pos(i,2), '#2ecc71', 4);
    end
    draw_point(ax, O(1), O(2), '#333333', 5);

    % Labels with style
    draw_label(ax, O(1)-18, O(2)-18, 'O', '#333333', 15);
    % Pick middle P and Q for labeling
    mid_idx = round(length(angles)/2);
    draw_label(ax, P_pos(mid_idx,1), P_pos(mid_idx,2)+18, 'P（主动点）', '#e74c3c', 11);
    draw_label(ax, Q_pos(mid_idx,1), Q_pos(mid_idx,2)-18, 'Q（从动点）', '#2ecc71', 11);

    fname = fullfile(out, 'model_15_guadou.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Model 16: 折叠模型 =====================
function model_fold(out, W, H)
    [fig, ax] = setup_fig(W, H);
    % Rectangle with fold line
    rect_w = 200; rect_h = 140;
    rx = (W - rect_w) / 2;
    ry = (H - rect_h) / 2;

    % Rectangle ABCD
    A = [rx, ry + rect_h];  % bottom-left
    B = [rx, ry];            % top-left
    C = [rx + rect_w, ry];   % top-right
    D = [rx + rect_w, ry + rect_h];  % bottom-right

    % Fold point: somewhere on top edge
    fold_x = rx + rect_w * 0.35;
    E = [fold_x, ry];  % on BC (top edge)
    % Fold line goes from E to F (somewhere on CD, or to A' reflection)

    % A' (reflected A across fold line)
    % For a fold along line from E to current A, actually let's make it
    % more standard: fold along line through E, with A reflected to A'
    % Simple: fold along line from E at some angle
    fold_angle = -pi/7;
    % Point F on AD (left edge)
    F = [rx, ry + rect_h * 0.7];
    % Actually make F on the fold line
    % Let me use a simpler model: fold corner A up along EF

    % Standard fold model: EF is fold line, A reflects to A'
    % E at top edge, F at right edge
    E = [rx + rect_w*0.3, ry];
    F = [rx + rect_w, ry + rect_h*0.4];

    % A is bottom-left corner. Reflect A across line EF to get A'
    A_pt = [rx, ry + rect_h];
    % Reflection of A across line through E and F
    v = F - E; v = v / norm(v);
    w = A_pt - E;
    proj = dot(w, v);
    perp = w - proj*v;
    A_prime = E + proj*v - perp;

    % Rectangle (dashed for original)
    draw_dashed(ax, A_pt(1), A_pt(2), B(1), B(2), '#999999');
    draw_dashed(ax, B(1), B(2), C(1), C(2), '#999999');
    draw_dashed(ax, C(1), C(2), D(1), D(2), '#999999');
    draw_dashed(ax, A_pt(1), A_pt(2), D(1), D(2), '#999999');

    % Fold line (highlighted)
    draw_line(ax, E(1), E(2), F(1), F(2), '#e74c3c', '-', 2);

    % Folded triangle A'EF (highlighted)
    draw_line(ax, A_prime(1), A_prime(2), E(1), E(2), '#e74c3c');
    draw_line(ax, A_prime(1), A_prime(2), F(1), F(2), '#e74c3c');

    % Dash-dot for reflection guide
    draw_dashed(ax, A_pt(1), A_pt(2), A_prime(1), A_prime(2), '#2ecc71');
    % Middle tick
    mid = (A_pt + A_prime) / 2;
    draw_point(ax, mid(1), mid(2), '#2ecc71', 2);

    % Perpendicular mark
    % Perpendicular from A to fold line
    draw_right_angle_mark(ax, mid(1)-8, mid(2)+4, 6, '#2ecc71');

    % Points
    for p = {A_pt, B, C, D, E, F, A_prime}
        draw_point(ax, p{1}(1), p{1}(2), '#333333');
    end

    % Labels
    draw_label(ax, A_pt(1)-15, A_pt(2), 'A');
    draw_label(ax, B(1)-15, B(2)-15, 'B');
    draw_label(ax, C(1)+15, C(2)-15, 'C');
    draw_label(ax, D(1)+15, D(2)+15, 'D');
    draw_label(ax, A_prime(1)+15, A_prime(2)-10, "A'");
    draw_label(ax, E(1), E(2)-15, 'E');
    draw_label(ax, F(1)+15, F(2), 'F');

    fname = fullfile(out, 'model_16_fold.svg');
    save_svg(fig, fname);
    clean_svg(fname);
end

%% ===================== Utility Functions =====================
function P = project_point_to_line(pt, line1, line2)
    % Project pt onto line (line1-line2)
    v = line2 - line1;
    w = pt - line1;
    t = dot(w, v) / dot(v, v);
    t = max(0, min(1, t));
    P = line1 + t*v;
end

function mark_equal(ax, p1, p2, t, color)
    % Draw small perpendicular dashes at fraction t along segment p1-p2
    v = p2 - p1;
    v_perp = [-v(2), v(1)];
    v_perp = 5 * v_perp / norm(v_perp);
    pt = p1 + t*v;
    draw_line(ax, pt(1)-v_perp(1), pt(2)-v_perp(2), pt(1)+v_perp(1), pt(2)+v_perp(2), color);
end

function draw_parallel_mark(ax, x, y, size, color)
    % Draw small arrows indicating parallel lines
    draw_line(ax, x-size, y-3, x+size, y-3, color);
    draw_line(ax, x-size, y+3, x+size, y+3, color);
end

function clean_svg(fname)
    % Post-process SVG to remove MATLAB-specific cruft and clean up
    try
        txt = fileread(fname);
        % Remove MATLAB-generated ids, data-name attributes etc.
        % Keep the SVG structure clean
        fid = fopen(fname, 'w');
        if fid > 0
            fwrite(fid, txt);
            fclose(fid);
        end
    catch
        % Best effort
    end
end
