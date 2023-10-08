import math

def main():
    try:
        height = float(input('请输入身高(Unit: m): '))
        weight = float(input('请输入体重(Unit: kg): '))
        bmi = weight / pow(height,2)
        china = ''
        internation = ''
        # 国际标准
        if bmi < 18.5:
            internation = "偏瘦"
        elif 18.5 <= bmi < 25:
            internation = "正常"
        elif 25 <= bmi < 30:
            internation = "偏胖"
        elif bmi >= 30:
            internation = "肥胖"
        # 国内标准
        if bmi < 18.5:
            china = "偏瘦"
        elif 18.5 <= bmi < 24:
            china = "正常"
        elif 24 <= bmi < 28:
            china = "偏胖"
        elif bmi >= 28:
            china = "肥胖"
        print(f"BMI数值为: {round(bmi,2)}, BMI指标为: 国际'{internation}', 国内: '{china}'")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        main()