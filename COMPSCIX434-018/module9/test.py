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

s = "my tel is 180-1234-1234"

print(re.search(r'\d{3}-\d{4}-\d{4}', s))

s1 = "my tel is 1238 xxy"

print(re.findall(r'1\d?8', s1))

# \d	匹配任意数字，等价于 [0-9]
# \w	匹配任意字母、数字、下划线，等价于 [a-zA-Z0-9_]
# {m}	匹配前面的字符 刚好 m 次
# {m, }	匹配前面的字符 m次 或以上
# {m, n}	匹配前面的字符 m 到 n 次
# *	匹配前面的字符0次或多次（尽可能多）
# +	匹配前面的字符1次或多次（尽可能多）
# ?	匹配前面的字符0次或1次