# Terminal Basics

## 1. Why This Matters
The terminal (command line) is essential for running scripts, installing packages, and managing files. It's faster than GUI for many tasks.

## 2. Core Concept
Common commands:

```mermaid
graph LR
    Nav[Navigate: cd, ls] --> Manage[Manage: mkdir, rm]
    Manage --> Run[Execute: python, pip]
```

- `ls` (list files), `cd` (change directory), `pwd` (print working dir)
- `mkdir` (make directory), `rm` (remove), `cp`, `mv`
- `pip install` (install Python packages)
- `python script.py` (run script)
- `jupyter notebook` (launch Jupyter)

## 3. Real-World Examples
• Create a virtual environment: `python -m venv venv`
• Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
• Install requirements: `pip install -r requirements.txt`
• Run training: `python train.py --config config.yaml`

## 4. Comparison
| GUI action | Terminal command |
|------------|------------------|
| Open folder | `cd myproject` |
| Create file | `touch README.md` |
| Delete file | `rm old.py` |
| Copy file | `cp data.csv backup.csv` |

## 5. Decision Tree
1. Need to quickly run a script? → terminal
2. Managing many files? → terminal (especially with wildcards)
3. Working on remote server? → terminal is the only option

## 6. Common Misconceptions
• The terminal is not scary – you only need ~10 commands to start.
• You can't break your computer with basic commands (unless you use `rm -rf` carelessly).

## 7. FAQ
**Q: Do I need to memorise all commands?** No, you'll remember the common ones; use `--help` or Google for others.
**Q: What's the difference between terminal and shell?** Terminal is the program, shell is the interpreter (bash, zsh).

## 8. Next Steps
Read about virtual environments next.

## 9. Running Example
Throughout this repo, you'll use the terminal to:
- Navigate to the project folder
- Activate the virtual environment
- Run `python train.py` to train the house price model
- Launch Streamlit with `streamlit run app.py`

## 10. Interview Prep
1. How do you list all Python files in a folder using terminal?
2. What does `pip freeze > requirements.txt` do?

