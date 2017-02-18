import math
count = 16
step = int(math.sqrt(count))
width = 1/(step*2)
with open('Poisson.txt', 'w', encoding='utf-8') as f:
    f.write('NumPoints = %d\n' % count)
    for j in range(0, step):
        for i in range(0, step):
            x = width*(2*i+1)
            y = width*(2*j+1)
            f.write('%f %f\n' % (x, y))