import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            # 遍历所有页面
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def scan_folder_for_pdfs(folder_path):
    pdf_files = []
    # 遍历目录，收集所有 PDF 文件路径
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            # 遍历所有页面
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def scan_folder_for_pdfs(folder_path):
    pdf_files = []
    # 遍历目录，收集所有 PDF 文件路径
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

if __name__ == "__main__":
    # 指定你要扫描的文件夹路径
    folder_path = r"C:\Users\54101\OneDrive\Desktop\ALY6010"
    
    # 获取所有 PDF 文件路径
    pdf_files = scan_folder_for_pdfs(folder_path)
    print(f"Found {len(pdf_files)} PDF files.")
    
    # 遍历每个 PDF 文件，提取并打印文本
    for pdf_file in pdf_files:
        print(f"Extracting text from: {pdf_file}")
        text = extract_text_from_pdf(pdf_file)
        print(f"--- Begin of {pdf_file} ---")
        print(text[:500])  # 打印前 500 个字符作为示例
        print(f"--- End of {pdf_file} ---\n")
    pdf_files = scan_folder_for_pdfs(folder_path)
    print(f"Found {len(pdf_files)} PDF files.")
    
    # 遍历每个 PDF 文件，提取并打印文本
    for pdf_file in pdf_files:
        print(f"Extracting text from: {pdf_file}")
        text = extract_text_from_pdf(pdf_file)
        print(f"--- Begin of {pdf_file} ---")
        print(text[:500])  # 打印前 500 个字符作为示例
        print(f"--- End of {pdf_file} ---\n")