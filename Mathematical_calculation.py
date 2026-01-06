import operator

def professional_calculator():
    # 定义运算符映射
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    try:
        n1 = float(input("数字1: "))
        action = input("运算符 (+, -, *, /): ")
        n2 = float(input("数字2: "))

        if action in ops:
            if action == "/" and n2 == 0:
                print("抱歉，数学上不能除以零。")
            else:
                result = ops[action](n1, n2)
                print(f"结果: {result}")
        else:
            print("不支持的运算符。")
            
    except ValueError:
        print("输入有误，请输入数字。")

professional_calculator()