import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import random
import numpy as np
 
# Seed for reproducibility (but feels hand-crafted)
random.seed(7)
 
# My actual daily tools - written how a student actually thinks
my_stack = {
    "Coding Stuff I Use 🖥️": [
        "Python – mostly VS Code tbh",
        "Tinkercad (still figuring out circuits)",
        "A compiler + lots of Googling errors 😂"
    ],
    "Working w/ Others 🤝": [
        "GitHub – learning as I go",
        "Google Docs for shared notes",
        "Discord – fastest way to reach ppl"
    ],
    "Staying Safe Online 🔐": [
        "Strong passwords (kinda hard to remember)",
        "2FA on acc that actually matter",
        "Back up files... sometimes lol",
        "Antivirus on my laptop"
    ]
}
 
# Slightly off-white background like actual paper
fig, ax = plt.subplots(figsize=(9.5, 7.5))
fig.patch.set_facecolor('#fdfbf5')
ax.set_facecolor('#fdfbf5')
ax.axis('off')
 
# Add faint ruled lines like notebook paper
for i in np.arange(0.06, 0.97, 0.045):
    ax.axhline(y=i, color='#c8daf0', linewidth=0.4, alpha=0.6, xmin=0.04, xmax=0.96)
 
# Red margin line (notebook style)
ax.axvline(x=0.08, color='#f0a0a0', linewidth=1.0, alpha=0.7, ymin=0.04, ymax=0.96)
 
# Slight rotation helper (makes text look hand-placed)
def jitter(val, amt=0.004):
    return val + random.uniform(-amt, amt)
 
# Title - handwriting-ish font, slightly tilted feel
fig.text(0.5, 0.935,
         "My Daily Tech Stack  💻",
         fontsize=17,
         ha='center',
         fontfamily='DejaVu Serif',
         fontweight='bold',
         color='#1a1a2e',
         rotation=random.uniform(-0.4, 0.4))
 
# Subtitle like a student's note below the title
fig.text(0.5, 0.895,
         "tools i actually use for coding, collab + staying safe online",
         fontsize=9.5,
         ha='center',
         fontstyle='italic',
         color='#555577',
         fontfamily='DejaVu Serif')
 
# Hand-drawn underline under title (wavy-ish via multiple short lines)
underline_x = np.linspace(0.2, 0.8, 30)
underline_y = [0.882 + random.uniform(-0.0015, 0.0015) for _ in underline_x]
ax.plot(underline_x, underline_y, color='#3355aa', linewidth=1.3, alpha=0.55)
 
# Section colors – muted, like colored pens
section_colors = ['#2255bb', '#228844', '#bb3322']
bullet_chars   = ['→', '•', '✦']
 
y = 0.825
for idx, (section, items) in enumerate(my_stack.items()):
    col = section_colors[idx]
    bul = bullet_chars[idx]
 
    # Section heading – slightly imperfect x placement
    ax.text(jitter(0.10), jitter(y, 0.003),
            section,
            fontsize=12.5,
            fontweight='bold',
            color=col,
            fontfamily='DejaVu Serif',
            transform=ax.transAxes)
 
    # Faint underline under section heading
    ax.plot([0.10, 0.55 + random.uniform(-0.03, 0.03)],
            [y - 0.022, y - 0.022 + random.uniform(-0.002, 0.002)],
            color=col, linewidth=0.7, alpha=0.4,
            transform=ax.transAxes)
 
    y -= 0.052
 
    for item in items:
        # Each item placed with micro-variation
        ax.text(jitter(0.135), jitter(y, 0.003),
                f"{bul}  {item}",
                fontsize=10.5,
                color='#222233',
                fontfamily='DejaVu Serif',
                transform=ax.transAxes)
        y -= 0.046
 
    y -= 0.03   # breathing room between sections
 
# Footer – like a student writing the assignment name
ax.text(0.5, 0.045,
        "Digital Literacy Project  —  made by me :)",
        fontsize=8.5,
        ha='center',
        color='#888899',
        fontstyle='italic',
        fontfamily='DejaVu Serif',
        transform=ax.transAxes)
 
# Tiny doodle star in corner (students do this)
ax.text(0.93, 0.93, "★",
        fontsize=14, color='#f0c040', alpha=0.7,
        transform=ax.transAxes)
 
ax.text(0.06, 0.045, "pg. 1",
        fontsize=7.5, color='#aaaacc', alpha=0.6,
        fontfamily='DejaVu Serif',
        transform=ax.transAxes)
 
plt.tight_layout(pad=0.3)
plt.savefig("student_tech_stack.png", dpi=150, bbox_inches='tight',
            facecolor='#fdfbf5')
plt.show()