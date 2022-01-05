import re
# # findall 匹配正则中所有的复合正则的内容
# lst = re.findall(r"\d+", "我的电话号码是：10086，他的是10010")
# print(lst)

# # finditer: 匹配字符串中所有的内容（返回的是迭代器），从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+", "我的电话号码是：10086，他的是10010")
# for i in it:
#     print(i.group())

# # search 全文匹配，找到一个结果就返回，返回的结果是迭代器对象，拿到数据需要.group()
# s = re.search(r"\d+", "我的电话号码是：10086，他的是10010")
# print(s.group())

# # match 从头匹配，找到一个结果就返回，返回的结果是迭代器对象，拿到数据需要.group()
# s = re.match(r"\d+", "10086，他的是10010")
# print(s.group())

# # 预加载正则表达式
# obj = re.compile(r"\d+")
# ret = obj.finditer("我的电话号码是：10086，他的是10010")
# for i in ret:
#     print(i.group())

s = """
<div class="ls"><span id="1">范哲思</span></div>
<div class="lss"><span id="2">张若雨</span></div>
<div class="lsss"><span id="3">你好啊</span></div>
<div class="lssss"><span id="4">python</span></div>
"""
obj = re.compile(
    r"<div class=\"(?P<res1>.*?)\"><span id=\"(?P<res2>\d+)\">(?P<res3>.*?)</span></div>", re.S)  # re.S 让.能匹配换行符

result = obj.finditer(s)
for i in result:
    print(i.group("res1", "res2", "res3"))
