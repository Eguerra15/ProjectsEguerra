mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 =s1.union(s2) #con este metodo unimos un set con otro
print(s3)
#tambien podemos agregar elementos con el metodo add

s1.add(6)
print(s1)

#tambien podemos remover lo que son los sets usando el metodo remove

s2.remove(4)
print(s2)

#ademas de remove existe el metodo discart que descarta los metodos que pongamos
s1.discard(3)
print(s1)

