import sys

sys.stdin = open("3_input.txt")


def word_to_num(word):
    num = ord(word)
    if 97 <= num <= 122:  # small
        return num - 96
    else:
        return num - 38


ans = 0

# part 1
# while True:
#     try:
#         words = input()
#         forward = words[:len(words) // 2]
#         backward = words[len(words) // 2:]
#
#         for word in forward:
#             if word in backward:
#                 # print(word)
#                 # print(ord(word))
#                 # print(word_to_num(word))
#                 ans = ans + word_to_num(word)
#                 break
#     except EOFError:
#         break
# print("Part1: ", ans)

# part 2
while True:
    try:
        line1 = input()
        line2 = input()
        line3 = input()

        for word in line1:
            if word in line2:
                if word in line3:
                    ans = ans + word_to_num(word)
                    break
    except EOFError:
        break
print("Part 2:", ans)
