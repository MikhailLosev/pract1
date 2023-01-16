def groupify(strs:list)->list:
    dict_ = {}

    for i in strs:
        if len(i) not in dict_:
            dict_[len(i)] = list()
        dict_[len(i)].append(i)

    res = list()
    for k in dict_.keys():
        words = dict_[k]
        buff = list()
        if len(words) == 1:
            res.append(words)
            next
        for idx_1, word_1 in enumerate(words):
            is_kernel = True
            if len(res) > 0:
                for class_ in res:
                    if sorted(list(word_1)) == sorted(list(class_[0])):
                        is_kernel = False
            if is_kernel:
                buff.append(word_1)
                for idx, word_2 in enumerate(words[idx_1 + 1:len(words)]):
                    if sorted(list(word_1)) == sorted(list(word_2)):
                        buff.append(word_2)

                res.append(buff)
                buff = list()
    return res

def main():
    # strs = ['qwe','ewq','asd','dsa','dsas','qwee','zxc','cxz','xxz','z','s','qweasdzxc','zzxc']
    strs = str(input())#qwe ewq asd dsa dsas qwee zxc cxz xxz z s qweasdzxc zzxc
    strs = strs.strip()
    strs = strs.split()
    print(groupify(strs))
if __name__ == "__main__":
    main()
