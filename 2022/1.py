import sys

sys.stdin = open("1_input.txt")

num = 1
res_num = 1
total_max = 0
one_sum = 0

while True:
    try:
        inp = input()

        if not inp:  # blank
            if total_max < one_sum:
                total_max = one_sum
                res_num = num
            one_sum = 0
            num += 1

        else:  # not blank
            inp = int(inp)
            one_sum = one_sum + inp

    except EOFError:
        break

print(total_max, res_num)
