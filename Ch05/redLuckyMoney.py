import random

def main():
    people = inputPeople()
    money = inputMoney()
    moneys = rndMoney(money,people)
    print('红包如下'.center(60,'-'),'\n',moneys)



def rndMoney(money, people):
    moneys = []
    sum = 0
    for i in range(people):
        while True:
            try:
                single = round(random.uniform(0.1, (money - sum) - (people - i)), 2)
                assert 0<=single<=(3*money/people)
                break
            except:
                pass
        moneys.append(single)
        sum = single + sum
    return moneys


def inputPeople():
    while True:
        try:
            people = int(input('请输入抢红包的人数(1-100): '))
            assert 1<=people<=100
            break
        except:
            print('输入错误')
    return people


def inputMoney():
    while True:
        try:
            money = int(input('请输入你包红包的总金额(1-200): '))
            assert 1<=money<=200
            break
        except:
            print('输入错误')
    return money


if __name__ == '__main__':
    main()
    