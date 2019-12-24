from math import floor

f = open("input", "r")
result = 0

for line in f:
    mass = int(line.strip())
    result += floor(mass/3-2)

f.close()
print(int(result))
