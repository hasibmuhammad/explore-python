def isArmstrong(num):
    l = len(str(num))
    s = num
    sum = 0

    while num != 0:
        r = num % 10
        sum += r**l
        num = num // 10

    if sum == s:
        return True
    else:
        return False

print(isArmstrong(153))