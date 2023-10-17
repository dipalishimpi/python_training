a={tuple(['a','b']):200}
print(a)
b={tuple([2,3,4]),'g',500}
print(b)
c={1:"a",1:"b",1:"f"}
c={1:"a",1:"b",1:"g"}
c={1:"a",1:"b",1:"m"}
print(c)    #it will consinder alwaylast value
print(id(c))
print(id(c[1]))
c={1:"a",1:"b",1:"e"}
print(c)
print(id(c))
print(id(c[1]))
print(c)
print(id(c))
print(id(c[1]))