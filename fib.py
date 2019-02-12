# still not solved

# def fib(n):
#     a,b=1,2
#     for _ in range(n):
#         yield a
#         a,b=b, a+b
# p=list(fib(4000000))
# sum=[i for i in p if i%2==0]
# print(sum)
#
#
#
#
#
# # def fib(n):
# #     if n==1:
# #         return [1]
# #     elif n==2:
# #         return [1,2]
# #     else:
# #         lst=fib(n-1)
# #         lst.append(lst[-1] + lst[-2])
# #         return lst
def fib(n,computed={0:0,1:1}):
    if n not in computed:
        computed[n]=fib(n-1,computed) + fib(n-2,computed)
    return computed(n)
fib(4)
