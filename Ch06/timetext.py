import time

def main():
    width = 50
    print('开始执行'.center(width//2,'-'))
    start = time.perf_counter()
    for i in range(width + 1):
        finished = '*' * i
        unfinished = '.' * (width - i)
        percent = (i / width) * 100
        runtime = time.perf_counter() - start
        print('\r{:^3.0f}%[{}->{}]{:.2f}秒'.format(percent,finished,unfinished,runtime),end=' '),
        time.sleep(0.1)
    print('\n' + '执行结束'.center(width//2,'-'))

if __name__ == '__main__':
    main()