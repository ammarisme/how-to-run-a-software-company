from docx import Document
import os

def merge_docx_files(input_files, output_file):
    merged_document = Document()

    for file in input_files:
        doc = Document(file)
        for element in doc.element.body:
            merged_document.element.body.append(element)

    merged_document.save(output_file)
    return output_file

# List of DOCX files to merge
files_to_merge = os.listdir() # Add your files here

# Merge DOCX files into one
merged_file = 'merged_document.docx'
merge_docx_files(files_to_merge, merged_file)
print(f"Merged files successfully into {merged_file}")
