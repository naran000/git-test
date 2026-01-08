import re  # 必须添加这一行！
from pypinyin import pinyin, Style, lazy_pinyin

def uppercase_english(text):
    # 匹配所有 a-z 的字母并替换为大写
    return re.sub(r'[a-z]+', lambda m: m.group(0).upper(), text)

# 测试
test_text = "Python is 优秀的 programming language!"
print(uppercase_english(test_text))