import numpy as n
from matplotlib import pyplot as p


x = range(0,10)


nlogn = x * n.log(x)
n2 = [temp ** 2 for temp in x]
logn = n.log(x)
n = x
dn = [2 ** temp for temp in x]

p.plot(x,n,label="f(n)=n")
p.plot(x,nlogn,label="f(n)=n log(n)")
p.plot(x,logn,label="f(n)=log(n)")
p.plot(x,n2,label="f(n)=n²")
p.plot(x,dn,label="f(n)=2^n")

p.legend()
p.show()
