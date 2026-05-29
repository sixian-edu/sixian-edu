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
fig, ax = plt.subplots(figsize=(8, 3.5))
ax.set_xlim(0, 10); ax.set_ylim(0, 3)
ax.axis('off')

boxes = [
    (0.3, 1.8, 1.2, 0.8, '① 审题\n圈关键量', '#c0392b'),
    (2.0, 1.8, 1.2, 0.8, '② 识别\n物理模型', '#2980b9'),
    (3.7, 1.8, 1.2, 0.8, '③ 选择\n对应公式', '#27ae60'),
    (5.4, 1.8, 1.2, 0.8, '④ 代入\n计算求解', '#e67e22'),
    (7.1, 1.8, 1.2, 0.8, '⑤ 检查\n单位&结果', '#8e44ad'),
]
for (x, y, w, h, txt, color) in boxes:
    rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                                     facecolor=color, edgecolor='white', linewidth=2, alpha=0.85)
    ax.add_patch(rect)
    ax.text(x+w/2, y+h/2, txt, ha='center', va='center', fontsize=9, color='white', fontweight='bold', linespacing=1.4)

for i in range(len(boxes)-1):
    x1 = boxes[i][0] + boxes[i][2]
    y1 = boxes[i][1] + boxes[i][3]/2
    x2 = boxes[i+1][0]
    y2 = boxes[i+1][1] + boxes[i+1][3]/2
    ax.annotate('', xy=(x2-0.05, y2), xytext=(x1+0.05, y1),
                arrowprops=dict(arrowstyle='->', color=GRAY, lw=2))

ax.text(5, 0.4, '每做一题，跑一遍流程，形成肌肉记忆', ha='center', fontsize=10, color=DARK,
        bbox=dict(boxstyle='round,pad=0.3', facecolor=GRAY_LIGHT, edgecolor='none'))
ax.text(5, 2.95, '中考物理解题思维流程图', ha='center', fontsize=11, fontweight='bold', color=DARK)
plt.tight_layout()
plt.savefig(os.path.join(out, 'phy_score_flow.svg'), bbox_inches='tight', dpi=150)
plt.close()

# ─── Chart 2: 常见物理模型分类 ───
fig, ax = plt.subplots(figsize=(7, 4))
ax.axis('off')

categories = [
    ('力学模型', ['受力平衡模型', '压强浮力模型', '机械功与功率', '简单机械'], '#c0392b'),
    ('电学模型', ['欧姆定律模型', '电功率模型', '电路故障分析', '电磁感应模型'], '#2980b9'),
    ('热学模型', ['物态变化模型', '内能比热容', '热值计算'], '#e67e22'),
    ('光学模型', ['反射成像模型', '折射与透镜', '凸透镜成像'], '#8e44ad'),
]
colors_pale = {'#c0392b':'#fadbd8', '#2980b9':'#d4e6f1', '#e67e22':'#fdebd0', '#8e44ad':'#e8daef'}

y_start = 3.6
for ci, (title, items, color) in enumerate(categories):
    y = y_start - ci * 0.8
    ax.text(0.2, y, title, fontsize=10, fontweight='bold', color=color)
    for j, item in enumerate(items):
        ax.text(2.0 + j * 1.2, y, item, fontsize=8, ha='center',
                bbox=dict(boxstyle='round,pad=0.15', facecolor=colors_pale[color],
                          edgecolor=color, alpha=0.8))

ax.text(3.5, 3.95, '中考物理常见模型分类', ha='center', fontsize=12, fontweight='bold', color=DARK)
ax.text(0.2, -0.1, '识别模型 = 知道考什么 = 选对公式', fontsize=10, color=DARK,
        bbox=dict(boxstyle='round,pad=0.2', facecolor=GRAY_LIGHT, edgecolor='none'))
plt.savefig(os.path.join(out, 'phy_score_model.svg'), bbox_inches='tight', dpi=150)
plt.close()

# ─── Chart 3: 公式选择策略 ───
fig, ax = plt.subplots(figsize=(7, 4))
ax.axis('off')

formulas = [
    ('已知: m, g  求: G', 'G = mg', '重力'),
    ('已知: rho, V  求: m', 'm = rho V', '质量'),
    ('已知: F, S  求: p', 'p = F/S', '压强'),
    ('已知: rho, g, h  求: p', 'p = rho g h', '液体压强'),
    ('已知: rho, g, V排  求: F浮', 'F浮 = rho g V排', '浮力'),
    ('已知: U, I  求: R', 'R = U/I', '电阻'),
    ('已知: U, I  求: P', 'P = UI', '电功率'),
    ('已知: m, c, DeltaT  求: Q', 'Q = cmDeltaT', '热量'),
]

ax.text(0.3, 3.6, '已知条件 --->', fontsize=9, fontweight='bold', color=DARK)
ax.text(4.2, 3.6, '公式', fontsize=9, fontweight='bold', color='#c0392b')
ax.text(5.8, 3.6, '--- > 所求', fontsize=9, fontweight='bold', color=DARK)
ax.plot([0.1, 6.8], [3.5, 3.5], color=GRAY, lw=0.5)

for i, (cond, formula, target) in enumerate(formulas):
    y = 3.2 - i * 0.37
    ax.text(0.3, y, cond, fontsize=7.5, color=DARK)
    ax.text(4.2, y, formula, fontsize=8, color='#c0392b', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.1', facecolor='#fadbd8', edgecolor='none'))
    ax.text(5.8, y, target, fontsize=7.5, color='#27ae60')

ax.text(3.5, 3.95, '公式选择策略: 已知 rarr 公式 rarr 所求', ha='center', fontsize=11, fontweight='bold', color=DARK)
plt.savefig(os.path.join(out, 'phy_score_formula.svg'), bbox_inches='tight', dpi=150)
plt.close()

# ─── Chart 4: 选择题技巧 ───
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.axis('off')

tips = [
    ('排除法', '排除明显错误选项', '#c0392b', 90),
    ('量纲法', '检查单位是否匹配', '#2980b9', 75),
    ('极限法', '取极端值判断', '#27ae60', 65),
    ('特殊值法', '代入简单数值验证', '#e67e22', 55),
    ('图像法', '画示意图辅助', '#8e44ad', 50),
]

for i, (name, desc, color, hits) in enumerate(tips):
    x = 0.3 + i * 1.35
    ax.bar(x, hits, width=0.8, color=color, alpha=0.75, edgecolor='white', linewidth=1)
    ax.text(x, hits + 3, f'{hits}%', ha='center', fontsize=9, fontweight='bold', color=color)
    ax.text(x, -5, name, ha='center', fontsize=9, fontweight='bold', color=DARK)
    ax.text(x, -14, desc, ha='center', fontsize=7, color=GRAY)

ax.set_ylim(-22, 105)
ax.text(3.5, 105, '选择题实用技巧', ha='center', fontsize=11, fontweight='bold', color=DARK)
ax.text(3.5, 95, '(命中率因题型而异，综合使用效果更好)', ha='center', fontsize=8, color=GRAY)
plt.savefig(os.path.join(out, 'phy_score_mc.svg'), bbox_inches='tight', dpi=150)
plt.close()

# ─── Chart 5: 计算题步骤得分 ───
fig, ax = plt.subplots(figsize=(6.5, 3.5))
ax.axis('off')

steps = [
    ('写公式', '列出所用公式', '2分', '#c0392b'),
    ('代数据', '代入数值带单位', '2分', '#e74c3c'),
    ('算结果', '正确算出结果', '1分', '#2980b9'),
    ('写单位', '结果后加单位', '0.5分', '#27ae60'),
    ('做答', '写答: ......', '0.5分', '#8e44ad'),
]

for i, (step, detail, score, color) in enumerate(steps):
    x = 0.2 + i * 1.2
    rect = mpatches.FancyBboxPatch((x, 1.5), 1.0, 0.7, boxstyle="round,pad=0.1",
                                     facecolor=color, edgecolor='white', linewidth=1.5, alpha=0.8)
    ax.add_patch(rect)
    ax.text(x+0.5, 1.85, step, ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    ax.text(x+0.5, 1.55, detail, ha='center', va='top', fontsize=7, color=GRAY)
    ax.text(x+0.5, 2.35, score, ha='center', fontsize=9, color=color, fontweight='bold')
    if i < len(steps) - 1:
        ax.annotate('', xy=(x+1.1, 1.85), xytext=(x+1.0, 1.85),
                    arrowprops=dict(arrowstyle='->', color=GRAY, lw=1.5))

ax.text(3.25, 3.2, '计算题步骤分策略', ha='center', fontsize=11, fontweight='bold', color=DARK)
ax.text(3.25, 2.85, '写对公式+代数据 = 保底4分', ha='center', fontsize=9, color='#c0392b')
plt.savefig(os.path.join(out, 'phy_score_calc.svg'), bbox_inches='tight', dpi=150)
plt.close()

# ─── Chart 6: 实验题常见题型分布 ───
fig, ax = plt.subplots(figsize=(6.5, 3.5))
ax.axis('off')

exp_types = [
    ('实验原理题', '考实验依据', 25, '#c0392b'),
    ('步骤设计题', '考操作顺序', 20, '#2980b9'),
    ('数据分析题', '考读图读表', 25, '#27ae60'),
    ('误差分析题', '考误差原因', 15, '#e67e22'),
    ('结论表述题', '考总结结论', 15, '#8e44ad'),
]

ax.set_xlim(0, 35); ax.set_ylim(-0.5, 5.5)
for i, (name, desc, pct, color) in enumerate(exp_types):
    ax.barh(i, pct, height=0.55, color=color, alpha=0.75, edgecolor='white')
    ax.text(pct + 0.5, i, f'{pct}%', va='center', fontsize=10, fontweight='bold', color=color)
    ax.text(-0.3, i + 0.3, name, ha='left', va='bottom', fontsize=9, fontweight='bold', color=DARK)
    ax.text(10, i - 0.15, desc, ha='left', va='top', fontsize=7.5, color=GRAY)

ax.set_yticks(range(5))
ax.set_yticklabels([])
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(left=False)

ax.text(17.5, 5.8, '实验探究题常见题型分布', ha='center', fontsize=11, fontweight='bold', color=DARK)
ax.text(17.5, 5.3, '原理题和数据分析题占比最高，是复习重点', ha='center', fontsize=8.5, color=GRAY)
plt.savefig(os.path.join(out, 'phy_score_exp.svg'), bbox_inches='tight', dpi=150)
plt.close()

print("All 6 charts generated!")
