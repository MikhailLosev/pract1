def main():
    n = int(input())
    in_str = str(input())

    lst = []
    banks = []
    in_str = in_str.split()
    for str_ in in_str:
        lst.append(int(str_.split(',')[1]))
        banks.append(str_.split(',')[0])


    dp = [0] * len(lst)
    names = [0] * n

    dp[0] = lst[0]

    names[0] = [0]
    cnt = 1
    if (n > 1):
        dp[1] = max(lst[0], lst[1])
        if lst[0] > lst[1]:
            names[1] = [0]
        else:
            names[1] = [1]
        cnt = 2
        for i in range(2, len(lst)):
            dp[i] = max(dp[i - 1], dp[i - 2] + lst[i])
            if (dp[i - 2] + lst[i]) > dp[i - 1]:
                cnt += 1
                names[i] = names[i - 2]
                names[i].append(i)

    print('Сумма: ', dp[-1])
    for i in names[cnt - 1]:
        print(banks[i], lst[i])

    # input : 2
    # input : sber,10 tin,5
if __name__ == "__main__":
    main()



