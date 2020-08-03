import re
import os
import pdfplumber


def process_file(directory, file_path):
    with pdfplumber.open(directory + file_path) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()

        text = "".join(text.split("\n")[4:])
        text = re.sub(r'\n', ' ', text)
        text = re.sub(r'  ', ' ', text)
        text = re.sub(r'\. ', '.\n\n', text)

        return text


directory = "./pdfs/"
file_name = "raw_text_lines"

with open(f"{file_name}.txt", 'w') as f:
    f.write("")

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        current_text = process_file(directory, filename)

        with open(f"{file_name}.txt", 'a') as f:
            f.write(current_text)
            # f.write("\n\n")
            # Ya quitando esto queda
