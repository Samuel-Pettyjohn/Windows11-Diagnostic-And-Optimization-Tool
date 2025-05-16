WINDOWS DIAGNOSTIC TOOL
=======================

[Python 3.8+]

A powerful, modular and user-friendly Windows 11 diagnostic and optimization suite

🔍 OVERVIEW
-----------
The Ultimate Windows Diagnostic Tool™ helps you analyze, optimize, and monitor your Windows 11 system. With both a CLI and a sleek dark‑mode GUI built on PyQt5, you can:

- Gather comprehensive system and network diagnostics
- Automatically save and revisit your last 5 scans
- Export detailed reports (HTML, Markdown, or plain text)
- Monitor live CPU, memory, and process stats in real time

🚀 FEATURES
-----------
Module                | Description
----------------------|-------------------------------------------------------
System Diagnostics    | CPU, memory, temperature (future), and hardware info
Network Speed Test    | Download, upload, and ping measurements
Auto‑Save             | Last 5 scans saved in %APPDATA%/DiagnosisTool
Report Export         | Generate report.html, report.md, or report.txt
CLI Interface         | scan, scan --fix, scan --export, history
GUI Interface         | It's a GUI what do you want from me?

🛠️ INSTALLATION
---------------
1. Clone the repo:
   git clone https://github.com/Samuel-Pettyjohn/Windows11-Diagnostic-And-Optimization-Tool.git  
   cd ultimate-windows-diagnostic-tool

2. Install dependencies:
   pip install -r requirements.txt

💻 USAGE
--------
**CLI**  
Run a scan:
   python main.py scan  
Apply safe optimizations:
   python main.py scan --fix  
Export HTML report:
   python main.py scan --export html  
View history:
   python main.py history

**GUI**  
   python main.py

📋 CONTRIBUTING
---------------
1. Fork it  
2. Create a branch  
3. Commit & push   

📄 LICENSE
-----------
MIT License
