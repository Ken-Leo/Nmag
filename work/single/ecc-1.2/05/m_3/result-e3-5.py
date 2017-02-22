import math
import numpy

# parameters
hard_h = 4.0
soft_h = 6.0
ms_hard = 1.3e6
ms_soft = 2.0e6
Stability_constant = 55*1.38e-23*350  # Stability Constant
Area_constant = 25e-27  # Area Constant = area * 1e-9
ku_hard = 1.8e6
ku_soft = (Stability_constant/Area_constant-ku_hard*hard_h)/soft_h
print('ku_soft:%f J/m^3' % ku_soft)
h_hard = 2*ku_hard*1e4/ms_hard
h_soft = 2*ku_soft*1e4/ms_soft
print('h_hard:%f oe' % h_hard)
print('h_soft:%f oe' % h_soft)
# Max Apply Field
H_max = h_hard*1e3/(4*math.pi)  # oe to A/m
print('H_max %f A/m' % H_max)
H_list = numpy.append(numpy.arange(-1, 0, 0.2), numpy.arange(0, 1.01, 0.01))
H_list *= H_max
index = 0
h_ext = 0.0
with open('ncol.txt', encoding='utf-8') as f:
    for line in f:
        line_token = line.split()
        ext = float(line_token[0].strip())
        hard = float(line_token[1].strip())
        soft = float(line_token[2].strip())
        if ext > 0 and hard > 0 and soft > 0 :
            h_ext = ext
            break
        index += 1
print('%d - %f - %f' % (index, h_ext*4*math.pi/1e3, H_list[index]*4*math.pi/1e3))