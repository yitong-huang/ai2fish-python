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

