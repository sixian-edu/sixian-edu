"""生成高中导数/圆锥曲线/函数深化 SVG 图表"""
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
# 一、导数相关图表（6张）
# ════════════════════════════════════════

# 1. 导数的几何意义——切线
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
x = np.linspace(-2, 3, 400)
y = x**3 - 3*x
ax.plot(x, y, 'b-', linewidth=2, label='f(x)=x³-3x')
x0, y0 = 1, -2
k = 3*x0**2 - 3  # f'(1)=0
tang = k*(x-x0) + y0
ax.plot(x, tang, 'r--', linewidth=2, label='切线 f\'(1)=0')
ax.scatter([x0], [y0], c='red', s=60, zorder=5)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_xlim(-2.5, 3.5)
ax.set_ylim(-5, 5)
ax.legend(fontsize=10)
ax.set_title('导数的几何意义——切线斜率', fontsize=13, color='#1a1a2e')
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'deriv_tangent.svg'), dpi=120, facecolor='white')
plt.close()

# 2. 函数单调性与导数
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.2))
plt.subplots_adjust(left=0.08, right=0.95, wspace=0.3, bottom=0.15, top=0.9)

x = np.linspace(-3, 3, 400)
y1 = x**3 - 3*x  # 递增区间导数>0
ax1.plot(x, y1, '#5688CC', linewidth=2)
ax1.axhline(0, color='gray', linewidth=0.5)
ax1.axvline(0, color='gray', linewidth=0.5)
ax1.axvspan(-3, -1, alpha=0.1, color='#e74c3c')
ax1.axvspan(1, 3, alpha=0.1, color='#e74c3c')
ax1.axvspan(-1, 1, alpha=0.1, color='#27ae60')
ax1.text(-2, 2, "f'(x)>0\n增", fontsize=10, color='#e74c3c', ha='center')
ax1.text(0, -2, "f'(x)<0\n减", fontsize=10, color='#27ae60', ha='center')
ax1.text(2, 2, "f'(x)>0\n增", fontsize=10, color='#e74c3c', ha='center')
ax1.set_title('f\'(x)正负决定单调性', fontsize=11, color='#1a1a2e')
ax1.grid(True, alpha=0.3)

x = np.linspace(0, 4, 400)
y2 = x*np.log(x) - x
ax2.plot(x, y2, '#e67e22', linewidth=2)
ax2.axhline(0, color='gray', linewidth=0.5)
ax2.axvline(0, color='gray', linewidth=0.5)
ax2.axvspan(0.1, 1, alpha=0.1, color='#27ae60')
ax2.axvspan(1, 4, alpha=0.1, color='#e74c3c')
ax2.text(0.5, -0.5, "递减", fontsize=10, color='#27ae60', ha='center')
ax2.text(2, 0.5, "递增", fontsize=10, color='#e74c3c', ha='center')
ax2.set_title('f\'(x)符号变化与单调区间', fontsize=11, color='#1a1a2e')
ax2.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'deriv_monotone.svg'), dpi=120, facecolor='white')
plt.close()

# 3. 极值与最值
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
x = np.linspace(-2.5, 3.5, 400)
y = x**3 - 3*x**2 + 2
ax.plot(x, y, 'b-', linewidth=2)
# 标注极值点
x_vals = [0, 2]
y_vals = [2, -2]
for i, (xv, yv, lbl) in enumerate(zip(x_vals, y_vals, ['极大值', '极小值'])):
    ax.scatter([xv], [yv], c='red', s=60, zorder=5)
    ax.annotate(f'{lbl}\n({xv}, {yv})', (xv, yv), xytext=(xv+0.3 if i==0 else xv-0.3, yv+0.5 if i==0 else yv-0.5),
                arrowprops=dict(arrowstyle='->', color='red'), fontsize=10, color='red')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_title('函数的极值与最值', fontsize=13, color='#1a1a2e')
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'deriv_extreme.svg'), dpi=120, facecolor='white')
plt.close()

# 4. 常见放缩不等式
fig, ax = plt.subplots(figsize=(5.5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
x = np.linspace(-1.5, 3, 400)
ax.plot(x, np.exp(x), 'b-', linewidth=2, label='y=eˣ')
ax.plot(x, x+1, 'r--', linewidth=2, label='y=x+1（切线放缩）')
ax.plot(x[x>-1], np.log(x[x>-1]+1), 'g-', linewidth=2, label='y=ln(x+1)')
ax.set_ylim(-2, 6)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.legend(fontsize=10)
ax.set_title('常用切线放缩：e^x >= x+1, ln(x+1) <= x', fontsize=12, color='#1a1a2e')
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'deriv_ineq.svg'), dpi=120, facecolor='white')
plt.close()

# 5. 导数与函数零点
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
x = np.linspace(-1, 4, 400)
for c, lbl in zip([1, -1, -3], ['3个零点', '2个零点', '1个零点']):
    y = x**3 - 6*x**2 + 9*x + c
    ax.plot(x, y, linewidth=1.5, label=lbl)
ax.axhline(0, color='black', linewidth=0.8)
ax.set_title('三次函数零点个数（参数变化）', fontsize=12, color='#1a1a2e')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'deriv_zero.svg'), dpi=120, facecolor='white')
plt.close()

# 6. 复合函数求导示意（链式法则图）
fig, ax = plt.subplots(figsize=(5, 2.5))
plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.1)
# 链式法则示意图
boxes = [('y=f(u)', 1), ('u=g(x)', 3), ('x', 5)]
for lbl, x in boxes:
    ax.add_patch(mpatches.FancyBboxPatch((x-0.6, 0.6), 1.2, 0.8, boxstyle="round,pad=0.15",
                                      facecolor='#5688CC' if lbl!='x' else '#e67e22', alpha=0.3))
    ax.text(x, 1.0, lbl, ha='center', va='center', fontsize=12, color='#1a1a2e', fontweight='bold')
# 箭头
ax.annotate('', xy=(2.3, 1.0), xytext=(3.7, 1.0), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax.annotate('', xy=(4.3, 1.0), xytext=(5.7-.6, 1.0), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
# 导数标注
ax.text(3.0, 1.6, "dy/du", ha='center', fontsize=11, color='#e74c3c')
ax.text(5.0, 1.6, "du/dx", ha='center', fontsize=11, color='#e74c3c')
ax.text(3.0, 0.2, "dy/dx = dy/du · du/dx", ha='center', fontsize=13, color='#1a1a2e', fontweight='bold')
ax.set_xlim(0, 6.5)
ax.set_ylim(0, 2.2)
ax.axis('off')
ax.set_title('复合函数求导——链式法则', fontsize=13, color='#1a1a2e', pad=8)
fig.savefig(os.path.join(OUT, 'deriv_chain.svg'), dpi=120, facecolor='white')
plt.close()


# ════════════════════════════════════════
# 二、圆锥曲线（4张）
# ════════════════════════════════════════

# 1. 椭圆
fig, ax = plt.subplots(figsize=(4.5, 4))
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.92)
theta = np.linspace(0, 2*np.pi, 400)
a, b = 3, 2
x, y = a*np.cos(theta), b*np.sin(theta)
ax.plot(x, y, 'b-', linewidth=2, label='椭圆 x²/9+y²/4=1')
# 焦点
c = np.sqrt(a**2 - b**2)
ax.scatter([-c, c], [0, 0], c='red', s=50, zorder=5)
ax.annotate('F₁', (c+0.1, 0.1), fontsize=11, color='red')
ax.annotate('F₂', (-c-0.4, 0.1), fontsize=11, color='red')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.5, 2.5)
ax.grid(True, alpha=0.3)
ax.set_title('椭圆 —— 定义：|PF₁|+|PF₂|=2a', fontsize=12, color='#1a1a2e')
fig.savefig(os.path.join(OUT, 'conic_ellipse.svg'), dpi=120, facecolor='white')
plt.close()

# 2. 双曲线
fig, ax = plt.subplots(figsize=(4.5, 4))
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.92)
x = np.linspace(-4, 4, 400)
a, b = 2, 1.5
y1 = b/a * np.sqrt(x**2 - a**2)
y2 = -b/a * np.sqrt(x**2 - a**2)
# 只画有效区域
mask = np.abs(x) >= a
ax.plot(x[mask], y1[mask], 'b-', linewidth=2, label='双曲线')
ax.plot(x[mask], y2[mask], 'b-', linewidth=2)
# 渐近线
ax.plot(x, b/a*x, 'k--', linewidth=1, alpha=0.5, label='渐近线')
ax.plot(x, -b/a*x, 'k--', linewidth=1, alpha=0.5)
# 焦点
c = np.sqrt(a**2 + b**2)
ax.scatter([-c, c], [0, 0], c='red', s=50, zorder=5)
ax.annotate('F₁', (c+0.1, 0.1), fontsize=11, color='red')
ax.annotate('F₂', (-c-0.4, 0.1), fontsize=11, color='red')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-3, 3)
ax.grid(True, alpha=0.3)
ax.set_title('双曲线 —— 定义：||PF₁|−|PF₂||=2a', fontsize=11, color='#1a1a2e')
fig.savefig(os.path.join(OUT, 'conic_hyperbola.svg'), dpi=120, facecolor='white')
plt.close()

# 3. 抛物线
fig, ax = plt.subplots(figsize=(4.5, 4))
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.92)
x = np.linspace(0, 4, 400)
p = 1
y_pos = np.sqrt(4*p*x)
y_neg = -np.sqrt(4*p*x)
ax.plot(x, y_pos, 'b-', linewidth=2, label='y²=4px (p=1)')
ax.plot(x, y_neg, 'b-', linewidth=2)
# 焦点和准线
ax.scatter([p], [0], c='red', s=50, zorder=5)
ax.annotate('F (p,0)', (p+0.1, 0.2), fontsize=11, color='red')
ax.axvline(-p, color='green', linestyle='--', linewidth=1.5, alpha=0.7, label='准线 x=-p')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_xlim(-1.5, 4.5)
ax.set_ylim(-3, 3)
ax.grid(True, alpha=0.3)
ax.set_title('抛物线 —— 定义：|PF|=d(P到准线)', fontsize=12, color='#1a1a2e')
fig.savefig(os.path.join(OUT, 'conic_parabola.svg'), dpi=120, facecolor='white')
plt.close()

# 4. 弦长与韦达定理（直线与圆锥曲线）
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
# 椭圆
theta = np.linspace(0, 2*np.pi, 400)
a, b = 3, 2
ax.plot(a*np.cos(theta), b*np.sin(theta), 'b-', linewidth=2)
# 直线与椭圆相交
x_pts = np.linspace(-2.5, 3, 100)
k, m = 0.6, 0.5
y_pts = k*x_pts + m
ax.plot(x_pts, y_pts, 'r-', linewidth=2, label='y=kx+m')
# 标注根与系数的关系
ax.text(-1, -2.5, '联立 → 一元二次方程\nx₁+x₂ = -b/a,  x₁x₂ = c/a\n弦长公式 d = √(1+k²)·√Δ/|a|',
        fontsize=10, color='#2d3436', bbox=dict(facecolor='#fef9e7', edgecolor='#f9e79f', boxstyle='round,pad=0.3'))
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-2.5, 2.5)
ax.grid(True, alpha=0.3)
ax.set_title('直线与圆锥曲线——弦长与韦达定理', fontsize=12, color='#1a1a2e')
fig.savefig(os.path.join(OUT, 'conic_chord.svg'), dpi=120, facecolor='white')
plt.close()


# ════════════════════════════════════════
# 三、函数深化（4张）
# ════════════════════════════════════════

# 1. 指数与对数函数
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
x = np.linspace(0.1, 4, 400)
ax.plot(x, np.exp(x), 'b-', linewidth=2, label='y=eˣ')
ax.plot(x, np.log(x), 'g-', linewidth=2, label='y=ln x')
ax.plot(x, x, 'k--', linewidth=1, alpha=0.5, label='y=x')
ax.set_xlim(0, 4)
ax.set_ylim(-3, 6)
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.legend(fontsize=10)
ax.set_title('指数函数与对数函数（互为反函数）', fontsize=12, color='#1a1a2e')
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'func_exp_log.svg'), dpi=120, facecolor='white')
plt.close()

# 2. 函数图像变换——平移
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
x = np.linspace(-3, 3, 400)
y0 = x**2
y1 = (x-1)**2 + 1
ax.plot(x, y0, 'b-', linewidth=2, label='y=x²')
ax.plot(x, y1, 'r-', linewidth=2, label='y=(x-1)²+1')
# 箭头标注平移
ax.annotate('', xy=(0, 0), xytext=(1, 1), arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax.text(0.5, -0.8, '向右1, 向上1', fontsize=10, color='#e74c3c', ha='center')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.legend(fontsize=10)
ax.set_title('函数图像平移：f(x) → f(x−a)+b', fontsize=12, color='#1a1a2e')
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'func_shift.svg'), dpi=120, facecolor='white')
plt.close()

# 3. 函数奇偶性与周期性
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.2))
plt.subplots_adjust(left=0.08, right=0.95, wspace=0.3, bottom=0.15, top=0.9)
x = np.linspace(-3, 3, 400)
y1 = x**3
ax1.plot(x, y1, '#5688CC', linewidth=2)
ax1.scatter([-2, 2], [-8, 8], c='red', s=40, zorder=5)
ax1.annotate('(x, y)', (2, 8), xytext=(2.5, 7.5), fontsize=9)
ax1.annotate('(-x, -y)', (-2, -8), xytext=(-4.5, -7.5), fontsize=9)
ax1.axhline(0, color='gray', linewidth=0.5)
ax1.axvline(0, color='gray', linewidth=0.5)
ax1.set_title('奇函数 f(-x) = -f(x)', fontsize=11, color='#1a1a2e')
ax1.grid(True, alpha=0.3)

x = np.linspace(-4, 4, 800)
y2 = np.sin(x)
ax2.plot(x, y2, '#e67e22', linewidth=2)
ax2.axhline(0, color='gray', linewidth=0.5)
ax2.axvline(0, color='gray', linewidth=0.5)
for k in range(-2, 3):
    ax2.axvspan(k*np.pi-0.05, k*np.pi+0.05, alpha=0.15, color='#e74c3c')
ax2.set_xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax2.set_xticklabels(['-2π', '-π', '0', 'π', '2π'])
ax2.set_title('周期函数 f(x+T) = f(x)', fontsize=11, color='#1a1a2e')
ax2.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'func_parity_period.svg'), dpi=120, facecolor='white')
plt.close()

# 4. 函数零点与二分法
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
x = np.linspace(-2, 3, 400)
y = x**3 - x - 1
ax.plot(x, y, 'b-', linewidth=2)
ax.axhline(0, color='gray', linewidth=0.5)
# 标注零点区间
ax.axvspan(1.3, 1.35, alpha=0.2, color='red')
ax.annotate('零点≈1.3247', xy=(1.32, 0), xytext=(1.8, 1.5),
            arrowprops=dict(arrowstyle='->', color='red'), fontsize=11, color='red')
ax.set_title('函数零点与二分法求近似解', fontsize=12, color='#1a1a2e')
ax.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'func_zero.svg'), dpi=120, facecolor='white')
plt.close()

print('所有SVG图表（导数+圆锥曲线+函数深化）生成完毕！')
