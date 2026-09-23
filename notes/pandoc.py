import os
import shutil
import re
import subprocess


def file_exists(file_path):
    return os.path.isfile(file_path)


def make_temp_copy(file_path):
    temp_file_path = f"TEMP_{os.path.basename(file_path)}"
    shutil.copy(file_path, temp_file_path)
    return temp_file_path


def find_tex_subfiles(main_tex_path):
    subfiles = []
    with open(main_tex_path, 'r') as file:
        for line in file:
            # Ignore lines that are commented out
            if line.strip().startswith('%'):
                continue
            # Find subfiles in non-commented lines
            match = re.search(r'\\subfile{([^}]+)}', line)
            if match:
                subfiles.append(match.group(1))
    return subfiles


def replace_in_file(file_path, pattern, replacement):
    with open(file_path, 'r') as file:
        content = file.read()
    content = re.sub(pattern, replacement, content)
    with open(file_path, 'w') as file:
        file.write(content)


def convert_pgfs_to_svg(tex_file_path):
    with open(tex_file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        # Ignore lines that are commented out
        if line.strip().startswith('%'):
            continue

        # Find all \input commands
        match = re.search(r'\\input{([^}]+)}', line)
        # Find all \input commands ending in .pgf
        if match and match.group(1).endswith('.pgf'):
            pgf_file = match.group(1)
            if file_exists(pgf_file):
                print(f"Converting {pgf_file} to SVG")
                svg_file = 'web/' + pgf_file[:-4] + '.svg'

                with open(pgf_file, 'r') as input_tex_file:
                    input_content = input_tex_file.read()

                # Check if the input file contains a pgfpicture environment
                pgf_match = re.search(
                    r'\\begin{pgfpicture}.*?\\end{pgfpicture}',
                    input_content, re.DOTALL)
                if pgf_match:
                    print(f"Converting PGF in {pgf_file} to SVG")
                    pgf_content = pgf_match.group(0)
                    svg_file = ("web/pgf/"
                                + os.path.splitext(pgf_file)[0].split("/")[-1]
                                + '.svg')

                    # Replace the \input command with \includegraphics command
                    lines[i] = line.replace(
                        match.group(0),
                        f'\\includegraphics{{{svg_file}}}')

                    # Check if the SVG file already exists and is up-to-date
                    if (file_exists(svg_file) and
                            os.path.getmtime(svg_file) > os.path.getmtime(pgf_file)):
                        print(f"Skipping generation of {svg_file} as it is up-to-date.")
                        continue

                    # Write the pgf content to a temporary file
                    with open('TEMP_pgf.tex', 'w') as temp_file:
                        temp_file.write(pgf_doc_template_start)
                        temp_file.write("\\input{" + pgf_file + "}\n")
                        temp_file.write(pgf_doc_template_end)

                    # Convert the pgf content to SVG
                    subprocess.run(['xelatex', 'TEMP_pgf.tex'])
                    subprocess.run(['pdfcrop', 'TEMP_pgf.pdf', 'TEMP_pgf.pdf'])
                    subprocess.run(['pdf2svg', 'TEMP_pgf.pdf',
                                    svg_file])

    # Write the modified content back to the file
    with open(tex_file_path, 'w') as file:
        file.writelines(lines)

    # Clean up temporary files
    for file in ['TEMP_pgf.tex',
                 'TEMP_pgf.aux',
                 'TEMP_pgf.log',
                 'TEMP_pgf.out',
                 'TEMP_pgf.auxlock',
                 'TEMP_pgf.pdf']:
        if file_exists(file):
            os.remove(file)
pgf_doc_template_start = """
\\input{preamble.tex}
%\\tikzexternaldisable
\\pagestyle{empty}
\\begin{document}
"""
pgf_doc_template_end = """
\\end{document}
"""

def convert_pdfs_to_svgs(tex_file_path):
    with open(tex_file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        # Ignore lines that are commented out
        if line.strip().startswith('%'):
            continue

        # Find all \includegraphics commands
        match = re.search(r'\\includegraphics(?:\[[^\]]*\])?{([^}]+)}', line)
        if match:
            graphic = match.group(1)
            # Check if the graphic has a .pdf extension or if a .pdf file exists with the base name
            if graphic.endswith('.pdf'):
                pdf_file = graphic
            else:
                pdf_file = graphic + '.pdf'

            if file_exists(pdf_file):
                print(f"Converting {pdf_file} to SVG")
                if graphic.endswith('.pdf'):
                    svg_file = 'web/' + graphic[:-4] + '.svg'
                else:
                    svg_file = 'web/' + graphic + '.svg'

                # Replace the graphic reference in the line
                lines[i] = line.replace(graphic, svg_file)

                # Check if the SVG file already exists and is up-to-date
                if (file_exists(svg_file)
                        and os.path.getmtime(svg_file) > os.path.getmtime(pdf_file)):
                    print(f"Skipping generation of {svg_file} as it is up-to-date.")
                    continue

                subprocess.run(['pdf2svg',
                                pdf_file, svg_file])
                # scale_svg(svg_file, 1.5)

    # Write the modified content back to the file
    with open(tex_file_path, 'w') as file:
        file.writelines(lines)


def convert_tikz_to_svgs(tex_file_path):
    with open(tex_file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        # Ignore lines that are commented out
        if line.strip().startswith('%'):
            continue

        # Find all \input commands
        match = re.search(r'\\input{([^}]+)}', line)
        if match:
            input_file = match.group(1)
            if file_exists(input_file):
                with open(input_file, 'r') as input_tex_file:
                    input_content = input_tex_file.read()

                # Check if the input file contains a tikzpicture environment
                tikz_match = re.search(
                    r'\\begin{tikzpicture}.*?\\end{tikzpicture}',
                    input_content, re.DOTALL)
                if tikz_match:
                    print(f"Converting TikZ in {input_file} to SVG")
                    tikz_content = tikz_match.group(0)
                    svg_file = ("web/tikz/"
                                + os.path.splitext(input_file)[0].split("/")[-1]
                                + '.svg')

                    # Replace the \input command with \includegraphics command
                    lines[i] = line.replace(
                        match.group(0),
                        f'\\includegraphics{{{svg_file}}}')

                    # Check if the SVG file already exists and is up-to-date
                    if (file_exists(svg_file) and
                            os.path.getmtime(svg_file) > os.path.getmtime(input_file)):
                        print(f"Skipping generation of {svg_file} as it is up-to-date.")
                        continue

                    # Write the tikz content to a temporary file
                    with open('TEMP_tikz.tex', 'w') as temp_file:
                        temp_file.write(tikz_doc_template_start)
                        temp_file.write(tikz_content)
                        temp_file.write(tikz_doc_template_end)

                    # Convert the tikz content to SVG
                    subprocess.run(['xelatex', 'TEMP_tikz.tex'])
                    subprocess.run(['pdfcrop', 'TEMP_tikz.pdf', 'TEMP_tikz.pdf'])
                    subprocess.run(['pdf2svg', 'TEMP_tikz.pdf',
                                    svg_file])

    # Write the modified content back to the file
    with open(tex_file_path, 'w') as file:
        file.writelines(lines)

    # Clean up temporary files
    for file in ['TEMP_tikz.tex',
                 'TEMP_tikz.aux',
                 'TEMP_tikz.log',
                 'TEMP_tikz.out',
                 'TEMP_tikz.auxlock',
                 'TEMP_tikz.pdf']:
        if file_exists(file):
            os.remove(file)

def format_cref(refs):
    ref_list = [f'\\cref{{{ref.strip()}}}' for ref in refs.split(',')]
    if len(ref_list) == 1:
        return ref_list[0]
    elif len(ref_list) == 2:
        return ' and '.join(ref_list)
    else:
        return ', '.join(ref_list[:-1]) + ' and ' + ref_list[-1]

def convert_unsupported_latex_to_unicode(temp_subfile):
    # Step 1: Open the file in read mode
    with open(temp_subfile, 'r', encoding='utf-8') as file:
        # Step 2: Read the contents of the file
        content = file.read()

    # Step 3a: Replace all occurrences of \t{\sigma} with 𝞼
    content = content.replace(r'\t{\sigma}', '\\normalsize{𝞼}')
    content = content.replace(r'\stress', '\\normalsize{𝞼}')

    # Step 3b: Force italic capital Greek letters
    content = content.replace(r'\Gamma', r'\mathit{\Gamma}')
    content = content.replace(r'\Theta', r'\mathit{\Theta}')
    content = content.replace(r'\Phi', r'\mathit{\Phi}')

    # Step 3c: Remove intertext
    content = re.sub(r'\\intertext\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}', r'\\end{align}\1\\begin{align}', content)

    # Step 3d: Replace \SI{300}{km} with 300\,\mathrm{km} (works in text mode too)
    content = re.sub(r'\\SI\{(.*?)\}\{(.*?)\}', r'\1\\,\\mathrm{\2}', content)

    # Step 3e: Deal with multiple references inside cref
    content = re.sub(r'\\cref\{([^}]+)\}', lambda m: format_cref(m.group(1)), content)

    # Step 3f: Replace unsupported colours
    content = content.replace(r'\color{C0}', r'\color{blue}')
    content = content.replace(r'\color{C1}', r'\color{orange}')

    # Step 3g: Replace \raisebox{0.5cm}{\includegraphics{images/beach.pdf}} with \includegraphics{images/beach.pdf}
    content = re.sub(r'\\raisebox\{[^}]*\}\{\\includegraphics\{([^}]*)\}\}', r'\\includegraphics{\1}', content)

    # Step 3h: Remove trailing spaces from all lines
    content = re.sub(r'[ \t]+$$', '', content, flags=re.MULTILINE)

    # Step 3i: Replace \begin{subequations}\label{something}\begin{align} with \begin{align}\label{something}
    content = re.sub(r'\\begin\{subequations\}\n\\label\{([^}]+)\}\n\\begin\{align\}', r'\\begin{align}\\label{\1}', content)
    content = re.sub(r'\\begin\{subequations\}\\label\{([^}]+)\}\n\\begin\{align\}', r'\\begin{align}\\label{\1}', content)
    content = re.sub(r'\\begin\{subequations\}\\label\{([^}]+)\}%\n\\begin\{align\}', r'\\begin{align}\\label{\1}', content)
    content = re.sub(r'\\begin\{subequations\}\n\\begin\{align\}', r'\\begin{align}', content)
    content = re.sub(r'\\end\{align\}\n\\end\{subequations\}', r'\\end{align}', content)

    content = re.sub(r'\\begin\{equation\}\n\\begin\{aligned\}', r'\\begin{align}', content)
    content = re.sub(r'\\end\{aligned\}\n\\end\{equation\}', r'\\end{align}', content)


    # Step 3j: Replace aligned with align
    content = re.sub(r'\{aligned\}', r'\{align\}', content)

    # Step 3k: Replace \begin{info} with \begin{info-box}
    content = content.replace(r'\begin{info}', r'\begin{info-box}')
    content = content.replace(r'\end{info}', r'\end{info-box}')
    content = content.replace(r'\begin{nem}', r'\begin{nem-box}')
    content = content.replace(r'\end{nem}', r'\end{nem-box}')

    # Step 3l: Remove \allowbreak
    content = content.replace(r'\allowbreak', '')

    # Step 3l: Substitute banned symbols in labels
    bad_symbols = [' ', '=', '_', ':']
    replacement_symbols = ['-SP-', '-EQ-', '-US-', '-CL-']
    for bad_symbol, replacement_symbol in zip(bad_symbols, replacement_symbols):
        content = re.sub(r'\\label\{([^}]+)\}', lambda m: '\\label{' + m.group(1).replace(bad_symbol, replacement_symbol) + '}', content)
        content = re.sub(r'\\cref\{([^}]+)\}', lambda m: '\\cref{' + m.group(1).replace(bad_symbol, replacement_symbol) + '}', content)
        content = re.sub(r'\\Cref\{([^}]+)\}', lambda m: '\\Cref{' + m.group(1).replace(bad_symbol, replacement_symbol) + '}', content)
        content = re.sub(r'\\ref\{([^}]+)\}', lambda m: '\\ref{' + m.group(1).replace(bad_symbol, replacement_symbol) + '}', content)
        content = re.sub(r'\\eqref\{([^}]+)\}', lambda m: '\\cref{' + m.group(1).replace(bad_symbol, replacement_symbol) + '}', content)

    # Step 3m: Remove subfloats, so change \subfloat[$r=0.5$]{stuff} into just stuff
    content = re.sub(r'\\subfloat\[[^\]]*\]\{([^}]+)\}', r'\1', content)


    # Step 4: Open the file in write mode and write the updated content
    with open(temp_subfile, 'w', encoding='utf-8') as file:
        file.write(content)


def run_pandoc(temp_main_tex_path):
    subprocess.run(['pandoc', 'pandoc/overwrite_commands.tex',
                    temp_main_tex_path, '-d', 'pandoc/tex2html'])


def clean_up_temp_files(temp_files):
    for temp_file in temp_files:
        os.remove(temp_file)


tikz_doc_template_start = """
\\input{preamble.tex}
\\tikzexternaldisable
\\pagestyle{empty}
\\begin{document}
"""
tikz_doc_template_end = """
\\end{document}
"""


# 0. Make a temporary copy of main.tex --> TEMP_main.tex
main_tex_path = 'main.tex'
temp_main_tex_path = make_temp_copy(main_tex_path)

# 1. Find the tex subfiles listed in main.tex and make temporary copies of
#    them --> TEMP_xxx.tex. Edit TEMP_main.tex to include these files instead.
#    If no subfiles are found, process the main file itself.
subfiles = find_tex_subfiles(main_tex_path)
temp_subfiles = []
if subfiles:
    # Process subfiles
    for subfile in subfiles:
        temp_subfile_path = make_temp_copy(subfile + '.tex')
        temp_subfiles.append(temp_subfile_path)
        replace_in_file(temp_main_tex_path, subfile, f'TEMP_{subfile}')
else:
    # No subfiles found, process the main file itself
    temp_subfiles = [temp_main_tex_path]

# 2. For each tex subfile, find the PDFs and convert them to PNGs. Then,
#    replace the PDFs with the PNGs in the tex subfiles.
# 3. For each tex subfile, find the tikzpicture environments and convert them
#    to SVGs. Then, replace the tikzpicture environments with the SVGs in the
#    tex subfiles.
for temp_subfile in temp_subfiles:
    print("Processing", temp_subfile, "...")
    print("Converting PDFs to SVGs...")
    convert_pdfs_to_svgs(temp_subfile)
    print("Converting TikZ to SVGs...")
    convert_tikz_to_svgs(temp_subfile)
    print("Converting PGF to SVGs...")
    convert_pgfs_to_svg(temp_subfile)
    print("Converting unsupported LaTeX to Unicode...")
    convert_unsupported_latex_to_unicode(temp_subfile)

# 4. Run pandoc on TEMP_main.tex to generate the output file.
run_pandoc(temp_main_tex_path)

# 5. Clean up the temporary files.
print("Cleaning up temporary files...")
# Remove temp_main_tex_path from temp_subfiles if it's there to avoid duplicate deletion
files_to_clean = [temp_main_tex_path] + [f for f in temp_subfiles if f != temp_main_tex_path]
clean_up_temp_files(files_to_clean)
