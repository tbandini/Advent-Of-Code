with open('input.txt') as f:
    lines = f.readlines()

# creo una lista bidimensionale di 1000 x 1000 piena di 0
map = [[0 for col in range(1000)] for row in range(1000)]

count = 0

for line in lines:
    # formatto l'output ottenendo un array contentente le due cordinate
    # e successivamente li divido a sua volta in x, y inizio e x, y fine
    line = line.split(" -> ")
    line[-1] = line[-1].replace("\n", "")

    xyStart = line[0].split(",")
    xyEnd = line[1].split(",")

    # scarto i movimenti in obliquo come richiesto da testo
    if [(val, x) for val, x in enumerate(xyStart) if x in xyEnd[val]]:
        # scopro il movimento che devo eseguire

        # se le x sono uguali **MUOVO LUNGO LA Y**
        if xyStart[0] == xyEnd[0]: 
            # se il movimento è verso il basso
            if xyStart[1] < xyEnd[1]:
                for i in range((int(xyEnd[1]) - int(xyStart[1])) + 1):
                    map[int(xyStart[0])][int(xyStart[1]) + i] += 1
                    if map[int(xyStart[0])][int(xyStart[1]) + i] == 2:
                        count += 1    
            # se il movimento è verso l'alto
            else: 
                for i in range(int(xyStart[1])  - int(xyEnd[1]) + 1):
                    map[int(xyStart[0])][int(xyStart[1]) - i] += 1
                    if map[int(xyStart[0])][int(xyStart[1]) - i] == 2:
                        count += 1
        # se le y sono uguali **MUOVO LUNGO LA X**
        elif xyStart[1] == xyEnd[1]:
            # se il movimento è verso destra
            if xyStart[0] < xyEnd[0]:
                for i in range((int(xyEnd[0]) - int(xyStart[0])) + 1):
                    map[int(xyStart[0]) + i][int(xyStart[1])] += 1
                    if map[int(xyStart[0]) + i][int(xyStart[1])] == 2:
                        count += 1
            else: # se il movimento è verso sinistra
                for i in range(int(xyStart[0]) - (int(xyEnd[0])) + 1):
                    map[int(xyStart[0]) - i][int(xyStart[1])] += 1
                    if map[int(xyStart[0]) - i][int(xyStart[1])] == 2:
                        count += 1

print(count)