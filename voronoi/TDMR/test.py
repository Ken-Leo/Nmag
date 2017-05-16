# import numpy as np
# from random import *
#
# cube_num = 10
# stage_num = 3
# M_result = np.zeros((cube_num, stage_num, 3))
#
#
# def assig():
#     for i in range(10):
#         M_result[i, i % 3] = 10 * random()
#
#
# assig()
#
# print(M_result)
# print(M_result[0, 0, 0])
# print(M_result[1, 1, 0])
# print(M_result[2, 0, 0])


# with open('test.txt', 'w') as f:
#     for i in range(25):
#         for j in range(7):
#             f.write('("H%d", H%d), ' % (98 + j + i*7, 98 + j + i*7))
#         f.write('\n')
#     f.close()

# data_list = [12, 9, 26, -36, -8]
# result_list = []
# for i in data_list:
#     result_list.append(i % 10)
#
# print(result_list)

# CUBE_NUM = 221
# mat_hard_lines = None
# with open('mat_hard', 'r', encoding='utf-8') as f:
#     mat_hard_line = f.read()
# # with open('mat_soft', 'r', encoding='utf-8') as f:
# #     mat_soft_line = f.read()
# with open('list_of_materials.py', 'a', encoding='utf-8') as f:
#     # Write MagMaterial
#     for i in range(1, CUBE_NUM+1):
#         mat_hard_name = 'H%d' % i
#         mat_hard = mat_hard_line.replace('MAT_NAME', mat_hard_name)
#         f.write(mat_hard)

# Write load mesh
# f.write('sim.load_mesh("%s"%mesh_file, [')
# mesh_list = []
# for i in range(1, CUBE_NUM+1):
#     mat_hard_name = 'H%d' % i
#     mesh_list.append('("%s", %s)' % (mat_hard_name, mat_hard_name))
# for i, mesh in enumerate(mesh_list):
#     if i == len(mesh_list) - 1:
#         f.write('%s' % mesh)
#     else:
#         if i % 7 == 6:
#             f.write('%s,\n    ' % mesh)
#         else:
#             f.write('%s, ' % mesh)
# f.write('],\n    unit_length = SI(1e-9,"m"))\n')

# position_list = []
# with open('Poisson/Poisson.txt', 'r', encoding='utf-8') as f:
#     first_line = True
#     for line in f:
#         if first_line:  # 1st line is just a specification declaring the num of points to generate
#             first_line = False
#             continue
#         line_token = line.split()
#         position_list.append((float(line_token[0]), float(line_token[1])))
#
# print(position_list)

# H_max = 0.5
#
# def set_H(position):
#     # positions unit is nm
#     x = position[0] / 1e-9
#     y = position[1] / 1e-9
#     z = position[2] / 1e-9
#     if x % 20 <= 10:
#         return [0, 0, -H_max]
#     elif x % 20 > 10:
#         return [0, 0, H_max]
#     return [0, 0, 0]
#
# print(set_H((18e-9,-20e-9,0e-9)))
# print(set_H((15e-9,-20e-9,0e-9)))
# print(set_H((10e-9,-20e-9,0e-9)))
# print(set_H((5e-9,-20e-9,0e-9)))
# print(set_H((0e-9,-20e-9,0e-9)))




def read_results(file_name='Result.txt', stage_index=2):
    result_list = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            line_token = line.split('\t')
            stage_value = line_token[2]
            stage_value = float(stage_value.strip())
            result_list.append(stage_value)
    return result_list

result_list = read_results()
print(result_list)


# def read_regions(file_name='Region.txt'):
#     region_point_list = []
#     with open(file_name, 'r', encoding='utf-8') as f:
#         first_line = True
#         for line in f:
#             if first_line:
#                 first_line = False
#                 continue
#             point_list = []
#             line_token = line.split('\t')
#             for token in line_token:
#                 if token == '\n':
#                     continue
#                 tokens = token.split(',')
#                 point_list.append((float(tokens[0].strip()), float(tokens[1].strip())))
#             region_point_list.append(point_list)
#     return region_point_list
#
# region_list = read_regions()
# print(region_list)


