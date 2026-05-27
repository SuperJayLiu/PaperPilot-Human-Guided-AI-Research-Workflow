# Upload PaperPilot Clean Structure To GitHub

From the unzipped folder:

```bash
git init
git branch -M main
git add .
git commit -m "init: add clean PaperPilot workflow structure"
git remote add origin https://github.com/SuperJayLiu/PaperPilot-Human-Guided-AI-Research-Workflow.git
git push --force -u origin main
```

Run checks first:

```bash
python 99_System_Do_Not_Touch/03_Check_Scripts/check_visible_structure.py
python 99_System_Do_Not_Touch/03_Check_Scripts/check_no_old_working_name.py
python 99_System_Do_Not_Touch/03_Check_Scripts/check_memory_protocol.py
python 99_System_Do_Not_Touch/03_Check_Scripts/check_skill_quality.py
python 99_System_Do_Not_Touch/03_Check_Scripts/quality_gate_check.py
```
