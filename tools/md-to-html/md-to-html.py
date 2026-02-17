from os import listdir
from os.path import isfile, join


def md_lines_to_html_lines(file):
    html_lines = ["<!Doctype html>", "<html>", "<body>"]

    for line in file:
        if line.startswith("# "):
            html_line = "<h1>"
            html_line += line.split("# ", 1)[1].split("\n", 1)[0]
            html_line += "</h1>"
        elif line.startswith("## "):
            html_line = "<h2>"
            html_line += line.split("## ", 1)[1].split("\n", 1)[0]
            html_line += "</h2>"
        elif line.startswith("### "):
            html_line = "<h3>"
            html_line += line.split("### ", 1)[1].split("\n", 1)[0]
            html_line += "</h3>"
        elif line.startswith("#### "):
            html_line = "<h4>"
            html_line += line.split("#### ", 1)[1].split("\n", 1)[0]
            html_line += "</h4>"
        elif line.startswith("---"):
            html_line = "<hr>"
        elif line == "\n":
            html_line = "<br>"
        else:
            html_line = "<p>"
            html_line += line.split("\n", 1)[0]
            html_line += "</p>"
        html_lines.append(html_line)
    html_lines.append("</body>")
    html_lines.append("</html>")
    return html_lines


md_path = "markdown"
html_path = "html"

onlyfiles = [f for f in listdir(md_path) if isfile(join(md_path, f))]
onlymarkdown = [f for f in onlyfiles if f.endswith(".md")]

for md in onlymarkdown:
    md_file_path = "" + md_path + "/" + md
    html_file_path = "" + html_path + "/" + md.split(".md", 1)[0] + ".html"
    with open(md_file_path, "r") as file:
        html_lines = md_lines_to_html_lines(file)
        print(html_lines)
    with open(html_file_path, "w") as file:
        for line in html_lines:
            file.write(line + "\n")
