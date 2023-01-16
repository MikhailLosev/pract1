from itertools import permutations

def find_closest_sum(numbers:list, target_n:int)->int:
        n = 4
        target = numbers[target_n]
        permlist = list(permutations(numbers, n))
        sumlist = [sum(l) for l in permlist]
        maxpos = 0
        for i in range(1, len(sumlist)):
            if abs(sumlist[i] - target) < abs(sumlist[maxpos] - target):
                maxpos = i

        return permlist[maxpos]
    
def main():
    numbers = str(input())
    numbers = numbers.strip()
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    target = int(input())
    result_shown = find_closest_sum(numbers, target)
    print(result_shown)
    print(numbers[target])
    
if __name__ == "__main__":
    main()
