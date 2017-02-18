import math

index = 0
h_ext = 0.0
with open('ncol.txt', encoding='utf-8') as f:
    for line in f:
        line_token = line.split()
        ext = float(line_token[0].strip())
        hard = float(line_token[1].strip())
        soft = float(line_token[2].strip())
        if hard > 0 and soft > 0 :
            h_ext = ext
            break
        index += 1
print('%d - %f' % (index, h_ext*4*math.pi/1e3))