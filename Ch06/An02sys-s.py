from sys import argv
import os

def ping(net, start=80, end=85, n=1, w=3):
    for x in range(start, end+1):
        ip = net + '.' + str(x)
        command = "ping %s -n %d -w %d"%(ip,n,w)
        print(ip,('通','不通')[os.system(command)])

def main():
    if len(argv) not in [2,4,6]:
        print('参数输入错误')
        print('An02sys-s.py 192.168.3')
        print('An02sys-s.py 192.168.3   70 80')
        print('An02sys-s.py 192.168.3   70 80 1 5')
    elif len(argv) == 2:
        net = argv[1]
        ping(net)
    elif len(argv) == 4:
        net = argv[1]
        ping(net,start=int(argv[2]),end=int(argv[3]))
    else:
        net = argv[1]
        ping(net,start=int(argv[2]),end=int(argv[3]),n=int(argv[4]),w=int(argv[5]))
    

if __name__ == '__main__':
    main()