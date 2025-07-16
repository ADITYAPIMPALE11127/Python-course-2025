
# 🐍 Python Course 2025 – Class Notes & Practice

Welcome to the **Python Course 2025** repo! 👋  
This is where we revise and update Python concepts taught in class – neatly, weekly, and with everyone's help!

---
## For Important References for study refer below: 
📚 [Click here for Important Library References](important_references.md)

## 👶 Who is this for?

This repo is made for beginners — imagine you're 5 years old and just learning Python!  
We are helping each other revise by adding weekly learnings.  
Each person contributes on their own **branch**, and (Aditya) and others who are better at github will review and merge it into the main code.

---

## 🧰 Prerequisites – What you need before starting

Before you can join the fun, install the following:

### ✅ 1. Python (latest version)
- Youtube Video Guide - https://youtu.be/ddGTXBhaGWA?si=x6yRWYCMlShqizG4
- Download from: https://www.python.org/downloads/
- Install it globally (check "Add to PATH" during installation)

### ✅ 2. Git
- Youtube Video guide - https://youtu.be/3Tsaxxv9sls?si=VK1deFJjjdAYmsSa
- Download from: https://git-scm.com/downloads
- Git helps in version control (tracking file changes)
- After installing, open your terminal and type:
  ```bash
  git --version
  ```

### ✅ 3. GitHub account
- Make one here: https://github.com

### ✅ 4. VS Code (Code Editor)

- Youtube video guide - https://youtu.be/cu_ykIfBprI?si=5IPfPIJ5uOzTVFG8
- Download from: https://code.visualstudio.com/

### ✅ 5. VS Code Extensions
Install these in VS Code:
- Youtube Video Guide - https://youtu.be/xS5ZXOC4e6A?si=DFi7VVec19Q2zv7N
- **Python Extension** (by Microsoft)
- **Jupyter Extension** (for running `.ipynb` notebooks)

### ✅ 6. Python Libraries – Install these once
-Youtube video guide - https://youtu.be/ThU13tikHQw?si=x_VSy_8cXQc6DDpt
Open your terminal and run:
```bash
pip install numpy pandas matplotlib seaborn
```

---

## 👨‍👩‍👧‍👦 Contribution Plan

We will divide the weekdays among contributors:

| Day       | Contributor Name | Task                                              |
|-----------|------------------|---------------------------------------------------|
| Monday    | Person A         | Add new topic & code                              |
| Tuesday   | Person B         | Add comments & correction to the topics added     |
| Wednesday | Person C         | Add new topic & code                              |
| Thursday  | Person D         | Add comments & correction to the topics added     |
| Friday    | Person E         | Final review/cleanup                              |

---

## 🛠️ How to Contribute (Step-by-Step)

1. **Fork the repo**  
   Click on the “Fork” button in the top-right corner of this repo.

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Python-course-2025.git
   cd Python-course-2025
   ```

3. **Create a new branch**
   Name it like this: `week1-topic-name`
   ```bash
   git checkout -b week1-functions
   ```

4. **Do your work**
   - Create a new file like `functions.py` or `week1_notes.ipynb`
   - Follow folder structure (or ask if unsure)
   - Save and test your code

5. **Stage and commit your changes**
   ```bash
   git add .
   git commit -m "Added week 1 - functions notes"
   ```

6. **Push your branch**
   ```bash
   git push origin week1-functions
   ```

7. **Make a Pull Request (PR)**
   - Go to your fork on GitHub
   - Click "Compare & Pull Request"
   - Title your PR clearly: `Week 1 - Functions by [Your Name]`

---

## 🚫 Rules to Follow

- **Do not merge to `main` directly**
- Make a new branch always
- Let Aditya and others review the branch and merge
- Use clear commit messages
- Make changes in your own file/folder to avoid conflicts

---

## 🔁 Weekly Sync – Pull Latest Changes

Every weekend, all PRs will be reviewed and merged.

To **stay up to date**:
```bash
git checkout main
git pull origin main
```

Then, update your own branch:
```bash
git checkout your-branch-name
git merge main
```

Resolve conflicts if any (ask for help if confused!).

---

## 📁 Folder Structure Suggestion

```
/Python-course-2025
│
├── Strings/
│   ├── existing.ipynb
│   └── new_strings.ipynb
└── README.md
```

---

## ❓FAQ

**Q. My Jupyter Notebook doesn't run in VS Code**  
A: Make sure you have installed the **Python** and **Jupyter** extensions in VS Code. Also check that Python is installed globally and selected as interpreter.

**Q. Can I add extra examples or explain concepts in my own way?**  
A: Yes! Please do. But put them in your own file to avoid mixing up.

---

## 👏 Thank you!

Let’s keep learning and help each other. Happy coding! 💻🐍  
If you are stuck, ask in the group – we are here to help!

---
