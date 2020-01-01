import sys
import json
import csv

def calculator(num):
    """计算税后薪资的函数，参数为原始收入"""

    # 应纳税所得额为收入减5000
    social_insurance_point = 0.08 + 0.02 + 0.005 + 0.06
    shouldPay = num*(1 - social_insurance_point) - 5000

    # 用条件判断语句，根据扣税表写出不同薪资的扣税公式
    if shouldPay <= 0:
        tax = 0
    elif 0 < shouldPay <= 3000:
        tax = shouldPay * 0.03
    elif 3000 < shouldPay <= 12000:
        tax = 3000 * 0.03 + (shouldPay-3000) * 0.10
    elif 12000 < shouldPay <= 25000:
        tax = 3000 * 0.03 + 9000 * 0.10 + (shouldPay-12000) * 0.20
    elif 25000 < shouldPay <= 35000:
        tax = 3000 * 0.03 + 9000 * 0.10 + 13000*0.20 + (shouldPay-25000) * 0.25
    elif 35000 < shouldPay <= 55000:
        tax = 3000 * 0.03 + 9000 * 0.10 + 13000*0.20 + 10000*0.25 +(shouldPay-35000) * 0.30
    elif 55000 < shouldPay <= 80000:
        tax = 3000 * 0.03 + 9000 * 0.10 + 13000*0.20 + 10000*0.25 + 20000*0.30 +(shouldPay-55000) * 0.35
    else:
        tax = 3000 * 0.03 + 9000 * 0.10 + 13000*0.20 + 10000*0.25 + 20000*0.30 + 25000 * 0.35 + (shouldPay-55000) * 0.45

    # 下面的请你补充


    # 最终收入为税前收入减去税款，并保留两位小数
    salary = num*(1 - social_insurance_point) - tax


    # 返回最终收入
    
    #return salary
    return '{:.2f}'.format(salary)

#print('你的税后收入是：{:.2f}'.format(calculator(income)))

def readfiletodict(file_name):
    # 读入csv文件，并将CSV文件转成数据字典
    '''
    with open(file_name,'r') as file:
        listfile = file.readlines()
    '''
    with open(file_name) as f:
        listfile=list(csv.reader(f))

    d1 = dict()
    
    for item in listfile :
        id = item[0]
        income = int(item[1])
        d1[id] = income
    return d1

def writetojsonfile(dica,json_filename):
    #将字典文件写入JSON文件
    with open(json_filename,'w') as f:
        json.dump(dica,f)




def main():
    read_file = sys.argv[1]
    write_file = sys.argv[2]
    
    usr_info = readfiletodict(read_file)
    usr_cal = {}

    print(usr_info)

    for id,income in usr_info.items():
        usr_cal[id] = calculator(int(income))

    writetojsonfile(usr_cal,write_file)




if __name__ == '__main__':
    main()


    """
    对命令行传入的每一个用户，依次调用计算器计算纳税额
    """
    # 循环处理每一个用户
'''
    for item in sys.argv[1:]:
        # 解析用户 ID 和工资
        id, income = item.split(':')
        try:
            income = int(income)
        except ValueError:
            print('请在薪资的位置输入数字')
            continue
        print('{}:{}'.format(id,calculator(income)))
'''
'''
    try:
    except:

        print('请首先输入读取文件的绝对位置，然后以空格为间隔输入要写入文件的绝对位置')    
'''

