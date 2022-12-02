import sys

sys.stdin = open("2_input.txt")

ans = 0

dic_me = {"X": 1, "Y": 2, "Z": 3}
dic_you = {"A": 1, "B": 2, "C": 3}

dic_2 = {"A": [0, 3, 1, 2], "B": [0, 1, 2, 3], "C": [0, 2, 3, 1]}
dic_res = {"X": 0, "Y": 3, "Z": 6}

def round_score(you, me):
    you = dic_you[you]
    me = dic_me[me]

    if you == me:  # same
        return 3 + me
    if me == 1:
        if you == 2:
            return 0 + me
        else:
            return 6 + me
    if me == 2:
        if you == 3:
            return 0 + me
        else:
            return 6 + me
    if me == 3:
        if you == 1:
            return 0 + me
        else:
            return 6 + me

# Part 1
# while True:
#     try:
#         a, b = input().split()
#         ans = ans + round_score(a, b)
#     except EOFError:
#         break
# print("Part 1:", ans)  # Part 1: 10718

# Part 2
while True:
    try:
        a, b = input().split()
        ans = ans + dic_res[b] + dic_2[a][dic_me[b]]
    except EOFError:
        break
print("Part 2:", ans)