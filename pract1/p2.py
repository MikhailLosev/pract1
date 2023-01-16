def main():
    s = input()
    s2 = ""
    for i in range(len(s)-1,-1,-1):
        s2 = s2 + s[i]
    if int(s) <0:
        s2 = '-'+ s2[:len(s2)-1]

    if -128<int(s2)<127:
        print(int(s2))
    else:
        print("no solution")
if __name__ == "__main__":
    main()

