import json
import os
from glob import glob

def split_ipynb_to_md_and_py(ipynb_file, output_dir=None):
    # 파일 경로와 이름 처리
    base_name = os.path.splitext(os.path.basename(ipynb_file))[0]
    output_dir = output_dir or os.path.dirname(ipynb_file)
    
    # 출력 디렉터리 생성 (없으면 생성)
    os.makedirs(output_dir, exist_ok=True)
    
    # 출력 파일 경로
    md_file = os.path.join(output_dir, f"{base_name}.md")
    py_file = os.path.join(output_dir, f"{base_name}.py")
    
    try:
        # .ipynb 파일 열기
        with open(ipynb_file, 'r', encoding='utf-8') as f:
            notebook_data = json.load(f)
        
        # 마크다운과 코드 셀 분리
        markdown_cells = []
        python_cells = []
        
        for cell in notebook_data.get("cells", []):
            if cell.get("cell_type") == "markdown":
                markdown_cells.append("".join(cell.get("source", [])))
            elif cell.get("cell_type") == "code":
                python_cells.append("".join(cell.get("source", [])))
        
        # .md 파일 저장
        if markdown_cells:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write("\n\n".join(markdown_cells))
            print(f"Markdown content saved to {md_file}")
        else:
            print(f"No Markdown content found in {ipynb_file}.")
        
        # .py 파일 저장
        if python_cells:
            with open(py_file, 'w', encoding='utf-8') as f:
                f.write("\n\n".join(python_cells))
            print(f"Python code saved to {py_file}")
        else:
            print(f"No Python code content found in {ipynb_file}.")
    
    except Exception as e:
        print(f"An error occurred with {ipynb_file}: {e}")

def process_multiple_ipynb_files(input_dir, output_dir=None):
    # 디렉터리 내 모든 .ipynb 파일 찾기
    ipynb_files = glob(os.path.join(input_dir, "*.ipynb"))
    
    if not ipynb_files:
        print("No .ipynb files found in the specified directory.")
        return
    
    # 각 파일 처리
    for ipynb_file in ipynb_files:
        print(f"Processing {ipynb_file}...")
        split_ipynb_to_md_and_py(ipynb_file, output_dir)
    print("Processing complete.")

# 예제 사용법
input_directory = "/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/notes"  # .ipynb 파일들이 위치한 디렉터리
output_directory = "/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/output_notes"  # 결과 파일을 저장할 디렉터리
process_multiple_ipynb_files(input_directory, output_directory)

