import json

def main():
    # 提示用户输入用户名
    username = input("请输入用户名: ")

    # 读取json文件
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)

    # 检查用户名是否已经存在
    if username in users:
        print("该用户名已经存在！")
    else:
        # 提示用户输入密码
        password = input("请输入密码: ")

        # 将用户名和密码以json格式存入文件
        users[username] = password
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(users, f)
        print("已经成功注册！")

if __name__ == '__main__':
    main()