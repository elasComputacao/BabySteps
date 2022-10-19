while True:
    try:
        list1 = input().split()
        X, Y = list1
        print(int(X) ^ int(Y))
    except:
        break