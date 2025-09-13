# import re
#
# pattern = r'[A-Z]{2,}|[a-z]{2,}\w*'
#
# test_words = ["UCX", "AM", "PM", "hello", "University", "Programming", "ABc", "abC", "123Test", "_test"]
#
# for word in test_words:
#     if re.match(pattern, word):
#         print(f"accept: {word}")
#     else:
#         print(f"refuse: {word}")
#
#
# s = "print('hello world') # print"
# pattern = r'#.*$'
# print(re.sub(pattern, '', s))

# regular expression

import re

# s = "my tel is 180-1234-1234"
#
# print(re.search(r'\d{3}-\d{4}-\d{4}', s))
#
# s1 = "my tel is 1238 xxy"
#
# print(re.findall(r'1\d?8', s1))

# \d	匹配任意数字，等价于 [0-9]
# \w	匹配任意字母、数字、下划线，等价于 [a-zA-Z0-9_]
# {m}	匹配前面的字符 刚好 m 次
# {m, }	匹配前面的字符 m次 或以上
# {m, n}	匹配前面的字符 m 到 n 次
# *	匹配前面的字符0次或多次（尽可能多）
# +	匹配前面的字符1次或多次（尽可能多）
# ?	匹配前面的字符0次或1次




# 1
import re

pattern = r"[A-Z]{2,}|[a-z]{2,}\w*"
test_words = ["UCX", "AM", "PM", "hello", "University", "Programming", "ABc", "abC", "123Test", "_test"]
for word in test_words:   # asdf
    if re.match(pattern, word):
        print(f"accept: {word}")
    else:
        print(f"reject: {word}")


# 2
import re
pattern = r'#.*$'
try:
    with open("test.py") as f:
        for line in f:
            removed_comment = re.sub(pattern, "", line)
            print(removed_comment)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission error")
except Exception as e:
    print("Something went wrong", e)

# 3
import re
pattern = r"[A-Za-z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"

try:
    with open("email.txt") as f:
        for line in f:
            if re.match(pattern, line):
                print(line)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission error")
except Exception as e:
    print("Something went wrong", e)


# 4
import re
pattern = r'\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s](\d{4})'

mobiles = ['(415)555-1212', '510-778-1234', '408 555 4321', '650.444.1213']
for mobile in mobiles:
    match = re.search(pattern, mobile)
    print(match.groups())
    standardized_mobile = '-'.join(match.groups())
    # standardized_mobile = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    print(standardized_mobile)

print("huang")

#  5 * (1 + (2 + 3 + (1 - 2)))
