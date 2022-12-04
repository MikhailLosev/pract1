def main():
    list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    ans_1 = []
    ans_2 = []
    list1_1 = list1.copy()
    list1_2 = list2.copy()
    for i in list1:
        if i in list2:
            ans_1.append(i)
    for i in list1:
        if i not in list2:
            ans_2.append(i)
    for i in list2:
        if i not in list1:
            ans_2.append(i)
    for i in list1:
        if i in list2:
            list1_1.remove(i)
    ans_3 = list1_1
    for i in list2:
        if i in list1:
            list1_2.remove(i)
    ans_4 = list1_2
    print(ans_1, ans_2, ans_3, ans_4)
if __name__ == "__main__":
    main()
