import os
import hashlib
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm  # 进度条库

def calculate_md5(file_path, block_size=8192):
    """计算文件的 MD5"""
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(block_size):
            md5.update(chunk)
    return md5.hexdigest()

def select_folder(title):
    """弹出文件夹选择对话框"""
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder = filedialog.askdirectory(title=title)
    return folder

# 选择源文件夹
source_dir = select_folder("选择源文件夹")
if not source_dir:
    print("❌ 未选择源文件夹，脚本终止。")
    exit()

# 选择目标文件夹
target_dir = select_folder("选择目标文件夹")
if not target_dir:
    print("❌ 未选择目标文件夹，脚本终止。")
    exit()

# 获取源文件夹的所有文件（用于进度条总数量）
all_files = []
for root, _, files in os.walk(source_dir):
    for file in files:
        all_files.append(os.path.join(root, file))

mismatched_files = []

print("🔍 正在比对文件 MD5，请稍候...")

# 使用 tqdm 显示进度条
for source_file in tqdm(all_files, desc="进度", unit="文件"):
    relative_path = os.path.relpath(source_file, source_dir)
    target_file = os.path.join(target_dir, relative_path)

    if os.path.exists(target_file):
        source_md5 = calculate_md5(source_file)
        target_md5 = calculate_md5(target_file)

        if source_md5 != target_md5:
            mismatched_files.append({
                "source_file": source_file,
                "target_file": target_file,
                "source_md5": source_md5,
                "target_md5": target_md5,
            })
    else:
        print(f"\n⚠️ 目标文件不存在: {target_file}")

# 输出结果
if mismatched_files:
    print("\n❌ 以下文件 MD5 不匹配:")
    for file in mismatched_files:
        print(f"源文件: {file['source_file']} (MD5: {file['source_md5']})")
        print(f"目标文件: {file['target_file']} (MD5: {file['target_md5']})")
        print("---")
else:
    print("\n✅ 所有文件 MD5 匹配！")