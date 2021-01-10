list = ['a', 1, 'b', 2]
d = dict()
for i in range(len(list)-1):
    d[list[i]] = list[i+1]

print(d['b'])



list = [1, 2, [3, 4]]
 
for i in list:
     print(i)

     
     
x = dict(name = "John", age = 36, country = "Norway")
for i in x:
    print (i)

for i in x:
    print (x[i])

print x['age']

c=dict()
c[0]='a'
c[1]='b'

print(c)
print(c[0])