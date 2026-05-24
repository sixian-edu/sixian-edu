"""生成数列专题SVG图表（修正中文字体）"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Noto Sans SC']
plt.rcParams['axes.unicode_minus'] = False

OUT = r'C:\Users\21342\Desktop\sixian-edu\资料\charts'

# ─── 1. 等差数列（AP）示意图 ───
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.12, bottom=0.12, right=0.95, top=0.92)
n = np.arange(1, 9)
a1, d = 2, 3
an = a1 + (n-1)*d
ax.scatter(n, an, c='#5688CC', s=60, zorder=5)
ax.plot(n, an, '--', color='#5688CC', alpha=0.4, linewidth=1)
for i in n:
    ax.plot([i, i], [0, a1+(i-1)*d], ':', color='#999', linewidth=0.6)
ax.set_xticks(n)
ax.set_xlabel('n (项数)', fontsize=11)
ax.set_ylabel('a_n (项值)', fontsize=11)
ax.set_title('等差数列  a_n = 2 + (n-1)*3', fontsize=13, color='#1a1a2e')
ax.grid(True, alpha=0.3)
ax.set_xlim(0.5, 8.5)
ax.text(4, a1+(4-1)*d+2, 'd=3', fontsize=11, color='#e74c3c', ha='center')
fig.savefig(os.path.join(OUT, 'seq_ap.svg'), dpi=120, facecolor='white')
plt.close()

# ─── 2. 等比数列（GP）示意图 ───
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.2))
plt.subplots_adjust(left=0.08, right=0.95, wspace=0.3, bottom=0.15, top=0.9)
n = np.arange(1, 9)
a1, q = 1, 2
an = a1 * q**(n-1)
ax1.scatter(n, an, c='#e67e22', s=50, zorder=5)
ax1.plot(n, an, '--', color='#e67e22', alpha=0.4, linewidth=1)
ax1.set_xticks(n)
ax1.set_xlabel('n', fontsize=10)
ax1.set_ylabel('a_n', fontsize=10)
ax1.set_title('等比数列 (q>1 增长)', fontsize=11, color='#1a1a2e')
ax1.grid(True, alpha=0.3)
a1, q = 16, 0.5
an = a1 * q**(n-1)
ax2.scatter(n, an, c='#27ae60', s=50, zorder=5)
ax2.plot(n, an, '--', color='#27ae60', alpha=0.4, linewidth=1)
ax2.set_xticks(n)
ax2.set_xlabel('n', fontsize=10)
ax2.set_title('等比数列 (0<q<1 衰减)', fontsize=11, color='#1a1a2e')
ax2.grid(True, alpha=0.3)
fig.savefig(os.path.join(OUT, 'seq_gp.svg'), dpi=120, facecolor='white')
plt.close()

# ─── 3. 数列求和——条形图与等差数列和 ───
fig, ax = plt.subplots(figsize=(5, 3.5))
plt.subplots_adjust(left=0.1, bottom=0.12, right=0.95, top=0.92)
n_terms = 6
a1, d = 2, 3
for i in range(n_terms):
    val = a1 + i*d
    ax.add_patch(plt.Rectangle((i+0.05, 0), 0.9, val, facecolor='#5688CC', alpha=0.6, edgecolor='#5688CC', linewidth=1))
    ax.text(i+0.5, val/2, str(val), ha='center', va='center', fontsize=9, color='#fff', fontweight='bold')
ax.set_xlim(0, n_terms+0.5)
ax.set_ylim(0, a1+(n_terms-1)*d+3)
ax.set_xticks(range(1, n_terms+1))
ax.set_xlabel('n', fontsize=11)
ax.set_ylabel('a_n', fontsize=11)
ax.set_title('等差数列前 n 项和 (条形图)', fontsize=13, color='#1a1a2e')
ax.grid(True, alpha=0.2)
fig.savefig(os.path.join(OUT, 'seq_sum_ap.svg'), dpi=120, facecolor='white')
plt.close()

# ─── 4. 裂项相消示意图 ───
fig, ax = plt.subplots(figsize=(6, 2.8))
plt.subplots_adjust(left=0.05, right=0.95, top=0.85, bottom=0.2)
terms = ['1/(1*2)', '1/(2*3)', '1/(3*4)', '...', '1/n(n+1)']
x_pos = [1, 3, 5, 7, 9]
colors = ['#e74c3c', '#e67e22', '#f1c40f', '#95a5a6', '#27ae60']
for t, x, c in zip(terms, x_pos, colors):
    ax.add_patch(plt.Rectangle((x-0.8, 0.3), 1.6, 0.8, facecolor=c, alpha=0.3, edgecolor=c, linewidth=1.5))
    ax.text(x, 0.7, t, ha='center', va='center', fontsize=12, color='#2d3436')

# 展开公式
ax.text(5, -0.1, '= (1-1/2) + (1/2-1/3) + (1/3-1/4) + ... + (1/n-1/(n+1))',
        ha='center', va='center', fontsize=11, color='#1a1a2e',
        bbox=dict(facecolor='#fef9e7', edgecolor='#f9e79f', boxstyle='round,pad=0.4'))
ax.text(5, -0.65, '= 1 - 1/(n+1) = n/(n+1)', ha='center', va='center',
        fontsize=12, color='#e74c3c', fontweight='bold')
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1.5)
ax.axis('off')
ax.set_title('裂项相消法原理', fontsize=13, color='#1a1a2e', pad=8)
fig.savefig(os.path.join(OUT, 'seq_split.svg'), dpi=120, facecolor='white')
plt.close()

# ─── 5. 错位相减法示意图 ───
fig, ax = plt.subplots(figsize=(5.5, 3))
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)
ax.text(0.5, 2.5, 'S_n = a + 2a^2 + 3a^3 + ... + na^n', fontsize=12, color='#1a1a2e', va='center')
ax.text(0.5, 1.8, '*a 得:  aS_n = a^2 + 2a^3 + ... + (n-1)a^n + na^{n+1}', fontsize=12, color='#5688CC', va='center')
ax.annotate('', xy=(3.8, 2.2), xytext=(3.8, 2.0), arrowprops=dict(arrowstyle='<->', color='#e74c3c', lw=1.5))
ax.text(4.2, 2.1, '错位', fontsize=10, color='#e74c3c', va='center')
ax.text(0.5, 1.0, '相减: (1-a)S_n = a + a^2 + a^3 + ... + a^n - na^{n+1}', fontsize=12, color='#e74c3c', va='center', fontweight='bold')
ax.text(0.5, 0.4, '-> 转化为等比数列求和', fontsize=11, color='#27ae60', va='center')
ax.set_xlim(0, 6)
ax.set_ylim(0, 3.2)
ax.axis('off')
ax.set_title('错位相减法 (等差 x 等比型求和)', fontsize=13, color='#1a1a2e', pad=8)
fig.savefig(os.path.join(OUT, 'seq_shift_sub.svg'), dpi=120, facecolor='white')
plt.close()

# ─── 6. 数学归纳法原理 ───
fig, ax = plt.subplots(figsize=(4.5, 3.5))
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.05)
n_domino = 6
for i in range(n_domino):
    x = i * 0.7
    rect = plt.Rectangle((x, 0.5), 0.4, 0.8, facecolor='#5688CC' if i == 0 else '#bdc3c7',
                         edgecolor='#2c3e50', linewidth=1.5, alpha=0.8)
    ax.add_patch(rect)
    if i == 0:
        ax.annotate('', xy=(x+0.2, 0.5), xytext=(x+0.2, 1.5),
                    arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=2))
        ax.text(x+0.2, 1.6, '推倒\n第1块', ha='center', fontsize=8, color='#e74c3c')
ax.text(0.2, 0.2, '(1) n=1 成立 (基础)', fontsize=11, color='#e74c3c', fontweight='bold')
ax.text(0.2, -0.1, '(2) 假设 n=k 成立 => n=k+1 成立 (递推)', fontsize=11, color='#27ae60', fontweight='bold')
ax.text(0.2, -0.4, '=> 命题对所有正整数 n 成立', fontsize=11, color='#5688CC', fontweight='bold')
ax.set_xlim(-0.3, n_domino*0.7+0.3)
ax.set_ylim(-0.6, 2)
ax.axis('off')
ax.set_title('数学归纳法 -- 多米诺骨牌原理', fontsize=13, color='#1a1a2e', pad=8)
fig.savefig(os.path.join(OUT, 'seq_induction.svg'), dpi=120, facecolor='white')
plt.close()

print('All SVGs generated with CJK font support!')
