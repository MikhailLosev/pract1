from datetime import datetime
import time


def cell_is_free(x: int, y: int, old_fig_arr: list, new_fig_arr: list) -> bool:
    return (x, y) not in (old_fig_arr + new_fig_arr)


def cell_is_attacked(x: int, y: int, old_fig_arr: list, new_fig_arr: list) -> bool:
    attack_mod_delta_x = (0, 1, 2, 3)
    attack_mod_delta_y = (0, 1, 2, 3)
    l = []
    for fig in (old_fig_arr + new_fig_arr):
        flag = False
        mod_delta_x = abs(fig[0] - x)
        mod_delta_y = abs(fig[1] - y)
        if (
                mod_delta_x == 1 and mod_delta_y == 1) or (
                mod_delta_x == 0 and mod_delta_y == 2) or (
                mod_delta_x == 2 and mod_delta_y == 0) or (
                mod_delta_x == 3 and mod_delta_y in [
            1, 2, 3]) or (
                mod_delta_x in [
            1, 2, 3] and mod_delta_y == 3) or (
                mod_delta_x == 2 and mod_delta_y == 2):
            flag = False
        elif (mod_delta_x in attack_mod_delta_x
              and mod_delta_y in attack_mod_delta_y):
            flag = True
        l.append(flag)
    if True in l:
        return True
    else:
        return False


def cell_is_good(x: int, y: int, old_fig_arr: list, new_fig_arr: list) -> bool:
    return cell_is_free(x, y, old_fig_arr, new_fig_arr) \
           and not cell_is_attacked(x, y, old_fig_arr, new_fig_arr)


def get_new_fig_arr(n: int, new_fig_count: int, old_fig_arr: list) -> list:
    new_fig_arr = []

    for y in range(n):
        for x in range(n):
            if cell_is_good(x, y, old_fig_arr, new_fig_arr):
                new_fig_arr.append((x, y))

                if len(new_fig_arr) == new_fig_count:
                    return new_fig_arr
    return None


def good_move_last_new_fig(n: int, old_fig_arr: list, new_fig_arr: list) -> bool:
    last_x, last_y = new_fig_arr.pop()

    for y in range(last_y, n):
        for x in range(n):
            if y > last_y or x > last_x:
                if cell_is_good(x, y, old_fig_arr, new_fig_arr):
                    new_fig_arr.append((x, y))
                    return True
    return False


def good_complete_new_fig_arr(n: int, new_fig_count: int, old_fig_arr: list, new_fig_arr: list) -> bool:
    last_x, last_y = new_fig_arr[-1]
    added_fig_arr = []

    for y in range(last_y, n):
        for x in range(n):
            if y > last_y or x > last_x:
                if cell_is_good(
                        x,
                        y,
                        old_fig_arr,
                        new_fig_arr + added_fig_arr):
                    added_fig_arr.append((x, y))
                    if len(new_fig_arr + added_fig_arr) == new_fig_count:
                        new_fig_arr += added_fig_arr
                        # print(new_fig_arr)
                        return True
    return False


def good_move_new_figures(n: int, new_fig_count: int, old_fig_arr: list, new_fig_arr: list) -> bool:
    while True:
        while not good_move_last_new_fig(n, old_fig_arr, new_fig_arr):
            if len(new_fig_arr) == 0:
                return False

        if len(new_fig_arr) == new_fig_count or good_complete_new_fig_arr(
                n, new_fig_count, old_fig_arr, new_fig_arr):
            return True


def print_variant(n: int, old_fig_arr: list, new_fig_arr: list) -> None:
    for y in range(n):
        s = ""
        for x in range(n):
            if (x, y) in old_fig_arr:
                s += 'O '
            elif (x, y) in new_fig_arr:
                s += 'n '
            elif cell_is_attacked(x, y, old_fig_arr, new_fig_arr):
                s += '# '
            else:
                s += '- '
        print(s)
    print('\n')


def count_variants(n: int, new_fig_count: int, old_fig_arr: list) -> int:
    new_list = []
    res = 0
    new_fig_arr = get_new_fig_arr(n, new_fig_count, old_fig_arr)

    if new_fig_count == 0:
        print_variant(n, old_fig_arr, old_fig_arr)
        res += 1

    if new_fig_arr:
        if res == 0:
            print_variant(n, old_fig_arr, new_fig_arr)
        res += 1
        for line in (old_fig_arr + new_fig_arr):
            new_list.append('(' + str(line[0]) + ',' + str(line[1]) + '),')
        new_list.append('\n')
        while good_move_new_figures(n, new_fig_count, old_fig_arr, new_fig_arr):
            res += 1
            if new_fig_arr == [(3, 2), (4, 4)]:
                print_variant(n, old_fig_arr, new_fig_arr)
            for line in (old_fig_arr + new_fig_arr):
                new_list.append('(' + str(line[0]) + ', ' + str(line[1]) + ') ')
            new_list.append('\n')
        new_list[-1] = new_list[-1][0:-2]
    if res == 0:
        new_list.append('No solution')
    with open(r"output.txt", "w") as file:
        for line in (new_list):
            file.write(line)
        file.close()
    return res


'''Получаем переменные из файла'''


def get_data_from_file(filename: str) -> tuple:
    flag = True
    old_fig_arr = []
    with open(filename, "r") as file1:
        for line in file1:

            if flag:
                n = int(line.strip().split(' ')[0])
                l = int(line.strip().split(' ')[1])
                k = int(line.strip().split(' ')[2])
                flag = False
            elif flag == False:
                a = line.strip().split(' ')
                a = [int(item) for item in a]
                old_fig_arr.append(tuple(a))
        file1.close()
    return n, l, k, old_fig_arr


def main():
    n, l, k, old_fig_arr = get_data_from_file("p2.txt")
    # print(n, l, k, old_fig_arr)

    print("Размер доски: ", n, " ,Нужно поставить фигур: ", l, " ,Уже стоят фигур: ", len(old_fig_arr), "\n",)
    start_time = time.time()
    print()
    res = count_variants(n, l, old_fig_arr)
    print("Количество решений: ", res)

    print("Время работы: ", (time.time() - start_time))


if __name__ == "__main__":
    main()
