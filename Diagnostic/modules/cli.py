import click
from modules.diagnostics import run_diagnostics
from modules.reporting import export_report
from modules.autosave import save_scan, load_scans
from modules.utils import ensure_scan_folder

@click.group()
@click.version_option('1.0.0')
def run():
    """Ultimate Windows Diagnostic Tool™ CLI"""
    ensure_scan_folder()

@run.command()
@click.option('--fix', is_flag=True, help='Apply safe optimizations')
@click.option('--export', type=click.Choice(['html','md','txt','all']), default=None)
def scan(fix, export):
    """Run diagnostics (and optional fixes)"""
    data = run_diagnostics(apply_fixes=fix)
    save_scan(data)
    click.echo('Scan complete.')
    if export:
        export_report(data, fmt=export)

@run.command()
def history():
    """List and load previous scans"""
    scans = load_scans()
    for idx, s in enumerate(scans, 1):
        click.echo(f"{idx}. {s['timestamp']} - Network: {s.get('network', {})}")

if __name__ == '__main__':
    run()