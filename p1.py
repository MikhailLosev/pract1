def santa_users(lis1):
    dict1 = {}
    for i in lis1:
        if len(i) == 1:
            dict1[i[0]] = None
        else:
            dict1[i[0]] = i[1]
    print(dict1)
lis1 = [["name1 surname2",12345],["name2 surname2"],["name3 surname3",12354],["name4 surname4",12435]]
santa_users(lis1)

