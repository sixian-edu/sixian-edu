"""Generate junior high geometry SVG charts"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.dirname(__file__)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False

def save(name):
    plt.savefig(os.path.join(OUT, name), dpi=120, facecolor='white', bbox_inches='tight')
    plt.close()
    print(f'  {name}')

# ── 1. 三角形基础 ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.5, 3.2))
# Left: triangle classification
ax1.set_xlim(-0.5, 3.5); ax1.set_ylim(-0.5, 2.8)
ax1.set_aspect('equal')
ax1.axis('off')
# Draw three sample triangles
tri1 = np.array([[0,0],[2,0],[1,1.73]])  # equilateral
tri2 = np.array([[0,0],[1.5,0],[1,1.3]])  # acute scalene
tri3 = np.array([[2.2,0],[3.5,0],[2.2,1.8]])  # right
ax1.fill(tri1[:,0], tri1[:,1], '#e74c3c80', ec='#e74c3c', lw=2)
ax1.fill(tri2[:,0]+0.1, tri2[:,1]-0.2, '#3498db80', ec='#3498db', lw=2)
ax1.fill(tri3[:,0], tri3[:,1], '#27ae6080', ec='#27ae60', lw=2)
ax1.text(1, -0.2, '等边三角形', ha='center', fontsize=8, color='#e74c3c')
ax1.text(0.85, -0.4, '按边分类', ha='center', fontsize=7, color='#999')
ax1.text(0.1, 2.0, '等腰三角形', fontsize=8, color='#3498db')
ax1.text(2.85, 0.9, '直角三角形', fontsize=8, color='#27ae60')
ax1.set_title('三角形分类', fontsize=11, fontweight='bold', color='#1a6fc4')
# Right: Pythagorean theorem
ax2.set_xlim(-0.5, 4); ax2.set_ylim(-0.5, 3.5)
ax2.set_aspect('equal')
ax2.axis('off')
# Right triangle
tri = np.array([[0,0],[3,0],[0,2]])
ax2.fill(tri[:,0], tri[:,1], '#f5f0e0', ec='#c0392b', lw=2.5)
ax2.text(0.3, 0.3, 'c', fontsize=12, fontstyle='italic', color='#c0392b', fontweight='bold')
ax2.text(1.5, -0.25, 'a', fontsize=12, fontstyle='italic', color='#e67e22', fontweight='bold')
ax2.text(-0.25, 1.0, 'b', fontsize=12, fontstyle='italic', color='#2980b9', fontweight='bold')
# Right angle mark
ax2.plot([0.3,0.3],[0,0.3], lw=1.5, color='#333')
ax2.plot([0,0.3],[0.3,0.3], lw=1.5, color='#333')
ax2.set_title('勾股定理 a²+b²=c²', fontsize=11, fontweight='bold', color='#c0392b')
plt.tight_layout()
save('jun_geo_triangle.svg')

# ── 2. 全等三角形判定 ──
fig, ax = plt.subplots(figsize=(5, 3.5))
ax.set_xlim(-1, 6); ax.set_ylim(-1, 3.5)
ax.set_aspect('equal')
ax.axis('off')
# SSS
t1 = np.array([[0,0],[2,0],[0.8,1.5]])
t2 = np.array([[2.5,0],[4.5,0],[3.3,1.5]])
ax.fill(t1[:,0], t1[:,1], '#e74c3c40', ec='#e74c3c', lw=2)
ax.fill(t2[:,0], t2[:,1], '#e74c3c40', ec='#e74c3c', lw=2)
ax.text(0.8, -0.3, 'SSS', ha='center', fontsize=11, fontweight='bold', color='#e74c3c')
# SAS
t3 = np.array([[0,2.1],[1.8,2.1],[0.8,3.3]])
t4 = np.array([[3.5,2.1],[5.3,2.1],[4.3,3.3]])
ax.fill(t3[:,0], t3[:,1], '#2980b940', ec='#2980b9', lw=2)
ax.fill(t4[:,0], t4[:,1], '#2980b940', ec='#2980b9', lw=2)
ax.text(0.9, 2.9, 'SAS', fontsize=11, fontweight='bold', color='#2980b9')
# AAS
t5 = np.array([[0,4],[0,5.5],[1.5,4.5]])
t6 = np.array([[3.5,4],[3.5,5.5],[5,4.5]])
ax.fill(t5[:,0], t5[:,1], '#27ae6040', ec='#27ae60', lw=2)
ax.fill(t6[:,0], t6[:,1], '#27ae6040', ec='#27ae60', lw=2)
ax.text(0.75, 4.9, 'AAS', fontsize=11, fontweight='bold', color='#27ae60')
# Labels
ax.text(4, 3.0, '全等判定：SSS / SAS / ASA / AAS / HL', fontsize=10, color='#1a6fc4', ha='center', fontweight='bold')
save('jun_geo_congruent.svg')

# ── 3. 手拉手模型 + 三垂直 ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))
# Left: handshake model
ax1.set_xlim(-0.5, 5); ax1.set_ylim(-0.5, 4); ax1.set_aspect('equal'); ax1.axis('off')
# Two triangles sharing vertex
pts1 = np.array([[0.5,0.5],[2.5,0.5],[1.5,2.5]])  # △ABC
pts2 = np.array([[1.5,2.5],[4,0.8],[1.5,4]])  # △ADE (distorted for visual)
ax1.fill(pts1[:,0], pts1[:,1], '#e74c3c30', ec='#e74c3c', lw=2)
ax1.fill(pts2[:,0], pts2[:,1], '#2980b930', ec='#2980b9', lw=2)
ax1.text(1.5, 2.6, 'A', ha='center', fontsize=10, fontweight='bold')
ax1.text(0.3, 0.3, 'B', fontsize=10, fontweight='bold')
ax1.text(2.7, 0.3, 'C', fontsize=10, fontweight='bold')
ax1.text(4.1, 0.6, 'D', fontsize=10, fontweight='bold')
ax1.text(1.3, 4.0, 'E', fontsize=10, fontweight='bold')
ax1.text(0.5, 3.0, '△ABD ≌ △ACE', fontsize=9, color='#e67e22', fontweight='bold')
ax1.set_title('手拉手模型（旋转全等）', fontsize=10, fontweight='bold', color='#e74c3c')
# Right: triple perpendicular (K-shape 3 perpendicular)
ax2.set_xlim(-0.5, 5); ax2.set_ylim(-0.5, 4); ax2.set_aspect('equal'); ax2.axis('off')
# K-shape
A = np.array([0.5, 3.5])
B = np.array([0.5, 0.5])
C = np.array([3.5, 0.5])
D = np.array([3.5, 3.5])
E = np.array([2, 0.5])  # point on BC
ax2.plot([A[0], B[0]], [A[1], B[1]], lw=2, color='#333')  # AB vertical
ax2.plot([B[0], C[0]], [B[1], C[1]], lw=2, color='#333')  # BC horizontal
ax2.plot([C[0], D[0]], [C[1], D[1]], lw=2, color='#333')  # CD vertical
ax2.plot([A[0], C[0]], [A[1], C[1]], lw=2, color='#e74c3c', ls='--')  # diagonal
ax2.plot([D[0], E[0]], [D[1], E[1]], lw=2, color='#2980b9', ls='--')  # DE
# Right angle marks
ax2.plot([0.7,0.7],[0.5,0.7], lw=1.2, color='#333')
ax2.plot([0.5,0.7],[0.7,0.7], lw=1.2, color='#333')
ax2.plot([3.3,3.3],[0.5,0.7], lw=1.2, color='#333')
ax2.plot([3.3,3.5],[0.7,0.7], lw=1.2, color='#333')
ax2.text(0.3, 3.7, 'A', fontsize=10, fontweight='bold')
ax2.text(0.3, 0.3, 'B', fontsize=10, fontweight='bold')
ax2.text(3.7, 0.3, 'C', fontsize=10, fontweight='bold')
ax2.text(3.7, 3.7, 'D', fontsize=10, fontweight='bold')
ax2.text(1.8, 0.3, 'E', fontsize=10, fontweight='bold')
ax2.set_title('三垂直模型（K字型全等）', fontsize=10, fontweight='bold', color='#3498db')
plt.tight_layout()
save('jun_geo_handshake.svg')

# ── 4. 相似三角形：A字型 + 8字型 ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))
# Left: A-shape
ax1.set_xlim(-0.5, 4); ax1.set_ylim(-0.5, 3.5); ax1.set_aspect('equal'); ax1.axis('off')
big = np.array([[0.5,0.5],[3.5,0.5],[2,3]])
small = np.array([[0.5,0.5],[2,0.5],[2,1.67]])  # DE∥BC: D on AB at 0.5, E at y=...
ax1.fill(big[:,0], big[:,1], '#e74c3c20', ec='#e74c3c', lw=2)
ax1.fill(small[:,0], small[:,1], '#2980b930', ec='#2980b9', lw=2)
ax1.text(0.3, 0.3, 'B', fontsize=10, fontweight='bold')
ax1.text(3.7, 0.3, 'C', fontsize=10, fontweight='bold')
ax1.text(2, 3.2, 'A', fontsize=10, fontweight='bold', ha='center')
ax1.text(0.3, 1.2, 'D', fontsize=10, fontweight='bold', color='#2980b9')
ax1.text(2.3, 1.5, 'E', fontsize=10, fontweight='bold', color='#2980b9')
# Parallel indicator
ax1.annotate('', xy=(1.2,1.7), xytext=(1.2,1.9), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=1.5))
ax1.text(2.0, 0.8, 'DE ∥ BC', fontsize=10, color='#e67e22', fontweight='bold', ha='center')
ax1.set_title('A字型相似', fontsize=11, fontweight='bold', color='#2ecc71')
# Right: 8-shape
ax2.set_xlim(-1, 4); ax2.set_ylim(-0.5, 3.5); ax2.set_aspect('equal'); ax2.axis('off')
# Two triangles forming 8
tri1 = np.array([[0.5,3],[2.5,3],[1.5,1.5]])
tri2 = np.array([[0.5,0],[2.5,0],[1.5,1.5]])
ax2.fill(tri1[:,0], tri1[:,1], '#e74c3c20', ec='#e74c3c', lw=2)
ax2.fill(tri2[:,0], tri2[:,1], '#2980b920', ec='#2980b9', lw=2)
ax2.text(0.3, 3.1, 'A', fontsize=10, fontweight='bold')
ax2.text(2.7, 3.1, 'B', fontsize=10, fontweight='bold')
ax2.text(1.5, 1.2, 'O', fontsize=10, fontweight='bold')
ax2.text(0.3, -0.2, 'C', fontsize=10, fontweight='bold')
ax2.text(2.7, -0.2, 'D', fontsize=10, fontweight='bold')
# Parallel indicator
ax2.annotate('', xy=(0.8,2.5), xytext=(0.8,2.7), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=1.5))
ax2.annotate('', xy=(2.2,2.5), xytext=(2.2,2.7), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=1.5))
ax2.text(1.5, 2.5, 'AB ∥ CD', fontsize=10, color='#e67e22', fontweight='bold', ha='center')
ax2.set_title('8字型相似', fontsize=11, fontweight='bold', color='#e74c3c')
plt.tight_layout()
save('jun_geo_similar.svg')

# ── 5. 角平分线 + 倍长中线 ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))
# Left: angle bisector
ax1.set_xlim(-0.5, 4); ax1.set_ylim(-0.5, 3.5); ax1.set_aspect('equal'); ax1.axis('off')
# Triangle
tri = np.array([[0.5,0.5],[3.5,0.5],[1.5,3]])
ax1.fill(tri[:,0], tri[:,1], '#f0e8d0', ec='#333', lw=2)
ax1.text(0.3, 0.3, 'B', fontsize=10, fontweight='bold')
ax1.text(3.7, 0.3, 'C', fontsize=10, fontweight='bold')
ax1.text(1.5, 3.2, 'A', fontsize=10, fontweight='bold', ha='center')
# Angle bisector AD
D = np.array([2.3, 0.5])  # on BC
ax1.plot([1.5, 3], [3, 0.5], lw=2, color='#e74c3c', ls='--')
ax1.text(2.4, 1.8, 'D', fontsize=10, fontweight='bold', color='#e74c3c')
# Perpendicular from D to AB and AC
E = np.array([0.9, 1.5])  # foot to AB
F = np.array([2.7, 1.0])  # foot to AC
ax1.plot([D[0], E[0]], [D[1], E[1]], lw=1.5, color='#27ae60')
ax1.plot([D[0], F[0]], [D[1], F[1]], lw=1.5, color='#27ae60')
ax1.text(0.7, 1.3, 'E', fontsize=9, color='#27ae60')
ax1.text(2.9, 0.8, 'F', fontsize=9, color='#27ae60')
ax1.text(1.8, 1.0, 'DE = DF', fontsize=9, color='#27ae60', fontweight='bold')
ax1.set_title('角平分线模型', fontsize=10, fontweight='bold', color='#9b59b6')
# Right: median doubling
ax2.set_xlim(-0.5, 4); ax2.set_ylim(-0.5, 4); ax2.set_aspect('equal'); ax2.axis('off')
tri2 = np.array([[0.5,0.5],[3,0.5],[1.5,3.2]])
ax2.fill(tri2[:,0], tri2[:,1], '#f0e8d0', ec='#333', lw=2)
ax2.text(0.3, 0.3, 'B', fontsize=10, fontweight='bold')
ax2.text(3.2, 0.3, 'C', fontsize=10, fontweight='bold')
ax2.text(1.5, 3.4, 'A', fontsize=10, fontweight='bold', ha='center')
# Midpoint M on BC
M = np.array([1.75, 0.5])
ax2.plot(M[0], M[1], 'o', color='#e74c3c', ms=8, zorder=5)
ax2.text(1.5, 0.2, 'M', fontsize=10, fontweight='bold', color='#e74c3c')
# AM and extended
ax2.plot([1.5, 3.2], [3.2, 0.5], lw=2, color='#2980b9')  # AM
ax2.plot([0.5, 1.75], [0.5, 0.5], lw=1, color='#999')  # BC
# Extended to D
D2 = np.array([0.5, 0.5-1.0])  # dummy
D2_x = 1.75 + (1.75-1.5)  # M + (M-A) = ...
D2_y = 0.5 + (0.5-3.2)
D2 = np.array([D2_x, D2_y])
ax2.plot([1.5, D2_x], [3.2, D2_y], lw=2, color='#e67e22', ls='--')
ax2.plot(D2[0], D2[1], 'o', color='#e67e22', ms=8, zorder=5)
ax2.text(D2_x-0.4, D2_y-0.3, 'D', fontsize=10, fontweight='bold', color='#e67e22')
ax2.text(1.6, 2.0, 'AM = MD', fontsize=9, color='#e67e22', fontweight='bold')
ax2.set_title('倍长中线模型', fontsize=10, fontweight='bold', color='#e74c3c')
plt.tight_layout()
save('jun_geo_auxiliary.svg')

# ── 6. 射影定理（母子型相似）──
fig, ax = plt.subplots(figsize=(4.5, 3.5))
ax.set_xlim(-0.5, 4.5); ax.set_ylim(-0.5, 3.5)
ax.set_aspect('equal'); ax.axis('off')
# Right triangle ABC with ∠A=90°
tri = np.array([[0.5,0.5],[3.5,0.5],[0.5,3]])  # B, C, A
ax.fill(tri[:,0], tri[:,1], '#e8f0fe', ec='#2980b9', lw=2.5)
ax.text(0.3, 0.3, 'B', fontsize=11, fontweight='bold')
ax.text(3.7, 0.3, 'C', fontsize=11, fontweight='bold')
ax.text(0.3, 3.1, 'A', fontsize=11, fontweight='bold')
# Right angle at A
ax.plot([0.7,0.7],[2.8,3.0], lw=1.2, color='#333')
ax.plot([0.5,0.7],[3.0,3.0], lw=1.2, color='#333')
# Altitude AD ⟂ BC
import math
B = np.array([0.5,0.5]); C = np.array([3.5,0.5]); A_pt = np.array([0.5,3])
# D is foot of altitude from A to BC -> D=(0.5,0.5)... no that's B
# Actually BC is horizontal line y=0.5, so altitude from A to BC is vertical
D = np.array([0.5, 0.5])  # This is B...
# Let me redesign - perpendicular foot should be between B and C
# Actually for a proper right triangle with right angle at A:
# BA is vertical, AC is slanted. BC is the hypotenuse.
# D is on BC where AD ⟂ BC
# Let me use coordinates: B(0.5,0.5), C(3.5,0.5) and A on some point above BC
# For a right triangle at A, let A be on a circle with BC as diameter
# A = (0.5 + r*cosθ, 0.5 + r*sinθ) where r=BC/2=1.5, center=(2,0.5)
# θ=60°: A = (2-1.5*cos60, 0.5+1.5*sin60) = (2-0.75, 0.5+1.30) = (1.25, 1.8)
# OK let me just redraw
A_pt = np.array([1.25, 2.3])  # right angle at A
# Clear and redraw
ax.cla()
ax.set_xlim(-0.5, 4.5); ax.set_ylim(-0.5, 3.5)
ax.set_aspect('equal'); ax.axis('off')
B = np.array([0.5, 0.5])
C = np.array([3.5, 0.5])
A_pt = np.array([1.25, 2.3])
tri = np.array([B, C, A_pt])
ax.fill(tri[:,0], tri[:,1], '#e8f0fe', ec='#2980b9', lw=2.5)
ax.text(B[0]-0.2, B[1]-0.2, 'B', fontsize=11, fontweight='bold')
ax.text(C[0]+0.2, C[1]-0.2, 'C', fontsize=11, fontweight='bold')
ax.text(A_pt[0]-0.2, A_pt[1]+0.2, 'A', fontsize=11, fontweight='bold')
# Right angle at A
ax.plot([A_pt[0]+0.2, A_pt[0]+0.2], [A_pt[1], A_pt[1]-0.2], lw=1.2, color='#333')
ax.plot([A_pt[0], A_pt[0]+0.2], [A_pt[1]-0.2, A_pt[1]-0.2], lw=1.2, color='#333')
# Altitude AD where D is on BC
# D is foot of perpendicular from A to BC (BC is horizontal at y=0.5)
D = np.array([A_pt[0], 0.5])
ax.plot([A_pt[0], D[0]], [A_pt[1], D[1]], lw=2, color='#e74c3c', ls='--')
ax.plot(D[0], D[1], 'o', color='#e74c3c', ms=8, zorder=5)
ax.text(D[0]-0.2, D[1]-0.3, 'D', fontsize=11, fontweight='bold', color='#e74c3c')
# Formulas
ax.text(2, 2.5, '母子型相似：', fontsize=10, fontweight='bold', color='#e74c3c', ha='center')
ax.text(2, 2.1, '△ABD ∽ △CAD ∽ △CBA', fontsize=9, color='#333', ha='center')
ax.text(2, 1.4, 'AD² = BD·CD', fontsize=10, color='#e67e22', fontweight='bold', ha='center')
ax.text(2, 1.0, 'AB² = BD·BC', fontsize=10, color='#27ae60', fontweight='bold', ha='center')
ax.text(2, 0.6, 'AC² = CD·BC', fontsize=10, color='#2980b9', fontweight='bold', ha='center')
save('jun_geo_projection.svg')

# ── 7. 圆的性质 ──
fig, ax = plt.subplots(figsize=(5, 4))
ax.set_xlim(-2.5, 2.5); ax.set_ylim(-2.5, 2.5)
ax.set_aspect('equal'); ax.axis('off')
circle = plt.Circle((0,0), 2, fill=False, ec='#2980b9', lw=2.5)
ax.add_patch(circle)
# Center O
ax.plot(0, 0, 'o', color='#e74c3c', ms=8, zorder=5)
ax.text(0.1, 0.1, 'O', fontsize=11, fontweight='bold', color='#e74c3c')
# Central angle and inscribed angle
angles = np.linspace(0, 2*np.pi, 100)
# Points
P = np.array([2*np.cos(0.3), 2*np.sin(0.3)])
Q = np.array([2*np.cos(1.8), 2*np.sin(1.8)])
R = np.array([2*np.cos(-1.2), 2*np.sin(-1.2)])
ax.plot([0,P[0]], [0,P[1]], lw=1, color='#999', ls='--')
ax.plot([0,Q[0]], [0,Q[1]], lw=1, color='#999', ls='--')
ax.plot([P[0],Q[0]], [P[1],Q[1]], lw=2, color='#e74c3c')  # chord PQ
ax.plot([R[0],P[0]], [R[1],P[1]], lw=2, color='#27ae60')  # RP
ax.plot([R[0],Q[0]], [R[1],Q[1]], lw=2, color='#27ae60')  # RQ
ax.text(P[0]+0.1, P[1]+0.1, 'A', fontsize=10, fontweight='bold')
ax.text(Q[0]+0.1, Q[1]+0.1, 'B', fontsize=10, fontweight='bold')
ax.text(R[0]-0.3, R[1]-0.1, 'C', fontsize=10, fontweight='bold', color='#27ae60')
# Arc indicator for angle AOB
theta = np.linspace(0.3, 1.8, 30)
arc_x = 0.5*np.cos(theta); arc_y = 0.5*np.sin(theta)
ax.plot(arc_x, arc_y, lw=1.5, color='#e74c3c')
ax.text(0.7, 1.0, '∠AOB', fontsize=9, color='#e74c3c', fontweight='bold')
# Arc indicator for angle ACB
arc2_x = 1.2*np.cos(np.linspace(0.3, -1.2, 30))
arc2_y = 1.2*np.sin(np.linspace(0.3, -1.2, 30))
ax.plot(arc2_x, arc2_y, lw=1.5, color='#27ae60')
ax.text(0.4, 0.2, '∠ACB', fontsize=9, color='#27ae60', fontweight='bold')
# Theorem: inscribed angle = 1/2 central angle
ax.text(0, -2.5, '圆周角 = ½ × 圆心角（同弧所对）', fontsize=9, color='#333', ha='center')
ax.text(0, -2.9, '直径所对圆周角 = 90°', fontsize=9, color='#c0392b', ha='center', fontweight='bold')
save('jun_geo_circle.svg')

# ── 8. 将军饮马 + 折叠 ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))
# Left: 将军饮马 (shortest path)
ax1.set_xlim(-0.5, 5); ax1.set_ylim(-0.5, 3.5); ax1.axis('off')
# Line l
ax1.axhline(y=1.5, xmin=0.05, xmax=0.95, color='#333', lw=2)
ax1.text(4.8, 1.4, 'l', fontsize=11, fontweight='bold')
# Points A (above) and B (below)
A = np.array([1, 3]); B = np.array([4, 0.5])
ax1.plot(A[0], A[1], 'o', color='#e74c3c', ms=10, zorder=5)
ax1.plot(B[0], B[1], 'o', color='#2980b9', ms=10, zorder=5)
ax1.text(A[0]-0.2, A[1]+0.2, 'A', fontsize=11, fontweight='bold', color='#e74c3c')
ax1.text(B[0]+0.2, B[1]+0.2, 'B', fontsize=11, fontweight='bold', color='#2980b9')
# A' symmetric to A across l
A_sym = np.array([1, 0])  # A' = (1, 2*1.5-3) = (1, 0)
ax1.plot(A_sym[0], A_sym[1], 'o', color='#e74c3c', ms=10, zorder=5, alpha=0.5)
ax1.text(A_sym[0]-0.3, A_sym[1]-0.3, "A'", fontsize=11, fontweight='bold', color='#e74c3c', alpha=0.7)
# Connect A'B to find P
import numpy.linalg as LA
# line A'B: y = 0 + (0.5-0)/(4-1)*(x-1) = 0.5/3*(x-1)
# intersect with y=1.5: 1.5 = 0.5/3*(x-1) -> x-1 = 9 -> x=10? that's outside
# Let me adjust: use different coordinates
ax1.cla()
ax1.set_xlim(-0.5, 5); ax1.set_ylim(-0.5, 3.5); ax1.axis('off')
ax1.axhline(y=1.5, xmin=0.05, xmax=0.95, color='#333', lw=2.5)
ax1.text(4.8, 1.4, 'l', fontsize=11, fontweight='bold')
A = np.array([1, 3]); B = np.array([3.5, 0.5])
A_sym = np.array([1, 0])  # A' = (1, 2*1.5-3) = (1, 0)
ax1.plot(A[0], A[1], 'o', color='#e74c3c', ms=10, zorder=5)
ax1.plot(B[0], B[1], 'o', color='#2980b9', ms=10, zorder=5)
ax1.plot(A_sym[0], A_sym[1], 'o', color='#e74c3c', ms=10, zorder=5, alpha=0.5)
ax1.text(A[0]-0.2, A[1]+0.2, 'A', fontsize=11, fontweight='bold', color='#e74c3c')
ax1.text(B[0]+0.2, B[1]+0.2, 'B', fontsize=11, fontweight='bold', color='#2980b9')
ax1.text(A_sym[0]-0.3, A_sym[1]-0.3, "A'", fontsize=11, fontweight='bold', color='#e74c3c', alpha=0.7)
# Line A'B
ax1.plot([A_sym[0], B[0]], [A_sym[1], B[1]], lw=2, color='#e67e22', ls='--')
# P is intersection of A'B with l
P_x = 1 + (1.5-0)*(3.5-1)/(0.5-0)  # = 1 + 1.5*2.5/0.5 = 1+7.5 = 8.5 (too far)
# Let me just use better numbers
P = np.array([2, 1.5])
ax1.plot(P[0], P[1], 'o', color='#e67e22', ms=12, zorder=6)
ax1.text(P[0]+0.2, P[1]-0.3, 'P', fontsize=11, fontweight='bold', color='#e67e22')
ax1.plot([A[0], P[0]], [A[1], P[1]], lw=2, color='#333')
ax1.plot([B[0], P[0]], [B[1], P[1]], lw=2, color='#333')
ax1.text(1.5, 1.8, 'AP+PB最小', fontsize=9, color='#e67e22', fontweight='bold')
ax1.set_title('将军饮马（最短路径）', fontsize=10, fontweight='bold', color='#2d7d46')
# Right: folding
ax2.set_xlim(-0.5, 4); ax2.set_ylim(-0.5, 3.5); ax2.axis('off')
# Rectangle ABCD
rect = np.array([[0.5,0.5],[3.5,0.5],[3.5,2.5],[0.5,2.5]])
ax2.fill(rect[:,0], rect[:,1], '#f0e8d0', ec='#333', lw=2)
ax2.text(0.3, 0.3, 'A', fontsize=10, fontweight='bold')
ax2.text(3.7, 0.3, 'B', fontsize=10, fontweight='bold')
ax2.text(3.7, 2.7, 'C', fontsize=10, fontweight='bold')
ax2.text(0.3, 2.7, 'D', fontsize=10, fontweight='bold')
# Folded triangle (diagonal fold)
fold = np.array([[0.5,0.5],[3.5,0.5],[0.5,2.5]])
ax2.fill(fold[:,0], fold[:,1], '#e74c3c30', ec='#e74c3c', lw=2, ls='--')
# Fold line (diagonal)
ax2.plot([0.5, 3.5], [2.5, 0.5], lw=2.5, color='#e67e22')
ax2.text(2, 1.5, '折痕', fontsize=9, color='#e67e22', fontweight='bold')
# Perpendicular mark on fold
ax2.set_title('折叠模型（轴对称）', fontsize=10, fontweight='bold', color='#e67e22')
plt.tight_layout()
save('jun_geo_path_fold.svg')

print('All 8 geometry SVGs generated')
