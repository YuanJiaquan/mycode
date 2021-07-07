import openpyxl

# excel测试用例的读取与执行
excel = openpyxl.load_workbook('../case/api_cases.xlsx')
sheet = excel['Sheet1']

# CR7同学的excel读写方案
for value in sheet.values:
    if type(value[0]) is int:
        dict1 = {}
        list1 = ['url', 'headers', value[6]]
        list2 = [
            value[1] + value[2], value[4], value[5]
        ]
        count = 0
        for i in list2:
            if i:
                try:
                    dict1['{}'.format(list1[count])] = eval(i)
                except:
                    dict1['{}'.format(list1[count])] = i
            count += 1
        print(dict1)
