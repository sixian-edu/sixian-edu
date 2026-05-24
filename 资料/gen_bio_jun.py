"""Generate SVG charts for 初中生物 遗传专题"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False
OUT = os.path.join(os.path.dirname(__file__), 'charts')

def save(name):
    plt.savefig(os.path.join(OUT, name), bbox_inches='tight', dpi=150, facecolor='white')
    plt.close()
    print(f'  -> charts/{name}')

# ── 1. 染色体 · DNA · 基因关系 ──
def chart_dna_gene():
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.axis('off')

    # 染色体 (chromosome) – large X shape
    # Left arm
    xs = [3.5, 2.2, 1.5, 1.5, 2.2, 3.5, 3.5]
    ys = [5.5, 4.2, 2.5, 1.0, 0.3, 0.8, 3.0]
    ax.fill(xs, ys, color='#8E44AD', alpha=0.85, ec='#6C3483', lw=1.5)
    # Right arm
    xs2 = [4.5, 5.8, 6.5, 6.5, 5.8, 4.5, 4.5]
    ys2 = [5.5, 4.2, 2.5, 1.0, 0.3, 0.8, 3.0]
    ax.fill(xs2, ys2, color='#8E44AD', alpha=0.85, ec='#6C3483', lw=1.5)
    # Centromere
    circle = plt.Circle((4, 0.8), 0.5, color='#6C3483', zorder=5)
    ax.add_patch(circle)

    ax.text(4, 5.9, '染色体', ha='center', fontsize=11, weight='bold', color='#6C3483')
    ax.text(4, 0.1, '着丝粒', ha='center', fontsize=8, color='#555')

    # DNA – spiral inside left arm
    x_dna = np.linspace(2.0, 3.2, 40)
    y_dna = 0.8 + (x_dna - 2.0) * (5.5-0.8)/(3.2-2.0)
    phase = np.linspace(0, 6*np.pi, 40)
    offset = 0.2
    ax.plot(x_dna + offset * np.sin(phase), y_dna, color='#2980B9', lw=1.5, alpha=0.7)
    ax.plot(x_dna - offset * np.sin(phase), y_dna, color='#2980B9', lw=1.5, alpha=0.7)
    # DNA inside right arm
    x_dna2 = np.linspace(4.8, 6.0, 40)
    y_dna2 = 0.8 + (x_dna2 - 4.8) * (5.5-0.8)/(6.0-4.8)
    ax.plot(x_dna2 + offset * np.sin(phase), y_dna2, color='#2980B9', lw=1.5, alpha=0.7)
    ax.plot(x_dna2 - offset * np.sin(phase), y_dna2, color='#2980B9', lw=1.5, alpha=0.7)

    ax.text(0.5, 3, 'DNA', color='#2980B9', fontsize=10, weight='bold')

    # Gene – highlighted segment on left arm
    # Box highlighting a gene region
    rect = FancyBboxPatch((1.9, 2.5), 0.6, 0.2, boxstyle="round,pad=0.02",
                          facecolor='#E74C3C', alpha=0.5, ec='#C0392B', lw=1.5)
    ax.add_patch(rect)
    ax.annotate('基因', xy=(2.2, 2.5), xytext=(0.3, 2.0),
                arrowprops=dict(arrowstyle='->', color='#C0392B', lw=1.5),
                fontsize=9, color='#C0392B', weight='bold')
    ax.annotate('（DNA上有遗传效应的片段）', xy=(0.3, 1.6), fontsize=7, color='#888')

    # Labels on right
    ax.text(7.5, 4.8, '染色体 = DNA + 蛋白质', fontsize=8, color='#555',
            bbox=dict(facecolor='#F5EEF8', ec='#D2B4DE', boxstyle='round,pad=0.3'))
    ax.text(7.5, 3.8, '基因在染色体上呈线性排列', fontsize=8, color='#555',
            bbox=dict(facecolor='#EBF5FB', ec='#AED6F1', boxstyle='round,pad=0.3'))

    # Title
    ax.text(5, -0.3, '染色体 · DNA · 基因的关系', ha='center', fontsize=9, color='#888', style='italic')
    save('bio_jun_dna_gene.svg')

# ── 2. 孟德尔碗豆高茎/矮茎杂交实验 ──
def chart_mendel_jun():
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7)
    ax.axis('off')

    # P generation
    # Tall plant (left)
    ax.add_patch(FancyBboxPatch((0.5, 4), 2.5, 2.5, boxstyle="round,pad=0.15",
                                 facecolor='#D5F5E3', ec='#27AE60', lw=1.5))
    ax.text(1.75, 5.8, 'P', fontsize=12, weight='bold', va='center', ha='center')
    ax.text(1.75, 5.3, '亲代', fontsize=9, color='#555', ha='center')
    # Tall stalk with leaves
    ax.plot([1.75, 1.75], [4, 5], color='#27AE60', lw=3)
    ax.plot([1.75, 2.4], [4.5, 4.8], color='#27AE60', lw=2)
    ax.plot([1.75, 1.1], [4.3, 4.6], color='#27AE60', lw=2)
    ax.scatter([1.75], [5], s=40, color='#F39C12', zorder=5)  # flower
    ax.text(1.75, 3.8, '高茎（DD）', ha='center', fontsize=9, color='#27AE60', weight='bold')

    # × symbol
    ax.text(4.2, 5.2, '×', fontsize=20, ha='center', va='center', color='#555', weight='bold')

    # Short plant (right)
    ax.add_patch(FancyBboxPatch((5.5, 4), 2.5, 2.5, boxstyle="round,pad=0.15",
                                 facecolor='#FDEBD0', ec='#E67E22', lw=1.5))
    ax.text(6.75, 5.8, 'P', fontsize=12, weight='bold', va='center', ha='center')
    ax.text(6.75, 5.3, '亲代', fontsize=9, color='#555', ha='center')
    # Short stalk
    ax.plot([6.75, 6.75], [4.2, 4.7], color='#E67E22', lw=3)
    ax.scatter([6.75], [4.7], s=40, color='#F39C12', zorder=5)
    ax.text(6.75, 3.8, '矮茎（dd）', ha='center', fontsize=9, color='#E67E22', weight='bold')

    # Arrow down
    ax.annotate('', xy=(4.75, 3.8), xytext=(4.75, 4.0),
                arrowprops=dict(arrowstyle='->', color='#888', lw=2))
    ax.text(4.75, 3.6, '杂交', ha='center', fontsize=8, color='#888')

    # F1 generation
    ax.add_patch(FancyBboxPatch((1.5, 1.2), 4, 2, boxstyle="round,pad=0.15",
                                 facecolor='#D5F5E3', ec='#27AE60', lw=2))
    ax.text(3.5, 2.7, 'F1', fontsize=12, weight='bold', ha='center')
    ax.text(3.5, 2.3, '子一代', fontsize=9, color='#555', ha='center')
    # Tall stalk
    ax.plot([3.5, 3.5], [1.2, 2.0], color='#27AE60', lw=3)
    ax.scatter([3.5], [2.0], s=40, color='#F39C12', zorder=5)
    ax.text(3.5, 1.0, '全部高茎（Dd）', ha='center', fontsize=10, color='#27AE60', weight='bold')

    # Self arrow
    ax.annotate('', xy=(5.8, 2.2), xytext=(5.5, 2.2),
                arrowprops=dict(arrowstyle='->', color='#888', lw=1.5))
    ax.text(6.0, 2.2, '自交', fontsize=8, color='#888')

    # F2 right side
    ax.add_patch(FancyBboxPatch((7.5, 0.3), 2.2, 1.8, boxstyle="round,pad=0.1",
                                 facecolor='#FDEDEC', ec='#E74C3C', lw=1.5))
    ax.text(8.6, 1.8, 'F2', fontsize=10, weight='bold', ha='center')
    ax.text(8.6, 1.4, '高茎 : 矮茎', ha='center', fontsize=8, color='#555')
    ax.text(8.6, 1.0, '3 : 1', ha='center', fontsize=12, weight='bold', color='#E74C3C')

    ax.text(5, -0.2, '孟德尔豌豆高茎/矮茎杂交实验', ha='center', fontsize=9, color='#888', style='italic')
    save('bio_jun_mendel.svg')

# ── 3. 遗传图解标准写法 ──
def chart_cross_example():
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7)
    ax.axis('off')

    # Title
    ax.text(5, 6.6, '遗传图解规范写法', ha='center', fontsize=12, weight='bold', color='#1a1a2e')

    # Example: Dd × dd
    # Parents
    colors = ['#27AE60', '#E67E22']
    labels = ['高茎', '矮茎']
    genotypes = ['Dd', 'dd']

    for i, (x, c, l, g) in enumerate(zip([2, 7], colors, labels, genotypes)):
        ax.add_patch(FancyBboxPatch((x-1, 5.2), 2, 0.7, boxstyle="round,pad=0.08",
                                     facecolor='#F0FAF4', ec=c, lw=1.5))
        ax.text(x, 5.55, f'亲代 {l} {g}', ha='center', fontsize=9, color=c, weight='bold')

    # × symbol
    ax.text(4.5, 5.55, '×', fontsize=18, ha='center', va='center', color='#555')

    # Connecting lines from parents down to gametes
    # Parent Dd → gametes D and d
    ax.plot([2, 1.2], [5.2, 4.0], color='#27AE60', lw=1.5)
    ax.plot([2, 2.8], [5.2, 4.0], color='#27AE60', lw=1.5)
    # Parent dd → gametes d and d
    ax.plot([7, 6.2], [5.2, 4.0], color='#E67E22', lw=1.5)
    ax.plot([7, 7.8], [5.2, 4.0], color='#E67E22', lw=1.5)

    # Gametes
    gam_xs = [1.2, 2.8, 6.2, 7.8]
    gam_labels = ['D', 'd', 'd', 'd']
    for x, gl in zip(gam_xs, gam_labels):
        ax.add_patch(plt.Circle((x, 3.7), 0.25, facecolor='white', ec='#888', lw=1.5))
        ax.text(x, 3.7, gl, ha='center', va='center', fontsize=9, weight='bold', color='#333')

    # Lines from gametes down to offspring
    # D can combine with d on left
    ax.plot([1.2, 1.8], [3.45, 2.6], color='#888', lw=1)
    ax.plot([1.2, 3.2], [3.45, 2.6], color='#888', lw=1)
    # d can combine with d
    ax.plot([2.8, 1.8], [3.45, 2.6], color='#888', lw=1)
    ax.plot([2.8, 3.2], [3.45, 2.6], color='#888', lw=1)
    # Second parent d, d
    ax.plot([6.2, 3.2], [3.45, 2.6], color='#888', lw=1)
    ax.plot([6.2, 1.8], [3.45, 2.6], color='#888', lw=1)
    ax.plot([7.8, 3.2], [3.45, 2.6], color='#888', lw=1)
    ax.plot([7.8, 1.8], [3.45, 2.6], color='#888', lw=1)

    # Offspring table
    table = ax.table(cellText=[['Dd', 'Dd'], ['dd', 'dd']],
                     rowLabels=['母本 D', '母本 d'],
                     colLabels=['父本 d', '父本 d'],
                     cellLoc='center',
                     loc='center',
                     bbox=[1.0, 0.5, 3, 1.8])

    table.auto_set_font_size(False)
    table.set_fontsize(8)
    for key, cell in table.get_celld().items():
        cell.set_facecolor('white')
        cell.set_edgecolor('#999')
        cell.set_linewidth(1)
        if key[0] == 0 or key[1] == -1:
            cell.set_facecolor('#F0FAF4')
            cell.set_text_props(weight='bold', color='#27AE60')

    # Annotations below
    ax.text(2, 0.3, '子代基因型：Dd : dd = 1 : 1', ha='center', fontsize=9, color='#333', weight='bold')
    ax.text(2, -0.05, '子代表型：高茎 : 矮茎 = 1 : 1', ha='center', fontsize=9, color='#E74C3C', weight='bold')

    save('bio_jun_cross.svg')

# ── 4. 性染色体与性别遗传 ──
def chart_sex():
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7)
    ax.axis('off')

    # Male (XY)
    ax.add_patch(FancyBboxPatch((0.5, 4.5), 3.0, 2.0, boxstyle="round,pad=0.12",
                                 facecolor='#EBF5FB', ec='#2980B9', lw=1.5))
    ax.text(2, 6.1, '男 [XY]', fontsize=12, weight='bold', ha='center', color='#2980B9')
    ax.text(2, 5.5, '体细胞染色体：44+XY', fontsize=8, ha='center', color='#555')
    ax.text(2, 5.0, '精子：含 X 或含 Y', fontsize=8, ha='center', color='#333', weight='bold')

    # Female (XX)
    ax.add_patch(FancyBboxPatch((5.5, 4.5), 3.0, 2.0, boxstyle="round,pad=0.12",
                                 facecolor='#FDEDEC', ec='#E74C3C', lw=1.5))
    ax.text(7, 6.1, '女性 [XX]', fontsize=12, weight='bold', ha='center', color='#E74C3C')
    ax.text(7, 5.5, '体细胞染色体：44+XX', fontsize=8, ha='center', color='#555')
    ax.text(7, 5.0, '卵细胞：只含 X', fontsize=8, ha='center', color='#333', weight='bold')

    # Arrow
    ax.annotate('', xy=(5.3, 5.5), xytext=(4, 5.5),
                arrowprops=dict(arrowstyle='->', color='#888', lw=2))
    ax.text(4.65, 5.8, '→', fontsize=14, ha='center')

    # Fertilization
    ax.text(4.5, 4.0, '受 精', fontsize=11, weight='bold', ha='center', color='#555')

    # Lines from parents down
    ax.plot([2, 1.2], [4.1, 3.0], color='#2980B9', lw=1.5)
    ax.plot([2, 2.8], [4.1, 3.0], color='#2980B9', lw=1.5)
    ax.plot([7, 5.2], [4.1, 3.0], color='#E74C3C', lw=1.5)
    ax.plot([7, 6.8], [4.1, 3.0], color='#E74C3C', lw=1.5)

    # Gametes
    gam = [(1.2, 2.7, 'X', '#2980B9'), (2.8, 2.7, 'Y', '#2980B9'),
           (5.2, 2.7, 'X', '#E74C3C'), (6.8, 2.7, 'X', '#E74C3C')]
    for x, y, l, c in gam:
        ax.add_patch(plt.Circle((x, y), 0.2, facecolor='white', ec=c, lw=1.5))
        ax.text(x, y, l, ha='center', va='center', fontsize=9, weight='bold', color=c)

    # Connecting to offspring
    # X(1.2) + X(5.2) → XX(2,1.5)
    ax.plot([1.2, 1.2], [2.5, 1.8], color='#888', lw=1)
    ax.plot([5.2, 2.0], [2.5, 1.8], color='#888', lw=1)
    ax.plot([1.2, 3.0], [2.5, 1.8], color='#888', lw=1)
    # X(1.2) + X(6.8) → same
    ax.plot([6.8, 2.0], [2.5, 1.8], color='#888', lw=1)
    ax.plot([6.8, 3.0], [2.5, 1.8], color='#888', lw=1)
    # Y(2.8) + X(5.2) → XY(5,1.5)
    ax.plot([2.8, 4.0], [2.5, 1.8], color='#888', lw=1)
    ax.plot([2.8, 5.0], [2.5, 1.8], color='#888', lw=1)
    ax.plot([5.2, 4.0], [2.5, 1.8], color='#888', lw=1)
    ax.plot([5.2, 5.0], [2.5, 1.8], color='#888', lw=1)
    # Y(2.8) + X(6.8) → XY
    ax.plot([2.8, 6.0], [2.5, 1.8], color='#888', lw=1)
    ax.plot([6.8, 6.0], [2.5, 1.8], color='#888', lw=1)
    ax.plot([2.8, 7.0], [2.5, 1.8], color='#888', lw=1)
    ax.plot([6.8, 7.0], [2.5, 1.8], color='#888', lw=1)

    # Offspring boxes
    offspring = [(2, 1.2, 'XX', '女孩 XX', '#E74C3C'),
                 (5, 1.2, 'XY', '男孩 XY', '#2980B9'),
                 (7, 1.2, 'Y', '', '#888')]
    # Actually just two
    ax.add_patch(FancyBboxPatch((1.0, 0.3), 2, 1.2, boxstyle="round,pad=0.08",
                                 facecolor='#FDEDEC', ec='#E74C3C', lw=1.5))
    ax.text(2, 1.1, 'XX', ha='center', fontsize=9, weight='bold', color='#E74C3C')
    ax.text(2, 0.7, '女孩', ha='center', fontsize=8, color='#E74C3C')

    ax.add_patch(FancyBboxPatch((4.0, 0.3), 2, 1.2, boxstyle="round,pad=0.08",
                                 facecolor='#EBF5FB', ec='#2980B9', lw=1.5))
    ax.text(5, 1.1, 'XY', ha='center', fontsize=9, weight='bold', color='#2980B9')
    ax.text(5, 0.7, '男孩', ha='center', fontsize=8, color='#2980B9')

    ax.add_patch(FancyBboxPatch((6.5, 0.3), 1.5, 1.2, boxstyle="round,pad=0.08",
                                 facecolor='#EBF5FB', ec='#2980B9', lw=1.5))
    ax.text(7.25, 1.1, 'XY', ha='center', fontsize=9, weight='bold', color='#2980B9')
    ax.text(7.25, 0.7, '男孩', ha='center', fontsize=8, color='#2980B9')

    ax.text(4.5, 0.05, '男 : 女 = 1 : 1', ha='center', fontsize=10, weight='bold', color='#333')

    save('bio_jun_sex.svg')

# ── 5. 遗传系谱图示例 ──
def chart_pedigree_jun():
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.axis('off')

    ax.text(5, 5.7, '家族遗传系谱图', ha='center', fontsize=11, weight='bold', color='#1a1a2e')

    # Generation labels
    for i, (sym, y) in enumerate(zip(['I', 'II', 'III'], [5.2, 3.5, 1.8])):
        ax.text(0.3, y, sym, fontsize=11, weight='bold', color='#555', va='center')

    # I-1 (normal female) and I-2 (affected male)
    cx1, cx2 = 2.5, 4.5
    ax.add_patch(plt.Circle((cx1, 5.2), 0.35, facecolor='white', ec='#333', lw=2))
    ax.text(cx1, 5.2, '1', ha='center', va='center', fontsize=8, weight='bold')
    r = plt.Rectangle((cx2-0.35, 4.85), 0.7, 0.7, facecolor='#EEC4C4', ec='#E74C3C', lw=2)
    ax.add_patch(r)
    ax.text(cx2, 5.2, '2', ha='center', va='center', fontsize=8, weight='bold')
    ax.plot([cx1+0.35, cx2-0.35], [5.2, 5.2], color='#333', lw=1.5)

    # II children: II-1 (normal female), II-2 (normal male), II-3 (affected male)
    ax.plot([cx1, cx1], [5.2-0.35, 3.9], color='#333', lw=1.5)
    ax.plot([cx2, cx2], [5.2-0.35, 3.9], color='#333', lw=1.5)
    ax.plot([cx1, 6], [3.9, 3.9], color='#333', lw=1.5)

    children_spec = [
        (2.0, 3.5, 'circle', 'white', '#333', '1'),
        (4.0, 3.5, 'rect', 'white', '#333', '2'),
        (6.0, 3.5, 'rect', '#EEC4C4', '#E74C3C', '3'),
    ]
    for i, (cx, cy, shape, fc, ec, label) in enumerate(children_spec):
        ax.plot([cx, cx], [3.9, 3.85], color='#333', lw=1.5)
        if shape == 'circle':
            ax.add_patch(plt.Circle((cx, cy), 0.35, facecolor=fc, ec=ec, lw=2))
        else:
            ax.add_patch(plt.Rectangle((cx-0.35, cy-0.35), 0.7, 0.7, facecolor=fc, ec=ec, lw=2))
        ax.text(cx, cy, label, ha='center', va='center', fontsize=8, weight='bold')

    # II-1 marries a normal male → III children
    hx = 4.5  # husband
    ax.add_patch(plt.Rectangle((hx-0.35, 3.15), 0.7, 0.7, facecolor='white', ec='#333', lw=2))
    # marriage line
    ax.plot([2+0.35, hx-0.35], [3.5, 3.5], color='#333', lw=1.5)
    # children line
    ax.plot([2, 2], [3.5-0.35, 2.3], color='#333', lw=1.5)
    ax.plot([4.5, 4.5], [3.5-0.35, 2.3], color='#333', lw=1.5)
    ax.plot([2, 4.5], [2.6, 2.6], color='#333', lw=1.5)
    # III-1 normal female
    ax.plot([3, 3], [2.6, 2.45], color='#333', lw=1.5)
    ax.add_patch(plt.Circle((3, 2.1), 0.3, facecolor='white', ec='#333', lw=2))
    ax.text(3, 2.1, '1', ha='center', va='center', fontsize=7, weight='bold')
    # III-2 affected male
    ax.add_patch(plt.Rectangle((4.5-0.3, 1.8), 0.6, 0.6, facecolor='#EEC4C4', ec='#E74C3C', lw=2))
    ax.text(4.5, 2.1, '2', ha='center', va='center', fontsize=7, weight='bold')

    # Legend
    ax.text(7.5, 5.2, '[正常男性] [患病男性]', fontsize=8, color='#555')
    ax.text(7.5, 4.7, '(正常女性) (患病女性)', fontsize=8, color='#555')

    save('bio_jun_pedigree.svg')

# ── 6. 生物的变异 ──
def chart_variation_jun():
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5)
    ax.axis('off')

    ax.text(5, 4.7, '生物的变异类型', ha='center', fontsize=12, weight='bold', color='#1a1a2e')

    # Branch 1: 可遗传的变异
    ax.add_patch(FancyBboxPatch((0.5, 2.8), 4, 1.5, boxstyle="round,pad=0.1",
                                 facecolor='#D5F5E3', ec='#27AE60', lw=2))
    ax.text(2.5, 3.8, '可遗传的变异', ha='center', fontsize=10, weight='bold', color='#27AE60')
    ax.text(2.5, 3.3, '遗传物质改变，可传给后代', ha='center', fontsize=8, color='#555')

    # Sub-items
    items = ['基因突变', '基因重组', '染色体变异']
    colors = ['#E74C3C', '#2980B9', '#8E44AD']
    for i, (it, c) in enumerate(zip(items, colors)):
        x = 0.8 + i * 1.6
        ax.add_patch(FancyBboxPatch((x, 1.8), 1.2, 0.6, boxstyle="round,pad=0.05",
                                     facecolor='white', ec=c, lw=1.2))
        ax.text(x+0.6, 2.1, it, ha='center', fontsize=7, color=c, weight='bold')
        ax.plot([x+0.6, 2.5], [1.8, 2.8], color=c, lw=1, linestyle='--')

    # Branch 2: 不可遗传的变异
    ax.add_patch(FancyBboxPatch((5.5, 2.8), 4, 1.5, boxstyle="round,pad=0.1",
                                 facecolor='#FDEBD0', ec='#E67E22', lw=2))
    ax.text(7.5, 3.8, '不可遗传的变异', ha='center', fontsize=10, weight='bold', color='#E67E22')
    ax.text(7.5, 3.3, '仅由环境引起，遗传物质不变', ha='center', fontsize=8, color='#555')

    ax.add_patch(FancyBboxPatch((6.2, 1.8), 1.5, 0.6, boxstyle="round,pad=0.05",
                                 facecolor='white', ec='#E67E22', lw=1.2))
    ax.text(6.95, 2.1, '环境影响', ha='center', fontsize=7, color='#E67E22', weight='bold')
    ax.plot([6.95, 7.5], [1.8, 2.8], color='#E67E22', lw=1, linestyle='--')

    # Examples at bottom
    ax.text(5, 1.0, '应用：杂交育种、诱变育种、转基因技术', ha='center', fontsize=9, color='#333', weight='bold')

    save('bio_jun_variation.svg')

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    chart_dna_gene()
    chart_mendel_jun()
    chart_cross_example()
    chart_sex()
    chart_pedigree_jun()
    chart_variation_jun()
    print('All charts generated.')
