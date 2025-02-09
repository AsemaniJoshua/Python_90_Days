from flask import Flask, render_template, request
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge_pdfs')
def merge_pdfs():
    actual_work()
    return render_template('results.html')


def select_pdfs():
    # Open a file dialog to select multiple PDF files
    files = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])
    return files

def merge_pdfs(pdf_files, output_path):
    # Create a PdfMerger object
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    # Write the merged PDF to the output path
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print(f"PDFs merged successfully into {output_path}")

def actual_work():
    # Create the root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Select PDF files
    pdf_files = select_pdfs()

    if pdf_files:
        # Ask the user for the name of the merged PDF
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if output_path:
            merge_pdfs(pdf_files, output_path)
if __name__ == '__main__':
    app.run(debug=True)