n='one two three four five six seven 7 8 eight nine ten'
q=list(n)
def strip_join(q):
    p=[]
    for i in q:
         if i !=' ' and  i != '-':
             p.append(i)
    print(len(p))
    l=(''.join(p))
    print(l)

d=[1,2,3,4,5,6,7,66,8,9,10]
def ten_special(d):
    for i in d:
        if i in range(10):
            return strip_join(q)
f=ten_special(d)
