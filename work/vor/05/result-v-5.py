import math

index = 0
h_ext = 0.0
with open('ncol.txt', encoding='utf-8') as f:
    for line in f:
        line_token = line.split()
        ext = float(line_token[0].strip())
        all_positive = True
        for i in range(1, 51):
            mag = float(line_token[i].strip())
            if mag < 0:
                all_positive = False
                break
        if all_positive:
            h_ext = ext
            break
        index += 1
print('%d - %f' % (index, h_ext*4*math.pi/1e3))