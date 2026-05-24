"""高中物理 电磁学+力学模型 专业SVG图表"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False

OUT = r'C:\Users\21342\Desktop\sixian-edu\资料\charts'

# ════════════════════════════════════════
# 一、电磁学（8张）
# ════════════════════════════════════════

# 1. 电场线分布——正负点电荷
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.5))
plt.subplots_adjust(left=0.05, right=0.95, wspace=0.25, bottom=0.08, top=0.92)

# 正电荷电场线（放射状）
for ax, q in [(ax1, 1), (ax2, -1)]:
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.scatter([0], [0], c='red' if q>0 else 'blue', s=120, zorder=5)
    ax.text(0.1, -0.3, '+' if q>0 else '−', fontsize=16, color='white', fontweight='bold', zorder=6)
    # 放射电场线
    for theta in np.linspace(0, 2*np.pi, 16, endpoint=False):
        dx = np.cos(theta)
        dy = np.sin(theta)
        r_start = 0.4
        r_end = 2.8 if q>0 else 2.8
        if q>0:
            ax.arrow(r_start*dx, r_start*dy, (r_end-r_start-0.2)*dx, (r_end-r_start-0.2)*dy,
                     head_width=0.15, head_length=0.15, fc='#e74c3c', ec='#e74c3c', alpha=0.7)
        else:
            ax.arrow(-r_start*dx, -r_start*dy, -(r_end-r_start-0.2)*dx, -(r_end-r_start-0.2)*dy,
                     head_width=0.15, head_length=0.15, fc='#3498db', ec='#3498db', alpha=0.7)
    ax.axhline(0, color='gray', linewidth=0.3)
    ax.axvline(0, color='gray', linewidth=0.3)
    ax.grid(True, alpha=0.15)
    ax.set_title('正点电荷' if q>0 else '负点电荷', fontsize=12, color='#1a1a2e')

fig.suptitle('点电荷的电场线分布', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'phy_efield.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 2. 带电粒子在匀强磁场中的匀速圆周运动
fig, ax = plt.subplots(figsize=(5, 5))
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.92)
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-3.5, 3.5)
ax.set_aspect('equal')

# 画圆轨迹
theta = np.linspace(0, 2*np.pi, 400)
R = 2.5
ax.plot(R*np.cos(theta), R*np.sin(theta), 'b-', linewidth=2, alpha=0.7)

# 坐标轴
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)

# 标注半径
ax.annotate('', xy=(0,0), xytext=(R,0), arrowprops=dict(arrowstyle='<->', color='#e67e22', lw=2))
ax.text(R/2, -0.3, 'r', fontsize=14, color='#e67e22', ha='center', fontweight='bold')

# 速度和洛伦兹力
# 在几个点标注速度方向和力方向
for angle in [np.pi/3, np.pi, 4*np.pi/3]:
    x0, y0 = R*np.cos(angle), R*np.sin(angle)
    # 速度方向（切线方向）
    vx, vy = -R*np.sin(angle), R*np.cos(angle)
    v_len = 0.8
    ax.arrow(x0, y0, v_len*vx/R, v_len*vy/R, head_width=0.15, head_length=0.15, fc='#27ae60', ec='#27ae60', linewidth=2)
    # 洛伦兹力方向（指向圆心）
    fx, fy = -x0, -y0
    f_len = 0.3
    ax.arrow(x0, y0, f_len*fx/R, f_len*fy/R, head_width=0.15, head_length=0.15, fc='#e74c3c', ec='#e74c3c', linewidth=2)

# 标注
ax.text(1.0, 2.8, 'v', fontsize=13, color='#27ae60', fontweight='bold')
ax.text(1.5, -1.8, 'F洛', fontsize=13, color='#e74c3c', fontweight='bold')

# 磁场方向
for i in range(-3, 4):
    for j in range(-3, 4):
        if i**2+j**2 < 9:
            ax.scatter(i*0.8, j*0.8, marker='.', c='#bbb', s=8, alpha=0.5)
ax.text(-3.3, 3.3, '×  ×  ×  ×  ×', fontsize=11, color='#888')
ax.text(-3.3, 3.0, '×  ×  ×  ×  ×', fontsize=11, color='#888')
ax.text(-3.3, -3.3, '磁场 ⊙ 垂直纸面向外', fontsize=11, color='#888')

ax.set_title('带电粒子在匀强磁场中的匀速圆周运动', fontsize=12, color='#1a1a2e')
ax.grid(True, alpha=0.15)
fig.savefig(os.path.join(OUT, 'phy_cyclotron.svg'), dpi=120, facecolor='white')
plt.close()

# 3. 导体切割磁感线——动生电动势
fig, ax = plt.subplots(figsize=(5.5, 4))
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.92)
# 磁场区域
ax.add_patch(plt.Rectangle((-2, -0.5), 4, 3, facecolor='#3498db', alpha=0.08, edgecolor='#3498db', linewidth=1))
ax.text(-0.3, 1.2, '匀强磁场 B', fontsize=12, color='#3498db', ha='center', alpha=0.6)
# 导轨
ax.plot([-2, 2], [-0.3, -0.3], 'k-', linewidth=3)  # 下导轨
ax.plot([-2, 2], [2.3, 2.3], 'k-', linewidth=3)   # 上导轨
# 导体棒
ax.add_patch(plt.Rectangle((0.3, -0.3), 0.6, 2.6, facecolor='#e74c3c', alpha=0.6, edgecolor='#e74c3c', linewidth=2))
ax.annotate('导体棒', xy=(0.6, 1.5), xytext=(1.5, 2.2), fontsize=11, color='#e74c3c',
            arrowprops=dict(arrowstyle='->', color='#e74c3c'))
# 速度箭头
ax.annotate('', xy=(0.6, 1.15), xytext=(1.8, 1.15), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=3))
ax.text(1.2, 1.5, 'v', fontsize=14, color='#e67e22', ha='center', fontweight='bold')
# 感应电流方向
ax.annotate('', xy=(1.0, 2.3), xytext=(1.0, -0.3), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax.text(1.3, 1.0, 'I', fontsize=13, color='#e74c3c', fontweight='bold')
# 公式
ax.text(-1.8, -0.8, 'ε = BLv', fontsize=14, color='#1a1a2e', fontweight='bold',
        bbox=dict(facecolor='#fef9e7', edgecolor='#f9e79f', boxstyle='round,pad=0.3'))
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1, 3)
ax.axis('off')
ax.set_title('导体切割磁感线——动生电动势', fontsize=13, color='#1a1a2e', pad=10)
fig.savefig(os.path.join(OUT, 'phy_emf.svg'), dpi=120, facecolor='white')
plt.close()

# 4. 正弦交流电图像
fig, ax = plt.subplots(figsize=(5.5, 3))
plt.subplots_adjust(left=0.08, bottom=0.15, right=0.95, top=0.9)
x = np.linspace(0, 4*np.pi, 400)
y = np.sin(x)
ax.plot(x, y, 'b-', linewidth=2.5)
ax.plot(x, np.cos(x), 'r--', linewidth=2, alpha=0.7)
# 标注
ax.annotate('峰值 Em', xy=(np.pi/2, 1), xytext=(np.pi/2+0.5, 1.3), fontsize=10, color='#e74c3c')
ax.annotate('周期 T', xy=(2*np.pi, 0.2), xytext=(2*np.pi+0.3, 0.6), fontsize=10, color='#e74c3c')
ax.annotate('', xy=(0, 0.15), xytext=(2*np.pi, 0.15), arrowprops=dict(arrowstyle='<->', color='#e74c3c', lw=1.5))
ax.axhline(0, color='gray', linewidth=0.8)
ax.set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi, 3*np.pi, 4*np.pi])
ax.set_xticklabels(['0', 'T/4', 'T/2', '3T/4', 'T', '3T/2', '2T'])
ax.set_ylabel('e / i', fontsize=12)
ax.set_xlabel('ωt', fontsize=12)
ax.legend(['e = Eₘ sin ωt', 'i = Iₘ sin(ωt−φ)'], fontsize=9)
ax.set_title('正弦式交流电——电动势与电流', fontsize=13, color='#1a1a2e')
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'phy_ac.svg'), dpi=120, facecolor='white')
plt.close()

# 5. 闭合电路欧姆定律
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.9)
# 画电路示意（抽象）
ax.plot([-2, 2], [1, 1], 'k-', linewidth=2)  # 上导线
ax.plot([-2, 2], [-1, -1], 'k-', linewidth=2)  # 下导线
ax.plot([-2, -2], [-1, 1], 'k-', linewidth=2)  # 左导线
ax.plot([2, 2], [-1, 1], 'k-', linewidth=2)    # 右导线

# 电源
ax.add_patch(plt.Rectangle((-2.3, -0.3), 0.6, 0.6, facecolor='white', edgecolor='#2c3e50', linewidth=2))
ax.plot([-2.3, -2.3], [-0.1, 0.1], 'k-', linewidth=3)
ax.plot([-2.0, -2.0], [-0.15, 0.15], 'k-', linewidth=1.5)
ax.text(-2.0, -0.7, 'E, r', fontsize=12, color='#2c3e50', ha='center', fontweight='bold')

# 电阻
ax.add_patch(plt.Rectangle((1.5, -0.4), 1.0, 0.8, facecolor='#f5f0fa', edgecolor='#8e44ad', linewidth=2))
ax.text(2.0, 0, 'R', fontsize=13, color='#8e44ad', ha='center', va='center', fontweight='bold')

# 电流方向
ax.annotate('', xy=(-2, 0.5), xytext=(2, 0.5), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax.text(0, 0.7, 'I', fontsize=14, color='#e74c3c', ha='center', fontweight='bold')

# 公式
ax.text(0, -2.0, 'I = E/(R+r)', fontsize=16, color='#1a1a2e', ha='center', fontweight='bold',
        bbox=dict(facecolor='#e8f8f5', edgecolor='#1abc9c', boxstyle='round,pad=0.4'))
ax.text(0, -2.6, '路端电压 U = E − Ir = IR', fontsize=12, color='#555', ha='center')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 1.5)
ax.axis('off')
ax.set_title('闭合电路欧姆定律', fontsize=13, color='#1a1a2e', pad=8)
fig.savefig(os.path.join(OUT, 'phy_circuit_law.svg'), dpi=120, facecolor='white')
plt.close()

# 6. 电容器充放电曲线
fig, ax = plt.subplots(figsize=(5.5, 3.2))
plt.subplots_adjust(left=0.1, bottom=0.15, right=0.95, top=0.9)
t = np.linspace(0, 5, 200)
# RC充电：u=U(1-e^{-t/RC})
tau = 1
u_charge = 1 - np.exp(-t/tau)
i_charge = np.exp(-t/tau)
ax.plot(t, u_charge, 'b-', linewidth=2.5, label='充电 u_C(t)')
ax.plot(t, i_charge, 'r--', linewidth=2, label='充电 i(t)')
ax.plot(t, np.exp(-t/tau), 'g-.', linewidth=2, label='放电 u_C(t)')
ax.axhline(1, color='gray', linewidth=0.5, linestyle=':')
ax.axvline(tau, color='gray', linewidth=0.5, linestyle=':')
ax.text(tau+0.1, 0.05, 'τ=RC', fontsize=10, color='gray')
ax.set_xlabel('t', fontsize=12)
ax.set_ylabel('u / i', fontsize=12)
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.2)
ax.legend(fontsize=9)
ax.set_title('RC电路充放电曲线', fontsize=13, color='#1a1a2e')
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'phy_rc.svg'), dpi=120, facecolor='white')
plt.close()

# 7. 楞次定律——感应电流方向
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.9)
# 条形磁铁
ax.add_patch(plt.Rectangle((-0.6, 0.5), 1.2, 2.5, facecolor='#e74c3c', alpha=0.7, edgecolor='#c0392b', linewidth=2))
ax.add_patch(plt.Rectangle((-0.6, -2.0), 1.2, 2.5, facecolor='#3498db', alpha=0.7, edgecolor='#2980b9', linewidth=2))
ax.text(0, 1.8, 'N', fontsize=16, color='white', ha='center', fontweight='bold')
ax.text(0, -0.8, 'S', fontsize=16, color='white', ha='center', fontweight='bold')
ax.annotate('', xy=(0, 3.2), xytext=(0, 3.6), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax.text(0.3, 3.4, 'v', fontsize=12, color='#e74c3c', fontweight='bold')

# 线圈
circle = plt.Circle((0, -4), 1.2, fill=False, edgecolor='#e67e22', linewidth=3)
ax.add_patch(circle)
ax.text(1.5, -4.5, '线圈', fontsize=11, color='#e67e22')

# 感应电流
ax.annotate('', xy=(1.2, -4), xytext=(-1.2, -4),
            arrowprops=dict(arrowstyle='->', color='#8e44ad', lw=2, connectionstyle='arc3,rad=0.3'))
ax.text(-1.8, -4, 'I感', fontsize=11, color='#8e44ad', fontweight='bold')

# 原磁场方向
ax.annotate('', xy=(-0.3, -1.5), xytext=(-0.3, -3.5), arrowprops=dict(arrowstyle='->', color='#3498db', lw=2, ls='dotted'))
ax.text(-1.0, -2.5, 'B原↓', fontsize=10, color='#3498db')

# 感应磁场
ax.annotate('', xy=(0.3, -3.5), xytext=(0.3, -1.5), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=2, ls='dotted'))
ax.text(0.8, -2.5, 'B感↑', fontsize=10, color='#e67e22')

# 定律文字
ax.text(0, 0.2, '增反减同\n来拒去留', fontsize=11, color='#e74c3c', ha='center',
        bbox=dict(facecolor='#fef9e7', edgecolor='#f9e79f', boxstyle='round,pad=0.3'))

ax.set_xlim(-3, 3)
ax.set_ylim(-5.5, 4)
ax.axis('off')
ax.set_title('楞次定律——感应电流方向的判断', fontsize=13, color='#1a1a2e', pad=8)
fig.savefig(os.path.join(OUT, 'phy_lens.svg'), dpi=120, facecolor='white')
plt.close()

# 8. 变压器原理
fig, ax = plt.subplots(figsize=(5.5, 3))
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.1, top=0.9)
# 铁芯
ax.add_patch(plt.Rectangle((-0.3, -1.5), 0.6, 3, facecolor='#95a5a6', edgecolor='#7f8c8d', linewidth=1, alpha=0.5))
ax.add_patch(plt.Rectangle((-0.3, -1.5), 2.0, 0.6, facecolor='#95a5a6', edgecolor='#7f8c8d', linewidth=1, alpha=0.5))
ax.add_patch(plt.Rectangle((-0.3, 0.9), 2.0, 0.6, facecolor='#95a5a6', edgecolor='#7f8c8d', linewidth=1, alpha=0.5))
# 绕组
ax.text(-0.3, -0.5, '♒♒♒', fontsize=16, color='#e74c3c', ha='center')
ax.text(1.0, -0.5, '♒♒♒', fontsize=16, color='#3498db', ha='center')
# 标注
ax.annotate('', xy=(-1.5, 0), xytext=(-0.5, 0), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax.text(-1.0, 0.5, 'u₁', fontsize=13, color='#e74c3c', ha='center', fontweight='bold')
ax.annotate('', xy=(1.5, 0), xytext=(2.5, 0), arrowprops=dict(arrowstyle='->', color='#3498db', lw=2))
ax.text(2.0, 0.5, 'u₂', fontsize=13, color='#3498db', ha='center', fontweight='bold')
ax.text(-0.3, 1.8, 'n₁匝', fontsize=10, color='#e74c3c', ha='center')
ax.text(1.0, 1.8, 'n₂匝', fontsize=10, color='#3498db', ha='center')
# 公式
ax.text(0, -2.5, 'U₁/U₂ = n₁/n₂', fontsize=15, color='#1a1a2e', ha='center', fontweight='bold')
ax.text(0, -3.2, '理想变压器：P₁ = P₂，U₁I₁ = U₂I₂', fontsize=11, color='#555', ha='center')
ax.set_xlim(-2.5, 3)
ax.set_ylim(-3.5, 2.5)
ax.axis('off')
ax.set_title('变压器原理', fontsize=13, color='#1a1a2e', pad=8)
fig.savefig(os.path.join(OUT, 'phy_transformer.svg'), dpi=120, facecolor='white')
plt.close()


# ════════════════════════════════════════
# 二、力学模型（8张）
# ════════════════════════════════════════

# 1. 板块模型
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 4.5))
plt.subplots_adjust(left=0.05, right=0.95, hspace=0.3, bottom=0.05, top=0.92)

# 上方：木板+滑块
ax1.set_xlim(0, 8)
ax1.set_ylim(0, 3)
ax1.axis('off')
# 滑块
ax1.add_patch(plt.Rectangle((2, 1.3), 1.5, 0.8, facecolor='#e74c3c', alpha=0.7, edgecolor='#c0392b', linewidth=2))
ax1.text(2.75, 1.7, 'm', fontsize=12, color='white', ha='center', fontweight='bold')
# 木板
ax1.add_patch(plt.Rectangle((1, 0.5), 5, 1.0, facecolor='#3498db', alpha=0.5, edgecolor='#2980b9', linewidth=2))
ax1.text(3.5, 1.0, 'M', fontsize=12, color='white', ha='center', fontweight='bold')
# 摩擦力箭头
ax1.annotate('', xy=(1.8, 2.1), xytext=(3.5, 2.1), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=2))
ax1.text(1.5, 2.3, 'F', fontsize=12, color='#e67e22', fontweight='bold')
# 标注
ax1.annotate('v₀', xy=(3.5, 0.5), xytext=(4.5, 0.2), fontsize=11, color='#e74c3c',
            arrowprops=dict(arrowstyle='->', color='#e74c3c'))
# 摩擦力
ax1.annotate('', xy=(3.5, 1.2), xytext=(2.5, 1.2), arrowprops=dict(arrowstyle='->', color='#8e44ad', lw=2))
ax1.text(3.0, 1.0, 'f', fontsize=10, color='#8e44ad', ha='center')

# 下方：v-t图
t = np.linspace(0, 5, 100)
v_m = np.piecewise(t, [t<3, t>=3], [lambda t: 2+2*t/3, lambda t: 4-2*(t-3)/2])
# 简化v-t
t1 = np.array([0, 0.5, 1.5, 2.5, 3.5])
v1 = np.array([0, 1, 3, 5, 5])
v2 = np.array([2, 2.5, 3.5, 4.5, 4.5])
ax2.plot(t1, v1, 'r-', linewidth=2, marker='o', markersize=4, label='滑块 m')
ax2.plot(t1, v2, 'b-', linewidth=2, marker='s', markersize=4, label='木板 M')
ax2.axhline(0, color='gray', linewidth=0.5)
ax2.set_xlabel('t/s', fontsize=11)
ax2.set_ylabel('v/(m·s⁻¹)', fontsize=11)
ax2.legend(fontsize=9, loc='lower right')
ax2.grid(True, alpha=0.3)
ax2.set_title('板块模型 v-t 图像', fontsize=11, color='#1a1a2e')

fig.suptitle('板块模型——滑块与木板', fontsize=14, color='#1a1a2e', y=1.0)
fig.savefig(os.path.join(OUT, 'phy_block.svg'), dpi=120, facecolor='white')
plt.close()


# 2. 传送带模型
fig, ax = plt.subplots(figsize=(6, 2.8))
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.1, top=0.88)
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis('off')
# 传送带
ax.add_patch(plt.Rectangle((-0.5, 1.0), 11, 0.6, facecolor='#95a5a6', alpha=0.4, edgecolor='#7f8c8d', linewidth=2))
# 轮子
for x in [0.5, 8.5]:
    circle = plt.Circle((x, 1.3), 0.5, fill=False, edgecolor='#7f8c8d', linewidth=2)
    ax.add_patch(circle)
# 物体
ax.add_patch(plt.Rectangle((2, 1.1), 0.8, 0.8, facecolor='#e74c3c', alpha=0.8, edgecolor='#c0392b', linewidth=2))
ax.text(2.4, 1.5, 'm', fontsize=13, color='white', ha='center', fontweight='bold')
# 速度方向
ax.annotate('', xy=(3.2, 1.5), xytext=(4.5, 1.5), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=2.5))
ax.text(3.8, 1.8, 'v物', fontsize=11, color='#e67e22', ha='center', fontweight='bold')
# 传送带方向
ax.annotate('', xy=(2, 1.0), xytext=(4.5, 1.0), arrowprops=dict(arrowstyle='->', color='#3498db', lw=2.5))
ax.text(3.8, 0.7, 'v带', fontsize=11, color='#3498db', ha='center', fontweight='bold')
# 摩擦力
ax.annotate('', xy=(2.8, 1.9), xytext=(4.0, 1.9), arrowprops=dict(arrowstyle='->', color='#8e44ad', lw=2))
ax.text(3.8, 2.1, 'f', fontsize=11, color='#8e44ad', ha='center', fontweight='bold')

# 标注两种情形
ax.text(5.5, 2.0, 'μ', fontsize=12, color='#8e44ad', fontweight='bold')
ax.annotate('', xy=(6.0, 0.5), xytext=(6.0, 1.8), arrowprops=dict(arrowstyle='<->', color='gray', lw=1))

# 文字说明
ax.text(5.5, 0.3, '两种情形：\n① v物 < v带：f为动力，物体加速\n② v物 > v带：f为阻力，物体减速\n③ v物 = v带：无相对滑动，f=0', fontsize=10, color='#2d3436',
        bbox=dict(facecolor='#fef9e7', edgecolor='#f9e79f', boxstyle='round,pad=0.3'))

ax.set_title('传送带模型——物体在传送带上的运动', fontsize=13, color='#1a1a2e', pad=8)
fig.savefig(os.path.join(OUT, 'phy_conveyor.svg'), dpi=120, facecolor='white')
plt.close()


# 3. 牛顿第二定律——a-F和a-1/m图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.2))
plt.subplots_adjust(left=0.1, right=0.95, wspace=0.3, bottom=0.15, top=0.9)
F = np.linspace(0, 10, 100)
for m, c in [(1, '#e74c3c'), (2, '#3498db'), (4, '#27ae60')]:
    a = F/m
    ax1.plot(F, a, '-', color=c, linewidth=2, label=f'm={m}kg')
ax1.set_xlabel('F/N', fontsize=11)
ax1.set_ylabel('a/(m·s⁻²)', fontsize=11)
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.set_title('a-F 图像（m一定）', fontsize=12, color='#1a1a2e')

inv_m = np.linspace(0.1, 2, 100)
for F_v, c in [(1, '#e74c3c'), (2, '#3498db'), (4, '#27ae60')]:
    a = F_v * inv_m
    ax2.plot(inv_m, a, '-', color=c, linewidth=2, label=f'F={F_v}N')
ax2.set_xlabel('1/m / kg⁻¹', fontsize=11)
ax2.set_ylabel('a/(m·s⁻²)', fontsize=11)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)
ax2.set_title('a-1/m 图像（F一定）', fontsize=12, color='#1a1a2e')

fig.suptitle('牛顿第二定律——控制变量法', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'phy_newton2.svg'), dpi=120, facecolor='white')
plt.close()


# 4. 竖直面内圆周运动——过山车模型
fig, ax = plt.subplots(figsize=(5, 4.5))
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.92)
theta_circle = np.linspace(0, 2*np.pi, 400)
R = 2
ax.plot(R*np.cos(theta_circle), R*np.sin(theta_circle), 'b-', linewidth=2.5, alpha=0.7)

# 标注几个关键点
points = [(0, R, '最高点'), (R, 0, '最右'), (0, -R, '最低点'), (-R, 0, '最左')]
for x, y, lbl in points:
    ax.scatter([x], [y], c='red', s=60, zorder=5)
    ax.text(x*1.15-0.2, y*1.15, lbl, fontsize=10, color='#e74c3c', ha='center')

# 在最高点和最低点画受力
# 最高点：重力向下，支持力向下或向上
ax.arrow(0, R, 0, -0.6, head_width=0.15, head_length=0.15, fc='#e67e22', ec='#e67e22', linewidth=2)
ax.text(-0.5, R-0.3, 'mg', fontsize=11, color='#e67e22', fontweight='bold')
ax.arrow(0, R, 0, 0.4, head_width=0.15, head_length=0.15, fc='#3498db', ec='#3498db', linewidth=2)
ax.text(0.2, R+0.2, 'N', fontsize=11, color='#3498db', fontweight='bold')

# 最低点：重力向下，支持力向上
ax.arrow(0, -R, 0, -0.5, head_width=0.15, head_length=0.15, fc='#e67e22', ec='#e67e22', linewidth=2)
ax.text(-0.5, -R-0.3, 'mg', fontsize=11, color='#e67e22', fontweight='bold')
ax.arrow(0, -R, 0, 1.2, head_width=0.15, head_length=0.15, fc='#3498db', ec='#3498db', linewidth=2)
ax.text(0.3, -R+0.3, 'N', fontsize=11, color='#3498db', fontweight='bold')

# 公式
ax.text(0, -3.2, '最高点临界：v₀ = √(gR)',
        fontsize=12, color='#e74c3c', ha='center', fontweight='bold',
        bbox=dict(facecolor='#fef9e7', edgecolor='#f9e79f', boxstyle='round,pad=0.3'))
ax.text(0, -3.8, '最低点：N − mg = mv²/R',
        fontsize=11, color='#555', ha='center')
ax.text(0, -4.3, '最高点：mg + N = mv²/R',
        fontsize=11, color='#555', ha='center')

ax.set_xlim(-3, 3)
ax.set_ylim(-4.5, 3)
ax.set_aspect('equal')
ax.grid(True, alpha=0.15)
ax.set_title('竖直面内圆周运动（过山车模型）', fontsize=13, color='#1a1a2e')
fig.savefig(os.path.join(OUT, 'phy_circular.svg'), dpi=120, facecolor='white')
plt.close()


# 5. v-t图像综合
fig, ax = plt.subplots(figsize=(5.5, 3.2))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.9)
t = np.linspace(0, 10, 1000)
# 复杂v-t：匀加速→匀速→匀减速
v = np.piecewise(t,
    [t<3, (t>=3)&(t<6), t>=6],
    [lambda t: 2*t, lambda t: 6, lambda t: 6-2*(t-6)])
ax.plot(t, v, 'b-', linewidth=2.5)
ax.fill_between(t, v, alpha=0.15, color='#3498db')
# 标注
ax.annotate('匀加速', xy=(1.5, 3), fontsize=10, color='#e74c3c')
ax.annotate('匀速', xy=(4.5, 6.5), fontsize=10, color='#e74c3c')
ax.annotate('匀减速', xy=(7.5, 3), fontsize=10, color='#e74c3c')
# 斜率标注
ax.annotate('', xy=(2, 3.5), xytext=(2.8, 4.5), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=1.5))
ax.text(3.5, 5.0, '斜率 a', fontsize=10, color='#e67e22')
ax.axhline(0, color='gray', linewidth=0.8)
ax.set_xlabel('t/s', fontsize=11)
ax.set_ylabel('v/(m·s⁻¹)', fontsize=11)
ax.set_xticks(range(0, 11))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.set_title('v-t 图像综合分析', fontsize=13, color='#1a1a2e')
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'phy_vt_graph.svg'), dpi=120, facecolor='white')
plt.close()


# 6. 功能关系——能量转化图
fig, ax = plt.subplots(figsize=(6, 4))
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.88)
ax.set_xlim(0, 6)
ax.set_ylim(0, 5)
ax.axis('off')

# 能量转化流程图
boxes = [('重力势能\nmgh', 1, 4, '#3498db'),
         ('动能\n½mv²', 3, 4, '#e74c3c'),
         ('弹性势能\n½kx²', 5, 4, '#27ae60'),
         ('内能\nQ=f·s相对', 3, 1.5, '#e67e22'),
         ('其他能\nW其他', 5, 1.5, '#8e44ad')]

for lbl, x, y, c in boxes:
    ax.add_patch(mpatches.FancyBboxPatch((x-0.8, y-0.5), 1.6, 1.0, boxstyle="round,pad=0.12",
                                      facecolor=c, alpha=0.2, edgecolor=c, linewidth=2))
    ax.text(x, y, lbl, ha='center', va='center', fontsize=10, color='#1a1a2e', fontweight='bold')

# 箭头关系
# 重力做功
ax.annotate('', xy=(2.2, 4.2), xytext=(1.8, 4.2), arrowprops=dict(arrowstyle='->', color='#555', lw=2))
ax.annotate('', xy=(2.2, 3.8), xytext=(2.6, 3.8), arrowprops=dict(arrowstyle='->', color='#555', lw=2))
ax.text(2.2, 4.5, 'WG', fontsize=9, color='#555', ha='center')

# 弹簧做功
ax.annotate('', xy=(4.2, 4.2), xytext=(4.6, 4.2), arrowprops=dict(arrowstyle='->', color='#555', lw=2))
ax.text(4.4, 4.5, 'W弹', fontsize=9, color='#555', ha='center')

# 合外力做功
ax.annotate('', xy=(2.2, 3.5), xytext=(2.8, 2.5), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2, connectionstyle='arc3,rad=-0.3'))
ax.text(2.0, 2.8, 'W合=ΔEk', fontsize=9, color='#e74c3c')

# 摩擦力做功
ax.annotate('', xy=(3.5, 2.5), xytext=(3.5, 3.5), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=2))
ax.text(4.0, 3.0, 'Wf→Q', fontsize=9, color='#e67e22')

# 功能原理
ax.text(3, -0.3, 'W其 = ΔE机 + Q', fontsize=14, color='#1a1a2e', ha='center', fontweight='bold',
        bbox=dict(facecolor='#e8f8f5', edgecolor='#1abc9c', boxstyle='round,pad=0.4'))

ax.set_title('功能关系——力做功与能量转化', fontsize=14, color='#1a1a2e', pad=8)
fig.savefig(os.path.join(OUT, 'phy_energy.svg'), dpi=120, facecolor='white')
plt.close()


# 7. 连接体问题
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.5))
plt.subplots_adjust(left=0.05, right=0.95, wspace=0.3, bottom=0.1, top=0.9)

# 左图：水平连接体
ax1.set_xlim(0, 8)
ax1.set_ylim(0, 3)
ax1.axis('off')
# 地面
ax1.plot([0, 8], [0.5, 0.5], 'k-', linewidth=1)
# 两个物块
ax1.add_patch(plt.Rectangle((1, 0.8), 1.5, 1.0, facecolor='#e74c3c', alpha=0.6, edgecolor='#c0392b', linewidth=2))
ax1.text(1.75, 1.3, 'm₁', fontsize=12, color='white', ha='center', fontweight='bold')
ax1.add_patch(plt.Rectangle((4, 0.8), 1.5, 1.0, facecolor='#3498db', alpha=0.6, edgecolor='#2980b9', linewidth=2))
ax1.text(4.75, 1.3, 'm₂', fontsize=12, color='white', ha='center', fontweight='bold')
# 外力
ax1.annotate('', xy=(6, 1.3), xytext=(7, 1.3), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=2.5))
ax1.text(6.5, 1.7, 'F', fontsize=12, color='#e67e22', fontweight='bold')
# 内部力
ax1.annotate('', xy=(3.5, 1.3), xytext=(4, 1.3), arrowprops=dict(arrowstyle='<->', color='#8e44ad', lw=1.5))
ax1.text(3.75, 1.6, 'T', fontsize=10, color='#8e44ad', ha='center')
ax1.set_title('水平连接体', fontsize=12, color='#1a1a2e')
ax1.text(1.75, 0.3, 'a = F/(m₁+m₂)\nT = m₂F/(m₁+m₂)', fontsize=10, color='#555')

# 右图：竖直连接体
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 5)
ax2.axis('off')
ax2.add_patch(plt.Rectangle((0.5, 1.0), 1.2, 1.0, facecolor='#e74c3c', alpha=0.6, edgecolor='#c0392b', linewidth=2))
ax2.text(1.1, 1.5, 'm₂', fontsize=12, color='white', ha='center', fontweight='bold')
ax2.add_patch(plt.Rectangle((1.5, 3.0), 1.2, 1.0, facecolor='#3498db', alpha=0.6, edgecolor='#2980b9', linewidth=2))
ax2.text(2.1, 3.5, 'm₁', fontsize=12, color='white', ha='center', fontweight='bold')
# 滑轮
circle = plt.Circle((2.5, 3.5), 0.3, fill=False, edgecolor='#555', linewidth=2)
ax2.add_patch(circle)
# 绳子连接
ax2.plot([2.1, 2.5, 2.5], [3.0, 3.5, 2.0], 'k-', linewidth=2)
# 标注
ax2.annotate('', xy=(1.1, 1.0), xytext=(1.1, 0), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=2))
ax2.text(1.4, 0.3, 'm₂g', fontsize=10, color='#e67e22', fontweight='bold')
ax2.set_title('竖直连接体（滑轮）', fontsize=12, color='#1a1a2e')
ax2.text(0.2, 4.5, 'a = m₂g/(m₁+m₂)\nT = m₁m₂g/(m₁+m₂)', fontsize=10, color='#555')

fig.suptitle('连接体问题——整体法与隔离法', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'phy_connected.svg'), dpi=120, facecolor='white')
plt.close()


# 8. 平抛运动与类平抛
fig, ax = plt.subplots(figsize=(5.5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
x = np.linspace(0, 5, 200)
g = 9.8
v0 = 5
# 真实平抛
y_t = 0.5*g*(x/v0)**2
ax.plot(x, y_t, 'b-', linewidth=2.5, label='平抛轨迹 y=½gt²')

# 标注分运动
for t_mark in np.arange(0.2, 1.1, 0.2):
    xm = v0 * t_mark
    ym = 0.5 * g * t_mark**2
    ax.scatter([xm], [ym], c='red', s=30, zorder=5)

# 速度分解
x0, y0 = 3, y_t[3]
vx, vy = v0, g*(x0/v0)
ax.arrow(x0, y0, 0.8, 0, head_width=0.1, head_length=0.12, fc='#e67e22', ec='#e67e22', linewidth=2)
ax.arrow(x0, y0, 0, 0.8, head_width=0.1, head_length=0.12, fc='#e67e22', ec='#e67e22', linewidth=2)
ax.arrow(x0, y0, 0.6, 0.6, head_width=0.1, head_length=0.12, fc='#e74c3c', ec='#e74c3c', linewidth=2)
ax.text(x0+0.7, 0.05, 'v_x', fontsize=10, color='#e67e22', fontweight='bold')
ax.text(x0+0.1, 0.8, 'v_y', fontsize=10, color='#e67e22', fontweight='bold')
ax.text(x0+0.5, 0.6, 'v', fontsize=10, color='#e74c3c', fontweight='bold')

# 水平位移标注
ax.annotate('', xy=(0, -0.3), xytext=(5, -0.3), arrowprops=dict(arrowstyle='<->', color='#3498db', lw=1.5))
ax.text(2.5, -0.6, 'x = v₀t（匀速直线）', fontsize=10, color='#3498db', ha='center')

# 等时性
ax.annotate('', xy=(5.2, 0), xytext=(5.2, y_t[-1]), arrowprops=dict(arrowstyle='<->', color='#27ae60', lw=1.5))
ax.text(5.2, y_t[-1]/2, 'y = ½gt²\n（自由落体）', fontsize=10, color='#27ae60', va='center')

ax.set_xlim(0, 5.5)
ax.set_ylim(-1, 6)
ax.set_xlabel('x/m', fontsize=11)
ax.set_ylabel('y/m', fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_title('平抛运动——水平匀速·竖直自由落体', fontsize=13, color='#1a1a2e')
ax.legend(fontsize=9)
fig.savefig(os.path.join(OUT, 'phy_projectile.svg'), dpi=120, facecolor='white')
plt.close()

print('高中物理所有SVG图表（电磁学+力学模型共16张）生成完毕！')
