def main():
    s = input()
    def is_balance(s):
        opening = "([<{"
        closing = ")]>}"
        stack = []
        for char in s:
            if char in opening:
                stack.append(opening.index(char))
            elif char in closing:
                if stack and stack[-1] == closing.index(char):
                    stack.pop()
                else:
                    return False
        return (not stack)
    lis = []
    if is_balance(s):
        print("True")
        print(s)
    else:
        print("False")
        for i in range(0,len(s) + 1):
            for j in range(i,len(s) + 1):
                a = s[i:j]
                if is_balance(a):
                    lis.append(a)
        max_uniq_len = 0
        max_str = ""
        for str_ in lis:
            if len(str_) > max_uniq_len:
                max_str = str_
                max_uniq_len = len(str_)
        print(max_str)
if __name__ == "__main__":
    main()


