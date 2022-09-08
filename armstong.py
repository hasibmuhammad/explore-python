def isArmstrong(num):
    l = len(str(num))
    s = num
    sum = 0

    while num != 0:
        r = num % 10
        sum += r**l
        num = num // 10

    return sum == s

print(isArmstrong(153))