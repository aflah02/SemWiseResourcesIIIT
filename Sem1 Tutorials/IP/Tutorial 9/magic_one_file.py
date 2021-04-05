def find_magic_num(x,y,z):
    return ((x**2+y)%z)**5
x = int(input())
y = int(input())
z = int(input())
print(find_magic_num(x, y, z))