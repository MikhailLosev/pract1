def main():
    s = str(input())
    r = s[::-1]
    if s == r:
        print('True')
    else:
        print("False")
if __name__ == "__main__":
    main()