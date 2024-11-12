from html_to_dash import parse_html
import os

html_file_directory = "html"
python_file_directory = "dash"

files = [file for file in os.listdir(html_file_directory) if file.endswith('.html')]

for file in files:
    with open(f"{html_file_directory}/{file}", "r", encoding="utf8") as f:
        html = f.read()
        parsed = parse_html(html, if_return=True, enable_dash_svg=True)
        with open(f"{python_file_directory}/{file.replace('.html', '.py')}", "w", encoding="utf8") as f:
            f.write(parsed)
print("Done...")