

def cal_xk():
    x = user_xk[0]
    y = user_expression

    if eval(y) == user_xk[1]:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    user_xk = list(map(int, input().lstrip().split()))
    user_expression = str(input())
    cal_xk() 