with open('input.txt') as f:
    lines = f.readlines()

x = 0
y = 0
aim = 0
t = 0

for line in lines:
    t+=1
    mov = line.split()
    if mov[0] == "forward":
        x += int(mov[1])
        y += (aim * int(mov[1]))
    if mov[0] == "up":
        aim -= int(mov[1])
    if mov[0] == "down":
        aim += int(mov[1])
    
print(x*y)

