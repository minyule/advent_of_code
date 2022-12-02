import sys

sys.stdin = open("1_input.txt")

num = 1
res_num = 1
total_max = 0
one_sum = 0
sum_lst = []

while True:
    try:
        inp = input()

        if not inp:  # blank
            if total_max < one_sum:
                total_max = one_sum
                res_num = num
            sum_lst.append(one_sum)
            one_sum = 0
            num += 1

        else:  # not blank
            inp = int(inp)
            one_sum = one_sum + inp

    except EOFError:
        break

# part 1 - ans: 69177
print("Part 1: ", total_max)

# part 2 - ans: 207456
sum_lst.sort()
s = sum_lst[-1] + sum_lst[-2] + sum_lst[-3]
print("Part 2: ", s)