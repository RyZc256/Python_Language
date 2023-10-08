def main():
    x,y = 1,2
    print(x,y,type(x),id(x),x==y,x is y)
    name = ['刘老根', '谢大脚', '药厘子', '刘能', '宋小宝', '药来']
    yourname = input('请输入你的名字: ')
    if yourname in name:
        print('查询结果：名单中有你的名字'.center(30, '-'))
    else:
        print('查询结果：名单中没有你的名字'.center(30, '-'))
    a, b = 64, 64
    print(a>>2,b<<2)

if __name__ == '__main__':
    main()
