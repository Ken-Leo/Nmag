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
a_exchange = 9e-11
d_max = 3
space_h = 0.05
ms_gap = ms_soft - ms_hard
j_hard = a_exchange/(ku_soft*(Area_constant/1e-9))
j_soft = a_exchange/(ku_hard*(Area_constant/1e-9))
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
# remember all mesh positions
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)
class MeshPos():
    def __init__(self, position, sub_name, sub_index):
        self.sub_name = sub_name
        self.sub_index = sub_index,
        self.position = position
        self.map_index = []
all_positions = sim.get_subfield_positions('H_ext', pos_units=SI(1e-9, 'm'))
# the meshing positions
mesh_positions = [MeshPos(position, '', -1) for position in all_positions]
hard_positions = []
soft_positions = []
# remember hard layer and soft layer positions
for i in range(1, cube_num+1):
    hard_index = i*2-1
    soft_index = i*2
    hard_name = 'H%d' % hard_index
    soft_name = 'S%d' % soft_index
    # hard layer
    pos_field = 'H_total_' + hard_name
    subfield_sites = sim.get_subfield_sites(pos_field)
    subfield_positions = sim.get_subfield_positions(pos_field, pos_units=SI(1e-9, 'm'))
    for sub_index, (index, position) in enumerate(zip(subfield_sites, subfield_positions)):
        index = index[0]
        m_position = mesh_positions[index].position
        # check
        for i in range(3):
            if m_position[i] != position[i]:
                print('Position is not Matched! ', hard_name, sub_index, index)
        # link
        hard_positions.append(index)
        mesh_positions[index].sub_name = hard_name
        mesh_positions[index].sub_index = sub_index
    # soft layer
    pos_field = 'H_total_' + soft_name
    subfield_sites = sim.get_subfield_sites(pos_field)
    subfield_positions = sim.get_subfield_positions(pos_field, pos_units=SI(1e-9, 'm'))
    for sub_index, (index, position) in enumerate(zip(subfield_sites, subfield_positions)):
        index = index[0]
        m_position = mesh_positions[index].position
        # check
        for i in range(3):
            if m_position[i] != position[i]:
                print('Position is not Matched! ', soft_name, sub_index, index)
        # link
        soft_positions.append(index)
        mesh_positions[index].sub_name = soft_name
        mesh_positions[index].sub_index = sub_index
print('Length of position : %d' % (len(mesh_positions)))
print('Length of position on hard layer: %d' % (len(hard_positions)))
print('Length of position on soft layer: %d' % (len(soft_positions)))
# get the position map
for m_position in mesh_positions:
    m_pos = m_position.position
    z = m_pos[2]
    find_positions = None
    if hard_h - d_max < z < hard_h + space_h/2:
        find_positions = soft_positions
    elif hard_h + space_h/2 < z < hard_h + space_h + d_max:
        find_positions = hard_positions
    else:
        find_positions = []
    for find_index in find_positions:
        find_pos = mesh_positions[find_index].position
        p_d = distance(m_pos, find_pos)
        if p_d < d_max:
            m_position.map_index.append(find_index)
# list map count to 9
for m_position in mesh_positions:
    map_index = m_position.map_index
    if len(map_index) > 9:
        sorted(map_index, key=lambda m_i: distance(mesh_positions[m_i].position, m_position.position))
        m_position.map_index = map_index[0:9]
# print the position map
for index, m_position in enumerate(mesh_positions):
    print('%d(%s) Map To: %s' % (index, str(m_position.position), str(m_position.map_index)))
# get ecc
mesh_index = 0
j_ext_hard = numpy.zeros(3)
j_ext_soft = numpy.zeros(3)
def get_ecc(sim):
    global mesh_index
    H_ext = sim.get_subfield_average_siv('H_ext')
    print('Set H_ext of stage %d with H_ext %s' % (sim.stage, str(H_ext)))
    mesh_index = 0
    j_ext_hard = numpy.zeros(3)
    j_ext_soft = numpy.zeros(3)
    def set_H(pos):
        z = pos[2]/1e-9
        global mesh_index, j_ext_hard, j_ext_soft
        j_value = numpy.zeros(3)
        map_index = mesh_positions[mesh_index].map_index
        for m_index in map_index:
            m_position = mesh_positions[m_index]
            m_v = sim.get_subfield('E_exch_' + m_position.sub_name)[m_position.sub_index]
            m_w = sim.get_subfield('m_' + m_position.sub_name)[m_position.sub_index]
            m_v = numpy.asarray(m_v)
            m_w = numpy.asarray(m_w)
            j_value += numpy.dot(m_v, m_w)

        if len(mesh_positions[mesh_index].map_index) > 0:
            j_value /= len(map_index)
        if hard_h - d_max < z < hard_h + space_h/2:
            j_value *= j_hard
            j_ext_hard = numpy.row_stack((j_ext_hard, j_value))
        elif hard_h + space_h/2 < z < hard_h + space_h + d_max:
            j_value *= j_soft
            j_ext_soft = numpy.row_stack((j_ext_soft, j_value))
        j_value += numpy.asarray(H_ext)
        # print('%d Set new H_ext of stage %d with new H_ext %s' % (set_H_ext_index, sim.stage, str(m_value)))
        mesh_index += 1
        return [0, 0, j_value[2]]
    sim.set_H_ext(set_H, unit=SI('A/m'))
# start time
start_time = time.time()
last_stage_time = start_time
def my_save(sim):
    # print last stage spend time
    global last_stage_time, j_ext_hard, j_ext_soft
    print('Last stage %d with hard ecc %s' % (sim.stage, str(numpy.average(j_ext_hard, axis=0))))
    print('Last stage %d with soft ecc %s' % (sim.stage, str(numpy.average(j_ext_soft, axis=0))))
    now_time = time.time()
    use_time = (now_time - last_stage_time) / 60
    last_stage_time = now_time
    print('Last stage %d spend %f min' % (sim.stage, use_time))
    # save all field
    sim.save_data(fields='all')
# start hysteresis loop
sim.hysteresis(Hs, save=[(my_save, at('convergence'))], do=[(get_ecc, every('stage', 1) & at('stage_step', 0))])
# print simulate time
use_time = (time.time() - start_time) / 60
print('Use Time %f min' % use_time)