def main():
    def permutList(l):
        if not l:
                return [[]]
        res = []
        for e in l:
                temp = l[:]
                temp.remove(e)
                res.extend([[e] + r for r in permutList(temp)])
        return res

    data = [1,1,2]
    new = []
    for i in permutList(data):
        if i not in new:
            new.append(i)
    print(new)
if __name__ == "__main__":
    main()