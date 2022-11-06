def funcName(list1,list2):
    ans_1 = list()
    for i in list1:
        if i in list2:
            ans_1.append(i)
    ans_2 = list()
    for i in list1:
        if i not in list2:
            ans_2.append(i)
    for i in list2:
        if i not in list1:
            ans_2.append(i)
    ans_3 = list1.copy()

    for i in list2:
        if i in ans_3:
            ans_3.remove(i)
    ans_4 = list2.copy()
    for i in list1:
        if i in ans_4:
            ans_4.remove(i)
    return [ans_1, ans_2, ans_3, ans_4]
if __name__ == "__main__":
    list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
    print(funcName(list1, list2))