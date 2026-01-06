from pypinyin import pinyin, Style, lazy_pinyin


def name_to_pinyin(name):
    # 1. 普通风格（带声调）：如 [ ['zhāng'], ['sān'] ]
    pinyin_with_tone = pinyin(name)

    # 2. 姓名风格（不带声调）：如 'Zhang San'
    # heteronym=True 可以开启多音字模式，这里使用 lazy_pinyin 转换为列表
    pinyin_list = lazy_pinyin(name, style=Style.NORMAL)

    # 将首字母大写并拼接，符合通用姓名格式
    standard_name = " ".join([p.capitalize() for p in pinyin_list])

    # 3. 电子邮箱/护照格式：如 'ZHANG SAN'
    passport_name = "".join(pinyin_list).upper()

    return {
        "原名": name,
        "通用格式": standard_name,
        "护照格式": passport_name,
        "带声调": " ".join([i[0] for i in pinyin_with_tone])
    }


# 测试
test_name = "张三"
result = name_to_pinyin(test_name)

for key, value in result.items():
    print(f"{key}: {value}")