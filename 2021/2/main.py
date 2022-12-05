with open('input.txt') as f:
    lines = f.readlines()

x = 0
y = 0

for line in lines:
    mov = line.split()
    if mov[0] == "forward":
        x += int(mov[1])        
    if mov[0] == "up":
        y -= int(mov[1])
    if mov[0] == "down":
        y += int(mov[1])
print(x*y)

