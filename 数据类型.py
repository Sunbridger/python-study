

# print(2j) 2j
# print(k) NameError: name 'k' is not defined

print(True)
print(False)
print(type(True))
print(type(False))

if type(False) == "<type 'bool'>":
    print(111)
else:
    print(0)
import os
import time

print('asdasd按时间按手动滑稽')
def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

# main()


print(__name__)
