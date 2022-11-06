def main():
    s = str(input())
    a = s.split()
    a.reverse()
    res = " ".join(a)
    b = res.capitalize()
    while b.find('  ') != -1:
        b = b.replace('  ', ' ')
    print(b)
if __name__ == "__main__":
    main()

