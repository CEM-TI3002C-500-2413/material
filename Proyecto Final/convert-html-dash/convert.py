from html_to_dash import parse_html
import os

files = [file for file in os.listdir() if file.endswith('.html')]

for file in files:
    with open(file, "r", encoding="utf8") as f:
        html = f.read()
        parsed = parse_html(html, if_return=True, enable_dash_svg=True)
        with open(file.replace('.html', '.py'), "w", encoding="utf8") as f:
            f.write(parsed)
print("Done...")