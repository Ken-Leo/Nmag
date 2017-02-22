import os
import math
import numpy
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

width_list = range(5, 15, 2)
ms_hard = 1.3e6
ku_hard = 1.8e6
h_hard = 2*ku_hard*1e4/ms_hard
print('h_hard %f oe' % h_hard)
h_list = numpy.append(numpy.arange(-1, 0, 0.2), numpy.arange(0, 1.01, 0.01))
h_list *= h_hard


def get_result(ncol_path):
    index = 0
    h_ext = 0.0
    with open(ncol_path, encoding='utf-8') as f:
        for line in f:
            line_token = line.split()
            ext = float(line_token[0].strip())
            hard = float(line_token[1].strip())
            soft = float(line_token[2].strip())
            if ext > 0 and hard > 0 and soft > 0 :
                h_ext = ext
                break
            index += 1
    return index, h_ext*4*math.pi/1e3

for width in width_list:
    folder_name = '%02d' % width
    ncol_path = os.path.join(folder_name, 'ncol.txt')
    result = (0, 0)
    if os.path.exists(ncol_path):
        result = get_result(ncol_path)
    print('width %02d hsw on %d with %f - %f' % (width, result[0], h_list[result[0]], result[1]))