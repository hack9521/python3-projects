# s=[]
# for i in range(1,1000):
#     if i%3==0 or i%5==0:
#         s.append(i)
#
# print(sum(s))

s=[i for i in range(1,10) if i%3==0 or i%5==0]
print(sum(s))
