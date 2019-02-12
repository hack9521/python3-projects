# # def pythogras(a,b,c):
# #     if ((a**2 + b**2)==c**2):
# #         print(a+b+c)
# #     else:
# #         print("not pythogras")
# # pythogras(3,4,5)
# # pythogras(0,500,500)
# def specialPythagoreanTriplet(s):
#
#     for a in xrange(s):
#         for b in xrange(a, s):
#             c = s - a - b;
#             if a**2 + b**2 == c**2:
#                 return (a, b,c)
# print specialPythagoreanTriplet(1000)
# def euler9():
# #     # Ensure a < c
# #     for c in xrange(2, 1000):
# #         for a in xrange(1, c):
# #             # Ensure a + b + c == 1000.  Since a is counting up, the first
# #             # answer we find should have a <= b.
# #             b = 1000 - c - a
# #
# #             # Ensure Pythagorean triple
# #             if a**2 + b**2 == c**2:
# #                 print("a = %d, b = %d, c = %d.  abc = %d" % (a, b, c, a * b * c))
# #                 return
# # euler9()
# # for a ,b ,c in list(range(1,500)):
# #     if (a+b+c==1000) and a**2 + b**2 ==c**2:
# #         print(a ,b ,c)
# for a in range(500):
#     for b in range(500):
#         for c in range(500):
#             if (a+b+c==1000) and (a**2 + b**2 == c**2):
#                 print(a,b,c)

lists=(range(500))
def ranlis(li):
    for m  in lists:
        for n in lists:
            if m*(m*n)==500:
                return(m,n)
