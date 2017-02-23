import os
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

Python_Exec = 'D:/Program Files/Python/Python34/python.exe'

width_list = range(5, 15, 2)

P_File = os.path.join(os.getcwd(), 'template/geo/poisson/Poisson.txt')
V_File = os.path.join(os.getcwd(), 'template/geo/voronoi.py')
G_File = os.path.join(os.getcwd(), 'template/geo/geo.py')
N_File = os.path.join(os.getcwd(), 'template/cubes.py')


def copy_files():
    # mkdir
    os.makedirs('geo/images')
    os.makedirs('geo/poisson')
    # copy poisson
    o_path = os.path.join(os.getcwd(), 'geo/poisson/Poisson.txt')
    i_file = open(P_File, 'r', encoding='utf-8')
    o_file = open(o_path, 'w', encoding='utf-8')
    for line in i_file:
        o_file.write(line)
    # copy voronoi
    o_path = os.path.join(os.getcwd(), 'geo/voronoi.py')
    i_file = open(V_File, 'r', encoding='utf-8')
    o_file = open(o_path, 'w', encoding='utf-8')
    line_index = 1
    for line in i_file:
        if line_index == 137:
            total_width = 5 * width
            total_width /= 2.0
            o_file.write('bound_vor = BoundVoronoi(bound=(-%.1f, %.1f, -%.1f, %.1f), space=0.1)\n' \
                         % (total_width, total_width, total_width, total_width))
        else:
            o_file.write(line)
        line_index += 1
    # copy geo
    o_path = os.path.join(os.getcwd(), 'geo/geo.py')
    i_file = open(G_File, 'r', encoding='utf-8')
    o_file = open(o_path, 'w', encoding='utf-8')
    for line in i_file:
        o_file.write(line)
    # copy nism cube.py
    o_path = os.path.join(os.getcwd(), 'cubes.py')
    i_file = open(N_File, 'r', encoding='utf-8')
    o_file = open(o_path, 'w', encoding='utf-8')
    for line in i_file:
        o_file.write(line)


def run_files():
    os.chdir('geo')
    # voronoi
    cmd_str = [Python_Exec, 'voronoi.py']
    logging.info('---- %s: %s' % (folder_name, cmd_str))
    subprocess.call(cmd_str, shell=True)
    # geo
    cmd_str = [Python_Exec, 'geo.py']
    logging.info('---- %s: %s' % (folder_name, cmd_str))
    subprocess.call(cmd_str, shell=True)
    os.chdir(os.pardir)


for width in width_list:
    folder_name = '%02d' % width
    os.mkdir(folder_name)
    os.chdir(folder_name)
    logging.info('---- %s: begin' % folder_name)
    # copy file
    copy_files()
    # run file
    run_files()
    logging.info('---- %s: done' % folder_name)
    os.chdir(os.pardir)



