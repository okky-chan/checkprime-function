def primechecker(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is Not Prime.")
                break
        else:
            print(num, "is Prime.")
    else:
        print(num, "is Not Prime.")

num = int(input('Input: '))

primechecker(num)