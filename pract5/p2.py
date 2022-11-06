def main():
    lis = ['a', 'b', 'c','d','d' ]
    lis2 = [[]]
    for i in lis:

        for j in range(len(lis2)):
            buff_list = lis2[j].copy()
            buff_list.append(i)
            lis2.append(buff_list)
    lis2.pop(0)
    for idx, val in enumerate(lis2):
        lis2[idx] = set(val)
    print(lis2)
if __name__ == "__main__":
    main()

