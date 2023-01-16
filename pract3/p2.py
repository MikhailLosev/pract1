import itertools
def func(list:list)->set:
    list2 = []
    res = itertools.permutations(list)
    for i in res:
        list2.append(i)
    return set(list2)

def main():
    list = [1,1,2]
    
    print(func(list))
if __name__ == "__main__":
    main()
