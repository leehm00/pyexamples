# _*_ coding.utf-8 _*_
# 开发人员 : leehm
# 开发时间 : 2020/7/12 17:18
# 文件名称 : 154.py
# 开发工具 : PyCharm
while True:
    n = input()
    if n == "0":
        break
    dp = [0 for i in range(len(n) + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(n) + 1):
        if 0 < int(n[i - 2] + n[i - 1]) <= 26 and n[i - 2] != "0":
            if n[i - 1] == "0":
                dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        elif n[i - 1] != "0":
            dp[i] = dp[i - 1]
    print(dp[-1])
