# Ultimate Windows Diagnostic Tool™

The Ultimate Windows Diagnostic Tool™ is a powerful and versatile application designed to help you analyze and optimize your Windows 11 system. It offers both a command-line interface (CLI) and a graphical user interface (GUI) for your convenience. This tool provides comprehensive system and network diagnostics, allowing you to identify potential issues and export detailed reports.

---

## Features

* **System Diagnostics**: Gathers information about your CPU and memory usage.
* **Network Speed Test**: Performs a reliable speed test to measure download, upload, and ping.
* **Automatic Scan Saving**: Automatically saves the last 5 scans for easy access to historical data.
* **Report Exporting**: Export detailed diagnostic reports in HTML, Markdown, or plain text formats.
* **Command-Line Interface (CLI)**:
    * Run scans with an option to apply safe optimizations.
    * View a history of previous scans.
    * Export reports directly from the command line.
* **Graphical User Interface (GUI)**:
    * User-friendly interface built with PyQt5.
    * "Diagnostics" tab to run scans and view reports.
    * "History" tab to load and review past scans.
    * "Live Stats" tab to monitor real-time CPU and memory usage.
    * Dark theme for improved readability.
    * Includes a placeholder for future ISLC (Intelligent Standby List Cleaner) integration.

---

## Installation

To set up the Ultimate Windows Diagnostic Tool™, follow these steps:

1.  **Clone the repository** (if applicable, though not provided in the snippets).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt [cite: 1]
    ```
    This will install necessary packages like `psutil`[cite: 2], `wmi`[cite: 2], `pywin32`[cite: 2], `speedtest-cli`[cite: 2], `click`[cite: 2], `jinja2`[cite: 2], `PyYAML`[cite: 2], and `PyQt5`[cite: 2].

---

## Usage

### Command-Line Interface (CLI)

To use the CLI, navigate to the project's root directory and run `main.py` with arguments.

* **Run a diagnostic scan**:
    ```bash
    python main.py scan
    ```
* **Run a diagnostic scan and apply safe optimizations**:
    ```bash
    python main.py scan --fix
    ```
* **Export a report after scanning (e.g., to HTML)**:
    ```bash
    python main.py scan --export html
    ```
    You can also choose `md`, `txt`, or `all` for the export format.
* **View scan history**:
    ```bash
    python main.py history
    ```

### Graphical User Interface (GUI)

To launch the GUI, simply run `main.py` without any command-line args:

```bash
python main.py