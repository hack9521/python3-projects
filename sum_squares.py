# sum_squares=[i**2 for i in range(1,101)]
# print(sum(sum_squares))
# # total=[i for i in range(1,101)]
# # 5050*5050--applicable but hard coded
# total_square= #(sum(total))**2
# print(total_square)
# diff=total_square-sum(sum_squares)
# print(diff)
def problem6(r): return sum(r)** 2- sum([x** 2 for x in r])
print(problem6(range(1,101)))
