import os

def display(dir_path):
    print("目录内容：")
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            print(f"父目录：{dir_path}")
            print(f"目录：{item}")
        else:
            print(f"文件：{item}")

if __name__ == '__main__':
    dir_path = r"C:\Users\horizon\Desktop\Work\Python"
    display(dir_path)
