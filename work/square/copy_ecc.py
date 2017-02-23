import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


width_list = range(5, 15, 2)

for width in width_list:
    folder_name = '%02d' % width
    sub_folder_name = os.path.join('ecc', folder_name)
    os.mkdir(sub_folder_name)
    # copy geo
    i_path = os.path.join(folder_name, 'cubes.geo')
    o_path = os.path.join('ecc', folder_name, 'cubes.geo')
    i_file = open(i_path, 'r', encoding='utf-8')
    o_file = open(o_path, 'w', encoding='utf-8')
    for line in i_file:
        o_file.write(line)
    # copy py
    i_path = os.path.join('ecc', 'cubes.py')
    o_path = os.path.join('ecc', folder_name, 'cubes.py')
    i_file = open(i_path, 'r', encoding='utf-8')
    o_file = open(o_path, 'w', encoding='utf-8')
    for line in i_file:
        o_file.write(line)
