import operator
import math

def professional_calculator():
    # 定义运算符映射
    # 对于单操作数运算，我们统一使用 lambda 接收两个参数，但忽略第二个
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "**": operator.pow,          # 幂运算 (x的y次方)
        "sqrt": lambda x, _: math.sqrt(x),  # 开平方 (忽略第二个参数)
        "log": lambda x, y: math.log(x, y if y else 10), # 对数 (默认以10为底)
        "sin": lambda x, _: math.sin(math.radians(x)),  # 正弦 (角度转弧度)
    }

    print("--- 增强版 Python 计算器 ---")
    print("支持: +, -, *, /, **(幂), sqrt(开方), log(对数), sin(正弦)")
    print("注：对于 sqrt 和 sin，只需在'数字2'处随便输入一个数或直接回车即可。")
    print("-" * 30)

    try:
        n1 = float(input("数字1: "))
        action = input("运算符: ").lower().strip()
        
        # 某些运算可能不需要第二个数字
        if action in ['sqrt', 'sin']:
            n2 = 0 # 占位符
        else:
            n2 = float(input("数字2: "))

        if action in ops:
            # 特殊情况处理
            if action == "/" and n2 == 0:
                print("抱歉，数学上不能除以零。")
            elif action == "sqrt" and n1 < 0:
                print("错误：负数不能开平方！")
            elif action == "log" and n1 <= 0:
                print("错误：对数的真数必须大于零！")
            else:
                result = ops[action](n1, n2)
                print(f"结果: {result}")
        else:
            print("不支持的运算符。")
            
    except ValueError:
        print("输入有误，请输入数字。")
    except Exception as e:
        print(f"发生错误: {e}")

# 运行
professional_calculator()