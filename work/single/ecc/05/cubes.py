import math
import time
import numpy
import nmag
from nmag.common import degrees_per_ns
from nmag import SI, at, every

# mesh file
mesh_file = 'cubes.nmesh.h5'

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

cube_num = 1
a_exchange = 1.8e-11
d_max = 3
space_h = 0.05
ms_gap = ms_soft - ms_hard
j_hard = math.sqrt(a_exchange/(ku_soft*(Area_constant/1e-9))/(2*math.pi*ms_gap))
j_soft = math.sqrt(a_exchange/(ku_hard*(Area_constant/1e-9))/(2*math.pi*ms_gap))
print('j_hard %f A/m' % j_hard)
print('j_soft %f A/m' % j_soft)

# Saturation Magnetization -- M
M_hard = SI(ms_hard, 'A/m')
M_soft = SI(ms_soft, 'A/m')
# Exchange coupling strength -- A
A_hard = SI(1.2e-11, "J/m")
A_soft = SI(1e-11, "J/m")
# Anisotropy -- K
KA_hard = [0, 0.05, -1.0]
KA_soft = [0, 0, -1.0]
K_hard = SI(ku_hard, "J/m^3")
K_soft = SI(ku_soft, "J/m^3")
# LLG damping
LLG_damping = 1.0

# create a simulation
sim = nmag.Simulation()

# --------------------------------------------------------------------------- #
H1 = nmag.MagMaterial(name='H1',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S2 = nmag.MagMaterial(name='S2',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)

sim.load_mesh("%s"%mesh_file, [("H1", H1), ("S2", S2)], unit_length=SI(1e-9, "m"))
# --------------------------------------------------------------------------- #


# Hysteresis Apply Field List
Hs = nmag.vector_set(direction=[0, 0, 1],
                     norm_list=[-1.0, -0.8, [], 0.0, 0.01, [], 1.0],
                     units=H_max*SI('A/m'))
# set initial magnetisation
sim.set_m([0, 0, 1])
sim.set_params(stopping_dm_dt=2*degrees_per_ns)
# remember all positions
all_positions = []
def remember_position(pos):
    all_positions.append((pos[0]/1e-9, pos[1]/1e-9, pos[2]/1e-9))
    return [0, 0, 0]
sim.set_H_ext(remember_position, unit=SI('A/m'))
print('Length of all position : %d' % (len(all_positions)))
# remember hard layer and soft layer positions
hard_positions = []
soft_positions = []
for i in range(1, cube_num+1):
    hard_index = i*2-1
    soft_index = i*2
    hard_name = 'M_H%d' % hard_index
    soft_name = 'M_S%d' % soft_index
    pos_index = 0
    for pos in sim.get_subfield_positions(hard_name, pos_units=SI(1e-9, 'm')):
        hard_positions.append((pos, hard_name, pos_index))
        pos_index += 1
    pos_index = 0
    for pos in sim.get_subfield_positions(soft_name, pos_units=SI(1e-9, 'm')):
        soft_positions.append((pos, soft_name, pos_index)) # remember x,y,z & mat_name & mat_index
        pos_index += 1
print('Length of position on hard layer: %d' % (len(hard_positions)))
print('Length of position on soft layer: %d' % (len(soft_positions)))
map_positions = [[] for i in range(len(all_positions))]
# get the position map
i = 0
for pos in all_positions:
    x, y, z = pos[0], pos[1], pos[2]
    find_positions = None
    if hard_h - d_max < z < hard_h + space_h/2:
        find_positions = soft_positions
    elif hard_h + space_h/2 < z < hard_h + space_h + d_max:
        find_positions = hard_positions
    else:
        find_positions = []
    for find_pos in find_positions:
        x_s, y_s, z_s = find_pos[0][0], find_pos[0][1], find_pos[0][2]
        distance = math.sqrt((x-x_s)**2+(y-y_s)**2+(z-z_s)**2)
        if distance < d_max:
            map_positions[i].append(find_pos)
    i += 1
# print the position map
i = 0
for map_pos in map_positions:
    print('%d(%s): %s' % (i, str(all_positions[i]), str(map_positions[i])))
    i += 1
# get ecc
set_H_ext_index = 0
j_ext_hard = numpy.zeros(3)
j_ext_soft = numpy.zeros(3)
def get_ecc(sim):
    global set_H_ext_index, j_ext_hard, j_ext_soft
    print('Last stage %d with hard ecc %s' % (sim.stage-1, str(numpy.average(j_ext_hard, axis=0))))
    print('Last stage %d with soft ecc %s' % (sim.stage-1, str(numpy.average(j_ext_soft, axis=0))))
    H_ext = sim.get_subfield_average_siv('H_ext')
    print('Set H_ext of stage %d with H_ext %s' % (sim.stage, str(H_ext)))
    set_H_ext_index = 0
    j_ext_hard = numpy.zeros(3)
    j_ext_soft = numpy.zeros(3)
    def set_H(pos):
        z = pos[2]/1e-9
        global set_H_ext_index, j_ext_hard, j_ext_soft
        m_value = numpy.zeros(3)
        for m_pos in map_positions[set_H_ext_index]:
            m_v = sim.get_subfield(m_pos[1])[m_pos[2]]
            m_value += numpy.asarray(m_v)
        if len(map_positions[set_H_ext_index]) > 0:
            m_value /= len(map_positions[set_H_ext_index])
        if hard_h - d_max < z < hard_h + space_h/2:
            m_value *= j_hard
            j_ext_hard = numpy.row_stack((j_ext_hard, m_value))
        elif hard_h + space_h/2 < z < hard_h + space_h + d_max:
            m_value *= j_soft
            j_ext_soft = numpy.row_stack((j_ext_soft, m_value))
        m_value += numpy.asarray(H_ext)
        # print('%d Set new H_ext of stage %d with new H_ext %s' % (set_H_ext_index, sim.stage, str(m_value)))
        set_H_ext_index += 1
        return m_value
    sim.set_H_ext(set_H, unit=SI('A/m'))
def my_save(sim):
    # print last stage spend time
    global last_stage_time
    now_time = time.time()
    use_time = (now_time - last_stage_time) / 60
    last_stage_time = now_time
    print('Last stage spend %f min' % use_time)
    # save all field
    sim.save_data(fields='all')
# start time
start_time = time.time()
last_stage_time = start_time
# start hysteresis loop
sim.hysteresis(Hs, save=[(my_save, at('convergence'))], do=[(get_ecc, every('stage', 1) & at('stage_step', 0))])
# print simulate time
use_time = (time.time() - start_time) / 60
print('Use Time %f min' % use_time)