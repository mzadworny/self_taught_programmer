
def divider(x):
  x = x / 2
  x = int(x)
  return x 

def multiplier(x):
  x = x * 4
  x = int(x)
  return x

g = input("GIVE ME A NUMBER! ")
g = int(g)
y = divider(g)
p = multiplier(y)
print(p)