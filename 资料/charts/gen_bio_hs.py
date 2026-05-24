"""高中生物 遗传专题+图像题专项 专业SVG图表"""
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
# 一、遗传专题（7张）
# ════════════════════════════════════════

# 1. 孟德尔豌豆杂交实验——一对相对性状
fig, axes = plt.subplots(1, 3, figsize=(9, 3.5))
plt.subplots_adjust(left=0.04, right=0.96, wspace=0.2, bottom=0.1, top=0.88)

colors_p = ['#27ae60', '#e67e22']
colors_f1 = ['#27ae60']
colors_f2 = ['#27ae60', '#27ae60', '#27ae60', '#e67e22']

bars_data = [
    (['高茎×矮茎\n(P)', 'F₁\n(全部高茎)', 'F₂'],
     [100, 100, 75], ['#27ae60', '#27ae60', '#27ae60'],
     '高茎'),
    (['', '', ''], [0, 0, 25], ['#e67e22', '#e67e22', '#e67e22'], '矮茎')
]

x = np.arange(3)
width = 0.6
ax = axes[0]
bars1 = ax.bar(x, [100, 100, 75], width, color='#27ae60', alpha=0.85, label='高茎', edgecolor='white')
bars2 = ax.bar(x, [0, 0, 25], width, bottom=[100, 100, 75], color='#e67e22', alpha=0.85, label='矮茎', edgecolor='white')
ax.set_xticks(x)
ax.set_xticklabels(['P\n高茎×矮茎', 'F₁', 'F₂'], fontsize=9)
ax.set_ylabel('比例 / %', fontsize=9)
ax.set_ylim(0, 125)
ax.set_title('一对相对性状的杂交实验', fontsize=11, color='#1a1a2e', fontweight='bold')
ax.legend(fontsize=8, loc='upper right')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for i, (v, c) in enumerate(zip([100, 100, 75], [100, 100, 100])):
    ax.text(i, v+1, f'{int(v)}%' if v>0 else '', ha='center', fontsize=8, color='#27ae60', fontweight='bold')
ax.text(2, 105, '3:1', fontsize=11, color='#c0392b', fontweight='bold', ha='center')

# 中间：遗传图解
ax2 = axes[1]
ax2.axis('off')
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 6)
ax2.set_title('遗传图解', fontsize=11, color='#1a1a2e', fontweight='bold', pad=10)

# P
ax2.text(0.5, 5.2, 'P', fontsize=10, fontweight='bold', color='#2d3436')
ax2.text(1.2, 5.2, '高茎(DD)', fontsize=9, color='#27ae60')
ax2.text(2.8, 5.2, '×', fontsize=10, color='#888')
ax2.text(3.3, 5.2, '矮茎(dd)', fontsize=9, color='#e67e22')
# arrow
ax2.annotate('', xy=(1.5, 4.5), xytext=(2.5, 4.5), arrowprops=dict(arrowstyle='->', color='#888', lw=1))
# F1
ax2.text(0.5, 3.8, 'F₁', fontsize=10, fontweight='bold', color='#2d3436')
ax2.text(2, 3.8, '高茎(Dd)', fontsize=9, color='#27ae60', ha='center')
# self
ax2.annotate('', xy=(1.5, 3.2), xytext=(2.5, 3.2), arrowprops=dict(arrowstyle='->', color='#888', lw=1))
ax2.text(1.5, 3.4, '自交', fontsize=8, color='#888')
# F2
ax2.text(0.5, 2.5, 'F₂', fontsize=10, fontweight='bold', color='#2d3436')
ax2.text(1.3, 2.5, 'DD(高茎)', fontsize=8, color='#27ae60')
ax2.text(2.0, 2.5, 'Dd(高茎)', fontsize=8, color='#27ae60')
ax2.text(2.0, 2.0, 'Dd(高茎)', fontsize=8, color='#27ae60')
ax2.text(3.0, 2.0, 'dd(矮茎)', fontsize=8, color='#e67e22')
ax2.text(1.8, 1.3, '比例  3    :   1', fontsize=10, color='#c0392b', fontweight='bold')
# gametes
ax2.text(1.8, 4.1, '配子: D  d', fontsize=8, color='#555', ha='center')

# 右边：基因分离定律的本质
ax3 = axes[2]
ax3.axis('off')
ax3.set_xlim(0, 4)
ax3.set_ylim(0, 5)
ax3.set_title('分离定律的本质', fontsize=11, color='#1a1a2e', fontweight='bold', pad=10)

# Draw homologous chromosomes
for y_pos, label, alleles in [(4.0, '母本', 'D'), (3.3, '父本', 'd')]:
    # chromosome pair
    ax3.add_patch(plt.Circle((1.0, y_pos), 0.3, fill=True, color='#3498db', alpha=0.3))
    ax3.add_patch(plt.Circle((2.5, y_pos), 0.3, fill=True, color='#e74c3c', alpha=0.3))
    ax3.text(1.0, y_pos, alleles[0], ha='center', va='center', fontsize=12, fontweight='bold', color='#3498db')
    ax3.text(2.5, y_pos, alleles[0] if len(alleles) > 1 else 'd', ha='center', va='center', fontsize=12, fontweight='bold', color='#e74c3c')
    ax3.text(-0.2, y_pos, label, fontsize=8, color='#555')

# Meiosis arrow
ax3.annotate('减数\n分裂', xy=(1.75, 2.8), xytext=(1.75, 3.9), ha='center', fontsize=7, color='#888',
             arrowprops=dict(arrowstyle='->', color='#888'))

# Gametes
for i, (x_p, allele, color) in enumerate([(0.5, 'D', '#3498db'), (1.5, 'D', '#3498db'), (2.5, 'd', '#e74c3c'), (3.5, 'd', '#e74c3c')]):
    ax3.add_patch(plt.Circle((1 + i*0.7, 1.8), 0.25, fill=True, color=color, alpha=0.5))
    ax3.text(1 + i*0.7, 1.8, allele, ha='center', va='center', fontsize=10, fontweight='bold', color='#1a1a2e')

ax3.text(1.75, 1.2, '配子种类: D 和 d 各占 50%', fontsize=9, color='#555', ha='center')
ax3.text(1.75, 0.5, '同源染色体分离→等位基因分离', fontsize=9, color='#c0392b', ha='center', fontweight='bold')

fig.suptitle('孟德尔分离定律', fontsize=14, color='#1a1a2e', y=1.03)
fig.savefig(os.path.join(OUT, 'bio_mendel.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 2. 自由组合定律——两对相对性状 9:3:3:1
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
plt.subplots_adjust(left=0.06, right=0.98, wspace=0.25, bottom=0.08, top=0.88)

# 左边：棋盘格示意图
ax1.axis('off')
ax1.set_xlim(0, 6)
ax1.set_ylim(0, 6)
ax1.set_title('F₂ 基因型与表型 (YyRr × YyRr)', fontsize=11, color='#1a1a2e', fontweight='bold', pad=10)

# Draw Punnett square grid
cells = [
    ['YR', 'Yr', 'yR', 'yr'],
    ['YYRR\n黄圆', 'YYRr\n黄圆', 'YyRR\n黄圆', 'YyRr\n黄圆'],
    ['YYRr\n黄圆', 'YYrr\n黄皱', 'YyRr\n黄圆', 'Yyrr\n黄皱'],
    ['YyRR\n黄圆', 'YyRr\n黄圆', 'yyRR\n绿圆', 'yyRr\n绿圆'],
    ['YyRr\n黄圆', 'Yyrr\n黄皱', 'yyRr\n绿圆', 'yyrr\n绿皱'],
]

# Header row (gametes)
gametes = ['YR', 'Yr', 'yR', 'yr']
for j, g in enumerate(gametes):
    ax1.add_patch(plt.Rectangle((j+1, 4.5), 1, 0.5, fill=True, facecolor='#f0f0f0', edgecolor='#ccc'))
    ax1.text(j+1.5, 4.75, g, ha='center', va='center', fontsize=8, fontweight='bold', color='#555')

# Header column
for i, g in enumerate(gametes):
    ax1.add_patch(plt.Rectangle((0, 3.5-i), 1, 0.5, fill=True, facecolor='#f0f0f0', edgecolor='#ccc'))
    ax1.text(0.5, 4 - i, g, ha='center', va='center', fontsize=8, fontweight='bold', color='#555')

# Punnett square cells
phenotypes = [
    ['#ffd700', '#ffd700', '#ffd700', '#ffd700'],
    ['#ffd700', '#ffec8b', '#ffd700', '#ffec8b'],
    ['#ffd700', '#ffd700', '#90ee90', '#90ee90'],
    ['#ffd700', '#ffec8b', '#90ee90', '#fff5ee'],
]

counts = [9, 3, 3, 1]  # 9黄圆:3黄皱:3绿圆:1绿皱
labels_sub = ['黄圆', '黄皱', '绿圆', '绿皱']
colors_sub = ['#ffd700', '#ffec8b', '#90ee90', '#fff5ee']

for i in range(4):
    for j in range(4):
        ax1.add_patch(plt.Rectangle((j+1, 3.5-i), 1, 0.5, fill=True, facecolor=phenotypes[i][j],
                                     edgecolor='#aaa', alpha=0.8))
        ax1.text(j+1.5, 3.75-i, cells[i+1][j], ha='center', va='center', fontsize=7, color='#333')

ax1.text(0.5, -0.3, '♂ 配子', fontsize=8, color='#555', fontweight='bold')
ax1.text(2.5, 5.2, '♀ 配子', fontsize=8, color='#555', fontweight='bold')
ax1.text(3, -0.5, '表型: 9 黄圆 : 3 黄皱 : 3 绿圆 : 1 绿皱', fontsize=9, color='#c0392b', fontweight='bold', ha='center')

# 右边：柱状图显示9:3:3:1
x = np.arange(4)
bars = ax2.bar(x, counts, width=0.55, color=['#ffd700', '#ffec8b', '#90ee90', '#fff5ee'],
               edgecolor='#888', linewidth=1, alpha=0.85)
ax2.set_xticks(x)
ax2.set_xticklabels(labels_sub, fontsize=9)
ax2.set_ylabel('比例', fontsize=9)
ax2.set_title('F₂ 表型比例 9:3:3:1', fontsize=11, color='#1a1a2e', fontweight='bold')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
for i, v in enumerate(counts):
    ax2.text(i, v+0.1, str(v), ha='center', fontsize=10, fontweight='bold', color='#333')
ax2.set_ylim(0, 11)

fig.suptitle('基因自由组合定律', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'bio_dihybrid.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 3. 系谱图分析
fig, ax = plt.subplots(1, 1, figsize=(8, 4.5))
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.08)
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.set_title('人类遗传病系谱图分析', fontsize=14, color='#1a1a2e', fontweight='bold', pad=10)

# Define family tree
# Row 1: I-1 (affected male) x I-2 (normal female)
# Row 2: II-1 (normal male), II-2 (normal female x affected male II-3), II-4 (normal female), II-5 (affected male)
# Row 3: III-1 (normal female), III-2 (affected male), III-3 (normal female), III-4 (normal male)

# Legend
ax.text(0.2, 6.5, '■ 患病男性  □ 正常男性  ● 患病女性  ○ 正常女性', fontsize=9, color='#555',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#f8f9fc', edgecolor='#ddd'))

# Row 1 (y=5.5): I-1 x I-2
# Male square
ax.add_patch(plt.Rectangle((2, 5.0), 0.7, 0.7, fill=True, facecolor='#e74c3c', edgecolor='#333', linewidth=2))
ax.text(2.35, 5.35, '■', ha='center', va='center', fontsize=14, color='white')
ax.text(2.35, 5.7, 'Ⅰ-1', ha='center', fontsize=7, color='#555')

# Marriage line
ax.plot([2.7, 3.8], [5.35, 5.35], 'k-', linewidth=1.5)
# Female circle
circle1 = plt.Circle((4.15, 5.35), 0.35, fill=True, facecolor='white', edgecolor='#333', linewidth=2)
ax.add_patch(circle1)
ax.text(4.15, 5.35, '○', ha='center', va='center', fontsize=12)
ax.text(4.15, 5.7, 'Ⅰ-2', ha='center', fontsize=7, color='#555')

# Descendant line
ax.plot([2.35, 4.15], [4.3, 4.3], 'k-', linewidth=1.5)
ax.plot([3.25, 3.25], [4.3, 4.65], 'k-', linewidth=1.5)  # vertical connector

# Row 2 (y=3.5): children
# II-1 normal male
ax.add_patch(plt.Rectangle((1, 3.2), 0.7, 0.7, fill=True, facecolor='white', edgecolor='#333', linewidth=1.5))
ax.text(1.35, 3.55, '□', ha='center', va='center', fontsize=12)
ax.text(1.35, 3.9, 'Ⅱ-1', ha='center', fontsize=7, color='#555')

# II-2 normal female — carrier
circle2 = plt.Circle((2.5, 3.55), 0.35, fill=True, facecolor='white', edgecolor='#333', linewidth=1.5)
ax.add_patch(circle2)
ax.text(2.5, 3.55, '○', ha='center', va='center', fontsize=12)
ax.text(2.5, 3.9, 'Ⅱ-2', ha='center', fontsize=7, color='#555')
# Carrier dot
ax.add_patch(plt.Circle((2.5, 3.4), 0.06, fill=True, color='#333'))

# Marriage line
ax.plot([2.85, 3.8], [3.55, 3.55], 'k-', linewidth=1.5)

# II-3 affected male
ax.add_patch(plt.Rectangle((4.15, 3.2), 0.7, 0.7, fill=True, facecolor='#e74c3c', edgecolor='#333', linewidth=2))
ax.text(4.5, 3.55, '■', ha='center', va='center', fontsize=14, color='white')
ax.text(4.5, 3.9, 'Ⅱ-3', ha='center', fontsize=7, color='#555')

# II-4 normal female
circle3 = plt.Circle((5.7, 3.55), 0.35, fill=True, facecolor='white', edgecolor='#333', linewidth=1.5)
ax.add_patch(circle3)
ax.text(5.7, 3.55, '○', ha='center', va='center', fontsize=12)
ax.text(5.7, 3.9, 'Ⅱ-4', ha='center', fontsize=7, color='#555')

# II-5 affected male
ax.add_patch(plt.Rectangle((6.9, 3.2), 0.7, 0.7, fill=True, facecolor='#e74c3c', edgecolor='#333', linewidth=2))
ax.text(7.25, 3.55, '■', ha='center', va='center', fontsize=14, color='white')
ax.text(7.25, 3.9, 'Ⅱ-5', ha='center', fontsize=7, color='#555')

# Descendant line for II-2 x II-3
ax.plot([2.5, 4.5], [2.6, 2.6], 'k-', linewidth=1.5)
ax.plot([3.5, 3.5], [2.6, 2.9], 'k-', linewidth=1.5)

# Row 3 (y=1.8): III children
# III-1 normal female
circle4 = plt.Circle((1.8, 1.8), 0.35, fill=True, facecolor='white', edgecolor='#333', linewidth=1.5)
ax.add_patch(circle4)
ax.text(1.8, 1.8, '○', ha='center', va='center', fontsize=12)
ax.text(1.8, 2.15, 'Ⅲ-1', ha='center', fontsize=7, color='#555')

# III-2 affected male
ax.add_patch(plt.Rectangle((3, 1.45), 0.7, 0.7, fill=True, facecolor='#e74c3c', edgecolor='#333', linewidth=2))
ax.text(3.35, 1.8, '■', ha='center', va='center', fontsize=14, color='white')
ax.text(3.35, 2.15, 'Ⅲ-2', ha='center', fontsize=7, color='#555')

# III-3 normal female
circle5 = plt.Circle((4.3, 1.8), 0.35, fill=True, facecolor='white', edgecolor='#333', linewidth=1.5)
ax.add_patch(circle5)
ax.text(4.3, 1.8, '○', ha='center', va='center', fontsize=12)
ax.text(4.3, 2.15, 'Ⅲ-3', ha='center', fontsize=7, color='#555')

# Descendant line for II-5
ax.text(7.25, 2.6, '?', fontsize=16, color='#888', ha='center', fontweight='bold')

# Generational labels
for i, (y, label) in enumerate([(6.0, 'Ⅰ'), (4.4, 'Ⅱ'), (2.8, 'Ⅲ')]):
    ax.text(0.2, y, label, fontsize=12, fontweight='bold', color='#1a1a2e')

# Inheritance arrows
ax.annotate('常染色体显性?', xy=(4.5, 3.8), xytext=(6.5, 5.0), fontsize=8, color='#e74c3c',
            arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1))
ax.annotate('伴X隐性?', xy=(2.5, 2.0), xytext=(0.5, 1.0), fontsize=8, color='#2980b9',
            arrowprops=dict(arrowstyle='->', color='#2980b9', lw=1))

# Analysis box
analysis_text = (
    "解题关键:\n"
    "① 无中生有为隐性 Ⅱ-2×Ⅱ-3→Ⅲ-2患病 → 隐性遗传\n"
    "② 若为伴X隐性: Ⅱ-2为携带者, Ⅲ-2基因型X^aY ✓\n"
    "③ 若为常隐: Ⅱ-2×Ⅱ-3均为Aa, Ⅲ-2为aa ✓\n"
    "④ 结合Ⅱ-5患病但Ⅱ-4正常 → 优先考虑常染色体隐性"
)
ax.text(7.5, 4.5, analysis_text, fontsize=8, color='#2d3436', ha='left', va='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef9e7', edgecolor='#f0c040'))

fig.savefig(os.path.join(OUT, 'bio_pedigree.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 4. 伴性遗传——红绿色盲
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.8))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.28, bottom=0.1, top=0.88)

# Left: X-linked recessive inheritance pattern
ax1.axis('off')
ax1.set_xlim(0, 6)
ax1.set_ylim(0, 5)
ax1.set_title('红绿色盲的遗传 (伴X隐性)', fontsize=11, color='#1a1a2e', fontweight='bold', pad=10)

# Show X and Y chromosomes
# Female carrier (X^B X^b) x Normal male (X^B Y)
ax1.text(0.5, 4.3, '亲代', fontsize=9, fontweight='bold', color='#555')
ax1.text(2, 4.3, '女性携带者 × 正常男性', fontsize=9, color='#333')
ax1.text(2, 3.9, '   X^B X^b       X^B Y', fontsize=9, color='#2980b9', fontweight='bold')

ax1.annotate('', xy=(2, 3.5), xytext=(4, 3.5), arrowprops=dict(arrowstyle='->', color='#888'))

ax1.text(1.2, 3.0, '配子', fontsize=9, fontweight='bold', color='#555')
ax1.text(2.5, 3.0, 'X^B    X^b      X^B    Y', fontsize=9, color='#c0392b')

ax1.annotate('', xy=(2, 2.6), xytext=(4, 2.6), arrowprops=dict(arrowstyle='->', color='#888'))

ax1.text(0.5, 2.1, '子代', fontsize=9, fontweight='bold', color='#555')
ax1.text(2, 2.1, 'X^BX^B  X^BX^b  X^BY  X^bY', fontsize=9, color='#2d3436')
ax1.text(2, 1.7, '正常女  携带者  正常男  色盲男', fontsize=8, color='#555')
ax1.text(2, 1.3, '比例   1  :  1  :  1  :  1', fontsize=9, color='#c0392b', fontweight='bold')

# Key point
ax1.text(3, 0.3, '特点: 男性患者多于女性\n      交叉遗传(外公→外孙)\n      女性患病→父必患', fontsize=8, color='#555',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#fef5f5', edgecolor='#e74c3c'))

# Right: Bar chart showing incidence
ax2.axis('off')
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 4)

# Draw a comparison of male vs female incidence
incidence_data = [
    ('红绿色盲', 7, 0.5),  # male 7%, female 0.5%
    ('血友病', 0.01, 0.0001),
    ('进行性肌\n营养不良', 0.003, 0.00001),
]
for i, (disease, male_pct, female_pct) in enumerate(incidence_data):
    y = 3.3 - i * 1.1
    ax2.text(0.2, y, disease, fontsize=8, color='#333')
    # Male bar
    width_m = male_pct * 0.4
    if width_m > 0.1:
        ax2.barh(y, min(width_m, 2.5), height=0.25, color='#3498db', alpha=0.8)
    ax2.text(min(width_m, 2.5) + 0.1, y, f'男 {male_pct}%' if male_pct >= 1 else f'男 {male_pct}%',
             fontsize=7, va='center', color='#3498db')
    # Female bar
    width_f = female_pct * 0.4
    if width_f > 0.005:
        ax2.barh(y-0.35, min(width_f, 2.5), height=0.25, color='#e74c3c', alpha=0.8)
    ax2.text(min(width_f, 2.5) + 0.1, y-0.35, f'女 {female_pct}%', fontsize=7, va='center', color='#e74c3c')

ax2.set_title('伴X隐性遗传病发病率对比', fontsize=11, color='#1a1a2e', fontweight='bold')
ax2.text(0.5, -0.2, '■ 男性   ■ 女性', fontsize=8, color='#555')

fig.suptitle('伴性遗传', fontsize=14, color='#1a1a2e', y=1.02)
fig.savefig(os.path.join(OUT, 'bio_sex_linkage.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 5. 减数分裂染色体数目变化
fig, axes = plt.subplots(2, 3, figsize=(9, 5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.92)

# Top row: Cell division stages (simplified diagrams)
stages_data = [
    ('减数分裂Ⅰ前期\n(联会/四分体)', [0.6, 0.6, 0.8, 0.8],  # 4 chromosomes as 2 bivalents
     [(0.3, 0.5), (0.9, 0.5), (0.3, 0.5), (0.9, 0.5)],
     ['#e74c3c', '#e74c3c', '#3498db', '#3498db']),
    ('减数分裂Ⅰ后期\n(同源染色体分离)', [0.3, 0.9, 0.3, 0.9],
     [(-0.1, 0.5), (0.5, 0.5), (1.1, 0.5), (0.7, 0.5)],
     ['#e74c3c', '#e74c3c', '#3498db', '#3498db']),
    ('减数分裂Ⅱ后期\n(姐妹染色单体分离)', [0.3, 0.3, 0.9, 0.9],
     [(0.1, 0.5), (0.5, 0.5), (0.7, 0.5), (1.1, 0.5)],
     ['#e74c3c', '#e74c3c', '#3498db', '#3498db']),
]

for idx, (title, positions, offsets, colors) in enumerate(stages_data):
    ax = axes[0, idx]
    ax.set_xlim(0, 1.4)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, fontsize=8, color='#1a1a2e', fontweight='bold')

    # Draw chromosomes as X shapes or lines
    for i, (x_pos, y_pos) in enumerate(zip(positions, [0.5]*4)):
        # Chromosome pair
        if idx == 0:  # Bivalents (tetrads)
            # Draw as X shapes
            ax.plot([x_pos-0.08, x_pos, x_pos+0.08], [y_pos-0.12, y_pos, y_pos-0.12],
                    color=colors[i], linewidth=2.5)
            ax.plot([x_pos-0.08, x_pos, x_pos+0.08], [y_pos+0.12, y_pos, y_pos+0.12],
                    color=colors[i], linewidth=2.5, alpha=0.6)
        elif idx == 1:  # Anaphase I - homologous chromosomes separate
            off_x, off_y = offsets[i]
            ax.plot([off_x-0.06, off_x, off_x+0.06], [off_y-0.1, off_y, off_y-0.1],
                    color=colors[i], linewidth=2.5)
            if i < 2:
                ax.plot([off_x-0.06, off_x, off_x+0.06], [off_y+0.1, off_y, off_y+0.1],
                        color=colors[i], linewidth=2, alpha=0.6)
        else:  # Anaphase II - sister chromatids separate
            off_x, off_y = offsets[i]
            ax.plot([off_x-0.05, off_x, off_x+0.05], [off_y-0.08, off_y, off_y-0.08],
                    color=colors[i], linewidth=2)
            ax.scatter([off_x], [off_y-0.15], s=8, color='#27ae60', zorder=3)  # centromere

# Bottom row: Chromosome number change graph
ax_chart = axes[1, :]
ax3 = ax_chart[0]
ax3.axis('off')
ax4 = ax_chart[1]

# Chromosome number vs DNA content through meiosis
stages = ['间期\n(G₁)', '间期\n(S期)', '减Ⅰ\n前期', '减Ⅰ\n后期', '减Ⅰ\n末期', '减Ⅱ\n前期', '减Ⅱ\n后期', '减Ⅱ\n末期']
x = np.arange(len(stages))
chromosome_num = [4, 4, 4, 4, 2, 2, 2, 1]  # 2n=4
dna_content = [4, 8, 8, 8, 4, 4, 4, 2]

ax4.plot(x, chromosome_num, 'o-', color='#e74c3c', linewidth=2, markersize=6, label='染色体数', zorder=3)
ax4.plot(x, dna_content, 's--', color='#3498db', linewidth=2, markersize=6, label='DNA含量', zorder=3)
ax4.set_xticks(x)
ax4.set_xticklabels(stages, fontsize=7, rotation=15)
ax4.set_ylabel('数目', fontsize=9)
ax4.set_title('减数分裂过程中染色体数目和DNA含量的变化', fontsize=10, color='#1a1a2e', fontweight='bold')
ax4.legend(fontsize=8, loc='upper right')
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.set_ylim(0, 10)
ax4.grid(True, alpha=0.15)

# Fill between
ax4.fill_between(x, chromosome_num, alpha=0.1, color='#e74c3c')
ax4.fill_between(x, dna_content, alpha=0.1, color='#3498db')

# Key points
key_text = (
    "关键点:\n"
    "• 减Ⅰ: 同源染色体分离→染色体数减半\n"
    "• 减Ⅱ: 姐妹染色单体分离→DNA再减半\n"
    "• 间期S期: DNA复制→DNA含量加倍\n"
    "• 最终: 染色体数2n→n, DNA 2C→C"
)
ax3.text(0.2, 0.5, key_text, fontsize=9, color='#2d3436', va='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fc', edgecolor='#ddd'))

fig.suptitle('减数分裂过程与数量变化', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'bio_meiosis.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 6. 染色体变异类型
fig, axes = plt.subplots(2, 3, figsize=(9, 5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.1, top=0.9)

variations = [
    ('缺失', 'ABCDEFG\n→ ABEFG', ['#3498db']*7, ['#3498db']*5),
    ('重复', 'ABCDEFG\n→ ABCDCDEFG', ['#3498db']*7, ['#3498db']*9),
    ('倒位', 'ABCDEFG\n→ AEDCBFG', ['#3498db']*7, ['#3498db']*7),
    ('易位', '甲乙: ABCDEFG\n     甲乙: 1234567\n→ 甲: ABCDE123\n  乙: 4567FG', ['#3498db']*7+['#e74c3c']*7, ['#3498db']*5+['#e74c3c']*3+['#3498db']*2+['#e74c3c']*4),
]

# Simplified graphical representation
titles_var = ['缺失 (Deletion)', '重复 (Duplication)', '倒位 (Inversion)', '易位 (Translocation)']
descriptions = [
    '染色体片段丢失\n→ 基因数量减少',
    '染色体片段重复\n→ 基因数量增加',
    '同一染色体内部\n旋转180°重新连接',
    '非同源染色体间\n片段交换',
]

for idx, ax in enumerate(axes.flat[:4]):
    ax.axis('off')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_title(titles_var[idx], fontsize=10, color='#1a1a2e', fontweight='bold')

    # Normal chromosome
    if idx < 3:
        # Normal
        ax.text(0.2, 2.3, '正常:', fontsize=8, color='#555')
        for i, letter in enumerate('ABCDEFG'):
            ax.add_patch(plt.Rectangle((0.8 + i*0.2, 2.2), 0.18, 0.3, fill=True,
                                       facecolor='#3498db', alpha=0.6, edgecolor='#2980b9', linewidth=0.5))
            ax.text(0.89 + i*0.2, 2.35, letter, ha='center', va='center', fontsize=6, color='white', fontweight='bold')

        # Variant
        ax.text(0.2, 1.5, '变异:', fontsize=8, color='#c0392b')
    else:
        # Translocation - show two chromosomes
        ax.text(0.2, 2.5, '正常:', fontsize=8, color='#555')
        for i, letter in enumerate('ABCDEFG'):
            ax.add_patch(plt.Rectangle((0.8 + i*0.2, 2.4), 0.18, 0.25, fill=True,
                                       facecolor='#3498db', alpha=0.6, edgecolor='#2980b9', linewidth=0.5))
            ax.text(0.89 + i*0.2, 2.52, letter, ha='center', va='center', fontsize=5, color='white')
        for i, letter in enumerate('1234567'):
            ax.add_patch(plt.Rectangle((0.8 + i*0.2, 2.0), 0.18, 0.25, fill=True,
                                       facecolor='#e74c3c', alpha=0.6, edgecolor='#c0392b', linewidth=0.5))
            ax.text(0.89 + i*0.2, 2.12, letter, ha='center', va='center', fontsize=5, color='white')
        ax.text(0.2, 1.2, '易位:', fontsize=8, color='#c0392b')

    if idx == 0:  # Deletion
        for i, letter in enumerate('ABEFG'):
            ax.add_patch(plt.Rectangle((0.8 + i*0.25, 1.4), 0.22, 0.3, fill=True,
                                       facecolor='#e74c3c', alpha=0.6, edgecolor='#c0392b', linewidth=0.5))
            ax.text(0.91 + i*0.25, 1.55, letter, ha='center', va='center', fontsize=6, color='white', fontweight='bold')
        # Show deleted region
        ax.annotate('缺失CD', xy=(1.3, 1.4), xytext=(1.8, 0.8), fontsize=7, color='#e74c3c',
                    arrowprops=dict(arrowstyle='->', color='#e74c3c'))
    elif idx == 1:  # Duplication
        letters_dup = list('ABCDCDEFG')
        for i, letter in enumerate(letters_dup):
            ax.add_patch(plt.Rectangle((0.8 + i*0.2, 1.4), 0.18, 0.3, fill=True,
                                       facecolor='#3498db' if i < 4 else '#e74c3c', alpha=0.6,
                                       edgecolor='#2980b9', linewidth=0.5))
            ax.text(0.89 + i*0.2, 1.55, letter, ha='center', va='center', fontsize=6, color='white', fontweight='bold')
        ax.annotate('重复CD', xy=(1.7, 1.4), xytext=(2.2, 0.8), fontsize=7, color='#e74c3c',
                    arrowprops=dict(arrowstyle='->', color='#e74c3c'))
    elif idx == 2:  # Inversion
        for i, (letter, col) in enumerate(zip('AEDCBFG', ['#3498db','#e74c3c','#e74c3c','#e74c3c','#e74c3c','#3498db','#3498db'])):
            ax.add_patch(plt.Rectangle((0.8 + i*0.2, 1.4), 0.18, 0.3, fill=True,
                                       facecolor=col, alpha=0.6, edgecolor='#2980b9', linewidth=0.5))
            ax.text(0.89 + i*0.2, 1.55, letter, ha='center', va='center', fontsize=6, color='white', fontweight='bold')
        ax.annotate('BCDEF倒位', xy=(1.6, 1.4), xytext=(2.2, 0.8), fontsize=7, color='#e74c3c',
                    arrowprops=dict(arrowstyle='->', color='#e74c3c'))
    elif idx == 3:  # Translocation
        # After translocation
        ax.text(0.2, 0.8, '甲: ', fontsize=8, color='#c0392b')
        for i, (letter, col) in enumerate(zip('ABCDE123', ['#3498db']*5+['#e74c3c']*3)):
            ax.add_patch(plt.Rectangle((0.8 + i*0.25, 0.7), 0.22, 0.25, fill=True,
                                       facecolor=col, alpha=0.7, edgecolor='#333', linewidth=0.5))
            ax.text(0.91 + i*0.25, 0.82, letter, ha='center', va='center', fontsize=5, color='white')
        ax.text(0.2, 0.4, '乙: ', fontsize=8, color='#c0392b')
        for i, (letter, col) in enumerate(zip('4567FG', ['#e74c3c']*4+['#3498db']*2)):
            ax.add_patch(plt.Rectangle((0.8 + i*0.25, 0.3), 0.22, 0.25, fill=True,
                                       facecolor=col, alpha=0.7, edgecolor='#333', linewidth=0.5))
            ax.text(0.91 + i*0.25, 0.42, letter, ha='center', va='center', fontsize=5, color='white')
        ax.annotate('非同源\n交换', xy=(2.0, 0.95), xytext=(2.3, 1.6), fontsize=7, color='#e74c3c',
                    arrowprops=dict(arrowstyle='->', color='#e74c3c'))

    # Description at bottom
    ax.text(1.5, -0.1, descriptions[idx], fontsize=8, color='#555', ha='center', va='top')

# 染色体组概念
ax5 = axes.flat[4]
ax5.axis('off')
ax5.set_xlim(0, 3)
ax5.set_ylim(0, 3)
ax5.set_title('染色体组', fontsize=10, color='#1a1a2e', fontweight='bold')
ax5.text(0.2, 2.5, '人类染色体组 (22条常+X/Y):', fontsize=8, color='#555')

# Draw simplified karyotype
for i in range(8):
    x_pos = 0.3 + i * 0.3
    y_start = 2.0
    for j in range(2):
        y = y_start - j * 0.15
        ax5.plot([x_pos, x_pos], [y, y+0.2], color='#3498db', linewidth=2)
        ax5.scatter(x_pos, y+0.1, s=5, color='#27ae60', zorder=3)

ax5.text(0.2, 1.5, '染色体组数判断:', fontsize=8, color='#333', fontweight='bold')
ax5.text(0.2, 1.2, '① 同种形态染色体有几条→几组', fontsize=8, color='#555')
ax5.text(0.2, 0.9, '② 控制同一性状的基因几个→几组', fontsize=8, color='#555')
ax5.text(0.6, 0.6, '例: AAaBBb → 3个A/a → 3组', fontsize=8, color='#c0392b')
ax5.text(0.6, 0.3, '    AaBb → 1个A/1个a → 2组', fontsize=8, color='#2980b9')

# 染色体数目变异
ax6 = axes.flat[5]
ax6.axis('off')
ax6.set_xlim(0, 3)
ax6.set_ylim(0, 3)
ax6.set_title('染色体数目变异', fontsize=10, color='#1a1a2e', fontweight='bold')

ax6.text(0.2, 2.6, '• 整倍体变异:', fontsize=9, color='#333', fontweight='bold')
ax6.text(0.4, 2.3, '单倍体 (n) — 体细胞含本物种配子染色体数', fontsize=8, color='#555')
ax6.text(0.4, 2.0, '二倍体 (2n) — 体细胞含两个染色体组', fontsize=8, color='#555')
ax6.text(0.4, 1.7, '多倍体 (3n,4n...) — 体细胞含三个以上染色体组', fontsize=8, color='#555')
ax6.text(0.2, 1.3, '• 非整倍体变异:', fontsize=9, color='#333', fontweight='bold')
ax6.text(0.4, 1.0, '三体 (2n+1) — 如 21三体综合征', fontsize=8, color='#e74c3c')
ax6.text(0.4, 0.7, '单体 (2n-1) — 如 Turner综合征(XO)', fontsize=8, color='#e74c3c')
ax6.text(0.2, 0.3, '多倍体优势: 茎秆粗壮、果实大、营养丰富', fontsize=8, color='#27ae60', fontweight='bold')

fig.suptitle('染色体变异', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'bio_variation.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 7. 基因工程流程
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
plt.subplots_adjust(left=0.05, right=0.95, top=0.92, bottom=0.06)
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.set_title('基因工程基本流程', fontsize=14, color='#1a1a2e', fontweight='bold')

steps = [
    (1, '获取目的基因',
     ['从供体细胞DNA中', '用限制酶切割', '获得目标基因片段'],
     ['#e74c3c', '#27ae60', '#3498db']),
    (2, '构建表达载体',
     ['目的基因 + 载体', 'DNA连接酶连接', '形成重组DNA分子'],
     ['#e74c3c', '#27ae60', '#3498db']),
    (3, '导入受体细胞',
     ['重组载体导入', '微生物/植物/动物细胞', '转化/转染/显微注射'],
     ['#e74c3c', '#27ae60', '#3498db']),
    (4, '筛选与表达',
     ['用标记基因筛选', '检测目的基因是否表达', '获得转基因生物'],
     ['#e74c3c', '#27ae60', '#3498db']),
]

for i, (num, title, details, colors) in enumerate(steps):
    x_center = 1.5 + i * 2.3
    # Circle for step number
    circle = plt.Circle((x_center, 6.2), 0.3, fill=True, facecolor='#27ae60', edgecolor='#1d8348', linewidth=1.5)
    ax.add_patch(circle)
    ax.text(x_center, 6.2, str(num), ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    # Title
    ax.text(x_center, 5.6, title, ha='center', fontsize=10, fontweight='bold', color='#1a1a2e')

    # Box with details
    box_height = len(details) * 0.5 + 0.3
    ax.add_patch(plt.Rectangle((x_center-1.0, 3.5), 2.0, box_height, fill=True,
                                facecolor='#f8f9fc', edgecolor='#ddd'))
    for j, (detail, color) in enumerate(zip(details, colors)):
        ax.text(x_center, 4.0 + box_height - 0.4 - j*0.5, '● ' + detail, ha='center',
                fontsize=8, color=color)

    # Arrow between steps
    if i < 3:
        ax.annotate('', xy=(x_center+1.2, 4.5), xytext=(x_center+1.0, 4.5),
                    arrowprops=dict(arrowstyle='->', color='#888', lw=2))

# Bottom: Key diagram - DNA recombination
# Draw a DNA schematic
ax.text(0.5, 1.8, '基因工程核心工具:', fontsize=10, color='#1a1a2e', fontweight='bold')
tools = ['限制酶(剪刀): 识别特定序列切割DNA',
         'DNA连接酶(针线): 连接DNA片段',
         '载体(运输车): 运载目的基因进入受体细胞']
for i, tool in enumerate(tools):
    ax.text(0.5, 1.4 - i*0.35, '• ' + tool, fontsize=8, color='#555')

# Application examples
ax.text(0.5, 0.1, '应用: 转基因作物 · 基因治疗 · 基因工程疫苗 · 转基因动物(乳腺反应器)', fontsize=8, color='#7f8c8d')

# Draw a simple plasmid
ax.add_patch(plt.Circle((7.5, 2.0), 0.8, fill=False, edgecolor='#3498db', linewidth=2))
ax.text(7.5, 2.3, '质粒载体', ha='center', fontsize=7, color='#3498db', fontweight='bold')
ax.text(7.5, 1.7, 'ori', ha='center', fontsize=6, color='#e74c3c')
# Marker gene
ax.add_patch(plt.Rectangle((6.9, 1.6), 0.3, 0.15, fill=True, facecolor='#27ae60', alpha=0.5))
ax.text(6.9, 1.55, 'Ampʳ', fontsize=5, color='#27ae60')
ax.add_patch(plt.Rectangle((8.0, 2.3), 0.3, 0.15, fill=True, facecolor='#e67e22', alpha=0.5))
ax.text(8.0, 2.45, 'tetʳ', fontsize=5, color='#e67e22')

fig.savefig(os.path.join(OUT, 'bio_genetic_flow.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# ════════════════════════════════════════
# 二、图像题专项（7张）
# ════════════════════════════════════════

# 1. 细胞周期与有丝分裂
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# Top: Cell cycle pie chart
ax_cycle = axes[0, 0]
ax_cycle.axis('off')
ax_cycle.set_xlim(0, 3)
ax_cycle.set_ylim(0, 3)
ax_cycle.set_title('细胞周期', fontsize=10, color='#1a1a2e', fontweight='bold')

# Pie chart for cell cycle phases
phases = ['G₁期\n(准备)', 'S期\n(DNA复制)', 'G₂期\n(检查)', 'M期\n(分裂)']
phase_sizes = [0.25, 0.35, 0.15, 0.25]
phase_colors = ['#73BFAA', '#3498db', '#e67e22', '#e74c3c']
wedges, texts = ax_cycle.pie(phase_sizes, labels=phases, colors=phase_colors,
                              startangle=90, textprops={'fontsize': 7})
for w in wedges:
    w.set_edgecolor('white')
    w.set_linewidth(2)

# DNA content change through cell cycle
ax_dna = axes[0, 1]
stages_cycle = ['G₁', 'S', 'G₂', '前期', '中期', '后期', '末期']
dna_values = [2, 3, 4, 4, 4, 4, 2]
x_cycle = np.arange(len(stages_cycle))

ax_dna.plot(x_cycle, dna_values, 'o-', color='#3498db', linewidth=2.5, markersize=8, zorder=3)
ax_dna.fill_between(x_cycle, dna_values, alpha=0.15, color='#3498db')
ax_dna.set_xticks(x_cycle)
ax_dna.set_xticklabels(stages_cycle, fontsize=8)
ax_dna.set_ylabel('DNA 含量 (C)', fontsize=9)
ax_dna.set_title('细胞周期中DNA含量变化', fontsize=10, color='#1a1a2e', fontweight='bold')
ax_dna.spines['top'].set_visible(False)
ax_dna.spines['right'].set_visible(False)
ax_dna.set_ylim(0, 5.5)
ax_dna.grid(True, alpha=0.15)

# Mitosis phases diagram
ax_mit = axes[0, 2]
ax_mit.axis('off')
ax_mit.set_xlim(0, 3)
ax_mit.set_ylim(0, 3)
ax_mit.set_title('有丝分裂各期特征', fontsize=10, color='#1a1a2e', fontweight='bold')

mitosis_info = [
    ('前期', '核膜消失、染色质→染色体'),
    ('中期', '着丝粒在赤道板, 最易观察'),
    ('后期', '着丝粒分裂, 姐妹染色单体分开'),
    ('末期', '核膜重建, 染色体→染色质'),
]
for i, (phase, desc) in enumerate(mitosis_info):
    ax_mit.text(0.2, 2.5 - i*0.55, f'• {phase}: ', fontsize=7, color='#e74c3c', fontweight='bold')
    ax_mit.text(1.0, 2.5 - i*0.55, desc, fontsize=7, color='#555')

# Bottom row: Chromosome behavior visualization
# Simplified mitotic cell drawings
for idx, (title, chrom_data, y_pos) in enumerate([
    ('前期', [(-0.3, 1.5), (0.3, 1.5), (-0.3, 0.5), (0.3, 0.5)], 1.5),
    ('中期', [(-0.3, 0.5), (0.3, 0.5), (-0.3, 1.5), (0.3, 1.5)], 1.5),
    ('后期', [(-0.6, 1), (-0.2, 1), (0.2, 1), (0.6, 1)], 1.5),
]):
    ax = axes[1, idx]
    ax.axis('off')
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 2.5)
    ax.set_title(title, fontsize=9, color='#1a1a2e', fontweight='bold')

    # Cell boundary
    ax.add_patch(plt.Circle((0, 1.2), 0.9, fill=True, facecolor='#f0f7ff', edgecolor='#3498db', linewidth=1.5, alpha=0.5))

    if idx == 0:  # Prophase - chromosomes condensing, scattered
        for ox, oy in [(-0.3, 1.3), (0.2, 1.1), (-0.15, 0.9), (0.25, 1.5)]:
            ax.plot([ox-0.06, ox, ox+0.06], [oy-0.08, oy, oy-0.08], color='#2d3436', linewidth=2)
    elif idx == 1:  # Metaphase - aligned at equator
        ax.plot([-0.5, -0.3, -0.1], [1.1, 1.15, 1.1], color='#2d3436', linewidth=2)
        ax.plot([0.1, 0.3, 0.5], [1.1, 1.15, 1.1], color='#2d3436', linewidth=2)
        ax.plot([-0.5, -0.3, -0.1], [1.3, 1.25, 1.3], color='#2d3436', linewidth=2, alpha=0.6)
        ax.plot([0.1, 0.3, 0.5], [1.3, 1.25, 1.3], color='#2d3436', linewidth=2, alpha=0.6)
        # Spindle fibers
        ax.plot([0, 0.5], [1.2, 0.5], color='#aaa', linewidth=0.5, linestyle='--')
        ax.plot([0, -0.5], [1.2, 0.5], color='#aaa', linewidth=0.5, linestyle='--')
    else:  # Anaphase - sister chromatids separating
        for x_c in [-0.5, -0.15, 0.15, 0.5]:
            ax.plot([x_c-0.04, x_c, x_c+0.04], [1.2-0.08, 1.2, 1.2-0.08], color='#2d3436', linewidth=2)
        ax.annotate('', xy=(0, 1.3), xytext=(0, 0.6), fontsize=7, color='#aaa',
                     arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))

# Bottom right: comparison table
ax_table = axes[1, 2]
ax_table.axis('off')
ax_table.set_xlim(0, 3)
ax_table.set_ylim(0, 3)
ax_table.set_title('动植物有丝分裂区别', fontsize=9, color='#1a1a2e', fontweight='bold')

table_data = [
    ['', '植物细胞', '动物细胞'],
    ['前期', '由两极发出\n纺锤丝', '中心体发出\n星射线'],
    ['末期', '形成细胞板\n→细胞壁', '凹陷缢裂\n成两个细胞'],
]
for i, row in enumerate(table_data):
    for j, cell in enumerate(row):
        ax_table.text(0.1 + j*1.0, 2.5 - i*0.6, cell, fontsize=7, ha='center', va='center',
                      bbox=dict(boxstyle='round,pad=0.15', facecolor='#f8f9fc' if i>0 else '#e8f5e9',
                                edgecolor='#ddd', linewidth=0.5))

fig.suptitle('细胞周期与有丝分裂', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'bio_cell_cycle.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 2. 减数分裂与有丝分裂比较
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# Top row: Comparison table
ax_table = axes[0, :2]
ax_comp = ax_table[0]
ax_comp.axis('off')
ax_comp.set_xlim(0, 4)
ax_comp.set_ylim(0, 5)
ax_comp.set_title('有丝分裂 vs 减数分裂', fontsize=11, color='#1a1a2e', fontweight='bold')

comparison_rows = [
    ['比较项目', '有丝分裂', '减数分裂'],
    ['发生部位', '体细胞', '生殖器官(精巢/卵巢)'],
    ['分裂次数', '1次', '2次(Ⅰ+Ⅱ)'],
    ['子细胞数', '2个', '4个'],
    ['染色体数', '不变(2n→2n)', '减半(2n→n)'],
    ['遗传物质', '相同(克隆)', '不同(重组)'],
    ['是否联会', '否', '是(减Ⅰ前期)'],
    ['意义', '生长/修复', '生殖/变异'],
]

for i, row in enumerate(comparison_rows):
    for j, cell in enumerate(row):
        bg = '#e8f5e9' if i == 0 else ('#f8f9fc' if j == 0 else ('#fef9e7' if j == 2 else '#fafafa'))
        fc = '#c0392b' if i == 0 else '#333'
        ax_comp.text(0.1 + j*1.3, 4.7 - i*0.55, cell, fontsize=7, ha='center', va='center',
                     bbox=dict(boxstyle='round,pad=0.15', facecolor=bg, edgecolor='#ddd', linewidth=0.5),
                     color=fc, fontweight='bold' if i == 0 or j == 0 else 'normal')

# Key diagram: Chromosome behavior comparison
ax_diag = axes[0, 2]
ax_diag.axis('off')
ax_diag.set_xlim(0, 3)
ax_diag.set_ylim(0, 3)
ax_diag.set_title('关键区别', fontsize=10, color='#1a1a2e', fontweight='bold')

ax_diag.text(0.2, 2.7, '减Ⅰ: 同源染色体分离', fontsize=8, color='#e74c3c', fontweight='bold')
# Draw homologous pair separating
ax_diag.plot([0.5, 0.7, 0.9], [2.2, 2.3, 2.2], color='#3498db', linewidth=2.5)
ax_diag.plot([1.1, 1.3, 1.5], [2.2, 2.3, 2.2], color='#e74c3c', linewidth=2.5)
ax_diag.annotate('', xy=(0.7, 2.1), xytext=(1.3, 2.1), fontsize=6, color='#888',
                 arrowprops=dict(arrowstyle='<->', color='#888'))

ax_diag.text(0.2, 1.8, '减Ⅰ: 交叉互换(重组)', fontsize=8, color='#e67e22', fontweight='bold')
ax_diag.plot([0.5, 0.7, 0.9], [1.4, 1.5, 1.4], color='#3498db', linewidth=2)
ax_diag.plot([0.9, 1.0, 1.1], [1.45, 1.5, 1.45], color='#e74c3c', linewidth=1)  # crossover
ax_diag.text(1.3, 1.45, '交叉互换', fontsize=7, color='#e67e22')

ax_diag.text(0.2, 0.8, '减Ⅱ: 姐妹染色单体分离', fontsize=8, color='#2980b9', fontweight='bold')
ax_diag.plot([0.5, 0.7, 0.9], [0.4, 0.5, 0.4], color='#3498db', linewidth=2)
ax_diag.plot([1.1, 1.3, 1.5], [0.4, 0.5, 0.4], color='#3498db', linewidth=1.5, alpha=0.6)

# Bottom row: Comparative curves
ax_chart1 = axes[1, 0]
ax_chart2 = axes[1, 1]
ax_chart3 = axes[1, 2]

# Mitosis vs Meiosis - DNA content
stages_m = ['间期', '前期', '中期', '后期', '末期']
dna_mitosis = [4, 8, 8, 8, 4]
dna_meiosis = [4, 8, 8, 4, 2]
x_m = np.arange(len(stages_m))

ax_chart1.plot(x_m, dna_mitosis, 'o-', color='#3498db', linewidth=2.5, markersize=7, label='有丝分裂')
ax_chart1.plot(x_m, dna_meiosis, 's--', color='#e74c3c', linewidth=2.5, markersize=7, label='减数分裂')
ax_chart1.set_xticks(x_m)
ax_chart1.set_xticklabels(stages_m, fontsize=7)
ax_chart1.set_ylabel('DNA含量', fontsize=9)
ax_chart1.set_title('DNA含量变化比较', fontsize=10, color='#1a1a2e', fontweight='bold')
ax_chart1.legend(fontsize=8)
ax_chart1.spines['top'].set_visible(False)
ax_chart1.spines['right'].set_visible(False)
ax_chart1.set_ylim(0, 10)
ax_chart1.grid(True, alpha=0.15)

# Chromosome number comparison
chrom_mitosis = [4, 4, 4, 8, 4]
chrom_meiosis = [4, 4, 4, 4, 2]

ax_chart2.plot(x_m, chrom_mitosis, 'o-', color='#3498db', linewidth=2.5, markersize=7, label='有丝分裂')
ax_chart2.plot(x_m, chrom_meiosis, 's--', color='#e74c3c', linewidth=2.5, markersize=7, label='减数分裂')
ax_chart2.set_xticks(x_m)
ax_chart2.set_xticklabels(stages_m, fontsize=7)
ax_chart2.set_ylabel('染色体数', fontsize=9)
ax_chart2.set_title('染色体数变化比较', fontsize=10, color='#1a1a2e', fontweight='bold')
ax_chart2.legend(fontsize=8)
ax_chart2.spines['top'].set_visible(False)
ax_chart2.spines['right'].set_visible(False)
ax_chart2.set_ylim(0, 10)
ax_chart2.grid(True, alpha=0.15)

# Summary
ax_sum = ax_chart3
ax_sum.axis('off')
ax_sum.set_xlim(0, 3)
ax_sum.set_ylim(0, 3)
ax_sum.set_title('图像题解题要点', fontsize=10, color='#1a1a2e', fontweight='bold')

tips = [
    '① 有同源染色体 ↔ 减Ⅰ或有丝',
    '  无同源染色体 ↔ 减Ⅱ',
    '② 有联会/四分体 ↔ 减Ⅰ前期',
    '  同源染色体分离 ↔ 减Ⅰ后期',
    '③ 着丝粒分裂 ↔ 有丝后/减Ⅱ后',
    '④ 染色体数=奇 ↔ 减Ⅱ(无同源)',
    '⑤ 结合DNA/染色单体数综合判断',
]
for i, tip in enumerate(tips):
    color = '#c0392b' if i in [1, 3, 5] else '#555'
    ax_sum.text(0.1, 2.7 - i*0.32, tip, fontsize=7, color=color)

fig.suptitle('有丝分裂与减数分裂的图像比较', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'bio_meiosis_compare.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 3. 光合作用与细胞呼吸
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.25, hspace=0.35, bottom=0.08, top=0.9)

# Left: Light-dependent reactions (类囊体膜)
ax1 = axes[0, 0]
ax1.axis('off')
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 3)
ax1.set_title('光反应 (类囊体膜)', fontsize=10, color='#27ae60', fontweight='bold')

# Thylakoid membrane
ax1.add_patch(plt.Rectangle((0.2, 1.2), 3.6, 0.5, fill=True, facecolor='#27ae60', alpha=0.15, edgecolor='#27ae60'))
ax1.text(2, 1.45, '类囊体膜', ha='center', fontsize=8, color='#27ae60')

# Light
ax1.text(3.2, 2.8, '☀', fontsize=18, ha='center')
ax1.annotate('光能', xy=(3.2, 2.5), xytext=(3.2, 1.8), fontsize=7, color='#e67e22',
             arrowprops=dict(arrowstyle='->', color='#e67e22'))

# H2O
ax1.text(0.3, 2.5, 'H₂O', fontsize=9, color='#3498db', fontweight='bold')
ax1.annotate('', xy=(0.5, 2.2), xytext=(0.8, 1.7), fontsize=7,
             arrowprops=dict(arrowstyle='->', color='#3498db'))

# Products
ax1.text(0.5, 0.5, 'O₂', fontsize=9, color='#e74c3c', fontweight='bold')
ax1.annotate('', xy=(0.8, 1.1), xytext=(0.5, 0.8), fontsize=7,
             arrowprops=dict(arrowstyle='->', color='#e74c3c'))

# ATP/NADPH
ax1.text(2.5, 0.5, 'ATP', fontsize=9, color='#e67e22', fontweight='bold')
ax1.text(2.5, 0.2, 'NADPH', fontsize=9, color='#8e44ad', fontweight='bold')
ax1.annotate('', xy=(2.2, 1.1), xytext=(2.5, 0.7), fontsize=7,
             arrowprops=dict(arrowstyle='->', color='#e67e22'))

ax1.text(0.3, 0.0, '光解: 2H₂O → O₂ + 4[H]', fontsize=7, color='#555')

# Middle: Calvin cycle (暗反应)
ax2 = axes[0, 1]
ax2.axis('off')
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 3)
ax2.set_title('暗反应 (叶绿体基质)', fontsize=10, color='#8e44ad', fontweight='bold')

# Cycle circle
cycle = plt.Circle((2, 1.5), 0.9, fill=True, facecolor='#f3e5f5', edgecolor='#8e44ad', linewidth=2)
ax2.add_patch(cycle)
ax2.text(2, 1.9, '卡尔文循环', ha='center', fontsize=8, color='#8e44ad', fontweight='bold')
ax2.text(2, 1.5, 'CO₂固定', ha='center', fontsize=7, color='#555')
ax2.text(2, 1.2, 'C₃→C₆→C₅', ha='center', fontsize=7, color='#555')
ax2.text(2, 0.9, '还原/再生', ha='center', fontsize=7, color='#555')

# Inputs/outputs
ax2.text(0.3, 2.3, 'CO₂', fontsize=9, color='#7f8c8d', fontweight='bold')
ax2.annotate('', xy=(1.0, 2.0), xytext=(0.5, 2.3), fontsize=7,
             arrowprops=dict(arrowstyle='->', color='#7f8c8d'))

ax2.text(3.2, 2.3, 'ATP', fontsize=8, color='#e67e22')
ax2.text(3.2, 2.0, 'NADPH', fontsize=8, color='#8e44ad')
ax2.annotate('', xy=(2.9, 2.0), xytext=(3.2, 2.3), fontsize=7,
             arrowprops=dict(arrowstyle='->', color='#e67e22'))

ax2.text(3.2, 0.8, 'ADP', fontsize=8, color='#e67e22')
ax2.text(3.2, 0.5, 'NADP⁺', fontsize=8, color='#8e44ad')
ax2.annotate('', xy=(2.9, 1.0), xytext=(3.2, 0.6), fontsize=7,
             arrowprops=dict(arrowstyle='->', color='#e67e22'))

ax2.text(0.5, 0.7, '(CH₂O)', fontsize=9, color='#27ae60', fontweight='bold')
ax2.text(0.5, 0.4, '有机物', fontsize=8, color='#27ae60')

# Right: Cellular respiration
ax3 = axes[0, 2]
ax3.axis('off')
ax3.set_xlim(0, 4)
ax3.set_ylim(0, 3)
ax3.set_title('细胞呼吸', fontsize=10, color='#e74c3c', fontweight='bold')

# Stages
stages_resp = [
    ('细胞质基质', '糖酵解\n(C₆ → 2C₃)', '少量ATP\nNADH'),
    ('线粒体基质', '柠檬酸循环\n(2C₃ → CO₂)', '少量ATP\nNADH/FADH₂'),
    ('线粒体内膜', '氧化磷酸化\n(电子传递链)', '大量ATP\nH₂O'),
]

for i, (loc, process, product) in enumerate(stages_resp):
    y = 2.5 - i * 0.8
    ax3.add_patch(plt.Rectangle((0.2, y-0.2), 1.5, 0.55, fill=True, facecolor='#fce4ec',
                                 edgecolor='#e74c3c', linewidth=0.5))
    ax3.text(0.5, y+0.15, loc, fontsize=7, color='#e74c3c', fontweight='bold')
    ax3.text(1.2, y+0.15, process, fontsize=7, color='#555', ha='center')
    ax3.text(3.2, y+0.05, product, fontsize=7, color='#2980b9')
    if i < 2:
        ax3.annotate('', xy=(1.8, y-0.2), xytext=(1.8, y+0.35), fontsize=7,
                     arrowprops=dict(arrowstyle='->', color='#888', lw=1))

ax3.text(0.3, 0.0, '总反应: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + 能量', fontsize=7, color='#555')

# Bottom row: Graph of photosynthetic rate vs light intensity
ax_chart1 = axes[1, 0]
light = np.linspace(0, 10, 100)
# Light saturation curve
photosynthesis = 3 * (1 - np.exp(-0.5 * light))
respiration = -1.0 * np.ones_like(light)
net_p = photosynthesis + respiration

ax_chart1.plot(light, photosynthesis, '-', color='#27ae60', linewidth=2, label='总光合')
ax_chart1.plot(light, net_p, '-', color='#e67e22', linewidth=2, label='净光合')
ax_chart1.axhline(y=0, color='#888', linewidth=0.5, linestyle='--')
ax_chart1.axhline(y=-1, color='#e74c3c', linewidth=0.5, linestyle=':', label='呼吸速率')
ax_chart1.set_xlabel('光照强度', fontsize=9)
ax_chart1.set_ylabel('光合速率', fontsize=9)
ax_chart1.set_title('光照强度对光合速率的影响', fontsize=9, color='#1a1a2e', fontweight='bold')
ax_chart1.legend(fontsize=7)
ax_chart1.spines['top'].set_visible(False)
ax_chart1.spines['right'].set_visible(False)
ax_chart1.grid(True, alpha=0.15)
# Light compensation point
ax_chart1.axvline(x=1.4, color='#888', linewidth=0.5, linestyle='--', alpha=0.5)
ax_chart1.text(1.4, -1.5, '光补偿点', fontsize=7, color='#888', ha='center')

# CO2 concentration
ax_chart2 = axes[1, 1]
co2 = np.linspace(0, 20, 100)
p_co2 = 3 * (1 - np.exp(-0.2 * co2))

ax_chart2.plot(co2, p_co2, '-', color='#8e44ad', linewidth=2)
ax_chart2.set_xlabel('CO₂浓度', fontsize=9)
ax_chart2.set_ylabel('光合速率', fontsize=9)
ax_chart2.set_title('CO₂浓度对光合速率的影响', fontsize=9, color='#1a1a2e', fontweight='bold')
ax_chart2.spines['top'].set_visible(False)
ax_chart2.spines['right'].set_visible(False)
ax_chart2.grid(True, alpha=0.15)

# Temperature
ax_chart3 = axes[1, 2]
temp = np.linspace(0, 45, 100)
# Temperature curve - bell shaped
p_temp = 3 * np.exp(-((temp - 25) / 10) ** 2)

ax_chart3.plot(temp, p_temp, '-', color='#e74c3c', linewidth=2)
ax_chart3.axvline(x=25, color='#888', linewidth=0.5, linestyle='--', alpha=0.5)
ax_chart3.text(25, 0.1, '最适温度', fontsize=7, color='#888', ha='center')
ax_chart3.set_xlabel('温度 (℃)', fontsize=9)
ax_chart3.set_ylabel('光合速率', fontsize=9)
ax_chart3.set_title('温度对光合速率的影响', fontsize=9, color='#1a1a2e', fontweight='bold')
ax_chart3.spines['top'].set_visible(False)
ax_chart3.spines['right'].set_visible(False)
ax_chart3.grid(True, alpha=0.15)

fig.suptitle('光合作用与细胞呼吸', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'bio_photosynthesis.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 4. 种群增长曲线
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# J-shaped growth
ax_j = axes[0, 0]
t = np.linspace(0, 10, 100)
N0 = 10
r_j = 0.5
Nj = N0 * np.exp(r_j * t)

ax_j.plot(t, Nj, '-', color='#e74c3c', linewidth=2.5)
ax_j.set_xlabel('时间', fontsize=9)
ax_j.set_ylabel('种群数量', fontsize=9)
ax_j.set_title('J型增长曲线\n(指数增长)', fontsize=10, color='#e74c3c', fontweight='bold')
ax_j.spines['top'].set_visible(False)
ax_j.spines['right'].set_visible(False)
ax_j.grid(True, alpha=0.15)

# S-shaped growth
ax_s = axes[0, 1]
K = 500
Ns = K / (1 + (K/N0 - 1) * np.exp(-0.8 * t))

ax_s.plot(t, Ns, '-', color='#3498db', linewidth=2.5)
ax_s.axhline(y=K, color='#888', linewidth=1, linestyle='--', alpha=0.7)
ax_s.text(5, K+15, 'K (环境容纳量)', fontsize=8, color='#888')
ax_s.set_xlabel('时间', fontsize=9)
ax_s.set_ylabel('种群数量', fontsize=9)
ax_s.set_title('S型增长曲线\n(逻辑斯蒂增长)', fontsize=10, color='#3498db', fontweight='bold')
ax_s.spines['top'].set_visible(False)
ax_s.spines['right'].set_visible(False)
ax_s.grid(True, alpha=0.15)

# Comparison
ax_comp = axes[0, 2]
ax_comp.plot(t, Nj, '-', color='#e74c3c', linewidth=2, label='J型', alpha=0.7)
ax_comp.plot(t, Ns, '-', color='#3498db', linewidth=2, label='S型')
ax_comp.axhline(y=K, color='#888', linewidth=0.5, linestyle='--')
ax_comp.set_xlabel('时间', fontsize=9)
ax_comp.set_ylabel('种群数量', fontsize=9)
ax_comp.set_title('J型 vs S型', fontsize=10, color='#1a1a2e', fontweight='bold')
ax_comp.legend(fontsize=8)
ax_comp.spines['top'].set_visible(False)
ax_comp.spines['right'].set_visible(False)
ax_comp.grid(True, alpha=0.15)

# Bottom: Growth rate
ax_rate = axes[1, 0]
# dN/dt for S-shaped (bell curve)
growth_rate = 0.8 * Ns * (1 - Ns/K)
ax_rate.plot(t, growth_rate, '-', color='#e67e22', linewidth=2)
ax_rate.axvline(x=np.log(K/N0-1)/0.8, color='#888', linewidth=0.5, linestyle='--', alpha=0.5)
ax_rate.set_xlabel('时间', fontsize=9)
ax_rate.set_ylabel('增长率 dN/dt', fontsize=9)
ax_rate.set_title('S型增长速率变化', fontsize=10, color='#e67e22', fontweight='bold')
ax_rate.spines['top'].set_visible(False)
ax_rate.spines['right'].set_visible(False)
ax_rate.grid(True, alpha=0.15)
# Mark K/2
k_half_idx = np.argmin(np.abs(Ns - K/2))
ax_rate.scatter(t[k_half_idx], growth_rate[k_half_idx], color='#e74c3c', s=50, zorder=5)
ax_rate.annotate('K/2\n(最大增长率)', xy=(t[k_half_idx], growth_rate[k_half_idx]),
                 xytext=(t[k_half_idx]+1, growth_rate[k_half_idx]*0.7), fontsize=7, color='#e74c3c',
                 arrowprops=dict(arrowstyle='->', color='#e74c3c'))

# Population density vs time with carrying capacity
ax_density = axes[1, 1]
# Different initial densities converging to K
for r0 in [20, 50, 100]:
    ns = K / (1 + (K/r0 - 1) * np.exp(-0.6 * t))
    ax_density.plot(t, ns, '-', linewidth=1.5, alpha=0.7, label=f'N₀={r0}')
ax_density.axhline(y=K, color='#888', linewidth=1, linestyle='--')
ax_density.set_xlabel('时间', fontsize=9)
ax_density.set_ylabel('种群数量', fontsize=9)
ax_density.set_title('不同初始种群的S型增长', fontsize=10, color='#1a1a2e', fontweight='bold')
ax_density.legend(fontsize=7)
ax_density.spines['top'].set_visible(False)
ax_density.spines['right'].set_visible(False)
ax_density.grid(True, alpha=0.15)

# Key points
ax_key = axes[1, 2]
ax_key.axis('off')
ax_key.set_xlim(0, 3)
ax_key.set_ylim(0, 3)
ax_key.set_title('种群增长图像题考点', fontsize=10, color='#1a1a2e', fontweight='bold')

key_points = [
    '① J型: 理想条件, λ>1',
    '② S型: 环境有限, 趋近K值',
    '③ K/2: 最大增长速率点',
    '④ 渔业捕捞 → 略高于K/2',
    '⑤ 害虫防治 → 远低于K/2',
    '⑥ K值可变(环境变化)',
    '⑦ 区分增长率与增长速率',
]
for i, point in enumerate(key_points):
    color = '#c0392b' if i in [3, 4] else '#555'
    ax_key.text(0.1, 2.7 - i*0.32, point, fontsize=8, color=color)

fig.suptitle('种群增长曲线', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'bio_population.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 5. 生态系统能量流动
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.25, hspace=0.35, bottom=0.08, top=0.9)

# Energy pyramid
ax_pyra = axes[0, 0]
ax_pyra.axis('off')
ax_pyra.set_xlim(0, 4)
ax_pyra.set_ylim(0, 5)
ax_pyra.set_title('能量金字塔', fontsize=10, color='#1a1a2e', fontweight='bold')

trophic_levels = [
    ('第四营养级\n(顶级消费者)', 1, '#e74c3c'),
    ('第三营养级\n(次级消费者)', 2, '#e67e22'),
    ('第二营养级\n(初级消费者)', 3, '#3498db'),
    ('第一营养级\n(生产者)', 4, '#27ae60'),
]

for i, (label, width_ratio, color) in enumerate(trophic_levels):
    width = width_ratio * 0.4
    y = i * 0.9 + 0.3
    ax_pyra.add_patch(plt.Rectangle((2 - width/2, y), width, 0.7, fill=True,
                                     facecolor=color, alpha=0.7, edgecolor=color, linewidth=1.5))
    ax_pyra.text(2, y+0.35, label, ha='center', va='center', fontsize=7, color='white', fontweight='bold')

# Energy flow diagram
ax_flow = axes[0, 1]
ax_flow.axis('off')
ax_flow.set_xlim(0, 4)
ax_flow.set_ylim(0, 3.5)
ax_flow.set_title('生态系统的能量流动', fontsize=10, color='#1a1a2e', fontweight='bold')

# Producer
ax_flow.add_patch(plt.Rectangle((1.3, 2.5), 1.4, 0.5, fill=True, facecolor='#27ae60', alpha=0.6, edgecolor='#27ae60'))
ax_flow.text(2, 2.75, '生产者\n(植物)', ha='center', fontsize=8, color='#27ae60', fontweight='bold')
# Sun
ax_flow.text(0.3, 3.0, '☀', fontsize=16)
ax_flow.annotate('光能', xy=(1.2, 2.8), xytext=(0.5, 3.0), fontsize=7, color='#e67e22',
                 arrowprops=dict(arrowstyle='->', color='#e67e22'))

# Primary consumer
ax_flow.add_patch(plt.Rectangle((1.3, 1.5), 1.4, 0.5, fill=True, facecolor='#3498db', alpha=0.6, edgecolor='#3498db'))
ax_flow.text(2, 1.75, '初级消费者\n(植食动物)', ha='center', fontsize=7, color='#3498db', fontweight='bold')
ax_flow.annotate('', xy=(2, 2.4), xytext=(2, 2.1), arrowprops=dict(arrowstyle='->', color='#888', lw=1.5))

# Secondary consumer
ax_flow.add_patch(plt.Rectangle((1.3, 0.5), 1.4, 0.5, fill=True, facecolor='#e67e22', alpha=0.6, edgecolor='#e67e22'))
ax_flow.text(2, 0.75, '次级消费者\n(肉食动物)', ha='center', fontsize=7, color='#e67e22', fontweight='bold')
ax_flow.annotate('', xy=(2, 1.4), xytext=(2, 1.1), arrowprops=dict(arrowstyle='->', color='#888', lw=1.5))

# Decomposers
ax_flow.text(0.3, 1.5, '分解者\n(细菌/真菌)', fontsize=7, color='#8e44ad',
             bbox=dict(boxstyle='round', facecolor='#f3e5f5', edgecolor='#8e44ad'))

# Arrows for decomposition
for x_pos in [1.5, 2, 2.5]:
    ax_flow.annotate('', xy=(x_pos, 2.0), xytext=(x_pos, 2.5), fontsize=7,
                     arrowprops=dict(arrowstyle='->', color='#8e44ad', lw=0.5, linestyle=':'))

# Energy loss annotations
ax_flow.text(3.2, 2.4, '呼吸作用\n(热能散失)', fontsize=6, color='#e74c3c', alpha=0.7)
ax_flow.text(3.2, 1.4, '呼吸作用\n(热能散失)', fontsize=6, color='#e74c3c', alpha=0.7)

# 10% law chart
ax_law = axes[0, 2]
trophic_names = ['生产者', '初级\n消费者', '次级\n消费者', '三级\n消费者']
energy_values = [10000, 1000, 100, 10]
x_law = np.arange(len(trophic_names))

bars = ax_law.bar(x_law, energy_values, width=0.5, color=['#27ae60', '#3498db', '#e67e22', '#e74c3c'], alpha=0.8)
ax_law.set_xticks(x_law)
ax_law.set_xticklabels(trophic_names, fontsize=8)
ax_law.set_ylabel('能量 (kJ)', fontsize=9)
ax_law.set_title('能量传递的效率 (10%)', fontsize=10, color='#1a1a2e', fontweight='bold')
ax_law.spines['top'].set_visible(False)
ax_law.spines['right'].set_visible(False)
ax_law.set_yscale('log')
ax_law.grid(True, alpha=0.15)
for i, v in enumerate(energy_values):
    ax_law.text(i, v*1.2, f'{v}', ha='center', fontsize=8, fontweight='bold', color='#333')

# Nutrient cycle vs energy flow
ax_nc = axes[1, 0]
ax_nc.axis('off')
ax_nc.set_xlim(0, 3)
ax_nc.set_ylim(0, 3)
ax_nc.set_title('物质循环 vs 能量流动', fontsize=10, color='#1a1a2e', fontweight='bold')

comparison = [
    '              物质循环         能量流动',
    '形式     无机物↔有机物       单向流动',
    '范围     全球性(生物圈)     生态系统内',
    '特点     循环利用           逐级递减',
    '渠道     食物链/食物网      食物链/网',
    '联系     物质是能量载体',
    '        能量推动物质循环',
]
for i, row in enumerate(comparison):
    ax_nc.text(0.1, 2.7 - i*0.32, row, fontsize=7, color='#555')

# Ecological efficiency practice
ax_ec = axes[1, 1]
ax_ec.axis('off')
ax_ec.set_xlim(0, 3)
ax_ec.set_ylim(0, 3)
ax_ec.set_title('图像题解题思路', fontsize=10, color='#1a1a2e', fontweight='bold')

steps_eco = [
    '① 判断营养级/食物链位置',
    '② 区分同化量 vs 摄入量',
    '③ 计算传递效率(10-20%)',
    '④ 关注粪便量≠同化量',
    '⑤ 呼吸消耗 → 生长繁殖 → 分解',
]
for i, step in enumerate(steps_eco):
    ax_ec.text(0.1, 2.5 - i*0.4, step, fontsize=8, color='#555')

# Carbon cycle
ax_c = axes[1, 2]
ax_c.axis('off')
ax_c.set_xlim(0, 4)
ax_c.set_ylim(0, 3)
ax_c.set_title('碳循环', fontsize=10, color='#1a1a2e', fontweight='bold')

# Atmosphere CO2
ax_c.add_patch(plt.Rectangle((1.2, 2.2), 1.6, 0.5, fill=True, facecolor='#e0e0e0', edgecolor='#888'))
ax_c.text(2, 2.45, '大气 CO₂', ha='center', fontsize=8, color='#555', fontweight='bold')

# Photosynthesis arrow
ax_c.annotate('光合作用', xy=(1.5, 2.1), xytext=(0.5, 1.5), fontsize=6, color='#27ae60',
              arrowprops=dict(arrowstyle='->', color='#27ae60'))
# Respiration arrow
ax_c.annotate('呼吸作用', xy=(2.5, 2.1), xytext=(3.5, 1.5), fontsize=6, color='#e74c3c',
              arrowprops=dict(arrowstyle='<-', color='#e74c3c'))

# Producer
ax_c.add_patch(plt.Rectangle((0.2, 0.8), 0.8, 0.5, fill=True, facecolor='#27ae60', alpha=0.6, edgecolor='#27ae60'))
ax_c.text(0.6, 1.05, '生产者', ha='center', fontsize=7, color='#27ae60')

# Consumer
ax_c.add_patch(plt.Rectangle((1.8, 0.5), 0.8, 0.5, fill=True, facecolor='#3498db', alpha=0.6, edgecolor='#3498db'))
ax_c.text(2.2, 0.75, '消费者', ha='center', fontsize=7, color='#3498db')

# Decomposer
ax_c.add_patch(plt.Rectangle((3.0, 0.8), 0.8, 0.5, fill=True, facecolor='#8e44ad', alpha=0.6, edgecolor='#8e44ad'))
ax_c.text(3.4, 1.05, '分解者', ha='center', fontsize=7, color='#8e44ad')

# Arrows between pools
ax_c.annotate('摄食', xy=(1.1, 1.0), xytext=(1.7, 0.9), fontsize=6, color='#888',
              arrowprops=dict(arrowstyle='->', color='#888'))
ax_c.annotate('遗体\n残骸', xy=(1.7, 1.3), xytext=(3.0, 1.1), fontsize=6, color='#888',
              arrowprops=dict(arrowstyle='->', color='#888', linestyle=':'))
ax_c.annotate('燃烧', xy=(2.5, 2.2), xytext=(1.5, 3.2), fontsize=6, color='#e74c3c',
              arrowprops=dict(arrowstyle='->', color='#e74c3c'))

ax_c.text(0.1, 0.1, '化石燃料', fontsize=7, color='#7f8c8d',
          bbox=dict(boxstyle='round', facecolor='#f5f5f5', edgecolor='#ccc'))

fig.suptitle('生态系统功能——能量流动与物质循环', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'bio_ecology.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 6. 神经调节
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# Action potential graph
ax_ap = axes[0, 0]
t_ms = np.linspace(0, 12, 1000)
# Action potential waveform
v_rest = -70
v_peak = 35
v_thresh = -55
v_undershoot = -80

# Simulate action potential
voltage = np.zeros_like(t_ms)
# Phase 1: resting
mask1 = t_ms < 1
voltage[mask1] = v_rest
# Phase 2: depolarization (rapid rise)
mask2 = (t_ms >= 1) & (t_ms < 2.5)
voltage[mask2] = v_rest + (v_peak - v_rest) * (1 - np.exp(-3 * (t_ms[mask2] - 1))) / (1 - np.exp(-3*1.5))
# Phase 3: repolarization
mask3 = (t_ms >= 2.5) & (t_ms < 4.5)
voltage[mask3] = v_peak * np.exp(-0.8 * (t_ms[mask3] - 2.5)) + v_rest * (1 - np.exp(-0.8 * (t_ms[mask3] - 2.5)))
# Phase 4: undershoot
mask4 = (t_ms >= 4.5) & (t_ms < 6)
voltage[mask4] = v_rest + (v_undershoot - v_rest) * np.exp(-1.5 * (t_ms[mask4] - 4.5))
# Phase 5: return to resting
mask5 = t_ms >= 6
voltage[mask5] = v_rest + (v_undershoot - v_rest) * np.exp(-2 * (t_ms[mask5] - 4.5))

ax_ap.plot(t_ms, voltage, '-', color='#2980b9', linewidth=2.5)
ax_ap.axhline(y=v_rest, color='#888', linewidth=0.5, linestyle='--', alpha=0.7)
ax_ap.axhline(y=v_thresh, color='#e74c3c', linewidth=0.5, linestyle=':', alpha=0.7)
ax_ap.text(0.5, v_rest+2, '静息电位\n-70mV', fontsize=7, color='#888')
ax_ap.text(7, v_thresh+2, '阈电位\n-55mV', fontsize=7, color='#e74c3c', fontweight='bold')

# Label phases
ax_ap.text(1.5, 20, '去极化\n(Na⁺内流)', fontsize=7, color='#c0392b', ha='center')
ax_ap.text(3.5, 20, '复极化\n(K⁺外流)', fontsize=7, color='#2980b9', ha='center')
ax_ap.text(5.5, v_undershoot-3, '超极化\n(过度 K⁺外流)', fontsize=7, color='#8e44ad', ha='center')

ax_ap.set_xlabel('时间 (ms)', fontsize=9)
ax_ap.set_ylabel('膜电位 (mV)', fontsize=9)
ax_ap.set_title('动作电位', fontsize=10, color='#1a1a2e', fontweight='bold')
ax_ap.spines['top'].set_visible(False)
ax_ap.spines['right'].set_visible(False)
ax_ap.grid(True, alpha=0.15)

# Synapse diagram
ax_syn = axes[0, 1]
ax_syn.axis('off')
ax_syn.set_xlim(0, 4)
ax_syn.set_ylim(0, 3)
ax_syn.set_title('突触传递', fontsize=10, color='#1a1a2e', fontweight='bold')

# Presynaptic neuron
ax_syn.add_patch(plt.Circle((1, 2.2), 0.5, fill=True, facecolor='#e8f5e9', edgecolor='#27ae60', linewidth=2))
ax_syn.text(1, 2.2, '突触\n前膜', ha='center', fontsize=8, color='#27ae60', fontweight='bold')

# Synaptic cleft
ax_syn.add_patch(plt.Rectangle((0.8, 1.5), 0.4, 0.2, fill=True, facecolor='#f0f0f0', edgecolor='#ccc'))
ax_syn.text(1, 1.4, '突触间隙', ha='center', fontsize=7, color='#888')

# Postsynaptic neuron
ax_syn.add_patch(plt.Circle((1, 0.8), 0.5, fill=True, facecolor='#e3f2fd', edgecolor='#3498db', linewidth=2))
ax_syn.text(1, 0.8, '突触\n后膜', ha='center', fontsize=8, color='#3498db', fontweight='bold')

# Vesicles
for ves in [(0.8, 2.4), (1.2, 2.4), (1.0, 2.6)]:
    ax_syn.add_patch(plt.Circle(ves, 0.08, fill=True, color='#e67e22', alpha=0.8))
ax_syn.text(1.4, 2.5, '突触小泡\n(递质)', fontsize=6, color='#e67e22')

# Neurotransmitter release
ax_syn.annotate('① Ca²⁺内流\n② 递质释放', xy=(1.0, 1.6), xytext=(2.2, 2.2), fontsize=7, color='#e74c3c',
                arrowprops=dict(arrowstyle='->', color='#e74c3c'))

# Receptors
ax_syn.add_patch(plt.Rectangle((0.8, 1.0), 0.4, 0.1, fill=True, facecolor='#e74c3c', alpha=0.5))
ax_syn.text(1.4, 1.0, '受体', fontsize=7, color='#e74c3c')

# Direction of transmission
ax_syn.annotate('', xy=(1, 1.5), xytext=(1, 2.8), fontsize=7,
                arrowprops=dict(arrowstyle='->', color='#888', lw=1, linestyle='--'))

# Reflex arc
ax_ref = axes[0, 2]
ax_ref.axis('off')
ax_ref.set_xlim(0, 4)
ax_ref.set_ylim(0, 3)
ax_ref.set_title('反射弧结构', fontsize=10, color='#1a1a2e', fontweight='bold')

# Simple reflex arc diagram
reflex_parts = [
    (0.3, 2.5, '感受器', '#e74c3c'),
    (1.3, 2.5, '传入神经', '#e67e22'),
    (2.3, 2.5, '神经中枢', '#3498db'),
    (3.3, 2.5, '传出神经', '#8e44ad'),
    (2.0, 1.2, '效应器', '#27ae60'),
]

for x_pos, y_pos, label, color in reflex_parts:
    ax_ref.add_patch(plt.Rectangle((x_pos-0.3, y_pos-0.2), 0.6, 0.4, fill=True,
                                    facecolor=color, alpha=0.2, edgecolor=color))
    ax_ref.text(x_pos, y_pos, label, ha='center', fontsize=7, color=color, fontweight='bold')

# Arrows connecting parts
for i in range(3):
    ax_ref.annotate('', xy=(1.0+1.0*i, 2.5), xytext=(0.7+1.0*i, 2.5),
                    arrowprops=dict(arrowstyle='->', color='#888', lw=1.5))

# Arrow to effector
ax_ref.annotate('', xy=(2.3, 1.5), xytext=(1.3, 2.3), fontsize=7,
                arrowprops=dict(arrowstyle='->', color='#888', lw=1))

# Bottom row: Ion channels and transport
ax_ion = axes[1, 0]
ax_ion.axis('off')
ax_ion.set_xlim(0, 3)
ax_ion.set_ylim(0, 3)
ax_ion.set_title('静息与动作电位的离子基础', fontsize=10, color='#1a1a2e', fontweight='bold')

ion_info = [
    ('静息电位:', 'K⁺外流(顺浓度)', '-70mV'),
    ('去极化:', 'Na⁺内流(电压门控)', '+35mV'),
    ('复极化:', 'K⁺外流(延迟)', '恢复负值'),
    ('超极化:', 'K⁺持续外流', '-80mV'),
    ('Na⁺-K⁺泵:', '3Na⁺出/2K⁺入', '消耗ATP'),
]
for i, (phase, mechanism, voltage) in enumerate(ion_info):
    ax_ion.text(0.1, 2.7 - i*0.45, phase, fontsize=8, color='#c0392b', fontweight='bold')
    ax_ion.text(1.3, 2.7 - i*0.45, mechanism, fontsize=7, color='#555')
    ax_ion.text(2.5, 2.7 - i*0.45, voltage, fontsize=7, color='#2980b9')

# Nerve impulse conduction
ax_cond = axes[1, 1]
ax_cond.axis('off')
ax_cond.set_xlim(0, 4)
ax_cond.set_ylim(0, 3)
ax_cond.set_title('兴奋在神经纤维上的传导', fontsize=10, color='#1a1a2e', fontweight='bold')

# Draw a nerve fiber
ax_cond.add_patch(plt.Rectangle((0.2, 1.2), 3.6, 0.6, fill=True, facecolor='#f0e6ff', edgecolor='#8e44ad', linewidth=2))
ax_cond.text(2, 1.5, '轴突', ha='center', fontsize=8, color='#8e44ad')

# Myelin sheath
for mx in [0.5, 1.5, 2.5, 3.5]:
    ax_cond.add_patch(plt.Rectangle((mx-0.35, 1.1), 0.5, 0.8, fill=True, facecolor='#ffd700', alpha=0.5, edgecolor='#daa520'))

# Nodes of Ranvier
for nx in [0.9, 1.9, 2.9]:
    ax_cond.add_patch(plt.Rectangle((nx-0.05, 1.2), 0.1, 0.6, fill=True, facecolor='#e74c3c', alpha=0.3))

ax_cond.text(3.8, 0.7, '髓鞘', fontsize=7, color='#daa520')
ax_cond.text(2.9, 0.5, '朗飞结(Node)', fontsize=7, color='#e74c3c')

# Direction of conduction
ax_cond.annotate('', xy=(1.5, 0.3), xytext=(0.5, 0.3), fontsize=7,
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
ax_cond.text(1, 0.15, '兴奋传导方向', fontsize=7, color='#e74c3c')

# Summary
ax_sum = axes[1, 2]
ax_sum.axis('off')
ax_sum.set_xlim(0, 3)
ax_sum.set_ylim(0, 3)
ax_sum.set_title('神经调节图像题考点', fontsize=10, color='#1a1a2e', fontweight='bold')

nerve_tips = [
    '① 静息: K⁺外流(协助扩散)',
    '② 动作: Na⁺内流(协助扩散)',
    '③ 恢复: Na⁺-K⁺泵(主动运输)',
    '④ 传导: 局部电流(双向)',
    '⑤ 传递: 突触→递质(单向)',
    '⑥ 突触延搁 → 传导慢',
    '⑦ 兴奋=抑制(递质类型)',
]
for i, tip in enumerate(nerve_tips):
    ax_sum.text(0.1, 2.7 - i*0.32, tip, fontsize=7, color='#555')

fig.suptitle('神经调节', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'bio_nerve.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 7. 免疫调节
fig, axes = plt.subplots(2, 3, figsize=(9, 5.5))
plt.subplots_adjust(left=0.06, right=0.97, wspace=0.3, hspace=0.35, bottom=0.08, top=0.9)

# Immune response overview
ax1 = axes[0, 0]
ax1.axis('off')
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 3.5)
ax1.set_title('免疫系统组成', fontsize=10, color='#1a1a2e', fontweight='bold')

# Three lines
lines = [
    ('第一道防线', '皮肤/黏膜', '#27ae60', 2.8),
    ('第二道防线', '吞噬细胞/溶菌酶', '#3498db', 2.0),
    ('第三道防线', 'B细胞/T细胞/抗体', '#e74c3c', 1.2),
]

for label, detail, color, y_pos in lines:
    ax1.add_patch(plt.Rectangle((0.2, y_pos-0.2), 3.6, 0.4, fill=True, facecolor=color, alpha=0.15, edgecolor=color))
    ax1.text(0.5, y_pos, label, fontsize=8, color=color, fontweight='bold')
    ax1.text(2, y_pos, detail, fontsize=8, color='#555', ha='center')
    if y_pos > 1.3:
        ax1.annotate('', xy=(2, y_pos-0.2), xytext=(2, y_pos+0.3), fontsize=7,
                    arrowprops=dict(arrowstyle='->', color='#888', lw=0.5))

ax1.text(0.3, 0.3, '前两道: 非特异性免疫(天生)\n第三道: 特异性免疫(获得)', fontsize=7, color='#555')

# Humoral vs Cell-mediated
ax2 = axes[0, 1]
ax2.axis('off')
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 3.5)
ax2.set_title('特异性免疫', fontsize=10, color='#1a1a2e', fontweight='bold')

# Humoral
ax2.add_patch(plt.Rectangle((0.2, 2.5), 1.6, 0.8, fill=True, facecolor='#e3f2fd', edgecolor='#3498db'))
ax2.text(1, 3.0, '体液免疫', ha='center', fontsize=9, color='#3498db', fontweight='bold')
humoral_steps = ['抗原→B细胞活化', '→浆细胞(产生抗体)', '→记忆B细胞']
for i, s in enumerate(humoral_steps):
    ax2.text(0.3, 2.7 - i*0.25, s, fontsize=7, color='#555')

# Cell-mediated
ax2.add_patch(plt.Rectangle((2.2, 2.5), 1.6, 0.8, fill=True, facecolor='#fce4ec', edgecolor='#e74c3c'))
ax2.text(3, 3.0, '细胞免疫', ha='center', fontsize=9, color='#e74c3c', fontweight='bold')
cell_steps = ['抗原→T细胞活化', '→效应T细胞', '→记忆T细胞']
for i, s in enumerate(cell_steps):
    ax2.text(2.3, 2.7 - i*0.25, s, fontsize=7, color='#555')

# Shared components
ax2.text(1, 1.8, '抗原提呈细胞(APC)', fontsize=8, color='#8e44ad', ha='center',
         bbox=dict(boxstyle='round', facecolor='#f3e5f5', edgecolor='#8e44ad'))
ax2.annotate('', xy=(1, 2.4), xytext=(1, 2.0), fontsize=7,
             arrowprops=dict(arrowstyle='->', color='#8e44ad'))
ax2.annotate('', xy=(3, 2.4), xytext=(3, 2.0), fontsize=7,
             arrowprops=dict(arrowstyle='->', color='#8e44ad'))

# Antibody structure
ax3 = axes[0, 2]
ax3.axis('off')
ax3.set_xlim(0, 3)
ax3.set_ylim(0, 3.5)
ax3.set_title('抗体结构与功能', fontsize=10, color='#1a1a2e', fontweight='bold')

# Y-shaped antibody
ax3.plot([1.3, 1.5, 1.7], [2.3, 2.8, 2.3], 'k-', linewidth=2)  # Top Y
ax3.plot([1.3, 1.5, 1.7], [2.0, 2.5, 2.0], 'k-', linewidth=2)  # Bottom Y
ax3.plot([1.5, 1.5], [2.5, 1.5], 'k-', linewidth=2)  # Stem

# Antigen binding sites
ax3.add_patch(plt.Circle((1.1, 2.5), 0.12, fill=True, color='#e74c3c', alpha=0.5))
ax3.add_patch(plt.Circle((1.9, 2.5), 0.12, fill=True, color='#e74c3c', alpha=0.5))
ax3.text(0.9, 2.7, '抗原结合位点', fontsize=6, color='#e74c3c')

ax3.text(1, 1.2, '轻链(2条)', fontsize=7, color='#3498db')
ax3.text(1, 0.9, '重链(2条)', fontsize=7, color='#e67e22')

ax3.text(0.3, 0.3, '功能: 中和/凝集/标记抗原', fontsize=7, color='#555')
ax3.text(0.3, 0.1, '通过Fc段与免疫细胞结合', fontsize=7, color='#555')

# Immune response over time
ax4 = axes[1, 0]
days = np.arange(0, 30, 0.5)
# Primary response
primary = 0.5 * (1 - np.exp(-0.3 * days)) * np.exp(-0.05 * days)
primary[days < 3] = 0
# Secondary response
secondary = 5 * (1 - np.exp(-0.8 * (days - 14))) * np.exp(-0.03 * (days - 14))
secondary[days < 14] = 0

ax4.plot(days, primary, '-', color='#3498db', linewidth=2, label='初次免疫')
ax4.plot(days, secondary, '-', color='#e74c3c', linewidth=2, label='二次免疫')
ax4.axvline(x=3, color='#888', linewidth=0.5, linestyle='--', alpha=0.5)
ax4.text(3, 3, '潜伏期', fontsize=7, color='#888')
ax4.set_xlabel('时间 (天)', fontsize=9)
ax4.set_ylabel('抗体浓度', fontsize=9)
ax4.set_title('初次与二次免疫应答', fontsize=10, color='#1a1a2e', fontweight='bold')
ax4.legend(fontsize=8)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.grid(True, alpha=0.15)

# Vaccine principle
ax5 = axes[1, 1]
ax5.axis('off')
ax5.set_xlim(0, 3)
ax5.set_ylim(0, 3)
ax5.set_title('疫苗原理 (主动免疫)', fontsize=10, color='#1a1a2e', fontweight='bold')

vaccine_steps = [
    '① 接种: 灭活/减毒病原体',
    '② 抗原提呈 → B/T细胞活化',
    '③ 产生记忆细胞(潜伏)',
    '④ 再次感染 → 快速应答',
    '⑤ 特点: 持续时间长',
]
for i, step in enumerate(vaccine_steps):
    ax5.text(0.1, 2.7 - i*0.4, step, fontsize=8, color='#555')

# Autoimmune and allergies
ax6 = axes[1, 2]
ax6.axis('off')
ax6.set_xlim(0, 3)
ax6.set_ylim(0, 3)
ax6.set_title('免疫异常', fontsize=10, color='#1a1a2e', fontweight='bold')

immune_issues = [
    ('过敏反应', '已免疫→再次刺激→过度反应', '#c0392b'),
    ('自身免疫', '攻击自身组织(类风湿)', '#e67e22'),
    ('免疫缺陷', 'HIV/AIDS(攻击T细胞)', '#8e44ad'),
]
for i, (name, desc, color) in enumerate(immune_issues):
    ax6.add_patch(plt.Rectangle((0.1, 2.5 - i*0.7), 2.8, 0.5, fill=True,
                                 facecolor=color, alpha=0.1, edgecolor=color))
    ax6.text(0.2, 2.65 - i*0.7, name, fontsize=8, color=color, fontweight='bold')
    ax6.text(1.2, 2.65 - i*0.7, desc, fontsize=7, color='#555')

fig.suptitle('免疫调节', fontsize=14, color='#1a1a2e', y=1.01)
fig.savefig(os.path.join(OUT, 'bio_immunity.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()


# 额外: 体液免疫与细胞免疫对比
fig, ax = plt.subplots(1, 1, figsize=(8, 4))
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.08)
ax.axis('off')
ax.set_xlim(0, 8)
ax.set_ylim(0, 5)
ax.set_title('体液免疫 vs 细胞免疫对比', fontsize=14, color='#1a1a2e', fontweight='bold')

# Create a table-style comparison
headers = ['比较项目', '体液免疫', '细胞免疫']
rows_data = [
    ['作用对象', '细胞外病原体/毒素', '胞内病原体/癌细胞'],
    ['主要细胞', 'B细胞 → 浆细胞', 'T细胞 → 效应T细胞'],
    ['效应分子', '抗体(免疫球蛋白)', '细胞因子(穿孔素等)'],
    ['作用方式', '抗体中和抗原', '效应T细胞裂解靶细胞'],
    ['与抗原接触', '直接接触', '需APC提呈'],
    ['记忆细胞', '记忆B细胞', '记忆T细胞'],
    ['相互关系', '相互配合, 共同清除病原体'],
]

# Draw table
for i, row in enumerate([headers] + rows_data):
    for j, cell in enumerate(row):
        if i == len(rows_data):  # Last row (merged)
            bg = '#fef5f5'
            ax.text(0.3 + j*2.5, 4.3 - i*0.45, cell, fontsize=9, color='#c0392b', fontweight='bold')
        else:
            bg = '#e8f5e9' if i == 0 else ('#f8f9fc' if j == 0 else ('#e3f2fd' if j == 1 else '#fce4ec'))
            ax.add_patch(plt.Rectangle((0.1 + j*2.5, 4.3 - i*0.45), 2.3, 0.4, fill=True,
                                        facecolor=bg, edgecolor='#ddd'))
            ax.text(0.3 + j*2.5, 4.4 - i*0.45, cell, fontsize=7.5, color='#333', va='center',
                    fontweight='bold' if i == 0 or j == 0 else 'normal')

fig.savefig(os.path.join(OUT, 'bio_immunity2.svg'), dpi=120, facecolor='white', bbox_inches='tight')
plt.close()

print("All 14 biology SVG charts generated successfully")
