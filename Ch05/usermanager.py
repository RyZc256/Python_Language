user = {'霍元甲': 'hyj',
        '陈真': 'cz',
        '霍东觉': 'hdj',
        '郭嘉': 'gj',
        '郭靖': 'gj',
        '黄蓉': 'gr',
        '东方不败': 'dfbb'}

def menu():
    while True:
        print('字典的使用———添加，删除，显示用户'.center(60,'-'))
        print('**** 1. 添加用户                 ****')
        print('**** 2. 删除用户                 ****')
        print('**** 3. 显示用户                 ****')
        print('**** 4. 退出                 ****')
        num = int(input('*** 请选择(0-3): '))
        if num == 1:
            addUser()
        elif num == 2:
            delUser()
        elif num == 3:
            displayUser()
        elif num == 4:
            exit()


def addUser():
    global user
    while True:
        name = input('请输入用户名: ')
        if name in user:
            print('用户名已存在')
        else:
            print('库中没有该用户，可以添加')
            password = input('请输入用户密码: ')
            user[name] = password
            flag = input('添加成功, 是否需要继续添加(Y继续, 其他退出): ')
            if flag.lower() != 'y':
                return None
            

def delUser():
    global user
    while True:
        name = input('请输入用户名: ')
        if name in user:
            flag = input('该用户存在，确定删除吗? (Y删除,其他退出): ')
            if flag.lower() != 'y':
                return None
            del user[name]
            flag = input('删除成功, 是否需要继续删除(Y继续, 其他退出): ')
            if flag.lower() != 'y':
                return None
        else:
            flag = input('库中没有该用户, 重试请按Y, 其他退出): ')
            if flag.lower() != 'y':
                return None

def displayUser():
    print('用户信息'.center(60))
    print('--------------------------------------')
    print(f'|   用户名  |   密码    |')
    for item in user:
        print(f'|   {item}  |   {user[item]}  |')
        print('--------------------------------------')
    a = input()

if __name__ == '__main__':
    menu()