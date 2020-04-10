# Igual a las listas pero no permiten tener elementos repetidos

s = set([1, 2, 3])
t = set([3, 4, 5])

# Union
union = s.union(t)
print("Union {}".format(union))

# intersección
intersection = s.intersection(t)
print("Intersección {}".format(intersection))

# Diff
diffST = s.difference(t)
print("Diferencia s de t {}".format(diffST))

diffTS = t.difference(s)
print("Diferencia t de s {}".format(diffTS))


1 in s # True
1 in t # False

1 not in s # False
1 not in t # True


print(s)
print(t)

print(s | t) # | union                  s.union(t)
print(s & t) # & interseccion           s.intersection(t)
print(s - t) # - diferencia             s.difference(t)
print(s ^ t) # ^ diferencia simetrica   s.symmetric_difference(t)
print(s <= t) # <= subconjunto          s.issubset(t)
print(s >= t) # >= superconjunto        s.issuperset(t)
