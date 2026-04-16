import os

OUTPUT = "teambook.tex"

def latex_escape(text):
    return (text.replace("\\", "\\textbackslash{}")
                .replace("_", "\\_")
                .replace("%", "\\%")
                .replace("#", "\\#")
                .replace("&", "\\&")
                .replace("{", "\\{")
                .replace("}", "\\}"))

def escribir_header(f):
    f.write(r"""
\documentclass[10pt,twocolumn]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

\usepackage[margin=0.5in]{geometry}
\usepackage{listings}
\usepackage{xcolor}

\lstset{
    language=C++,
    basicstyle=\ttfamily\tiny,
    keywordstyle=\color{blue},
    commentstyle=\color{gray},
    stringstyle=\color{green!50!black},
    numbers=left,
    numberstyle=\tiny,
    breaklines=true,
    frame=single,
    tabsize=2,
    showstringspaces=false,
    literate=
        {→}{{$\rightarrow$}}1
        {≤}{{$\leq$}}1
        {≥}{{$\geq$}}1
}

\title{ICPC Team Notebook}
\date{}

\begin{document}
\maketitle
\tableofcontents
""")

def escribir_footer(f):
    f.write("\n\\end{document}")

def main():
    with open(OUTPUT, "w") as f:
        escribir_header(f)

        for root, dirs, files in os.walk("."):
            # ignorar carpetas innecesarias
            if ".git" in root:
                continue

            cpp_files = [file for file in files if file.endswith(".cpp")]

            if cpp_files:
                section_name = root.replace("./", "")
                section_name = latex_escape(section_name)

                f.write(f"\n\\section{{{section_name}}}\n")

                for file in sorted(cpp_files):
                    path = os.path.join(root, file)
                    safe_file = latex_escape(file)

                    f.write(f"\n\\subsection{{{safe_file}}}\n")
                    f.write(f"\\lstinputlisting{{{path}}}\n")

        escribir_footer(f)

if __name__ == "__main__":
    main()
