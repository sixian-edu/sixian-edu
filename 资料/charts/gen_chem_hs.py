"""高中化学 工艺流程+实验题+方程式 专业SVG图表"""
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
# 一、工艺流程（6张）
# ════════════════════════════════════════

# 1. 合成氨工业 (Haber-Bosch)
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, bottom=0.1, top=0.88)

# Left: Flow diagram
ax1 = axes[0]
ax1.axis('off')
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)
ax1.set_title('合成氨工艺流程', fontsize=11, color='#e67e22', fontweight='bold', pad=10)

# Flow boxes
steps = [
    (0.5, 4.0, '原料气\nN₂ + H₂', '#3498db'),
    (2.0, 4.0, '压缩\n(10-30MPa)', '#e67e22'),
    (3.5, 4.0, '合成塔\n(400-500℃)', '#e74c3c'),
    (2.0, 2.0, '冷凝分离\nNH₃液化', '#27ae60'),
    (0.5, 2.0, '产品\n液氨', '#8e44ad'),
    (3.5, 2.0, '未反应气体\n循环利用', '#7f8c8d'),
]

for x, y, label, color in steps:
    ax1.add_patch(plt.Rectangle((x-0.45, y-0.25), 0.9, 0.5, fill=True, facecolor=color, alpha=0.15, edgecolor=color))
    ax1.text(x, y, label, ha='center', va='center', fontsize=7.5, color='#333', fontweight='bold')

# Flow arrows
ax1.annotate('', xy=(1.0, 4.0), xytext=(1.5, 4.0), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=1.5))
ax1.annotate('', xy=(2.5, 4.0), xytext=(3.0, 4.0), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=1.5))
ax1.annotate('', xy=(3.5, 3.7), xytext=(3.5, 2.5), arrowprops=dict(arrowstyle='->', color='#27ae60', lw=1.5))
ax1.annotate('', xy=(2.5, 2.0), xytext=(1.0, 2.0), arrowprops=dict(arrowstyle='->', color='#8e44ad', lw=1.5))
# Recycle arrow
ax1.annotate('', xy=(3.5, 2.0), xytext=(4.2, 3.0), fontsize=7, color='#888',
             arrowprops=dict(arrowstyle='->', color='#7f8c8d', lw=1, connectionstyle='arc3,rad=0.3'))
ax1.annotate('循环', xy=(4.0, 2.8), fontsize=7, color='#7f8c8d')

# Key conditions box
ax1.text(0.3, 0.4, '条件: 10-30MPa, 400-500℃\n铁触媒(Fe)做催化剂\nN₂+3H₂ ⇌ 2NH₃ ΔH<0', fontsize=7, color='#555',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef9e7', edgecolor='#f0c040'))

# Right: Yield vs temperature/pressure
ax2 = axes[1]
T = np.linspace(300, 600, 100)
# Yield curves at different pressures
for P, color in [(10, '#3498db'), (20, '#27ae60'), (30, '#e74c3c')]:
    # Simulated yield: lower T and higher P favor yield (exothermic, volume decreasing)
    yield_curve = 100 / (1 + np.exp(0.015 * (T - 450 - P * 2))) * (0.5 + P * 0.015)
    ax2.plot(T, yield_curve, '-', color=color, linewidth=2, label=f'{P} MPa')

ax2.set_xlabel('温度 (℃)', fontsize=9)
ax2.set_ylabel('NH₃ 平衡产率 (%)', fontsize=9)
ax2.set_title('不同条件下合成氨平衡产率', fontsize=10, color='#1a1a2e', fontweight='bold')
ax2.legend(fontsize=8, title='压强')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_ylim(0, 70)
ax2.grid(True, alpha=0.15)

fig.suptitle('合成氨工业 (Haber-Bosch)', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'chem_flow_ammonia.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 2. 接触法制硫酸
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)
ax.axis('off')
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.set_title('接触法制硫酸工艺流程', fontsize=14, color='#e67e22', fontweight='bold')

# Three main stages
stages = [
    (0.3, 3.5, '第一步\n硫铁矿/硫磺\n煅烧', '#3498db',
     ['4FeS₂+11O₂→2Fe₂O₃+8SO₂', '或 S+O₂→SO₂', ''], 1.5),
    (3.3, 3.5, '第二步\nSO₂催化氧化\n(接触氧化)', '#e74c3c',
     ['2SO₂+O₂ ⇌ 2SO₃', '催化剂: V₂O₅', '450℃, 常压'], 1.5),
    (6.3, 3.5, '第三步\nSO₃吸收\n制硫酸', '#27ae60',
     ['SO₃+H₂O→H₂SO₄', '用98%浓硫酸吸收', '不用水(防酸雾)'], 1.5),
]

for x, y, title, color, equations, w in stages:
    ax.add_patch(plt.Rectangle((x, y-0.3), w, 0.6, fill=True, facecolor=color, alpha=0.15, edgecolor=color))
    ax.text(x+w/2, y, title, ha='center', va='center', fontsize=8, color=color, fontweight='bold')
    for i, eq in enumerate(equations):
        if eq:
            ax.text(x+w/2, y-0.7-i*0.35, eq, ha='center', fontsize=7, color='#555')

# Arrows between stages
ax.annotate('', xy=(1.9, 3.8), xytext=(3.1, 3.8), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=2))
ax.annotate('', xy=(4.9, 3.8), xytext=(6.1, 3.8), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=2))

# Raw materials and products
ax.text(0.5, 2.0, '原料:\n硫铁矿/硫磺', fontsize=8, color='#3498db', ha='center',
        bbox=dict(boxstyle='round', facecolor='#eaf2f8', edgecolor='#3498db'))
ax.text(6.5, 2.0, '产品:\n硫酸 · 发烟硫酸', fontsize=8, color='#27ae60', ha='center',
        bbox=dict(boxstyle='round', facecolor='#e8f8f0', edgecolor='#27ae60'))

# Key point
ax.text(0.5, 0.5, '核心反应: 2SO₂+O₂ ⇌ 2SO₃ ΔH<0\n催化剂V₂O₅ 加快反应速率\n常压即可(加压产率提升不大)', fontsize=7.5, color='#555',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef9e7', edgecolor='#f0c040'))

# Arrow diagrams for yield
ax.annotate('', xy=(3.3, 1.8), xytext=(5.8, 1.8), arrowprops=dict(arrowstyle='->', color='#e67e22', lw=1))
ax.text(4.5, 1.5, 'SO₂转化率约93-99%', ha='center', fontsize=8, color='#e67e22')

fig.savefig(os.path.join(OUT, 'chem_flow_sulfuric.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 3. 氯碱工业
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.25, bottom=0.1, top=0.88)

# Left: Ion-exchange membrane cell
ax1.axis('off')
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 4)
ax1.set_title('离子交换膜电解槽', fontsize=11, color='#e67e22', fontweight='bold', pad=10)

# Anode compartment (left)
ax1.add_patch(plt.Rectangle((0.2, 1.0), 1.3, 2.0, fill=True, facecolor='#fce4ec', edgecolor='#e74c3c', linewidth=1.5))
ax1.text(0.85, 2.8, '阳极室', ha='center', fontsize=9, color='#e74c3c', fontweight='bold')
ax1.text(0.85, 2.3, '2Cl⁻→Cl₂↑+2e⁻', ha='center', fontsize=7, color='#c0392b')
ax1.text(0.85, 1.9, 'Cl₂ 产生', ha='center', fontsize=7, color='#c0392b')
ax1.text(0.85, 1.3, 'NaCl溶液', ha='center', fontsize=7, color='#555')
ax1.text(0.3, 2.2, 'Cl⁻', fontsize=8, color='#27ae60')
ax1.text(0.3, 1.9, 'Cl⁻', fontsize=8, color='#27ae60')
ax1.text(0.3, 1.6, 'Cl⁻', fontsize=8, color='#27ae60')

# Membrane
ax1.add_patch(plt.Rectangle((1.6, 1.0), 0.3, 2.0, fill=True, facecolor='#d5f5e3', edgecolor='#27ae60', linewidth=2))
ax1.text(1.75, 2.0, '离子\n交换膜', ha='center', fontsize=7, color='#27ae60', fontweight='bold', rotation=90)

# Cathode compartment (right)
ax1.add_patch(plt.Rectangle((2.0, 1.0), 1.5, 2.0, fill=True, facecolor='#e8f8f0', edgecolor='#27ae60', linewidth=1.5))
ax1.text(2.75, 2.8, '阴极室', ha='center', fontsize=9, color='#27ae60', fontweight='bold')
ax1.text(2.75, 2.3, '2H₂O+2e⁻→H₂↑+2OH⁻', ha='center', fontsize=7, color='#1d8348')
ax1.text(2.75, 1.9, 'H₂ 产生', ha='center', fontsize=7, color='#1d8348')
ax1.text(2.75, 1.3, 'NaOH溶液', ha='center', fontsize=7, color='#555')
ax1.text(3.3, 2.2, 'Na⁺', fontsize=8, color='#2980b9')
ax1.text(3.3, 1.9, 'Na⁺', fontsize=8, color='#2980b9')

# Power supply
ax1.text(0.2, 3.5, '电源(+)→', fontsize=8, color='#e74c3c', fontweight='bold')
ax1.text(2.5, 3.5, '←电源(-)', fontsize=8, color='#27ae60', fontweight='bold')

# Products
ax1.text(0.85, 0.5, '阳极产物: Cl₂', fontsize=7, color='#c0392b', ha='center')
ax1.text(2.75, 0.5, '阴极产物: H₂ + NaOH', fontsize=7, color='#1d8348', ha='center')

# Right: Overall reaction and key points
ax2.axis('off')
ax2.set_xlim(0, 3)
ax2.set_ylim(0, 4)
ax2.set_title('氯碱工业要点', fontsize=11, color='#e67e22', fontweight='bold', pad=10)

points = [
    '总反应:',
    '2NaCl+2H₂O → H₂↑+Cl₂↑+2NaOH',
    '(电解)',
    '',
    '阳极: 2Cl⁻ - 2e⁻ → Cl₂↑ (氧化)',
    '阴极: 2H₂O+2e⁻ → H₂↑+2OH⁻ (还原)',
    '',
    '离子交换膜作用:',
    '• 允许Na⁺通过(维持电荷平衡)',
    '• 阻止Cl⁻进入阴极室(防副反应)',
    '• 阻止OH⁻进入阳极室(Cl₂+2OH⁻',
    '  →Cl⁻+ClO⁻+H₂O 损耗Cl₂)',
    '',
    '产品用途:',
    'H₂: 合成氨、燃料',
    'Cl₂: 漂白剂、PVC制备',
    'NaOH: 化工原料',
]
for i, point in enumerate(points):
    color = '#c0392b' if '阳极' in point else ('#1d8348' if '阴极' in point else ('#8e44ad' if '总反应' in point else '#555'))
    ax2.text(0.1, 3.7 - i*0.25, point, fontsize=7, color=color)

fig.suptitle('氯碱工业 — 离子交换膜法', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'chem_flow_chloralkali.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 4. 氨氧化法制硝酸
fig, ax = plt.subplots(1, 1, figsize=(8, 3.5))
plt.subplots_adjust(left=0.05, right=0.95, top=0.88, bottom=0.1)
ax.axis('off')
ax.set_xlim(0, 8)
ax.set_ylim(0, 4.5)
ax.set_title('氨氧化法制硝酸工艺流程', fontsize=14, color='#e67e22', fontweight='bold')

steps = [
    (0.2, 3.2, '氨氧化\n(转化器)', '#e74c3c',
     ['4NH₃+5O₂ →', '4NO+6H₂O', 'Pt-Rh网, 800℃']),
    (2.2, 3.2, 'NO氧化\n(氧化塔)', '#e67e22',
     ['2NO+O₂ → 2NO₂', '', '']),
    (4.2, 3.2, 'NO₂吸收\n(吸收塔)', '#27ae60',
     ['3NO₂+H₂O →', '2HNO₃+NO', '']),
    (6.2, 3.2, '尾气处理', '#8e44ad',
     ['NO/NO₂→NaNO₂', '或选择性催化还原', '环保排放']),
]

for x, y, title, color, eqs in steps:
    ax.add_patch(plt.Rectangle((x, y-0.3), 1.6, 0.7, fill=True, facecolor=color, alpha=0.15, edgecolor=color))
    ax.text(x+0.8, y+0.1, title, ha='center', va='center', fontsize=8, color=color, fontweight='bold')
    for i, eq in enumerate(eqs):
        ax.text(x+0.8, y-0.45-i*0.25, eq, ha='center', fontsize=7, color='#555')

# Arrows
for x_start in [1.2, 3.2, 5.2]:
    ax.annotate('', xy=(x_start+0.6, 3.45), xytext=(x_start+0.2, 3.45),
                arrowprops=dict(arrowstyle='->', color='#e67e22', lw=2))

# Recycle arrow (NO from absorption)
ax.annotate('NO循环氧化', xy=(4.6, 2.3), xytext=(3.8, 2.8), fontsize=7, color='#27ae60',
            arrowprops=dict(arrowstyle='->', color='#27ae60', lw=1, connectionstyle='arc3,rad=0.3'))

# Bottom summary
summary = (
    '三步反应: ① 4NH₃+5O₂ → 4NO+6H₂O (催化氧化)'
    '  ② 2NO+O₂ → 2NO₂ (常温自氧化)'
    '  ③ 3NO₂+H₂O → 2HNO₃+NO (吸收)'
)
ax.text(0.3, 0.5, summary, fontsize=8, color='#555')

# Byproduct
ax.text(6.5, 1.0, '尾气含NO/NO₂\n必须处理\n→ 氨还原法\n→ 碱液吸收', fontsize=7, color='#8e44ad',
        bbox=dict(boxstyle='round', facecolor='#f3e5f5', edgecolor='#8e44ad'))

fig.savefig(os.path.join(OUT, 'chem_flow_nitric.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 5. 海水资源综合利用
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.05, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# 海水中元素含量
ax1 = axes[0, 0]
elements = ['Cl', 'Na', 'Mg', 'S', 'Ca', 'K', 'Br', 'C', 'Sr', 'B']
concentrations = [19000, 10500, 1350, 900, 400, 380, 65, 28, 8, 4.5]
colors = ['#3498db', '#e74c3c', '#27ae60', '#e67e22', '#8e44ad', '#f39c12', '#1abc9c', '#2c3e50', '#d35400', '#7f8c8d']

bars = ax1.bar(range(len(elements)), concentrations, color=colors, alpha=0.8)
ax1.set_xticks(range(len(elements)))
ax1.set_xticklabels(elements, fontsize=9)
ax1.set_ylabel('浓度 (mg/L)', fontsize=9)
ax1.set_title('海水中主要元素含量', fontsize=10, color='#1a1a2e', fontweight='bold')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(True, alpha=0.15, axis='y')

# 海水提溴
ax2 = axes[0, 1]
ax2.axis('off')
ax2.set_xlim(0, 3)
ax2.set_ylim(0, 3)
ax2.set_title('海水提溴流程', fontsize=10, color='#1a1a2e', fontweight='bold')

steps_br = [
    '① 浓缩: 海水晒盐后卤水',
    '② 氧化: Cl₂+2Br⁻→Br₂+2Cl⁻',
    '③ 吹出: 空气/水蒸气吹出Br₂',
    '④ 吸收: SO₂+Br₂+2H₂O→',
    '        2HBr+H₂SO₄',
    '⑤ 再氧化: Cl₂+2HBr→Br₂+2HCl',
    '⑥ 产品: 高纯度溴',
]
for i, step in enumerate(steps_br):
    ax2.text(0.1, 2.7 - i*0.32, step, fontsize=7, color='#555')

ax2.text(0.1, 0.1, '关键: 富集 + 氧化还原循环', fontsize=7, color='#c0392b', fontweight='bold')

# 海水提镁
ax3 = axes[0, 2]
ax3.axis('off')
ax3.set_xlim(0, 3)
ax3.set_ylim(0, 3)
ax3.set_title('海水提镁流程', fontsize=10, color='#1a1a2e', fontweight='bold')

steps_mg = [
    '① 沉淀: Mg²⁺+2OH⁻→Mg(OH)₂↓',
    '② 过滤分离Mg(OH)₂',
    '③ 溶解: Mg(OH)₂+2HCl→',
    '        MgCl₂+2H₂O',
    '④ 蒸发结晶得MgCl₂',
    '⑤ 电解: MgCl₂(熔融)→',
    '        Mg+Cl₂↑',
]
for i, step in enumerate(steps_mg):
    ax3.text(0.1, 2.7 - i*0.32, step, fontsize=7, color='#555')

# Bottom row: 海水淡化 + 综合
ax4 = axes[1, 0]
ax4.axis('off')
ax4.set_xlim(0, 3)
ax4.set_ylim(0, 3)
ax4.set_title('海水淡化方法对比', fontsize=10, color='#1a1a2e', fontweight='bold')

methods = [
    '蒸馏法: 能耗高, 淡水纯度高',
    '反渗透法: 能耗低, 应用最广',
    '电渗析法: 利用离子交换膜',
    '冷冻法: 能耗高, 较少使用',
]
for i, m in enumerate(methods):
    ax4.text(0.1, 2.5 - i*0.45, '• ' + m, fontsize=7, color='#555')

# 综合
ax5 = axes[1, 1]
ax5.axis('off')
ax5.set_xlim(0, 3)
ax5.set_ylim(0, 3)
ax5.set_title('海水化学资源开发', fontsize=10, color='#1a1a2e', fontweight='bold')

products = [
    ('食盐(NaCl)', '#3498db'),
    ('溴(Br₂)', '#e74c3c'),
    ('镁(Mg)', '#27ae60'),
    ('钾肥(KCl)', '#e67e22'),
    ('碘(I₂)', '#8e44ad'),
    ('重水(D₂O)', '#2c3e50'),
]
for i, (product, color) in enumerate(products):
    ax5.text(0.1, 2.5 - i*0.35, '■ ' + product, fontsize=8, color=color)

# 综合流程
ax6 = axes[1, 2]
ax6.axis('off')
ax6.set_xlim(0, 3)
ax6.set_ylim(0, 3)
ax6.set_title('海水综合利用图', fontsize=10, color='#1a1a2e', fontweight='bold')

ax6.text(0.1, 2.7, '海水', fontsize=9, color='#2980b9', fontweight='bold')
ax6.text(0.1, 2.3, '├─ 晒盐 → NaCl → Cl₂+H₂+NaOH', fontsize=7, color='#555')
ax6.text(0.1, 2.0, '│       └→ 卤水 → Br₂/I₂/Mg', fontsize=7, color='#555')
ax6.text(0.1, 1.7, '├─ 直接提镁 → Mg(OH)₂ → Mg', fontsize=7, color='#555')
ax6.text(0.1, 1.4, '├─ 淡化 → 淡水', fontsize=7, color='#555')
ax6.text(0.1, 1.1, '└─ 核电 → 冷却水', fontsize=7, color='#555')

fig.suptitle('海水资源的综合利用', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'chem_flow_seawater.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 6. 石油化工
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.25, bottom=0.12, top=0.88)

# Left: Fractional distillation tower
ax1 = axes[0]
ax1.axis('off')
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 5)
ax1.set_title('石油分馏塔', fontsize=11, color='#e67e22', fontweight='bold', pad=10)

# Tower shape
ax1.add_patch(plt.Rectangle((0.8, 0.5), 1.4, 4.0, fill=True, facecolor='#f8f9fc', edgecolor='#888', linewidth=2))

# Fractions (bottom to top)
fractions = [
    (0.7, '重油\n(沥青/燃料油)', '#e74c3c', 3.7),
    (0.7, '蜡油\n(润滑油/石蜡)', '#e67e22', 3.0),
    (0.7, '柴油', '#f39c12', 2.3),
    (0.7, '煤油', '#3498db', 1.6),
    (0.7, '汽油', '#27ae60', 0.9),
]

for w, label, color, y_pos in fractions:
    ax1.add_patch(plt.Rectangle((0.8, y_pos-0.25), 1.4, 0.4, fill=True, facecolor=color, alpha=0.3, edgecolor=color))
    ax1.text(1.5, y_pos, label, ha='center', va='center', fontsize=7, color='#333', fontweight='bold')

# Temperature gradient
ax1.text(2.5, 4.2, '高温↓', fontsize=7, color='#e74c3c')
ax1.text(2.5, 0.3, '↑低温', fontsize=7, color='#3498db')

# Label
ax1.text(0.2, 2.5, '原油\n进料', fontsize=7, color='#555', fontweight='bold', rotation=90)
ax1.annotate('', xy=(0.8, 2.5), xytext=(0.4, 2.5), arrowprops=dict(arrowstyle='->', color='#888'))

# Bottom heat
ax1.text(1.5, 0.1, '加热炉 (350-400℃)', ha='center', fontsize=7, color='#e74c3c')

# Right: Cracking and reforming
ax2 = axes[1]
ax2.axis('off')
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 5)
ax2.set_title('石油的深加工', fontsize=11, color='#e67e22', fontweight='bold', pad=10)

# Cracking
ax2.add_patch(plt.Rectangle((0.2, 3.5), 1.6, 1.2, fill=True, facecolor='#fce4ec', edgecolor='#e74c3c'))
ax2.text(1.0, 4.4, '裂化/裂解', ha='center', fontsize=9, color='#e74c3c', fontweight='bold')
ax2.text(1.0, 4.0, '长链烃 → 短链烃', ha='center', fontsize=7, color='#555')
ax2.text(1.0, 3.7, '产品: 汽油、乙烯等', ha='center', fontsize=7, color='#555')

# Reforming
ax2.add_patch(plt.Rectangle((2.2, 3.5), 1.6, 1.2, fill=True, facecolor='#e8f8f0', edgecolor='#27ae60'))
ax2.text(3.0, 4.4, '催化重整', ha='center', fontsize=9, color='#27ae60', fontweight='bold')
ax2.text(3.0, 4.0, '环烷烃/烷烃→芳香烃', ha='center', fontsize=7, color='#555')
ax2.text(3.0, 3.7, '产品: 苯、甲苯、二甲苯', ha='center', fontsize=7, color='#555')

# Downstream products
downstream = [
    '乙烯 → 聚乙烯/乙醇/乙二醇',
    '丙烯 → 聚丙烯/丙二醇',
    '丁二烯 → 合成橡胶',
    '苯 → 苯乙烯/苯酚/己内酰胺',
    '甲苯 → TNT/苯甲酸',
    '二甲苯 → PTA(涤纶)',
    '『三烯三苯』是基础化工原料',
]
ax2.text(0.2, 2.8, '下游化工产品:', fontsize=8, color='#1a1a2e', fontweight='bold')
for i, prod in enumerate(downstream):
    ax2.text(0.2, 2.5 - i*0.28, prod, fontsize=7, color='#555')

fig.suptitle('石油化工 — 分馏与深加工', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'chem_flow_oil.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# ════════════════════════════════════════
# 二、实验题精讲（6张）
# ════════════════════════════════════════

# 7. 酸碱滴定曲线
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
plt.subplots_adjust(left=0.07, right=0.97, wspace=0.3, bottom=0.1, top=0.88)

# Strong acid - strong base titration
ax1 = axes[0]
V_base = np.linspace(0, 50, 500)
V_eq = 25  # equivalence point
# Simulate pH for strong acid (0.1M HCl) titrated with strong base (0.1M NaOH)
pH = np.zeros_like(V_base)
for i, V in enumerate(V_base):
    if V < V_eq - 0.01:
        excess_H = (0.1 * 0.025 - 0.1 * V/1000) / ((0.025 + V/1000))  # simplification
        if excess_H > 0:
            pH[i] = -np.log10(excess_H)
        else:
            pH[i] = 7.0
    elif V > V_eq + 0.01:
        excess_OH = (0.1 * (V/1000 - 0.025)) / (0.025 + V/1000)
        if excess_OH > 0:
            pH[i] = 14 + np.log10(excess_OH)
        else:
            pH[i] = 7.0
    else:
        pH[i] = 7.0

# Clean up pH range
pH = np.clip(pH, 0, 14)

ax1.plot(V_base, pH, '-', color='#e74c3c', linewidth=2.5)
ax1.axvline(x=25, color='#888', linewidth=1, linestyle='--', alpha=0.7)
ax1.text(25, 0.5, '等当点\npH=7', ha='center', fontsize=8, color='#888')
ax1.set_xlabel('NaOH 加入体积 (mL)', fontsize=9)
ax1.set_ylabel('pH', fontsize=9)
ax1.set_title('强酸强碱滴定 (HCl × NaOH)', fontsize=10, color='#1a1a2e', fontweight='bold')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_xlim(0, 50)
ax1.set_ylim(0, 14)
ax1.grid(True, alpha=0.15)

# 指示剂选择
ax1.annotate('突跃范围\npH 4.3~9.7', xy=(25, 4), xytext=(30, 3), fontsize=8, color='#c0392b',
            arrowprops=dict(arrowstyle='->', color='#c0392b'))
ax1.add_patch(plt.Rectangle((24.5, 4.3), 1, 5.4, fill=True, facecolor='#fce4ec', alpha=0.15))

# Right: Weak acid - strong base
ax2 = axes[1]
pH_weak = np.zeros_like(V_base)
# Simulate weak acid (HAc, Ka=1.8e-5) titrated with strong base
for i, V in enumerate(V_base):
    if V < 0.01:
        pH_weak[i] = 0.5 * (-np.log10(1.8e-5) - np.log10(0.1))
    elif V < V_eq - 0.01:
        # Buffer region
        ratio = V / (V_eq - V)
        pH_weak[i] = -np.log10(1.8e-5) + np.log10(ratio)
    elif V > V_eq + 0.01:
        excess_OH = (0.1 * (V/1000 - 0.025)) / (0.025 + V/1000)
        if excess_OH > 0:
            pH_weak[i] = 14 + np.log10(excess_OH)
        else:
            pH_weak[i] = 8.87
    else:
        # At equivalence - weak base salt
        pH_weak[i] = 7 + 0.5 * (-np.log10(1.8e-5)) + 0.5 * np.log10(0.05)

pH_weak = np.clip(pH_weak, 0, 14)

ax2.plot(V_base, pH_weak, '-', color='#3498db', linewidth=2.5)
ax2.axvline(x=25, color='#888', linewidth=1, linestyle='--', alpha=0.7)
ax2.text(25, 0.5, '等当点\npH=8.72', ha='center', fontsize=8, color='#888')
ax2.set_xlabel('NaOH 加入体积 (mL)', fontsize=9)
ax2.set_ylabel('pH', fontsize=9)
ax2.set_title('弱酸强碱滴定 (HAc × NaOH)', fontsize=10, color='#1a1a2e', fontweight='bold')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_xlim(0, 50)
ax2.set_ylim(0, 14)
ax2.grid(True, alpha=0.15)

# 指示剂选择
ax2.annotate('突跃范围\npH 7.7~9.7', xy=(25, 9), xytext=(32, 8), fontsize=8, color='#2980b9',
            arrowprops=dict(arrowstyle='->', color='#2980b9'))

# Indicator choices
ax1.text(25, 12.5, '指示剂: 酚酞(8.2-10.0)\n甲基橙(3.1-4.4)\n均可', ha='center', fontsize=7, color='#555')
ax2.text(25, 12.5, '指示剂: 酚酞(8.2-10.0)\n不可用甲基橙\n(变色范围偏离突跃)', ha='center', fontsize=7, color='#555')

fig.suptitle('酸碱滴定曲线与指示剂选择', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'chem_exp_titration.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 8. 常见实验装置
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.05, right=0.97, wspace=0.25, hspace=0.35, bottom=0.08, top=0.9)

# 蒸馏装置
ax1 = axes[0, 0]
ax1.axis('off')
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 3)
ax1.set_title('蒸馏装置', fontsize=10, color='#2980b9', fontweight='bold')

ax1.add_patch(plt.Circle((0.8, 0.8), 0.4, fill=True, facecolor='#e8f8f0', edgecolor='#27ae60'))
ax1.text(0.8, 0.8, '加热', ha='center', fontsize=8, color='#27ae60')

ax1.add_patch(plt.Rectangle((0.6, 1.2), 0.4, 0.8, fill=True, facecolor='#f0f0f0', edgecolor='#888'))
ax1.text(0.8, 1.6, '蒸馏\n烧瓶', ha='center', fontsize=7, color='#555')

ax1.add_patch(plt.Rectangle((1.2, 1.4), 0.8, 0.3, fill=True, facecolor='#eaf2f8', edgecolor='#3498db'))
ax1.text(1.6, 1.55, '冷凝管', ha='center', fontsize=7, color='#3498db')
ax1.text(2.1, 1.5, '冷水\n出', fontsize=6, color='#3498db')
ax1.text(1.2, 1.3, '冷水\n入', fontsize=6, color='#3498db', ha='right')

ax1.add_patch(plt.Circle((2.0, 0.5), 0.4, fill=True, facecolor='#fce4ec', edgecolor='#e74c3c'))
ax1.text(2.0, 0.5, '接收', ha='center', fontsize=8, color='#e74c3c')

# 过滤装置
ax2 = axes[0, 1]
ax2.axis('off')
ax2.set_xlim(0, 3)
ax2.set_ylim(0, 3)
ax2.set_title('过滤装置', fontsize=10, color='#2980b9', fontweight='bold')

# Funnel shape (triangle)
ax2.add_patch(plt.Rectangle((0.8, 1.0), 0.2, 1.5, fill=True, facecolor='#eaf2f8', edgecolor='#3498db'))
ax2.add_patch(plt.Rectangle((0.65, 2.0), 0.5, 0.3, fill=True, facecolor='#fce4ec', edgecolor='#e74c3c'))
ax2.text(0.9, 2.15, '滤纸', ha='center', fontsize=7, color='#e74c3c')

# Filter paper (dashed triangle)
ax2.plot([0.7, 1.1, 0.7], [1.0, 1.0, 1.8], '-', color='#e74c3c', linewidth=1)

# Beaker below
ax2.add_patch(plt.Rectangle((0.4, 0.3), 1.0, 0.5, fill=True, facecolor='#e8f8f0', edgecolor='#27ae60'))
ax2.text(0.9, 0.55, '滤液', ha='center', fontsize=7, color='#27ae60')

# 萃取分液
ax3 = axes[0, 2]
ax3.axis('off')
ax3.set_xlim(0, 3)
ax3.set_ylim(0, 3)
ax3.set_title('分液漏斗(萃取)', fontsize=10, color='#2980b9', fontweight='bold')

# Funnel shape
ax3.add_patch(plt.Rectangle((0.9, 0.8), 0.2, 1.8, fill=True, facecolor='#f0f0f0', edgecolor='#888'))
ax3.add_patch(plt.Circle((1.0, 2.6), 0.3, fill=True, facecolor='#e8f8f0', edgecolor='#27ae60'))
ax3.text(1.0, 2.6, '塞', ha='center', fontsize=7, color='#27ae60')

ax3.text(0.6, 1.8, '有机层', fontsize=7, color='#e74c3c')
ax3.text(0.6, 1.1, '水层', fontsize=7, color='#3498db')

# 常见仪器
ax4 = axes[1, 0]
ax4.axis('off')
ax4.set_xlim(0, 3)
ax4.set_ylim(0, 3)
ax4.set_title('计量仪器', fontsize=10, color='#2980b9', fontweight='bold')

instruments = [
    '量筒: 粗略量取液体',
    '容量瓶: 精确配制溶液',
    '滴定管: 精确量取液体',
    '移液管: 精确转移液体',
    '托盘天平: 称量固体(0.1g)',
    '分析天平: 精确称量(0.0001g)',
]
for i, inst in enumerate(instruments):
    ax4.text(0.1, 2.5 - i*0.35, '• ' + inst, fontsize=7, color='#555')

# 加热仪器
ax5 = axes[1, 1]
ax5.axis('off')
ax5.set_xlim(0, 3)
ax5.set_ylim(0, 3)
ax5.set_title('加热与安全', fontsize=10, color='#2980b9', fontweight='bold')

items = [
    ('酒精灯', '加热温度400-500℃'),
    ('水浴加热', '均匀受热, 控温方便'),
    ('油浴/沙浴', '更高温度加热'),
    ('石棉网', '均匀传热, 防炸裂'),
    ('坩埚钳', '夹取高温物品'),
    ('蒸发皿', '蒸发浓缩溶液'),
]
for i, (name, desc) in enumerate(items):
    ax5.text(0.1, 2.5 - i*0.35, f'• {name}: {desc}', fontsize=7, color='#555')

# 气体收集
ax6 = axes[1, 2]
ax6.axis('off')
ax6.set_xlim(0, 3)
ax6.set_ylim(0, 3)
ax6.set_title('气体收集方法', fontsize=10, color='#2980b9', fontweight='bold')

methods_gas = [
    '向上排空气: Cl₂, CO₂, SO₂',
    '向下排空气: H₂, NH₃, CH₄',
    '排水法: H₂, O₂, NO, CH₄',
    '(不溶于水/微溶于水的气体)',
    '',
    '检验纯度: H₂/CO/CH₄点火',
    '听爆鸣声(先收集后点燃)',
]
for i, m in enumerate(methods_gas):
    ax6.text(0.1, 2.5 - i*0.28, m, fontsize=7, color='#555')

fig.suptitle('常见化学实验装置与仪器', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'chem_exp_apparatus.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 9. 气体制取
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.05, right=0.97, wspace=0.25, hspace=0.35, bottom=0.08, top=0.9)

# O2
ax1 = axes[0, 0]
ax1.axis('off')
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 3)
ax1.set_title('O₂ 制取', fontsize=10, color='#e74c3c', fontweight='bold')

ax1.text(0.1, 2.7, '原理: 2KClO₃ → 2KCl+3O₂↑', fontsize=7, color='#555')
ax1.text(0.1, 2.4, '催化剂: MnO₂', fontsize=7, color='#e67e22')
ax1.text(0.1, 2.1, '收集: 排水法/向上排空气', fontsize=7, color='#555')
ax1.text(0.1, 1.8, '检验: 带火星木条复燃', fontsize=7, color='#c0392b')
ax1.text(0.1, 1.3, '装置: 固+固加热', fontsize=7, color='#555')
ax1.text(0.1, 1.0, '试管口略向下倾斜', fontsize=7, color='#c0392b', fontweight='bold')
ax1.text(0.1, 0.7, '(防止冷凝水倒流炸裂) ', fontsize=6, color='#888')

# H2
ax2 = axes[0, 1]
ax2.axis('off')
ax2.set_xlim(0, 3)
ax2.set_ylim(0, 3)
ax2.set_title('H₂ 制取', fontsize=10, color='#3498db', fontweight='bold')

ax2.text(0.1, 2.7, '原理: Zn+H₂SO₄→ZnSO₄+H₂↑', fontsize=7, color='#555')
ax2.text(0.1, 2.4, '装置: 固+液不加热', fontsize=7, color='#555')
ax2.text(0.1, 2.1, '启普发生器/简易装置', fontsize=7, color='#555')
ax2.text(0.1, 1.8, '收集: 排水法/向下排空气', fontsize=7, color='#555')
ax2.text(0.1, 1.5, '验纯: 收集→点燃(爆鸣声)', fontsize=7, color='#c0392b', fontweight='bold')
ax2.text(0.1, 1.1, '注意事项:', fontsize=7, color='#1a1a2e')
ax2.text(0.1, 0.8, '• 使用前必须验纯', fontsize=7, color='#555')
ax2.text(0.1, 0.5, '• 不能用浓H₂SO₄', fontsize=7, color='#e74c3c')

# CO2
ax3 = axes[0, 2]
ax3.axis('off')
ax3.set_xlim(0, 3)
ax3.set_ylim(0, 3)
ax3.set_title('CO₂ 制取', fontsize=10, color='#27ae60', fontweight='bold')

ax3.text(0.1, 2.7, '原理: CaCO₃+2HCl→', fontsize=7, color='#555')
ax3.text(0.1, 2.4, '     CaCl₂+CO₂↑+H₂O', fontsize=7, color='#555')
ax3.text(0.1, 2.1, '装置: 固+液不加热', fontsize=7, color='#555')
ax3.text(0.1, 1.8, '收集: 向上排空气法', fontsize=7, color='#555')
ax3.text(0.1, 1.5, '检验: 澄清石灰水变浑浊', fontsize=7, color='#c0392b', fontweight='bold')
ax3.text(0.1, 1.1, '注意:', fontsize=7, color='#1a1a2e')
ax3.text(0.1, 0.8, '• 不能用H₂SO₄', fontsize=7, color='#e74c3c')
ax3.text(0.1, 0.5, '  (CaSO₄微溶→包裹) ', fontsize=6, color='#888')

# NH3
ax4 = axes[1, 0]
ax4.axis('off')
ax4.set_xlim(0, 3)
ax4.set_ylim(0, 3)
ax4.set_title('NH₃ 制取', fontsize=10, color='#8e44ad', fontweight='bold')

ax4.text(0.1, 2.7, '原理: 2NH₄Cl+Ca(OH)₂→', fontsize=7, color='#555')
ax4.text(0.1, 2.4, '     CaCl₂+2NH₃↑+2H₂O', fontsize=7, color='#555')
ax4.text(0.1, 2.1, '干燥: 碱石灰(不可用CaCl₂)', fontsize=7, color='#e67e22')
ax4.text(0.1, 1.8, '收集: 向下排空气法', fontsize=7, color='#555')
ax4.text(0.1, 1.5, '检验: 湿润红色石蕊试纸变蓝', fontsize=7, color='#c0392b', fontweight='bold')
ax4.text(0.1, 1.0, '尾气处理: 水吸收', fontsize=7, color='#555')
ax4.text(0.1, 0.7, '(防倒吸: 倒置漏斗) ', fontsize=6, color='#888')

# Cl2
ax5 = axes[1, 1]
ax5.axis('off')
ax5.set_xlim(0, 3)
ax5.set_ylim(0, 3)
ax5.set_title('Cl₂ 制取', fontsize=10, color='#e67e22', fontweight='bold')

ax5.text(0.1, 2.7, '原理: MnO₂+4HCl(浓)→', fontsize=7, color='#555')
ax5.text(0.1, 2.4, '     MnCl₂+Cl₂↑+2H₂O', fontsize=7, color='#555')
ax5.text(0.1, 2.1, '净化: 饱和食盐水(除HCl)', fontsize=7, color='#555')
ax5.text(0.1, 1.8, '干燥: 浓H₂SO₄', fontsize=7, color='#555')
ax5.text(0.1, 1.5, '收集: 向上排空气法', fontsize=7, color='#555')
ax5.text(0.1, 1.2, '检验: 湿润KI淀粉试纸变蓝', fontsize=7, color='#c0392b', fontweight='bold')
ax5.text(0.1, 0.8, '尾气: NaOH吸收', fontsize=7, color='#c0392b', fontweight='bold')

# 综合对比
ax6 = axes[1, 2]
ax6.axis('off')
ax6.set_xlim(0, 3)
ax6.set_ylim(0, 3)
ax6.set_title('气体干燥剂选择', fontsize=10, color='#2980b9', fontweight='bold')

drying = [
    '酸性干燥剂:',
    '  浓H₂SO₄ — 干燥酸性气体',
    '   (不可干燥H₂S/NH₃)',
    '中性干燥剂:',
    '  CaCl₂ — 大多数气体',
    '   (不可干燥NH₃)',
    '碱性干燥剂:',
    '  碱石灰 — 干燥碱性气体',
    '   (不可干燥酸性气体)',
]
for i, d in enumerate(drying):
    ax6.text(0.1, 2.7 - i*0.25, d, fontsize=7, color='#555')

fig.suptitle('常见气体的实验室制取', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'chem_exp_gas.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 10. 物质分离提纯
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.06)
ax.axis('off')
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.set_title('物质分离提纯方法归纳', fontsize=14, color='#2980b9', fontweight='bold')

methods_data = [
    ('过滤', '固-液分离', '一贴二低三靠', '#3498db'),
    ('蒸发结晶', '固体从溶液中分离', '玻璃棒搅拌防飞溅', '#27ae60'),
    ('蒸馏', '液-液分离(沸点差)', '温度计位置: 支管口', '#e74c3c'),
    ('分液', '互不相溶液体分离', '下层从下口出', '#e67e22'),
    ('萃取', '溶质在不同溶剂中\n分配比不同', '常用CCl₄/苯/乙醚', '#8e44ad'),
    ('升华', '固体直接变气体', '适用于易升华物质\n(I₂, 萘等)', '#f39c12'),
    ('色谱法', '混合物在固定相/\n流动相中分配不同', '柱色谱/纸色谱/薄层', '#1abc9c'),
    ('重结晶', '利用溶解度随温度\n变化差异', '趁热过滤防结晶', '#2c3e50'),
]

for i, (name, principle, note, color) in enumerate(methods_data):
    row = i // 4
    col = i % 4
    x = 0.3 + col * 2.0
    y = 4.5 - row * 2.2

    ax.add_patch(plt.Rectangle((x, y-0.5), 1.7, 1.8, fill=True, facecolor=color, alpha=0.08, edgecolor=color, linewidth=1.5))
    ax.text(x+0.85, y+1.1, name, ha='center', fontsize=10, color=color, fontweight='bold')
    ax.text(x+0.85, y+0.7, principle, ha='center', fontsize=7, color='#555')
    ax.text(x+0.85, y-0.1, note, ha='center', fontsize=7, color='#c0392b')

# Bottom tips
tips = [
    '提纯原则: 不增(不增新杂质) · 不减(不减被提纯物) · 易分离 · 易转化',
    '除杂顺序: 先除杂后干燥 → Na₂CO₃→NaOH→盐酸(调节pH)是常见除杂组合',
]
for i, tip in enumerate(tips):
    ax.text(0.3, 0.5 - i*0.3, tip, fontsize=8, color='#1a1a2e')

fig.savefig(os.path.join(OUT, 'chem_exp_purify.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 11. 溶解度与温度曲线
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
plt.subplots_adjust(left=0.08, right=0.97, wspace=0.25, bottom=0.1, top=0.88)

# Solubility curves
ax1 = axes[0]
T = np.linspace(0, 100, 200)

solubility_data = [
    ('KNO₃', 13.9 + 0.4 * T + 0.001 * T**2, '#e74c3c'),
    ('NaCl', 35.7 + 0.02 * T, '#3498db'),
    ('NH₄Cl', 29.4 + 0.15 * T + 0.001 * T**2, '#27ae60'),
    ('KCl', 27.6 + 0.08 * T + 0.001 * T**2, '#e67e22'),
]

for name, s, color in solubility_data:
    ax1.plot(T, s, '-', linewidth=2, label=name, color=color)

ax1.set_xlabel('温度 (℃)', fontsize=9)
ax1.set_ylabel('溶解度 (g/100g水)', fontsize=9)
ax1.set_title('常见物质溶解度曲线', fontsize=10, color='#1a1a2e', fontweight='bold')
ax1.legend(fontsize=8)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(True, alpha=0.15)

# Temperature change in a reaction (cooling curve)
ax2 = axes[1]
t_min = np.linspace(0, 10, 200)
# Simulate cooling curve of a hot solution
T_hot = 80 * np.exp(-0.2 * t_min) + 25
ax2.plot(t_min, T_hot, '-', color='#e74c3c', linewidth=2.5)
ax2.set_xlabel('时间 (min)', fontsize=9)
ax2.set_ylabel('温度 (℃)', fontsize=9)
ax2.set_title('热溶液的冷却结晶曲线', fontsize=10, color='#1a1a2e', fontweight='bold')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.grid(True, alpha=0.15)

ax2.annotate('降温→溶解度下降\n→晶体析出', xy=(3, 45), xytext=(4.5, 55), fontsize=8, color='#e67e22',
            arrowprops=dict(arrowstyle='->', color='#e67e22'))

fig.suptitle('溶解度与结晶', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'chem_exp_temp.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 12. 定量实验数据分析
fig, axes = plt.subplots(2, 2, figsize=(8, 5.5))
plt.subplots_adjust(left=0.09, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# 中和热测定
ax1 = axes[0, 0]
times = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
temps = np.array([22.0, 22.5, 25.0, 27.5, 28.0, 28.0, 27.8, 27.5, 27.2])
extrap = np.polyfit(times[2:5], temps[2:5], 1)
t_max_line = extrap[0] * times + extrap[1]

ax1.plot(times, temps, 'o-', color='#e74c3c', linewidth=2, markersize=6, label='实测值')
ax1.plot(times, t_max_line, '--', color='#3498db', linewidth=1.5, alpha=0.7, label='外推线')
ax1.axvline(x=0, color='#888', linewidth=0.5, linestyle='--')
ax1.set_xlabel('时间 (min)', fontsize=9)
ax1.set_ylabel('温度 (℃)', fontsize=9)
ax1.set_title('中和反应热测定', fontsize=10, color='#1a1a2e', fontweight='bold')
ax1.legend(fontsize=7)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(True, alpha=0.15)

# 化学反应速率
ax2 = axes[0, 1]
t_rate = np.linspace(0, 10, 100)
conc = 0.5 * np.exp(-0.3 * t_rate)
rate = -0.3 * conc

ax2.plot(t_rate, conc, '-', color='#3498db', linewidth=2, label='反应物浓度')
ax2_twin = ax2.twinx()
ax2_twin.plot(t_rate, rate, '--', color='#e74c3c', linewidth=2, label='反应速率')

ax2.set_xlabel('时间 (min)', fontsize=9)
ax2.set_ylabel('浓度 (mol/L)', fontsize=9, color='#3498db')
ax2_twin.set_ylabel('速率 (mol·L⁻¹·min⁻¹)', fontsize=9, color='#e74c3c')
ax2.set_title('化学反应速率变化', fontsize=10, color='#1a1a2e', fontweight='bold')
lines1, labels1 = ax2.get_legend_handles_labels()
lines2, labels2 = ax2_twin.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, fontsize=7)
ax2.spines['top'].set_visible(False)
ax2.grid(True, alpha=0.15)

# 误差分析
ax3 = axes[1, 0]
ax3.axis('off')
ax3.set_xlim(0, 3)
ax3.set_ylim(0, 3)
ax3.set_title('定量实验误差分析思路', fontsize=10, color='#1a1a2e', fontweight='bold')

errors = [
    '① 系统误差: 仪器/方法固有缺陷',
    '② 偶然误差: 操作/读数随机波动',
    '③ 过失误差: 操作明显错误',
    '',
    '减小误差方法:',
    '• 多次测量取平均值',
    '• 校准仪器',
    '• 空白实验/对照实验',
    '• 选择精密度更高的仪器',
]
for i, e in enumerate(errors):
    ax3.text(0.1, 2.7 - i*0.28, e, fontsize=7, color='#555')

# 实验数据处理
ax4 = axes[1, 1]
ax4.axis('off')
ax4.set_xlim(0, 3)
ax4.set_ylim(0, 3)
ax4.set_title('数据处理方法', fontsize=10, color='#1a1a2e', fontweight='bold')

methods_data = [
    '列表法: 原始数据整理',
    '图像法: 直观展示变量关系',
    '公式法: 代入公式直接计算',
    '线性回归: 求最佳拟合直线',
    '',
    '有效数字:',
    '• 加减: 以小数位最少为准',
    '• 乘除: 以有效数字最少为准',
    '• 结果保留与仪器精度一致',
]
for i, m in enumerate(methods_data):
    ax4.text(0.1, 2.7 - i*0.28, m, fontsize=7, color='#555')

fig.suptitle('定量实验与数据分析', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'chem_exp_quant.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# ════════════════════════════════════════
# 三、化学方程式（6张）
# ════════════════════════════════════════

# 13. 反应能量变化图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
plt.subplots_adjust(left=0.08, right=0.97, wspace=0.3, bottom=0.1, top=0.88)

# Exothermic
ax1.axis('off')
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 4)
ax1.set_title('放热反应 (ΔH < 0)', fontsize=11, color='#e74c3c', fontweight='bold')

# Energy diagram
r = np.linspace(0.5, 3.5, 100)
# Reaction coordinate: simple path
Ea = 2.5  # activation energy
E_reactant = 0.5
E_product = 1.0

# Draw energy curve
x_path = [0.5, 1.5, 2.5, 3.5]
y_path = [E_reactant, Ea, Ea, E_product]
x_smooth = np.linspace(0.5, 3.5, 200)
y_smooth = E_reactant + (Ea - E_reactant) * np.exp(-((x_smooth - 1.5) / 0.4) ** 2)
# Add product side
y_smooth[x_smooth > 2.5] = Ea + (E_product - Ea) * (1 - np.exp(-((x_smooth[x_smooth > 2.5] - 2.5) / 0.5) ** 2))
y_smooth = np.minimum(y_smooth, Ea * 1.2)

ax1.plot(x_smooth, y_smooth, '-', color='#c0392b', linewidth=2.5)

# Labels
ax1.text(1.0, E_reactant-0.2, '反应物', ha='center', fontsize=8, color='#3498db')
ax1.text(3.0, E_product-0.2, '生成物', ha='center', fontsize=8, color='#27ae60')
ax1.annotate('ΔH < 0\n(放热)', xy=(3.0, (E_reactant+E_product)/2), xytext=(3.5, 1.5), fontsize=8, color='#e74c3c',
            arrowprops=dict(arrowstyle='->', color='#e74c3c'))
ax1.annotate('活化能\n(Ea)', xy=(1.5, (E_reactant+Ea)/2), xytext=(0.2, 2.5), fontsize=8, color='#8e44ad',
            arrowprops=dict(arrowstyle='<->', color='#8e44ad'))

# Endothermic
ax2.axis('off')
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 4)
ax2.set_title('吸热反应 (ΔH > 0)', fontsize=11, color='#2980b9', fontweight='bold')

y_path2 = [E_reactant, Ea+0.3, Ea+0.3, E_reactant+1.0]
y_smooth2 = E_reactant + (Ea+0.3 - E_reactant) * np.exp(-((x_smooth - 1.5) / 0.4) ** 2)
y_smooth2[x_smooth > 2.5] = Ea+0.3 + (E_reactant+1.0 - Ea-0.3) * (1 - np.exp(-((x_smooth[x_smooth > 2.5] - 2.5) / 0.5) ** 2))
y_smooth2 = np.minimum(y_smooth2, Ea*1.3)

ax2.plot(x_smooth, y_smooth2, '-', color='#2980b9', linewidth=2.5)

ax2.text(1.0, E_reactant-0.2, '反应物', ha='center', fontsize=8, color='#3498db')
ax2.text(3.0, E_reactant+1.0-0.2, '生成物', ha='center', fontsize=8, color='#e74c3c')
ax2.annotate('ΔH > 0\n(吸热)', xy=(3.0, E_reactant+0.5), xytext=(3.5, 1.5), fontsize=8, color='#2980b9',
            arrowprops=dict(arrowstyle='->', color='#2980b9'))
ax2.annotate('活化能\n(Ea)', xy=(1.5, (E_reactant+Ea+0.3)/2), xytext=(0.2, 2.5), fontsize=8, color='#8e44ad',
            arrowprops=dict(arrowstyle='<->', color='#8e44ad'))

fig.suptitle('化学反应中的能量变化', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'chem_eq_energy.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 14. 反应速率与化学平衡
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.07, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# 浓度-时间图
ax1 = axes[0, 0]
t = np.linspace(0, 10, 100)
A0, B0, C0 = 1.0, 0, 0
k = 0.3
A_t = A0 * np.exp(-k * t)
B_t = A0 * (1 - np.exp(-k * t)) * 0.5
C_t = A0 * (1 - np.exp(-k * t)) * 0.5

ax1.plot(t, A_t, '-', color='#e74c3c', linewidth=2, label='A (反应物)')
ax1.plot(t, B_t, '-', color='#3498db', linewidth=2, label='B (产物)')
ax1.plot(t, C_t, '--', color='#27ae60', linewidth=2, label='C (产物)')
ax1.set_xlabel('时间', fontsize=9)
ax1.set_ylabel('浓度', fontsize=9)
ax1.set_title('反应物浓度随时间变化', fontsize=9, color='#1a1a2e', fontweight='bold')
ax1.legend(fontsize=7)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.grid(True, alpha=0.15)

# 勒夏特列原理
ax2 = axes[0, 1]
ax2.axis('off')
ax2.set_xlim(0, 3)
ax2.set_ylim(0, 3)
ax2.set_title('勒夏特列原理图解', fontsize=9, color='#1a1a2e', fontweight='bold')

ax2.text(0.1, 2.7, '平衡移动方向', fontsize=9, color='#1a1a2e', fontweight='bold')
ax2.text(0.1, 2.3, '改变条件→平衡向', fontsize=8, color='#555')
ax2.text(0.1, 2.0, '"减弱这种改变"的方向移动', fontsize=8, color='#c0392b', fontweight='bold')

factors = [
    ('浓度↑', '向消耗该物质的方向'),
    ('压强↑', '向气体体积减小的方向'),
    ('温度↑', '向吸热方向移动'),
    ('催化剂', '同等改变正逆反应速率'),
]
for i, (change, effect) in enumerate(factors):
    ax2.text(0.1, 1.5 - i*0.3, f'• {change}: {effect}', fontsize=7, color='#555')

# 速率-时间图 (催化剂)
ax3 = axes[0, 2]
t_rate2 = np.linspace(0, 8, 100)
v_fwd = 0.5 + 0.3 * np.exp(-0.5 * t_rate2)
v_rev = 0.2 * (1 - np.exp(-0.5 * t_rate2))

ax3.plot(t_rate2, v_fwd, '-', color='#e74c3c', linewidth=2, label='正反应')
ax3.plot(t_rate2, v_rev, '-', color='#3498db', linewidth=2, label='逆反应')
ax3.axhline(y=0.5, color='#888', linewidth=1, linestyle='--', alpha=0.5)
ax3.text(5, 0.55, '加入催化剂', fontsize=8, color='#27ae60')
ax3.vlines(x=4, ymin=0.2, ymax=0.7, color='#27ae60', linewidth=1, linestyle=':')
ax3.set_xlabel('时间', fontsize=9)
ax3.set_ylabel('速率', fontsize=9)
ax3.set_title('催化剂对反应速率的影响', fontsize=9, color='#1a1a2e', fontweight='bold')
ax3.legend(fontsize=7)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.grid(True, alpha=0.15)

# 转化率-温度
ax4 = axes[1, 0]
T_plot = np.linspace(200, 600, 100)
conv_exo = 0.9 / (1 + np.exp(0.01 * (T_plot - 400)))  # exothermic
conv_endo = 0.3 + 0.6 / (1 + np.exp(-0.015 * (T_plot - 400)))  # endothermic

ax4.plot(T_plot, conv_exo, '-', color='#e74c3c', linewidth=2, label='放热反应')
ax4.plot(T_plot, conv_endo, '-', color='#3498db', linewidth=2, label='吸热反应')
ax4.set_xlabel('温度', fontsize=9)
ax4.set_ylabel('转化率', fontsize=9)
ax4.set_title('温度对平衡转化率的影响', fontsize=9, color='#1a1a2e', fontweight='bold')
ax4.legend(fontsize=7)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.grid(True, alpha=0.15)

# 压强影响
ax5 = axes[1, 1]
P_plot = np.linspace(1, 10, 100)
conv_P = 0.3 + 0.5 * (1 - np.exp(-0.3 * P_plot))  # volume decreasing

ax5.plot(P_plot, conv_P, '-', color='#8e44ad', linewidth=2)
ax5.set_xlabel('压强 (atm)', fontsize=9)
ax5.set_ylabel('转化率', fontsize=9)
ax5.set_title('压强对平衡转化率的影响\n(气体分子数减少)', fontsize=9, color='#1a1a2e', fontweight='bold')
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.grid(True, alpha=0.15)

# 平衡常数
ax6 = axes[1, 2]
ax6.axis('off')
ax6.set_xlim(0, 3)
ax6.set_ylim(0, 3)
ax6.set_title('化学平衡常数', fontsize=9, color='#1a1a2e', fontweight='bold')

ax6.text(0.1, 2.7, 'aA + bB ⇌ cC + dD', fontsize=9, color='#1a1a2e', fontweight='bold')
ax6.text(0.1, 2.3, 'K = [C]^c[D]^d / [A]^a[B]^b', fontsize=8, color='#c0392b')
ax6.text(0.1, 1.9, 'K只与温度有关', fontsize=8, color='#e67e22', fontweight='bold')
ax6.text(0.1, 1.5, 'K > 10⁵: 反应完全', fontsize=7, color='#27ae60')
ax6.text(0.1, 1.2, 'K < 10⁻⁵: 反应几乎不发生', fontsize=7, color='#e74c3c')
ax6.text(0.1, 0.9, 'K在10⁻⁵~10⁵: 可逆反应', fontsize=7, color='#e67e22')

fig.suptitle('化学反应速率与化学平衡', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'chem_eq_rate.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 15. 原电池与电解池
fig, axes = plt.subplots(2, 2, figsize=(8, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# 原电池 (Zn-Cu)
ax1 = axes[0, 0]
ax1.axis('off')
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 4)
ax1.set_title('铜锌原电池', fontsize=11, color='#27ae60', fontweight='bold')

# Beaker 1 (Zn)
ax1.add_patch(plt.Rectangle((0.2, 0.5), 1.2, 2.0, fill=True, facecolor='#e8f8f0', edgecolor='#27ae60'))
ax1.text(0.8, 2.2, 'ZnSO₄溶液', ha='center', fontsize=7, color='#27ae60')
ax1.add_patch(plt.Rectangle((0.5, 1.0), 0.3, 1.5, fill=True, facecolor='#e0e0e0', edgecolor='#888'))
ax1.text(0.65, 1.75, 'Zn', ha='center', fontsize=10, color='#333', fontweight='bold')
# Oxidation
ax1.text(0.65, 0.8, 'Zn - 2e⁻→Zn²⁺', ha='center', fontsize=7, color='#c0392b')

# Beaker 2 (Cu)
ax1.add_patch(plt.Rectangle((2.6, 0.5), 1.2, 2.0, fill=True, facecolor='#fce4ec', edgecolor='#e74c3c'))
ax1.text(3.2, 2.2, 'CuSO₄溶液', ha='center', fontsize=7, color='#e74c3c')
ax1.add_patch(plt.Rectangle((2.9, 1.0), 0.3, 1.5, fill=True, facecolor='#e8a080', edgecolor='#c0392b'))
ax1.text(3.05, 1.75, 'Cu', ha='center', fontsize=10, color='#333', fontweight='bold')
# Reduction
ax1.text(3.05, 0.8, 'Cu²⁺+2e⁻→Cu', ha='center', fontsize=7, color='#2980b9')

# Salt bridge
ax1.add_patch(plt.Rectangle((1.5, 1.2), 0.8, 0.3, fill=True, facecolor='#f0f0f0', edgecolor='#888'))
ax1.text(1.9, 1.35, '盐桥', ha='center', fontsize=8, color='#555')
ax1.text(1.9, 1.7, 'KCl饱和溶液', ha='center', fontsize=6, color='#888')

# Wire
ax1.plot([0.65, 3.05], [3.0, 3.0], 'k-', linewidth=2)
ax1.plot([0.65, 0.65], [2.5, 3.0], 'k-', linewidth=2)
ax1.plot([3.05, 3.05], [2.5, 3.0], 'k-', linewidth=2)

# Electron flow
ax1.annotate('e⁻', xy=(1.5, 3.2), xytext=(2.5, 3.2), fontsize=10, color='#e74c3c',
            arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax1.text(2.0, 3.4, '电流方向', ha='center', fontsize=7, color='#888')

# Electrode signs
ax1.text(0.65, 3.1, '(-)', fontsize=8, color='#2980b9', ha='center')
ax1.text(3.05, 3.1, '(+)', fontsize=8, color='#e74c3c', ha='center')

# 电解池
ax2 = axes[0, 1]
ax2.axis('off')
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 4)
ax2.set_title('电解饱和食盐水', fontsize=11, color='#2980b9', fontweight='bold')

# Electrolysis cell
ax2.add_patch(plt.Rectangle((0.8, 0.5), 2.4, 2.0, fill=True, facecolor='#eaf2f8', edgecolor='#3498db'))
ax2.text(2.0, 2.2, 'NaCl溶液', ha='center', fontsize=8, color='#2980b9')

# Anode (+)
ax2.add_patch(plt.Rectangle((0.8, 0.8), 0.8, 1.2, fill=True, facecolor='#fce4ec', edgecolor='#e74c3c'))
ax2.text(1.2, 1.4, '阳极\n(+)', ha='center', fontsize=8, color='#e74c3c', fontweight='bold')
ax2.text(1.2, 0.8, '2Cl⁻→Cl₂', ha='center', fontsize=7, color='#c0392b')

# Cathode (-)
ax2.add_patch(plt.Rectangle((2.8, 0.8), 0.8, 1.2, fill=True, facecolor='#e8f8f0', edgecolor='#27ae60'))
ax2.text(3.2, 1.4, '阴极\n(-)', ha='center', fontsize=8, color='#27ae60', fontweight='bold')
ax2.text(3.2, 0.8, '2H₂O→H₂+OH⁻', ha='center', fontsize=7, color='#1d8348')

# Power
ax2.plot([1.2, 3.2], [3.0, 3.0], 'k-', linewidth=2)
ax2.text(2.0, 3.3, '直流电源', ha='center', fontsize=7, color='#888')
ax2.text(1.2, 3.1, '(+)', fontsize=8, color='#e74c3c', ha='center')
ax2.text(3.2, 3.1, '(-)', fontsize=8, color='#27ae60', ha='center')

# 金属腐蚀
ax3 = axes[1, 0]
ax3.axis('off')
ax3.set_xlim(0, 3)
ax3.set_ylim(0, 3)
ax3.set_title('金属腐蚀与防护', fontsize=10, color='#1a1a2e', fontweight='bold')

corrosion = [
    '化学腐蚀: 金属与干燥气体/非电解质',
    '电化学腐蚀(更常见):',
    '  吸氧腐蚀: Fe+O₂+H₂O→Fe₂O₃',
    '  析氢腐蚀: Fe+2H⁺→Fe²⁺+H₂↑',
    '',
    '防护方法:',
    '• 表面涂覆(油漆/电镀)',
    '• 牺牲阳极(Zn保护Fe)',
    '• 外加电流阴极保护',
    '• 制成合金(不锈钢)',
]
for i, c in enumerate(corrosion):
    ax3.text(0.1, 2.7 - i*0.25, c, fontsize=7, color='#555')

# 燃料电池
ax4 = axes[1, 1]
ax4.axis('off')
ax4.set_xlim(0, 3)
ax4.set_ylim(0, 3)
ax4.set_title('氢氧燃料电池', fontsize=10, color='#27ae60', fontweight='bold')

# Cell
ax4.add_patch(plt.Rectangle((0.8, 0.8), 1.6, 1.6, fill=True, facecolor='#e8f8f0', edgecolor='#27ae60'))
ax4.text(1.6, 2.0, '电解液\n(KOH)', ha='center', fontsize=8, color='#555')

# Electrodes
ax4.add_patch(plt.Rectangle((0.8, 0.8), 0.3, 1.6, fill=True, facecolor='#e0e0e0', edgecolor='#888'))
ax4.add_patch(plt.Rectangle((2.1, 0.8), 0.3, 1.6, fill=True, facecolor='#e0e0e0', edgecolor='#888'))

# Anode
ax4.text(0.95, 1.6, '负极\nH₂', ha='center', fontsize=7, color='#e74c3c', fontweight='bold')
ax4.text(0.95, 1.2, 'H₂+2OH⁻→', ha='center', fontsize=6, color='#c0392b')
ax4.text(0.95, 0.9, '2H₂O+2e⁻', ha='center', fontsize=6, color='#c0392b')

# Cathode
ax4.text(2.25, 1.6, '正极\nO₂', ha='center', fontsize=7, color='#2980b9', fontweight='bold')
ax4.text(2.25, 1.2, 'O₂+2H₂O+4e⁻', ha='center', fontsize=6, color='#2980b9')
ax4.text(2.25, 0.9, '→4OH⁻', ha='center', fontsize=6, color='#2980b9')

# External circuit
ax4.plot([0.95, 2.25], [2.6, 2.6], 'k-', linewidth=1.5)
ax4.text(1.6, 2.8, '负载(灯泡)', ha='center', fontsize=7, color='#888')

fig.suptitle('电化学基础', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'chem_eq_electrochemical.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 16. 氧化还原反应
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# 氧化还原概念
ax1 = axes[0, 0]
ax1.axis('off')
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 3)
ax1.set_title('氧化还原反应概念', fontsize=10, color='#e74c3c', fontweight='bold')

concepts = [
    '升失氧化还原剂',
    '(化合价升高, 失去电子,',
    ' 被氧化, 发生氧化反应,',
    ' 作为还原剂)',
    '',
    '降得还原氧化剂',
    '(化合价降低, 得到电子,',
    ' 被还原, 发生还原反应,',
    ' 作为氧化剂)',
]
for i, c in enumerate(concepts):
    color = '#c0392b' if i == 0 else ('#2980b9' if i == 5 else '#555')
    fontw = 'bold' if i in [0, 5] else 'normal'
    ax1.text(0.1, 2.7 - i*0.28, c, fontsize=7, color=color, fontweight=fontw)

# 化合价变化
ax2 = axes[0, 1]
ax2.axis('off')
ax2.set_xlim(0, 3)
ax2.set_ylim(0, 3)
ax2.set_title('化合价升降分析示例', fontsize=10, color='#e74c3c', fontweight='bold')

examples = [
    'Zn + CuSO₄ → ZnSO₄ + Cu',
    'Zn: 0 → +2 (升2, 还原剂)',
    'Cu: +2 → 0 (降2, 氧化剂)',
    '',
    '2KMnO₄ + 16HCl →',
    '2MnCl₂ + 5Cl₂ + ...',
    'Mn: +7→+2 (降5×2=10)',
    'Cl: -1→0 (升1×10=10)',  # Actually 10 electrons for 5Cl2
    '得失电子总数相等',
]
for i, ex in enumerate(examples):
    ax2.text(0.1, 2.7 - i*0.25, ex, fontsize=7, color='#555')

# 常见氧化剂还原剂
ax3 = axes[0, 2]
ax3.axis('off')
ax3.set_xlim(0, 3)
ax3.set_ylim(0, 3)
ax3.set_title('常见氧化剂/还原剂', fontsize=10, color='#e74c3c', fontweight='bold')

ax3.text(0.1, 2.7, '常见氧化剂:', fontsize=8, color='#c0392b', fontweight='bold')
oxi = ['O₂, Cl₂, Br₂', 'KMnO₄(H⁺)', 'HNO₃, H₂SO₄(浓)', 'FeCl₃', 'H₂O₂']
for i, o in enumerate(oxi):
    ax3.text(0.1, 2.4 - i*0.25, '• ' + o, fontsize=7, color='#555')

ax3.text(0.1, 0.8, '常见还原剂:', fontsize=8, color='#2980b9', fontweight='bold')
red = ['H₂, C, CO', 'Fe²⁺, Cu', 'S²⁻, I⁻', 'Na, Al, Zn']
for i, r in enumerate(red):
    ax3.text(0.1, 0.5 - i*0.25, '• ' + r, fontsize=7, color='#555')

# 配平方法
ax4 = axes[1, 0]
ax4.axis('off')
ax4.set_xlim(0, 3)
ax4.set_ylim(0, 3)
ax4.set_title('氧化还原配平方法', fontsize=10, color='#2980b9', fontweight='bold')

steps_bal = [
    '① 标化合价: 标出变价元素',
    '② 列变化: 化合价升降数值',
    '③ 求最小公倍数: 使升降相等',
    '④ 系数配平: 先配变价元素',
    '⑤ 检查: 原子守恒+电荷守恒',
    '',
    '离子方程式配平:',
    '  还需电荷守恒 + 得失电子守恒',
    '  酸性环境可加H⁺/H₂O',
    '  碱性环境可加OH⁻/H₂O',
]
for i, s in enumerate(steps_bal):
    ax4.text(0.1, 2.7 - i*0.25, s, fontsize=7, color='#555')

# 歧化与归中
ax5 = axes[1, 1]
ax5.axis('off')
ax5.set_xlim(0, 3)
ax5.set_ylim(0, 3)
ax5.set_title('歧化反应与归中反应', fontsize=10, color='#8e44ad', fontweight='bold')

ax5.text(0.1, 2.7, '歧化反应:', fontsize=8, color='#8e44ad', fontweight='bold')
ax5.text(0.1, 2.3, '同种元素化合价 高+低', fontsize=7, color='#555')
ax5.text(0.1, 2.0, '例: Cl₂+H₂O→HCl+HClO', fontsize=7, color='#c0392b')
ax5.text(0.1, 1.7, '   Cl: 0→-1(降) + 0→+1(升)', fontsize=6, color='#888')

ax5.text(0.1, 1.3, '归中反应:', fontsize=8, color='#8e44ad', fontweight='bold')
ax5.text(0.1, 0.9, '同种元素不同价态→同一价态', fontsize=7, color='#555')
ax5.text(0.1, 0.6, '例: 2H₂S+SO₂→3S+2H₂O', fontsize=7, color='#2980b9')
ax5.text(0.1, 0.3, '   S: -2→0 + +4→0', fontsize=6, color='#888')

# 电子转移
ax6 = axes[1, 2]
ax6.axis('off')
ax6.set_xlim(0, 3)
ax6.set_ylim(0, 3)
ax6.set_title('电子转移表示方法', fontsize=10, color='#27ae60', fontweight='bold')

ax6.text(0.1, 2.7, '双线桥法:', fontsize=8, color='#27ae60', fontweight='bold')
ax6.text(0.1, 2.4, 'Zn + CuSO₄ → ZnSO₄ + Cu', fontsize=7, color='#333')
ax6.text(0.1, 2.1, '失去2e⁻(氧化)', fontsize=7, color='#e74c3c')
ax6.text(0.1, 1.8, '得到2e⁻(还原)', fontsize=7, color='#2980b9')

ax6.text(0.1, 1.3, '单线桥法:', fontsize=8, color='#27ae60', fontweight='bold')
ax6.text(0.1, 1.0, 'Zn + CuSO₄ → ZnSO₄ + Cu', fontsize=7, color='#333')
ax6.text(0.1, 0.7, '2e⁻', fontsize=8, color='#c0392b', fontweight='bold')
ax6.text(0.1, 0.4, '(从还原剂指向氧化剂)', fontsize=6, color='#888')

fig.suptitle('氧化还原反应', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'chem_eq_redox.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 17. 有机反应类型
fig, ax = plt.subplots(1, 1, figsize=(8, 5.5))
plt.subplots_adjust(left=0.05, right=0.95, top=0.92, bottom=0.06)
ax.axis('off')
ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.set_title('有机化学反应类型归纳', fontsize=14, color='#8e44ad', fontweight='bold')

rxns = [
    ('取代反应', 'CH₄+Cl₂→CH₃Cl+HCl\n(光照)\n\nC₆H₆+Br₂→C₆H₅Br+HBr\n(FeBr₃催化)', '#3498db'),
    ('加成反应', 'CH₂=CH₂+Br₂→\nCH₂BrCH₂Br\n\nCH₂=CH₂+H₂O→\nCH₃CH₂OH\n(酸催化)', '#e74c3c'),
    ('消去反应', 'CH₃CH₂OH→\nCH₂=CH₂+H₂O\n(170℃,浓H₂SO₄)\n\nCH₃CH₂Br→\nCH₂=CH₂+HBr\n(NaOH/醇)', '#27ae60'),
    ('氧化反应', 'CH₃CH₂OH→\nCH₃CHO→\nCH₃COOH\n(Cu/Ag催化)\n\n燃烧: CO₂+H₂O', '#e67e22'),
    ('还原反应', 'RCHO→RCH₂OH\n(NaBH₄/H₂催化)\n\n加成H₂也属于\n还原反应', '#8e44ad'),
    ('聚合反应', 'nCH₂=CH₂→\n[CH₂-CH₂]n\n(聚乙烯)\n\n缩聚: 尼龙/涤纶\n(有小分子生成)', '#f39c12'),
]

positions = [(0.2, 3.5), (3.0, 3.5), (5.8, 3.5), (0.2, 0.2), (3.0, 0.2), (5.8, 0.2)]

for (name, eq, color), (x, y) in zip(rxns, positions):
    ax.add_patch(plt.Rectangle((x, y), 2.5, 2.5, fill=True, facecolor=color, alpha=0.08, edgecolor=color, linewidth=1.5))
    ax.text(x+1.25, y+2.2, name, ha='center', fontsize=10, color=color, fontweight='bold')

    lines = eq.split('\n')
    for i, line in enumerate(lines):
        ax.text(x+0.2, y+1.8 - i*0.3, line, fontsize=7, color='#555')

fig.savefig(os.path.join(OUT, 'chem_eq_organic.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 18. 离子反应
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# 离子反应条件
ax1 = axes[0, 0]
ax1.axis('off')
ax1.set_xlim(0, 3)
ax1.set_ylim(0, 3)
ax1.set_title('离子反应发生条件', fontsize=10, color='#2980b9', fontweight='bold')

conditions = [
    '复分解反应:', '',
    '• 生成沉淀(↓)',
    '• 生成气体(↑)',
    '• 生成弱电解质',
    '  (水/弱酸/弱碱)',
    '',
    '氧化还原反应:',
    '• 离子间电子转移',
]
for i, c in enumerate(conditions):
    ax1.text(0.1, 2.7 - i*0.25, c, fontsize=7, color='#555')

# 离子共存
ax2 = axes[0, 1]
ax2.axis('off')
ax2.set_xlim(0, 3)
ax2.set_ylim(0, 3)
ax2.set_title('离子共存判断', fontsize=10, color='#e74c3c', fontweight='bold')

no_coexist = [
    '不能共存的组合:',
    'H⁺ + CO₃²⁻/HCO₃⁻/OH⁻',
    'OH⁻ + H⁺/NH₄⁺/Mg²⁺/Al³⁺',
    'Ag⁺ + Cl⁻/Br⁻/I⁻',
    'Ba²⁺ + SO₄²⁻/CO₃²⁻',
    'Ca²⁺ + CO₃²⁻',
    'Fe³⁺ + SCN⁻/OH⁻',
    '强氧化+强还原:',
    'MnO₄⁻+Fe²⁺/Cl⁻/I⁻',
]
for i, n in enumerate(no_coexist):
    color = '#c0392b' if i in [0, 7] else '#555'
    ax2.text(0.1, 2.7 - i*0.25, n, fontsize=7, color=color)

# 离子方程式书写
ax3 = axes[0, 2]
ax3.axis('off')
ax3.set_xlim(0, 3)
ax3.set_ylim(0, 3)
ax3.set_title('离子方程式书写', fontsize=10, color='#27ae60', fontweight='bold')

steps_ion = [
    '① 写: 写出化学方程式',
    '② 拆: 可溶强电解质拆成离子',
    '③ 删: 删去两边相同离子',
    '④ 查: 质量守恒+电荷守恒',
    '',
    '拆与不拆:',
    '拆: 强酸/强碱/可溶盐',
    '不拆: 单质/气体/沉淀/',
    '  弱电解质/氧化物',
]
for i, s in enumerate(steps_ion):
    ax3.text(0.1, 2.7 - i*0.25, s, fontsize=7, color='#555')

# 离子检验
ax4 = axes[1, 0]
ax4.axis('off')
ax4.set_xlim(0, 3)
ax4.set_ylim(0, 3)
ax4.set_title('常见离子检验', fontsize=10, color='#8e44ad', fontweight='bold')

tests = [
    'Cl⁻: AgNO₃+HNO₃ →白色↓',
    'SO₄²⁻: BaCl₂+HCl →白色↓',
    'CO₃²⁻: HCl →CO₂→石灰水变浑',
    'NH₄⁺: NaOH加热→湿润红石蕊变蓝',
    'Fe³⁺: KSCN→血红色',
    'Fe²⁺: K₃[Fe(CN)₆]→蓝色↓',
    'Na⁺: 焰色反应→黄色火焰',
    'K⁺: 焰色反应→紫色火焰',
]
for i, t in enumerate(tests):
    ax4.text(0.1, 2.7 - i*0.28, t, fontsize=7, color='#555')

# 电荷守恒
ax5 = axes[1, 1]
ax5.axis('off')
ax5.set_xlim(0, 3)
ax5.set_ylim(0, 3)
ax5.set_title('三大守恒', fontsize=10, color='#1a1a2e', fontweight='bold')

conservations = [
    '① 物料守恒:',
    '  元素原子总数不变',
    '  例: Na₂CO₃溶液',
    '  [Na⁺]=2([CO₃²⁻]+[HCO₃⁻]',
    '        +[H₂CO₃])',
    '',
    '② 电荷守恒:',
    '  阳离子电荷=阴离子电荷',
    '',
    '③ 质子守恒:',
    '  得质子总数=失质子总数',
]
for i, c in enumerate(conservations):
    ax5.text(0.1, 2.7 - i*0.25, c, fontsize=7, color='#555')

# 酸碱中和
ax6 = axes[1, 2]
ax6.axis('off')
ax6.set_xlim(0, 3)
ax6.set_ylim(0, 3)
ax6.set_title('酸碱中和的离子反应', fontsize=10, color='#e67e22', fontweight='bold')

acid_base = [
    '强酸+强碱:',
    'H⁺+OH⁻→H₂O',
    '',
    '强酸+弱碱:',
    'H⁺+NH₃·H₂O→NH₄⁺+H₂O',
    '',
    '弱酸+强碱:',
    'HAc+OH⁻→Ac⁻+H₂O',
    '',
    '多元酸+碱:',
    'H₂SO₄+2OH⁻→SO₄²⁻+2H₂O',
]
for i, ab in enumerate(acid_base):
    ax6.text(0.1, 2.7 - i*0.25, ab, fontsize=7, color='#555')

fig.suptitle('离子反应与离子方程式', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'chem_eq_ion.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()

print("All 18 chemistry SVG charts generated successfully")
