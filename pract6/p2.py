def main(str_:str)->int:
    print(str_)
    integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    res = 0
    for i,val in enumerate(str_):
        if i + 1 < len(str_) and integers[str_[i]] < integers[str_[i + 1]] :
            res -= integers[str_[i]]
        else:
            res += integers[str_[i]]
    return res


if __name__ == "__main__":
    str_ = str(input())
    print(main(str_)) # IV IX
