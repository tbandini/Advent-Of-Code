with open('input.txt') as f:
    lines = f.readlines()

vals = [0] * 2000
count = 0

for val in lines:
    vals[count] = int(val)
    count+=1

sumVals = [0] * 3
sumNow = 0
tot = 0
t = 0
index = 0

while True:
    if t != 3:
        if index > 1997:
            break
        sumVals[t] = vals[index + t]
        t+=1
    else:
        sumPrev = sumNow
        sumNow = sum(sumVals)

        index += 1
        t = 0

        if sumPrev != 0:
            if sumNow > sumPrev:
                tot+=1
print(tot)  


