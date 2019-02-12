# # found{1:99997}
# lists=[2,3,5,]
# for i in range(100000,500000):
#     if i not in lists and (i%2 !=0 and i%3 !=0 and i%5 !=0):
#         lists.append(i)
# print(lists)
# marked = [0] * 2000000
# value = 3
# s = 2
# while value < 2000000:
#      if marked[value] == 0:
#          s += value
#          i = value
#          while i < 2000000:
#              marked[i] = 1
#              i += value
#      value += 2
# print s
