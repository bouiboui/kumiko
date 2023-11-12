import os
import subprocess
import argparse
from tqdm import tqdm
from pathlib import Path


def process_folder(folder_path, pdf_flag, save_panels_flag):
    folder = Path(folder_path)
    pdf_files = folder.glob('*.pdf')

    for pdf_file in tqdm(pdf_files, desc="Processing PDFs"):
        output_file = folder / f"{pdf_file.stem}_panel_0.jpg"  # Example output file check
        if not output_file.exists():
            args = ["py.exe", "kumiko", "-i", str(pdf_file)]
            if pdf_flag:
                args.append("--pdf")
            if save_panels_flag:
                args.append("-s")
            subprocess.run(args)
        else:
            print(f"Skipping {pdf_file} as output already exists.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process all PDFs in a folder")
    parser.add_argument("folder", type=str, help="Folder containing PDF files")
    parser.add_argument("--pdf", action="store_true", help="Indicates the input is a PDF file")
    parser.add_argument("-s", "--save-panels", action="store_true", help="Save detected panels as images")

    args = parser.parse_args()

    process_folder(args.folder, args.pdf, args.save_panels)
