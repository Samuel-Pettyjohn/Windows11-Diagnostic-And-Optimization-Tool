import json
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QPushButton, QTextEdit, QTabWidget, QProgressBar, QTableWidget, QTableWidgetItem, QLabel, QComboBox)
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QColor, QBrush
import psutil
from modules.diagnostics import run_diagnostics
from modules.reporting import export_report
from modules.autosave import save_scan, load_scans
from modules.utils import ensure_scan_folder

def color_status(status):
    if status == "OK":
        return '<span style="color: #00b300; font-weight:bold;">🟢 OK</span>'
    elif status == "WARNING":
        return '<span style="color: #e6b800; font-weight:bold;">🟡 WARNING</span>'
    else:
        return '<span style="color: #d9534f; font-weight:bold;">🔴 CRITICAL</span>'

class DiagnosticWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(dict)

    def run(self):
        # Simulate progress for demonstration; replace with real progress if possible
        import time
        for i in range(1, 101, 10):
            self.progress.emit(i)
            time.sleep(0.1)
        data = run_diagnostics()
        self.finished.emit(data)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ultimate Win11 Diagnostic™')
        self.resize(1000, 700)
        self.set_dark_theme()
        self._setup_ui()

    def set_dark_theme(self):
        dark_style = """
QWidget {
    background-color: #1e1e2e;
    color: #cfcfcf;
    font-family: Consolas, monospace;
}
QTextEdit, QPlainTextEdit {
    background-color: #232346;
    color: #e0e0e0;
    border: 1px solid #444;
}
QPushButton {
    background-color: #223366;
    color: #cfcfcf;
    border: 1px solid #3377cc;
    padding: 6px;
    border-radius: 5px;
}
QPushButton:hover {
    background-color: #335599;
    border: 1px solid #55aaff;
}
QTabWidget::pane {
    border: 1px solid #3377cc;
}
QTabBar::tab {
    background: #232346;
    color: #8ecfff;
    padding: 6px;
    border: 1px solid #3377cc;
}
QTabBar::tab:selected {
    background: #3377cc;
    color: #fff;  /* blue highlight */
    border-bottom: 2px solid #55aaff;
}
"""
        self.setStyleSheet(dark_style)

    def _setup_ui(self):
        tabs = QTabWidget()
        tabs.addTab(self._build_diagnostics_tab(), 'Diagnostics')
        tabs.addTab(self._build_history_tab(), 'History')
        tabs.addTab(self._build_live_stats_tab(), 'Live Stats')
        tabs.addTab(self._build_islc_tab(), 'ISLC')
        self.setCentralWidget(tabs)

    def _build_diagnostics_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        self.report_view = QTextEdit(readOnly=True)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        run_btn = QPushButton('Run Scan')
        run_btn.clicked.connect(self._on_run)
        save_btn = QPushButton('Export Report')
        save_btn.clicked.connect(self._on_export)
        layout.addWidget(run_btn)
        layout.addWidget(save_btn)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.report_view)
        widget.setLayout(layout)
        return widget

    def _build_history_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        self.history_view = QTextEdit(readOnly=True)
        load_btn = QPushButton('Load History')
        load_btn.clicked.connect(self._on_load_history)
        layout.addWidget(load_btn)
        layout.addWidget(self.history_view)
        widget.setLayout(layout)
        return widget

    def _build_live_stats_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        self.live_stats = QTextEdit(readOnly=True)
        self.live_stats.setStyleSheet("font-family: Consolas, monospace; font-size: 13px;")
        layout.addWidget(self.live_stats)
        widget.setLayout(layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_live_stats)
        self.timer.start(1000)
        return widget

    def _build_islc_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        info_label = QLabel("StandbyCleanerLite Modified On 5/16/25\n\nISLC integration coming soon\nProb will use ISLC lightweight by Mephres.")
        info_label.setStyleSheet("font-weight: bold; color: #3399ff; font-size: 15px;")
        layout.addWidget(info_label)
        widget.setLayout(layout)
        return widget

    def update_live_stats(self):
        cpu_percents = psutil.cpu_percent(percpu=True)
        mem = psutil.virtual_memory()
        cpu_lines = []
        for idx, percent in enumerate(cpu_percents):
            cpu_lines.append(f"<b>Core {idx+1}:</b> <span style='color:#0af;'>{percent}%</span>")
        cpu_html = '<br>'.join(cpu_lines)
        mem_html = f"<b>Memory Usage:</b> <span style='color:#0af;'>{mem.percent}%</span> (<span style='color:#aaa;'>{mem.used // (1024 ** 2)}MB / {mem.total // (1024 ** 2)}MB</span>)"
        self.live_stats.setHtml(f"""
        <div style='font-size:15px;'><b>CPU Usage Per Core</b></div>
        {cpu_html}
        <br><br>
        {mem_html}
        """)

    def _on_run(self):
        ensure_scan_folder()
        self.progress_bar.setValue(0)
        self.report_view.clear()
        self.worker = DiagnosticWorker()
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.finished.connect(self._on_diagnostics_finished)
        self.worker.start()

    def _on_diagnostics_finished(self, data):
        save_scan(data)
        def render_html(d):
            html = "<pre>"
            for k, v in d.items():
                if isinstance(v, dict) and 'status' in v:
                    status_html = color_status(v['status'])
                    html += f"<b>{k}:</b> {status_html}\n"
                else:
                    html += f"<b>{k}:</b> {v}\n"
            html += "</pre>"
            return html
        self.report_view.setHtml(render_html(data))
        self.progress_bar.setValue(100)

    def _on_export(self):
        data = run_diagnostics()
        export_report(data, fmt='all')
        self.report_view.append('\n<Report Exported>')

    def _on_load_history(self):
        scans = load_scans()
        pretty = "\n\n".join(json.dumps(s, indent=2) for s in scans)
        self.history_view.setPlainText(pretty)


def gui_main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())