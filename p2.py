def func(str):
    print(str)
    integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    res = 0
    for i,val in enumerate(str):
        if i + 1 < len(str) and integers[str[i]] < integers[str[i + 1]] :
            res -= integers[str[i]]
        else:
            res += integers[str[i]]
    print(res)
func('IV')
func('IX')

