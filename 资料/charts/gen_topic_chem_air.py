"""生成 空气成分饼图 + O₂ 检验方法 图表"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.8),
                                gridspec_kw={'width_ratios': [1, 0.7]})

# ── 饼图数据 ──
labels = ['氮气 N2', '氧气 O2', '稀有气体', 'CO2', '其他']
sizes = [78, 21, 0.94, 0.03, 0.03]
colors = ['#5c6bc0', '#42a5f5', '#66bb6a', '#ffa726', '#ef5350']
explode = [0, 0, 0.05, 0.08, 0.08]

wedges, _ = ax1.pie(
    sizes, labels=None, autopct=None,
    colors=colors, explode=explode,
    startangle=90, counterclock=False,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
    textprops={'fontsize': 9}
)
ax1.set_xlim(-1.8, 1.8)
ax1.set_ylim(-1.8, 1.8)

# ── 为主扇区（氮气、氧气）添加内部标签 ──
big_indices = [0, 1]  # 氮气 78%, 氧气 21%
for i in big_indices:
    ang = (wedges[i].theta2 - wedges[i].theta1) / 2. + wedges[i].theta1
    x = np.cos(np.deg2rad(ang))
    y = np.sin(np.deg2rad(ang))
    # 百分比文字在内部
    ax1.annotate(f'{sizes[i]}%',
                 xy=(x * 0.65, y * 0.65),
                 ha='center', va='center',
                 fontsize=10, fontweight='bold', color='white')
    # 标签文字在外部稍远
    ax1.annotate(labels[i],
                 xy=(x * 1.0, y * 1.0),
                 ha='center', va='center',
                 fontsize=9, fontweight='bold', color='#333')

# ── 小扇区用牵引线引出 ──
small = [
    {'label': '稀有气体', 'pct': '0.94%', 'idx': 2, 'angle_offset': -5,
     'out_x': -1.5, 'out_y': 1.0},
    {'label': 'CO2', 'pct': '0.03%', 'idx': 3, 'angle_offset': 0,
     'out_x': 1.65, 'out_y': -0.2},
    {'label': '其他', 'pct': '0.03%', 'idx': 4, 'angle_offset': 5,
     'out_x': 0, 'out_y': -1.55},
]

for s in small:
    i = s['idx']
    ang = (wedges[i].theta2 - wedges[i].theta1) / 2. + wedges[i].theta1 + s['angle_offset']
    x = np.cos(np.deg2rad(ang))
    y = np.sin(np.deg2rad(ang))

    # 饼图边缘点
    edge_x = x * 1.05
    edge_y = y * 1.05

    # 外部标签位置
    label_x = s['out_x']
    label_y = s['out_y']

    # 牵引线：饼边缘 → 外部标签位置（用两个线段组成折线）
    # 中间拐点在 edge 到 label 方向上向外延伸
    dx = label_x - edge_x
    dy = label_y - edge_y
    dist = np.sqrt(dx**2 + dy**2)
    if dist > 0:
        mid_x = edge_x + dx / dist * 0.4
        mid_y = edge_y + dy / dist * 0.4
    else:
        mid_x, mid_y = edge_x, edge_y

    ax1.plot([edge_x, mid_x, label_x - 0.05],
             [edge_y, mid_y, label_y],
             color='#666', linewidth=0.8, linestyle='-', solid_capstyle='round')

    # 小圆点标记位置
    ax1.scatter([edge_x], [edge_y], s=15, c='#666', zorder=5)

    # 标签文字
    ha = 'center' if abs(label_x) < 0.3 else ('right' if label_x < 0 else 'left')
    ax1.annotate(f"{s['label']}\n{s['pct']}",
                 xy=(label_x, label_y),
                 ha=ha, va='center',
                 fontsize=8, color='#333', annotation_clip=False,
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                           edgecolor='#ccc', linewidth=0.5))

# ── 右侧：O₂ 检验方法 ──
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_facecolor('#e3f2fd')

# 木条
rect = mpatches.Rectangle((2.0, 0.8), 0.3, 2.2, facecolor='#a0522d', edgecolor='none')
ax2.add_patch(rect)
# 火星
star = mpatches.RegularPolygon((2.15, 3.0), numVertices=5, radius=0.25,
                                facecolor='#ffa500', edgecolor='none')
ax2.add_patch(star)
star2 = mpatches.RegularPolygon((2.15, 2.7), numVertices=5, radius=0.18,
                                 facecolor='#ffd700', edgecolor='none')
ax2.add_patch(star2)
# 标题
ax2.text(2.15, 4.3, 'O2', fontsize=16, fontweight='bold',
         ha='center', va='center', color='#1565c0')
ax2.text(2.15, 3.7, '带火星木条复燃', fontsize=9,
         ha='center', va='center', color='#e65100')
ax2.text(2.15, 0.3, 'O2 检验方法', fontsize=12, fontweight='bold',
         ha='center', va='center', color='#333')

# ── 总标题 ──
fig.suptitle('空气成分（体积分数）', fontsize=14, fontweight='bold',
             y=0.98, color='#333')

plt.tight_layout()
plt.savefig('topic_chem_air.svg', bbox_inches='tight',
            dpi=150, format='svg')
plt.close()
print('topic_chem_air.svg 已生成')
