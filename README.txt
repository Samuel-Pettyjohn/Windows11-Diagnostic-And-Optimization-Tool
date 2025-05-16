# 
Ultimate Windows Diagnostic Tool

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/) [![PyPI](https://img.shields.io/badge/pypi-v1.0.0-green)](#)

> **A powerful, modular and user-friendly Windows 11 diagnostic and optimization suite**

## 🔍 Overview  
The **Ultimate Windows Diagnostic Tool™** helps you analyze, optimize, and monitor your Windows 11 system. With both a CLI and a sleek dark‑mode GUI built on PyQt5, you can:

- 📊 Gather comprehensive system and network diagnostics  
- 💾 Automatically save and revisit your last 5 scans  
- 📝 Export detailed reports (HTML, Markdown, or plain text)  
- 🖥️ Monitor live CPU, memory, and process stats in real time  

## 🚀 Features

| Module                | Description                                            |
|-----------------------|--------------------------------------------------------|
| **System Diagnostics**| CPU, memory, temperature (future), and hardware info   |
| **Network Speed Test**| Download, upload, and ping measurements                |
| **Auto‑Save**         | Retain the last 5 scans in `%APPDATA%/DiagnosisTool`   |
| **Report Export**     | Generate `report.html`, `report.md`, or `report.txt`   |
| **CLI Interface**     | `scan`, `scan --fix`, `scan --export`, `history`       |
| **GUI Interface**     | Dark‑themed PyQt5 app with tabs for Diagnostics, Live Stats, History, and Processes |

## 📂 Folder Structure
```
windows_diagnostic_tool/        # project root
├── modules/                   # core logic
│   ├── diagnostics.py        # perform system/net checks
│   ├── reporting.py          # export reports via Jinja2
│   ├── autosave.py           # manage scan history
│   ├── cli.py                # CLI commands (click)
│   └── utils.py              # helper functions (paths, setup)
├── ui/                        # GUI code
│   └── gui.py                # PyQt5 application
├── scans/                     # auto-saved JSON scans
├── main.py                    # decides CLI vs GUI launch
└── requirements.txt           # Python dependencies
```

## 🛠️ Installation

1. Clone the repo (or download source):  
   ```bash
   git clone https://github.com/yourusername/ultimate-windows-diagnostic-tool.git
   cd ultimate-windows-diagnostic-tool
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Command‑Line Interface (CLI)
- **Run a scan**:  
  ```bash
  python main.py scan
  ```
- **Run a scan & apply safe optimizations**:  
  ```bash
  python main.py scan --fix
  ```
- **Export report in HTML**:  
  ```bash
  python main.py scan --export html
  ```  
  > Formats: `html`, `md`, `txt`, or `all`
- **View scan history**:  
  ```bash
  python main.py history
  ```

### Graphical User Interface (GUI)
Launch without arguments to open the dark‑mode GUI:  
```bash
python main.py
```

**GUI Tabs:**
- **Diagnostics**: Run full system and network scans  
- **Live Stats**: Real‑time CPU & memory usage updates  
- **History**: Browse the last 5 saved scans with color‑coded metrics  
- **Processes**: Top 20 processes by CPU usage (color‑coded)  

## 📋 Contributing

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/awesome`)  
3. Commit your changes (`git commit -m "Add awesome feature"`)  
4. Push to branch (`git push origin feature/awesome`)  
5. Open a Pull Request  

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Built with ❤️ and PyQt5*