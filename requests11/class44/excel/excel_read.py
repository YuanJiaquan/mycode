from class42.api_keyword.api_key import ApiKey
import openpyxl

# excel测试用例的读取与执行
excel = openpyxl.load_workbook('../case/api_cases.xlsx')
sheet = excel['Sheet1']
ak = ApiKey()
for value in sheet.values:
    # 接口测试咒语：准备数据——模拟请求——校验结果
    if type(value[0]) is int:
        # 准备测试数据
        data = value[5]
        assert_value = value[7]
        expect_value = value[8]
        if value[4]:
            if value[5]:
                dict_data = {
                    'url': value[1] + value[2],
                    'headers': eval(value[4]),
                    value[6]: eval(data)
                }
            else:
                dict_data = {
                    'url': value[1] + value[2],
                    'headers': eval(value[4])
                }
        else:
            if value[5]:
                dict_data = {
                    'url': value[1] + value[2],
                    value[6]: eval(data)
                }
            else:
                dict_data = {
                    'url': value[1] + value[2]
                }
        # print(dict_data)
        # # 模拟请求
        res = getattr(ak, value[3])(**dict_data)
        '''
            常规传递参数
            request.get(name="",
                        value="",
                        json="")
            如果接口封装时，参数做了**kwargs的处理，可以直接通过字典传递
            dict = {name:123,
                    value:234,
                    json:45645}
            request.get(dict)等同于常规传递行为
        '''
        # # 校验结果
        result = ak.get_text(res.text, assert_value)
        print(ak.assert_text(result, expect_value))
