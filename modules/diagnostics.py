import psutil
import wmi
import subprocess
import speedtest
from datetime import datetime

def run_diagnostics(apply_fixes=False):
    """Gather system, network, and Windows 11 tweaks diagnostics"""
    result = { 'timestamp': datetime.now().isoformat() }

    # --- System Health ---
    result['cpu'] = psutil.cpu_percent(percpu=True)
    vm = psutil.virtual_memory()
    result['memory'] = {k: getattr(vm, k) for k in ['total','available','percent']}

    # --- Network Speed Test (safe) ---
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download()
        upload = st.upload()
        ping = st.results.ping
        result['network'] = {
            'download': download,
            'upload': upload,
            'ping': ping
        }
    except Exception as e:
        result['network'] = {'error': f'Network test failed: {e}'}

    # Additional diagnostics (GPU, SMART, battery) go here

    # Optional fixes/tweaks
    if apply_fixes:
        # call to apply safe Windows 11 optimizations
        pass

    return result