def main():
    s = str(input("Введите строку:"))
    buff_str = ""
    uniq_strs = []
    for char in s:
        if char in buff_str:
            uniq_strs.append(buff_str)
            buff_str = ""
            buff_str += char
        else:
            buff_str = buff_str + char
    uniq_strs.append(buff_str)

    max_uniq_len = 0
    for str_ in uniq_strs:
        if len(str_) > max_uniq_len:
            max_str = str_
            max_uniq_len = len(str_)
    print(max_str)
if __name__ == "__main__":
    main()
