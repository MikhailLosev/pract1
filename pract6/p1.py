def santa_users(lis1:list)->dict:
        dict1 = {}
        for i in lis1:
            if len(i) == 1:
                dict1[i[0]] = None
            else:
                dict1[i[0]] = i[1]
        return dict1

def main():
    lis1 = [["name1 surname2",12345],["name2 surname2"],["name3 surname3",12354],["name4 surname4",12435]]
    print(santa_users(lis1))

if __name__ == "__main__":
    main()

