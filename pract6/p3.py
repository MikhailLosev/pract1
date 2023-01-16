from itertools import combinations

def get_pins(str_: str) -> list:
    lis1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [None, 0, None]]
    lis_res = []
    for k in str_:
        for idx_i, val_i in enumerate(lis1):
            for idx_j, val_j in enumerate(val_i):
                if str(val_j) in k:
                    lis_res.append(val_j)
                    if idx_j != 2 :
                        lis_res.append(lis1[idx_i][idx_j + 1])
                    if idx_j != 0 :
                        lis_res.append(lis1[idx_i][idx_j - 1])
                    if idx_i != 3:
                        lis_res.append(lis1[idx_i + 1][idx_j])
                    if idx_i != 0:
                        lis_res.append(lis1[idx_i - 1][idx_j])
    result = list(set(list(combinations(lis_res, len(str_)))))
    return result
def main():
    str_ = str(input())
    print(get_pins(str_))
if __name__ == "__main__":
    main()



