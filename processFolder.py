import os
import subprocess
import argparse
from tqdm import tqdm


def process_folder(folder_path, pdf_flag, save_panels_flag):
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]

    for filename in tqdm(pdf_files, desc="Processing PDFs"):
        file_path = os.path.join(folder_path, filename)
        args = ["py.exe", "kumiko", "-i", file_path]
        if pdf_flag:
            args.append("--pdf")
        if save_panels_flag:
            args.append("-s")
        subprocess.run(args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process all PDFs in a folder")
    parser.add_argument("folder", type=str, help="Folder containing PDF files")
    parser.add_argument("--pdf", action="store_true", help="Indicates the input is a PDF file")
    parser.add_argument("-s", "--save-panels", action="store_true", help="Save detected panels as images")

    args = parser.parse_args()

    process_folder(args.folder, args.pdf, args.save_panels)
