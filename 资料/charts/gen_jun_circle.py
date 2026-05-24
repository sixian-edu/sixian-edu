"""生成 初中数学·圆 专题 SVG 图表 (7张)"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ═══════════════ 1. 圆的基本元素 ═══════════════
fig, ax = plt.subplots(figsize=(5.5, 5.2))
ax.set_aspect('equal'); ax.set_xlim(-2.8, 2.8); ax.set_ylim(-2.6, 2.8)
ax.axis('off')
c = plt.Circle((0, 0), 2, fill=False, edgecolor='#1a6fc4', linewidth=2.5)
ax.add_patch(c)
ax.plot(0, 0, 'o', color='#e74c3c', markersize=9, zorder=5)
ax.text(0, -0.2, 'O', ha='center', va='top', fontsize=13, fontweight='bold', color='#333')

# Radius
th = np.pi/6
re = (2*np.cos(th), 2*np.sin(th))
ax.plot([0, re[0]], [0, re[1]], color='#27ae60', linewidth=2)
ax.text(re[0]*0.5-0.15, re[1]*0.5+0.15, '半径 r', fontsize=11, fontweight='bold', color='#27ae60')
ax.plot(re[0], re[1], 'o', color='#27ae60', ms=5)

# Diameter
ax.plot([-2, 2], [0, 0], color='#e67e22', linewidth=2, linestyle='--')
ax.plot(-2, 0, 'o', color='#e67e22', ms=5); ax.plot(2, 0, 'o', color='#e67e22', ms=5)
ax.text(-2, -0.2, 'A', ha='center', va='top', fontsize=11, fontweight='bold', color='#e67e22')
ax.text(2, -0.2, 'B', ha='center', va='top', fontsize=11, fontweight='bold', color='#e67e22')
ax.text(0, -0.35, '直径 d=2r', ha='center', va='top', fontsize=10, fontweight='bold', color='#e67e22')

# Chord
ca, cb = (-1.3, -1.5), (1.7, -0.6)
ax.plot([ca[0], cb[0]], [ca[1], cb[1]], color='#8e44ad', linewidth=2)
ax.text(ca[0]-0.1, ca[1]-0.15, 'C', ha='center', va='top', fontsize=11, fontweight='bold', color='#8e44ad')
ax.text(cb[0]+0.1, cb[1]-0.1, 'D', ha='center', va='top', fontsize=11, fontweight='bold', color='#8e44ad')
mc = ((ca[0]+cb[0])/2, (ca[1]+cb[1])/2)
ax.text(mc[0]+0.25, mc[1]-0.2, '弦', fontsize=11, fontweight='bold', color='#8e44ad')

# Arc highlight
arc = mpatches.Arc((0, 0), 4, 4, theta1=30, theta2=80, color='#e74c3c', linewidth=3)
ax.add_patch(arc)
ax.text(2.3*np.cos(np.deg2rad(55)), 2.3*np.sin(np.deg2rad(55)),
        '弧', ha='center', fontsize=11, fontweight='bold', color='#e74c3c')
ax.text(0, 2.6, '圆的基本元素', ha='center', fontsize=14, fontweight='bold', color='#1a1a2e')
plt.tight_layout()
plt.savefig('jun_circle_basics.svg', bbox_inches='tight', dpi=150, format='svg')
plt.close()

# ═══════════════ 2. 垂径定理 ═══════════════
fig, ax = plt.subplots(figsize=(5.5, 5.2))
ax.set_aspect('equal'); ax.set_xlim(-2.8, 2.8); ax.set_ylim(-2.8, 2.8)
ax.axis('off')
c = plt.Circle((0, 0), 2, fill=False, edgecolor='#1a6fc4', linewidth=2.5)
ax.add_patch(c)
ax.plot(0, 0, 'o', color='#333', ms=6, zorder=5)
ax.text(0, -0.2, 'O', ha='center', va='top', fontsize=13, fontweight='bold', color='#333')

# Chord AB
chord_y = -0.8
ax.plot([-np.sqrt(4 - chord_y**2), np.sqrt(4 - chord_y**2)], [chord_y, chord_y],
        color='#e74c3c', linewidth=2.5)
l = np.sqrt(4 - chord_y**2)
ax.text(-l-0.15, chord_y, 'A', ha='center', va='center', fontsize=12, fontweight='bold', color='#e74c3c')
ax.text(l+0.15, chord_y, 'B', ha='center', va='center', fontsize=12, fontweight='bold', color='#e74c3c')

# Perpendicular diameter
ax.plot([0, 0], [-2, 2], color='#e67e22', linewidth=2, linestyle='--')
ax.text(0.1, 2.1, 'CD 是直径', fontsize=10, fontweight='bold', color='#e67e22', rotation=90)
ax.text(0.1, -2.1, 'CD⊥AB', fontsize=10, fontweight='bold', color='#e67e22', rotation=90)

# Intersection point M
ax.plot(0, chord_y, 'o', color='#e67e22', ms=6, zorder=5)
ax.text(0.15, chord_y-0.15, 'M', fontsize=12, fontweight='bold', color='#e67e22')

# Right angle marker
r_size = 0.15
ax.plot([0, -r_size], [chord_y, chord_y], color='#999', lw=1)
ax.plot([-r_size, -r_size], [chord_y, chord_y+r_size], color='#999', lw=1)

# Arc marks for equal arcs
ax.plot([2*np.cos(np.deg2rad(100)), 2*np.cos(np.deg2rad(104))],
        [2*np.sin(np.deg2rad(100)), 2*np.sin(np.deg2rad(104))],
        color='#27ae60', lw=2)
ax.plot([2*np.cos(np.deg2rad(80)), 2*np.cos(np.deg2rad(84))],
        [2*np.sin(np.deg2rad(80)), 2*np.sin(np.deg2rad(84))],
        color='#27ae60', lw=2)

# Labels for equal arcs
ax.text(1.5, 1.5, '⌒', fontsize=14, fontweight='bold', color='#27ae60')
ax.text(-1.7, 1.5, '⌒', fontsize=14, fontweight='bold', color='#27ae60')

# Theorem text
ax.text(0, -2.65,
        '垂径定理：CD⊥AB 且 CD 过圆心 O → AM=BM, 弧 AC=弧 BC',
        ha='center', fontsize=10, fontweight='bold', color='#e74c3c')

ax.text(0, 2.6, '垂径定理', ha='center', fontsize=14, fontweight='bold', color='#1a1a2e')
plt.tight_layout()
plt.savefig('jun_circle_perp.svg', bbox_inches='tight', dpi=150, format='svg')
plt.close()

# ═══════════════ 3. 圆周角与圆心角 ═══════════════
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))
for ax in (ax1, ax2):
    ax.set_aspect('equal'); ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)
    ax.axis('off')
    c = plt.Circle((0, 0), 2, fill=False, edgecolor='#1a6fc4', linewidth=2)
    ax.add_patch(c)
    ax.plot(0, 0, 'o', color='#333', ms=5)
    ax.text(0, -0.2, 'O', ha='center', va='top', fontsize=11, fontweight='bold', color='#333')

# Left: central angle
a1 = np.deg2rad(130); b1 = np.deg2rad(20)
ax1.plot([0, 2*np.cos(a1)], [0, 2*np.sin(a1)], color='#e74c3c', lw=2)
ax1.plot([0, 2*np.cos(b1)], [0, 2*np.sin(b1)], color='#e74c3c', lw=2)
ax1.text(2.1*np.cos(a1), 2.1*np.sin(a1), 'A', fontsize=12, fontweight='bold', color='#e74c3c')
ax1.text(2.1*np.cos(b1), 2.1*np.sin(b1), 'B', fontsize=12, fontweight='bold', color='#e74c3c')

# Central angle arc
arc1 = mpatches.Arc((0, 0), 0.8, 0.8, theta1=np.rad2deg(b1), theta2=np.rad2deg(a1), color='#e67e22', lw=2)
ax1.add_patch(arc1)
mid_angle = (a1 + b1) / 2
ax1.text(0.55*np.cos(mid_angle), 0.55*np.sin(mid_angle), '∠AOB',
         ha='center', fontsize=9, fontweight='bold', color='#e67e22')

# Arc AB
arc_ab = mpatches.Arc((0, 0), 4, 4, theta1=np.rad2deg(b1), theta2=np.rad2deg(a1), color='#27ae60', lw=2.5)
ax1.add_patch(arc_ab)
ax1.text(2.2*np.cos(mid_angle), 2.2*np.sin(mid_angle), '弧 AB',
         ha='center', fontsize=9, fontweight='bold', color='#27ae60')
ax1.text(0, 2.4, '圆心角', ha='center', fontsize=13, fontweight='bold', color='#1a1a2e')

# Right: inscribed angle
a2 = np.deg2rad(120); b2 = np.deg2rad(10); c_pt = np.deg2rad(-80)
ax2.plot([0, 2*np.cos(a2)], [0, 2*np.sin(a2)], color='#999', lw=1.5, ls='--')
ax2.plot([0, 2*np.cos(b2)], [0, 2*np.sin(b2)], color='#999', lw=1.5, ls='--')
ax2.text(2.1*np.cos(a2), 2.1*np.sin(a2), 'A', fontsize=12, fontweight='bold', color='#333')
ax2.text(2.1*np.cos(b2), 2.1*np.sin(b2), 'B', fontsize=12, fontweight='bold', color='#333')
# Inscribed angle chords
ax2.plot([2*np.cos(a2), 2*np.cos(c_pt)], [2*np.sin(a2), 2*np.sin(c_pt)], color='#e74c3c', lw=2)
ax2.plot([2*np.cos(b2), 2*np.cos(c_pt)], [2*np.sin(b2), 2*np.sin(c_pt)], color='#e74c3c', lw=2)
ax2.text(2.1*np.cos(c_pt), 2.1*np.sin(c_pt), 'C', fontsize=12, fontweight='bold', color='#e74c3c')

# Inscribed angle arc
arc_start = np.rad2deg(b2); arc_end = np.rad2deg(a2)
arc2 = mpatches.Arc((2*np.cos(c_pt), 2*np.sin(c_pt)), 0.7, 0.7,
                     theta1=arc_start, theta2=arc_end, color='#e67e22', lw=2)
ax2.add_patch(arc2)

# Relationship text
ax2.text(0, -2.4, '∠ACB = ½∠AOB', ha='center', fontsize=11, fontweight='bold', color='#e74c3c')

# Arc AB
arc_ab2 = mpatches.Arc((0, 0), 4, 4, theta1=np.rad2deg(b2), theta2=np.rad2deg(a2), color='#27ae60', lw=2.5)
ax2.add_patch(arc_ab2)
ax2.text(0, 2.4, '圆周角', ha='center', fontsize=13, fontweight='bold', color='#1a1a2e')

fig.suptitle('圆周角与圆心角关系', fontsize=14, fontweight='bold', y=1.02, color='#1a1a2e')
plt.tight_layout()
plt.savefig('jun_circle_angles.svg', bbox_inches='tight', dpi=150, format='svg')
plt.close()

# ═══════════════ 4. 切线 ═══════════════
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.8))
for ax in (ax1, ax2):
    ax.set_aspect('equal'); ax.set_xlim(-2.8, 2.8); ax.set_ylim(-2.6, 2.6)
    ax.axis('off')

# Left: tangent perpendicular to radius
c = plt.Circle((0, 0), 2, fill=False, edgecolor='#1a6fc4', lw=2.5)
ax1.add_patch(c)
ax1.plot(0, 0, 'o', color='#333', ms=5)
ax1.text(0, -0.2, 'O', ha='center', va='top', fontsize=12, fontweight='bold', color='#333')

# Tangent at point T (top)
t = (0, 2)
ax1.plot([t[0]-1.8, t[0]+1.8], [t[1], t[1]], color='#e74c3c', lw=2.5)
ax1.plot([0, 0], [0, 2], color='#27ae60', lw=2)
ax1.text(0.15, 1, '半径 r', fontsize=10, fontweight='bold', color='#27ae60', rotation=90)
ax1.plot(0, 2, 'o', color='#e74c3c', ms=6, zorder=5)
ax1.text(0, 2.2, 'T（切点）', ha='center', va='bottom', fontsize=10, fontweight='bold', color='#e74c3c')
# Right angle marker
rs = 0.2
ax1.plot([-rs, -rs], [2, 2-rs], color='#999', lw=1.5)
ax1.plot([-rs, 0], [2-rs, 2-rs], color='#999', lw=1.5)
ax1.text(2.1, 1.2, '切线 ⊥ 半径', ha='center', fontsize=10, fontweight='bold', color='#e74c3c')
ax1.text(0, -2.5, '切线的性质', ha='center', fontsize=13, fontweight='bold', color='#1a1a2e')

# Right: tangent lengths equal
c = plt.Circle((0, 0), 2, fill=False, edgecolor='#1a6fc4', lw=2.5)
ax2.add_patch(c)
ax2.plot(0, 0, 'o', color='#333', ms=5)
ax2.text(0, -0.2, 'O', ha='center', va='top', fontsize=12, fontweight='bold', color='#333')

# External point P
px, py = -0.5, 2.8
ax2.plot(px, py, 'o', color='#e74c3c', ms=7, zorder=5)
ax2.text(px-0.2, py+0.2, 'P', fontsize=12, fontweight='bold', color='#e74c3c')

# Two tangent points
t1 = (2*np.cos(np.deg2rad(-30)), 2*np.sin(np.deg2rad(-30)))
t2 = (2*np.cos(np.deg2rad(-150)), 2*np.sin(np.deg2rad(-150)))

# Tangent line through P to T1
ax2.plot([px, t1[0]], [py, t1[1]], color='#e67e22', lw=2)
ax2.plot([px, t2[0]], [py, t2[1]], color='#e67e22', lw=2)
ax2.plot(t1[0], t1[1], 'o', color='#e67e22', ms=5, zorder=5)
ax2.plot(t2[0], t2[1], 'o', color='#e67e22', ms=5, zorder=5)
ax2.text(t1[0]+0.15, t1[1]-0.1, 'A', fontsize=11, fontweight='bold', color='#e67e22')
ax2.text(t2[0]-0.15, t2[1]-0.1, 'B', fontsize=11, fontweight='bold', color='#e67e22')

# Radii to tangent points
ax2.plot([0, t1[0]], [0, t1[1]], color='#27ae60', lw=1.5, ls='--')
ax2.plot([0, t2[0]], [0, t2[1]], color='#27ae60', lw=1.5, ls='--')

# Right angle markers
for tx, ty in [t1, t2]:
    d = np.array([px - tx, py - ty])
    d = d / np.linalg.norm(d) * 0.18
    ax2.plot([tx + d[0], tx + d[0]], [ty, ty + d[1]], color='#999', lw=1)
    ax2.plot([tx, tx + d[0]], [ty + d[1], ty + d[1]], color='#999', lw=1)

# Equal mark on tangent segments
mid1 = ((px+t1[0])/2, (py+t1[1])/2)
mid2 = ((px+t2[0])/2, (py+t2[1])/2)
ax2.text(mid1[0]+0.2, mid1[1]-0.15, 'PA', fontsize=10, fontweight='bold', color='#e67e22')
ax2.text(mid2[0]-0.2, mid2[1]-0.15, 'PB', fontsize=10, fontweight='bold', color='#e67e22')
ax2.text(0, -2.5, '切线长定理：PA = PB', ha='center', fontsize=13, fontweight='bold', color='#1a1a2e')

fig.suptitle('圆的切线', fontsize=14, fontweight='bold', y=1.02, color='#1a1a2e')
plt.tight_layout()
plt.savefig('jun_circle_tangent.svg', bbox_inches='tight', dpi=150, format='svg')
plt.close()

# ═══════════════ 5. 圆与圆的位置关系 ═══════════════
fig, axes = plt.subplots(1, 5, figsize=(13, 3.2))
titles = ['外离\nd > R+r', '外切\nd = R+r', '相交\n|R-r|<d<R+r', '内切\nd = |R-r|', '内含\nd < |R-r|']
params = [
    (-0.9, 0, 0.9, 0, 0.6, 0.6),  # 外离
    (-0.7, 0, 0.7, 0, 0.6, 0.6),  # 外切
    (-0.6, 0, 0.6, 0, 0.7, 0.7),  # 相交
    (-0.75, 0, 0.45, 0, 0.75, 0.55),  # 内切
    (-0.7, 0, 0.35, 0, 0.7, 0.45),  # 内含
]
colors = ['#e74c3c', '#e67e22']

for i, ax in enumerate(axes):
    ax.set_aspect('equal'); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.2, 1.2)
    ax.axis('off')
    x1, y1, x2, y2, r1, r2 = params[i]
    c1 = plt.Circle((x1, y1), r1, fill=False, edgecolor=colors[0], lw=2)
    c2 = plt.Circle((x2, y2), r2, fill=False, edgecolor=colors[1], lw=2)
    ax.add_patch(c1); ax.add_patch(c2)
    ax.plot(x1, y1, 'o', color=colors[0], ms=3)
    ax.plot(x2, y2, 'o', color=colors[1], ms=3)
    ax.text(x1, y1-r1-0.15, 'O1', ha='center', fontsize=8, fontweight='bold', color=colors[0])
    ax.text(x2, y2-r2-0.15, 'O2', ha='center', fontsize=8, fontweight='bold', color=colors[1])
    ax.text(0, -1.0, titles[i], ha='center', fontsize=8, fontweight='bold', color='#333')

fig.suptitle('圆与圆的五种位置关系', fontsize=14, fontweight='bold', y=1.06, color='#1a1a2e')
plt.tight_layout()
plt.savefig('jun_circle_positions.svg', bbox_inches='tight', dpi=150, format='svg')
plt.close()

# ═══════════════ 6. 弧长与扇形面积 ═══════════════
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))
for ax in (ax1, ax2):
    ax.set_aspect('equal'); ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)
    ax.axis('off')

# Left: sector
c = plt.Circle((0, 0), 2, fill=False, edgecolor='#1a6fc4', lw=2)
ax1.add_patch(c)
ax1.plot(0, 0, 'o', color='#333', ms=5)
ax1.text(0, -0.2, 'O', ha='center', va='top', fontsize=12, fontweight='bold', color='#333')

th1, th2 = np.deg2rad(20), np.deg2rad(70)
# Fill sector
angles = np.linspace(th1, th2, 100)
sector_x = [0] + list(2*np.cos(angles)) + [0]
sector_y = [0] + list(2*np.sin(angles)) + [0]
ax1.fill(sector_x, sector_y, color='#ffd699', alpha=0.6, edgecolor='none')
# Sector edges
ax1.plot([0, 2*np.cos(th1)], [0, 2*np.sin(th1)], color='#e67e22', lw=2)
ax1.plot([0, 2*np.cos(th2)], [0, 2*np.sin(th2)], color='#e67e22', lw=2)
ax1.text(2.1*np.cos(th1), 2.1*np.sin(th1), 'A', fontsize=11, fontweight='bold', color='#e67e22')
ax1.text(2.1*np.cos(th2), 2.1*np.sin(th2), 'B', fontsize=11, fontweight='bold', color='#e67e22')

# Arc highlight
arc = mpatches.Arc((0, 0), 4, 4, theta1=np.rad2deg(th1), theta2=np.rad2deg(th2), color='#e74c3c', lw=3)
ax1.add_patch(arc)

# Radius label
ax1.text(1, 0.1, 'r', fontsize=11, fontweight='bold', color='#e67e22')

# Central angle label
arc_l = mpatches.Arc((0, 0), 0.6, 0.6, theta1=np.rad2deg(th1), theta2=np.rad2deg(th2), color='#e74c3c', lw=2)
ax1.add_patch(arc_l)
mid_a = (th1+th2)/2
ax1.text(0.45*np.cos(mid_a), 0.45*np.sin(mid_a), 'n°', ha='center', fontsize=10, fontweight='bold', color='#e74c3c')

# Labels
ax1.text(2.3*np.cos((th1+th2)/2), 2.3*np.sin((th1+th2)/2), '弧 l',
         ha='center', fontsize=10, fontweight='bold', color='#e74c3c')
ax1.text(0, -2.4, '扇形', ha='center', fontsize=13, fontweight='bold', color='#1a1a2e')

# Right: formulas
ax2.text(0, 1.8, '弧长公式', ha='center', fontsize=14, fontweight='bold', color='#e74c3c')
ax2.text(0, 0.8, 'l = nπr / 180', ha='center', fontsize=18, fontweight='bold', color='#333',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff3e0', edgecolor='#ffcc80', lw=2))

ax2.text(0, -0.5, '扇形面积公式', ha='center', fontsize=14, fontweight='bold', color='#e67e22')
ax2.text(0, -1.3, 'S = nπr² / 360', ha='center', fontsize=18, fontweight='bold', color='#333',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff3e0', edgecolor='#ffcc80', lw=2))

ax2.text(0, -2.0, 'S = ½lr', ha='center', fontsize=16, fontweight='bold', color='#8e44ad')
ax2.text(0, -2.4, '（l 为弧长，r 为半径，n 为圆心角度数）',
         ha='center', fontsize=9, color='#999')

fig.suptitle('弧长与扇形面积', fontsize=14, fontweight='bold', y=1.02, color='#1a1a2e')
plt.tight_layout()
plt.savefig('jun_circle_sector.svg', bbox_inches='tight', dpi=150, format='svg')
plt.close()

# ═══════════════ 7. 圆内接四边形 ═══════════════
fig, ax = plt.subplots(figsize=(5.5, 5.2))
ax.set_aspect('equal'); ax.set_xlim(-2.6, 2.6); ax.set_ylim(-2.6, 2.6)
ax.axis('off')
c = plt.Circle((0, 0), 2, fill=False, edgecolor='#1a6fc4', lw=2.5)
ax.add_patch(c)
ax.plot(0, 0, 'o', color='#333', ms=5)
ax.text(0, -0.2, 'O', ha='center', va='top', fontsize=12, fontweight='bold', color='#333')

# Quadrilateral vertices at 15°, 105°, 195°, 285°
pts_deg = [15, 105, 195, 285]
pts = [(2*np.cos(np.deg2rad(d)), 2*np.sin(np.deg2rad(d))) for d in pts_deg]
labels_pt = ['A', 'B', 'C', 'D']
offsets = [(0.2, 0.1), (0.1, 0.2), (-0.2, -0.1), (-0.1, -0.2)]
for j, (p, lab, off) in enumerate(zip(pts, labels_pt, offsets)):
    ax.plot(p[0], p[1], 'o', color='#e74c3c', ms=6, zorder=5)
    ax.text(p[0]+off[0], p[1]+off[1], lab, fontsize=12, fontweight='bold', color='#e74c3c')

# Connect quadrilateral
for j in range(4):
    ax.plot([pts[j][0], pts[(j+1)%4][0]], [pts[j][1], pts[(j+1)%4][1]],
            color='#e67e22', lw=2)
# Diagonals
ax.plot([pts[0][0], pts[2][0]], [pts[0][1], pts[2][1]],
        color='#999', lw=1.2, ls='--')
ax.plot([pts[1][0], pts[3][0]], [pts[1][1], pts[3][1]],
        color='#999', lw=1.2, ls='--')

# Angle A = angle at pts[0] = between vectors to D and B
# For angle marks, use arc at each vertex
# A: 180+15=195° to 15+90=105° (reflex)... let me just use angle markers
# Opposite angles A and C
# A is at 15°, between D(285°) and B(105°)
# The interior angle at A: vectors to D and B
ang_markers = [
    (pts[0], np.deg2rad(285-90), np.deg2rad(105-90), '∠A'),  # A
    (pts[1], np.deg2rad(105-90), np.deg2rad(195-90), '∠B'),  # B
    (pts[2], np.deg2rad(195-90+180), np.deg2rad(285-90+180), '∠C'),  # C
    (pts[3], np.deg2rad(285-90-180), np.deg2rad(15-90-180), '∠D'),  # D
]

# Simpler: just label the angles with text
# Angle A = ∠DAB, Angle C = ∠BCD
ax.text(pts[0][0]+0.35, pts[0][1]+0.3, '∠A', fontsize=9, fontweight='bold', color='#e74c3c')
ax.text(pts[2][0]-0.45, pts[2][1]-0.3, '∠C', fontsize=9, fontweight='bold', color='#e74c3c')
ax.text(pts[1][0]+0.3, pts[1][1]-0.3, '∠B', fontsize=9, fontweight='bold', color='#e67e22')
ax.text(pts[3][0]-0.3, pts[3][1]+0.3, '∠D', fontsize=9, fontweight='bold', color='#e67e22')

# Theorem: opposite angles sum to 180°
ax.text(0, -2.5, '对角互补：∠A + ∠C = 180°, ∠B + ∠D = 180°',
        ha='center', fontsize=11, fontweight='bold', color='#e74c3c')

# Also show the exterior angle property
ax2_text = '外角等于内对角：∠ADE = ∠ABC（D处延长线到E）'
ax.text(0, 2.55, '圆内接四边形', ha='center', fontsize=14, fontweight='bold', color='#1a1a2e')
plt.tight_layout()
plt.savefig('jun_circle_cyclic_quad.svg', bbox_inches='tight', dpi=150, format='svg')
plt.close()

print('7 张圆专题 SVG 图表已生成')
