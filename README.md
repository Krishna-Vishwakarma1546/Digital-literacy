# My Student Tech Stack – Visual Chart 💻

A simple Python script I made for my **Digital Literacy Project**. It creates a notebook-style chart showing the tools I actually use day-to-day as a student — for coding, working with others, and staying safe online.

---

## What It Does

Generates a `.png` image that looks like something hand-written in a notebook. It has ruled lines, a red margin, slightly imperfect text placement, and casual language — basically the opposite of a boring auto-generated chart.

---

## Why I Made It This Way

Most charts look too "clean" and robotic. I wanted mine to feel like a real student actually sat down and made it — messy underlines, emoji, lowercase subtitles, a little star doodle in the corner. It's still organized, just... human.

---

## Requirements

You'll need Python 3 and these libraries:

```
matplotlib
numpy
```

Install them with:

```bash
pip install matplotlib numpy
```

---

## How to Run

Just run the script:

```bash
python student_tech_stack.py
```

It will:
- Show the chart on your screen
- Save it as `student_tech_stack.png` in the same folder

---

## What's Inside the Chart

| Section | What it covers |
|---|---|
| Coding Stuff I Use 🖥️ | Python, VS Code, Tinkercad, debugging |
| Working w/ Others 🤝 | GitHub, Google Docs, Discord |
| Staying Safe Online 🔐 | Passwords, 2FA, backups, antivirus |

---

## Customizing It

Want to change the tools listed? Just edit the `my_stack` dictionary near the top of the file — it's straightforward, each section is a list of strings.

Want different colors? The `section_colors` list controls the heading colors for each section.

---

## Output

Saves as: `student_tech_stack.png`  
Resolution: 150 DPI  
Background: off-white (`#fdfbf5`), like actual paper

---

*Made as part of a Digital Literacy project — by me :)*
