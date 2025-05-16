import os
from jinja2 import Environment, FileSystemLoader
from modules.utils import get_scan_folder

env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

def export_report(data, fmt='all'):
    """Export diagnostic data to HTML/Markdown/Text"""
    base = data['timestamp'].replace(':','-')
    if fmt in ('html','all'):
        template = env.get_template('report.html.j2')
        with open(f'report_{base}.html','w') as f:
            f.write(template.render(data=data))
    if fmt in ('md','all'):
        template = env.get_template('report.md.j2')
        with open(f'report_{base}.md','w') as f:
            f.write(template.render(data=data))
    if fmt in ('txt','all'):
        with open(f'report_{base}.txt','w') as f:
            f.write(str(data))