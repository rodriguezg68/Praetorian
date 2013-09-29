import collections, itertools
a=B=A=list(itertools.product([range(1,7)]*4))
r=lambda g,k:(sum(x==y for x,y in zip(g,k)),sum(min(g.count(c),k.count(c))for c in set(g)))
while a!=4:
    g=A[1:]and min(B,key=lambda x:max(collections.Counter(r(x,i)for i in A).values()))or A[0]
    print"%d "*4%tuple(g)
    b,a=map(int,raw_input().split())
    A=[x for x in A if r(g,x)==(a,a+b)]
