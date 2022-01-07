# def input_s(n):
#     l_s = []
#     for i in range(n):
#         l_s.append(str(input("Input string: ")))
#
#     return l_s
#
#
# def print_arr(arr):
#     for i in range(len(arr)):
#         print(arr[i])
#
#
# def del_words(arr):
#     for i in range(0, len(arr), 2):
#         l_w = arr[i].split()
#         buff = l_w[:]
#         for j in range(len(buff)):
#             for k in range(len(buff[j])):
#                 if k != len(buff[j]) - 1 and buff[j][k] == buff[j][k + 1]:
#                     index = l_w.index(buff[j])
#                     l_w.pop(index)
#                     break
#
#         arr[i] = ' '.join(l_w)
#
#
# def replacer(arr):
#     for i in range(1, len(arr), 2):
#         l_w = arr[i].split()
#         buff = l_w[0]
#         l_w[0] = l_w[-1]
#         l_w[-1] = buff
#         arr[i] = ' '.join(l_w)
#
#
# def find_min(arr):
#     min_s = arr[0]
#     for i in range(len(arr)):
#         if len(arr[i]) < len(min_s):
#             min_s = arr[i]
#
#     return min_s
#
