CUBE_NUM = 49

with open('ncol.cmd', 'w', encoding='utf-8') as f:
    f.write('ncol cubes \\\n')
    for i in range(1, CUBE_NUM+1):
        physical_hard_index = i * 2 - 1
        physical_soft_index = i * 2
        mat_hard_name = 'H%d' % physical_hard_index
        mat_soft_name = 'S%d' % physical_soft_index
        f.write('M_' + mat_hard_name + '_2 ')
        f.write('M_' + mat_soft_name + '_2 ')
        if i % 4 == 0:
            f.write('\\\n')