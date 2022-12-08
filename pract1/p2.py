def main():
    s = int(input())
    s2 = str(s)
    r = s2[:-2:]
    if -2**7 <= s <= 2**7 - 1:
        print(r)
    else:
        print("no solution")
if __name__ == "__main__":
    main()
