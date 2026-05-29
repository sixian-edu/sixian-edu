import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei','SimHei','Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False
out = r'C:\Users\21342\Desktop\sixian-edu\资料\charts'

PHY_RED = '#c0392b'
GRAY = '#7f8c8d'
GRAY_LIGHT = '#ecf0f1'
DARK = '#2c3e50'

# ─── Chart 1: 解题思维流程图 ───
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10); ax.set_ylim(0, 3.5)
ax.axis('off')

boxes = [
    (0.3, 1.8, 1.3, 1.0, '1 审题\n圈关键量', PHY_RED),
    (2.1, 1.8, 1.3, 1.0, '2 识别\n物理模型', '#2980b9'),
    (3.9, 1.8, 1.3, 1.0, '3 选择\n对应公式', '#27ae60'),
    (5.7, 1.8, 1.3, 1.0, '4 代入\n计算求解', '#e67e22'),
    (7.5, 1.8, 1.3, 1.0, '5 检查\n单位和结果', '#8e44ad'),
]
for (x, y, w, h, txt, color) in boxes:
    rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                                     facecolor=color, edgecolor='white', linewidth=2.5, alpha=0.85)
    ax.add_patch(rect)
    ax.text(x+w/2, y+h/2, txt, ha='center', va='center', fontsize=13, color='white',
            fontweight='bold', linespacing=1.5)

for i in range(len(boxes)-1):
    x1 = boxes[i][0] + boxes[i][2]
    y1 = boxes[i][1] + boxes[i][3]/2
    x2 = boxes[i+1][0]
    y2 = boxes[i+1][1] + boxes[i+1][3]/2
    ax.annotate('', xy=(x2-0.05, y2), xytext=(x1+0.05, y1),
                arrowprops=dict(arrowstyle='->', color=GRAY, lw=2.5, shrinkA=5, shrinkB=5))

ax.text(5, 0.5, '每做一题跑一遍流程，养成解题肌肉记忆', ha='center', fontsize=13, color=DARK,
        bbox=dict(boxstyle='round,pad=0.4', facecolor=GRAY_LIGHT, edgecolor='none'))
ax.text(5, 3.3, '中考物理解题思维流程图', ha='center', fontsize=15, fontweight='bold', color=DARK)
plt.tight_layout()
plt.savefig(os.path.join(out, 'phy_score_flow.svg'), bbox_inches='tight', dpi=180)
plt.close()
print('1/6 flow done')

# ─── Chart 2: 常见物理模型分类 ───
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.axis('off')

categories = [
    ('力学模型', ['受力平衡', '压强浮力', '功和功率', '简单机械', '密度测量'], '#c0392b'),
    ('电学模型', ['欧姆定律', '电功率计算', '电路故障', '电磁感应', '家庭电路'], '#2980b9'),
    ('热学模型', ['物态变化', '内能和比热容', '热值计算', '分子动理论'], '#e67e22'),
    ('光学模型', ['反射定律', '平面镜成像', '折射规律', '凸透镜成像'], '#8e44ad'),
]
pale_map = {'#c0392b':'#fadbd8', '#2980b9':'#d4e6f1', '#e67e22':'#fdebd0', '#8e44ad':'#e8daef'}

y_start = 3.8
for ci, (title, items, color) in enumerate(categories):
    y = y_start - ci * 0.9
    ax.text(0.3, y, title, fontsize=14, fontweight='bold', color=color, va='center')
    for j, item in enumerate(items):
        ax.text(2.2 + j * 1.4, y, item, fontsize=12, ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.25', facecolor=pale_map[color],
                          edgecolor=color, linewidth=1.5))

ax.text(4.2, 4.3, '中考物理常见模型分类速查', ha='center', fontsize=16, fontweight='bold', color=DARK)
ax.text(0.3, -0.2, '识别模型 = 知道考什么 = 选对公式', fontsize=13, color=DARK,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=GRAY_LIGHT, edgecolor='none'))
plt.savefig(os.path.join(out, 'phy_score_model.svg'), bbox_inches='tight', dpi=180)
plt.close()
print('2/6 model done')

# ─── Chart 3: 公式选择策略 ───
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.axis('off')

# Redesigned as a clean 2-column comparison: 所求量 → 公式
sections = [
    ('力学', [
        ('重力', 'G = mg'),
        ('密度', 'ρ = m / V'),
        ('压强', 'p = F / S'),
        ('液体压强', 'p = ρ g h'),
        ('浮力', 'F浮 = ρ g V排'),
    ]),
    ('电学', [
        ('欧姆定律', 'I = U / R'),
        ('电功率', 'P = U I'),
        ('电功', 'W = U I t'),
        ('焦耳定律', 'Q = I² R t'),
        ('电阻串联', 'R = R1 + R2'),
    ]),
    ('热学', [
        ('吸放热', 'Q = c m Δt'),
        ('热值', 'Q = m q'),
    ]),
    ('光学', [
        ('像距公式', '1/f = 1/u + 1/v'),
        ('折射率', 'n = sin i / sin r'),
    ]),
]

y_base = 3.8
for si, (sec_name, formulas) in enumerate(sections):
    x = 0.3 + si * 2.0
    ax.text(x + 0.8, y_base + 0.15, sec_name, fontsize=13, fontweight='bold', color=PHY_RED, ha='center')
    for fi, (name, formula) in enumerate(formulas):
        y = y_base - 0.4 - fi * 0.45
        # formula box
        ax.text(x + 0.8, y, name, fontsize=10, va='center', ha='center', color=DARK)
        ax.text(x + 0.8, y - 0.28, formula, fontsize=11, va='center', ha='center', color=PHY_RED,
                fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#fdf2f2', edgecolor=PHY_RED, linewidth=1))

ax.text(4.2, 4.35, '公式定位速查表', ha='center', fontsize=16, fontweight='bold', color=DARK)
ax.text(4.2, 4.05, '根据所求量直接查找对应公式', ha='center', fontsize=12, color=GRAY)
plt.savefig(os.path.join(out, 'phy_score_formula.svg'), bbox_inches='tight', dpi=180)
plt.close()
print('3/6 formula done')

# ─── Chart 4: 选择题技巧 ───
fig, ax = plt.subplots(figsize=(7, 4))
ax.axis('off')

tips = [
    ('排除法', '排除明显\n错误选项', '#c0392b', 90),
    ('量纲法', '检查单位\n是否匹配', '#2980b9', 75),
    ('极限法', '取极端值\n快速判断', '#27ae60', 65),
    ('特殊值法', '代入简单数\n验证选项', '#e67e22', 55),
    ('图像法', '画示意图\n找规律', '#8e44ad', 50),
]

for i, (name, desc, color, hits) in enumerate(tips):
    x = 0.3 + i * 1.35
    ax.bar(x, hits, width=0.7, color=color, alpha=0.8, edgecolor='white', linewidth=1.5)
    ax.text(x, hits + 3, f'{hits}%', ha='center', fontsize=13, fontweight='bold', color=color)
    ax.text(x, -6, name, ha='center', fontsize=14, fontweight='bold', color=DARK)
    ax.text(x, -18, desc, ha='center', fontsize=10, color=GRAY, linespacing=1.3)

ax.set_ylim(-28, 110)
ax.text(3.5, 108, '选择题实用技巧及命中率', ha='center', fontsize=16, fontweight='bold', color=DARK)
ax.text(3.5, 97, '综合使用多种技巧命中率更高', ha='center', fontsize=11, color=GRAY)
plt.savefig(os.path.join(out, 'phy_score_mc.svg'), bbox_inches='tight', dpi=180)
plt.close()
print('4/6 mc done')

# ─── Chart 5: 计算题步骤分 ───
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.axis('off')

steps = [
    ('写公式', '列出原始公式\n得 2 分', PHY_RED),
    ('代数据', '代入数值和单位\n得 2 分', '#e74c3c'),
    ('算结果', '正确算出\n得 1 分', '#2980b9'),
    ('写单位', '结果加单位\n得 0.5 分', '#27ae60'),
    ('作答', '写答:...\n得 0.5 分', '#8e44ad'),
]

for i, (step, detail, color) in enumerate(steps):
    x = 0.3 + i * 1.5
    rect = mpatches.FancyBboxPatch((x, 1.2), 1.2, 1.0, boxstyle="round,pad=0.15",
                                     facecolor=color, edgecolor='white', linewidth=2, alpha=0.8)
    ax.add_patch(rect)
    ax.text(x+0.6, 1.7, step, ha='center', va='center', fontsize=14, color='white', fontweight='bold')
    ax.text(x+0.6, 1.2, detail, ha='center', va='top', fontsize=10, color='white', alpha=0.9, linespacing=1.3)
    if i < len(steps) - 1:
        ax.annotate('', xy=(x+1.35, 1.7), xytext=(x+1.2, 1.7),
                    arrowprops=dict(arrowstyle='->', color=GRAY, lw=2.5))

ax.text(0.3, 2.8, '即使算不出最终结果', fontsize=11, color=DARK, fontweight='bold')
ax.text(4.0, 2.8, '写对公式 + 代入数据', fontsize=11, color=PHY_RED, fontweight='bold')
ax.text(7.2, 2.8, '也能拿 4/6 分', fontsize=11, color='#27ae60', fontweight='bold')
ax.text(4.2, 3.3, '计算题步骤分策略', ha='center', fontsize=16, fontweight='bold', color=DARK)

plt.savefig(os.path.join(out, 'phy_score_calc.svg'), bbox_inches='tight', dpi=180)
plt.close()
print('5/6 calc done')

# ─── Chart 6: 实验题题型分布 ───
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.axis('off')

exp_types = [
    ('实验原理题', '考实验的物理依据', 25, PHY_RED),
    ('步骤设计题', '考操作顺序规范', 20, '#2980b9'),
    ('数据分析题', '考读图描点找规律', 25, '#27ae60'),
    ('误差分析题', '考误差原因和改进', 15, '#e67e22'),
    ('结论表述题', '考实验结论总结', 15, '#8e44ad'),
]

ax.set_xlim(0, 35); ax.set_ylim(-0.5, 5.5)
for i, (name, desc, pct, color) in enumerate(exp_types):
    ax.barh(i, pct, height=0.55, color=color, alpha=0.8, edgecolor='white', linewidth=1.5)
    ax.text(pct + 0.5, i, f'{pct}%', va='center', fontsize=13, fontweight='bold', color=color)
    ax.text(-0.3, i + 0.3, name, ha='left', va='bottom', fontsize=12, fontweight='bold', color=DARK)
    ax.text(10, i - 0.15, desc, ha='left', va='top', fontsize=10, color=GRAY)

ax.set_yticks(range(5))
ax.set_yticklabels([])
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(left=False)

ax.text(17.5, 5.7, '实验探究题题型分布', ha='center', fontsize=16, fontweight='bold', color=DARK)
ax.text(17.5, 5.2, '原理题和数据分析题占比最高，复习重点', ha='center', fontsize=11, color=GRAY)
plt.savefig(os.path.join(out, 'phy_score_exp.svg'), bbox_inches='tight', dpi=180)
plt.close()
print('6/6 exp done')

print('\nAll 6 charts regenerated!')
