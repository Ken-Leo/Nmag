import math
import time
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

sim.load_mesh("%s"%mesh_file, [("H1", H1), ("S2", S2)], unit_length=SI(1e-9,"m"))
# --------------------------------------------------------------------------- #


# Hysteresis Apply Field List
Hs = nmag.vector_set(direction=[0, 0, 1],
                     norm_list=[-1.0, -0.8, [], 0.0, 0.01, [], 1.0],
                     units=H_max*SI('A/m'))
# set initial magnetisation
sim.set_m([0, 0, 1])
sim.set_params(stopping_dm_dt=2*degrees_per_ns)
# start time
start_time = time.time()
last_stage_time = start_time
# custom save
def my_save(sim):
    # print stage info
    H_ext = sim.get_subfield_average_siv('H_ext')
    print('Set new H_ext of stage %d with H_ext %s' % (sim.stage, str(H_ext)))
    # print last stage spend time
    global last_stage_time
    now_time = time.time()
    use_time = (now_time - last_stage_time) / 60
    last_stage_time = now_time
    print('Last stage spend %f min' % use_time)
    # save all field
    sim.save_data(fields='all')
# start hysteresis loop
sim.hysteresis(Hs, save=[(my_save, at('convergence'))])
# print simulate time
use_time = (time.time() - start_time) / 60
print('Use Time %f min' % use_time)