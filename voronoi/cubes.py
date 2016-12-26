import math
import time
import numpy as np
import nmag
from nmag.common import degrees_per_ns
from nmag import SI, at

# mesh file
mesh_file = 'cubes.nmesh.h5'

# height
hard_h = 6.0
soft_h = 4.0
# Saturation Magnetization -- M
ms_hard = 0.5e6
M_hard = SI(ms_hard, 'A/m')
M_soft = SI(0.75e6, 'A/m')
# Exchange coupling strength -- A
A_hard = SI(1.2e-11, "J/m")
A_soft = SI(1e-11, "J/m")
# Anisotropy -- K
KA_hard = [0, 0.05, -1.0]
KA_soft = [0, 0, -1.0]
Stability_constant = 55*1.38e-23*350  # Stability Constant
Area_constant = 25e-27  # Area Constant = area * 1e-9
ku_soft = 2.5e5
ku_hard = (Stability_constant/Area_constant-ku_soft*soft_h)/hard_h
print('ku_hard %f' % ku_hard)
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
H3 = nmag.MagMaterial(name='H3',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S4 = nmag.MagMaterial(name='S4',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H5 = nmag.MagMaterial(name='H5',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S6 = nmag.MagMaterial(name='S6',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H7 = nmag.MagMaterial(name='H7',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S8 = nmag.MagMaterial(name='S8',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H9 = nmag.MagMaterial(name='H9',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S10 = nmag.MagMaterial(name='S10',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H11 = nmag.MagMaterial(name='H11',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S12 = nmag.MagMaterial(name='S12',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H13 = nmag.MagMaterial(name='H13',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S14 = nmag.MagMaterial(name='S14',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H15 = nmag.MagMaterial(name='H15',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S16 = nmag.MagMaterial(name='S16',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H17 = nmag.MagMaterial(name='H17',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S18 = nmag.MagMaterial(name='S18',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H19 = nmag.MagMaterial(name='H19',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S20 = nmag.MagMaterial(name='S20',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H21 = nmag.MagMaterial(name='H21',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S22 = nmag.MagMaterial(name='S22',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H23 = nmag.MagMaterial(name='H23',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S24 = nmag.MagMaterial(name='S24',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H25 = nmag.MagMaterial(name='H25',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S26 = nmag.MagMaterial(name='S26',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H27 = nmag.MagMaterial(name='H27',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S28 = nmag.MagMaterial(name='S28',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H29 = nmag.MagMaterial(name='H29',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S30 = nmag.MagMaterial(name='S30',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H31 = nmag.MagMaterial(name='H31',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S32 = nmag.MagMaterial(name='S32',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H33 = nmag.MagMaterial(name='H33',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S34 = nmag.MagMaterial(name='S34',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H35 = nmag.MagMaterial(name='H35',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S36 = nmag.MagMaterial(name='S36',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H37 = nmag.MagMaterial(name='H37',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S38 = nmag.MagMaterial(name='S38',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H39 = nmag.MagMaterial(name='H39',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S40 = nmag.MagMaterial(name='S40',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H41 = nmag.MagMaterial(name='H41',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S42 = nmag.MagMaterial(name='S42',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H43 = nmag.MagMaterial(name='H43',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S44 = nmag.MagMaterial(name='S44',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H45 = nmag.MagMaterial(name='H45',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S46 = nmag.MagMaterial(name='S46',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H47 = nmag.MagMaterial(name='H47',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S48 = nmag.MagMaterial(name='S48',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H49 = nmag.MagMaterial(name='H49',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S50 = nmag.MagMaterial(name='S50',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H51 = nmag.MagMaterial(name='H51',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S52 = nmag.MagMaterial(name='S52',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H53 = nmag.MagMaterial(name='H53',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S54 = nmag.MagMaterial(name='S54',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H55 = nmag.MagMaterial(name='H55',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S56 = nmag.MagMaterial(name='S56',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H57 = nmag.MagMaterial(name='H57',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S58 = nmag.MagMaterial(name='S58',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H59 = nmag.MagMaterial(name='H59',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S60 = nmag.MagMaterial(name='S60',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H61 = nmag.MagMaterial(name='H61',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S62 = nmag.MagMaterial(name='S62',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H63 = nmag.MagMaterial(name='H63',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S64 = nmag.MagMaterial(name='S64',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H65 = nmag.MagMaterial(name='H65',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S66 = nmag.MagMaterial(name='S66',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H67 = nmag.MagMaterial(name='H67',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S68 = nmag.MagMaterial(name='S68',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H69 = nmag.MagMaterial(name='H69',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S70 = nmag.MagMaterial(name='S70',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H71 = nmag.MagMaterial(name='H71',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S72 = nmag.MagMaterial(name='S72',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H73 = nmag.MagMaterial(name='H73',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S74 = nmag.MagMaterial(name='S74',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H75 = nmag.MagMaterial(name='H75',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S76 = nmag.MagMaterial(name='S76',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H77 = nmag.MagMaterial(name='H77',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S78 = nmag.MagMaterial(name='S78',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H79 = nmag.MagMaterial(name='H79',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S80 = nmag.MagMaterial(name='S80',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H81 = nmag.MagMaterial(name='H81',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S82 = nmag.MagMaterial(name='S82',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H83 = nmag.MagMaterial(name='H83',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S84 = nmag.MagMaterial(name='S84',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H85 = nmag.MagMaterial(name='H85',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S86 = nmag.MagMaterial(name='S86',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H87 = nmag.MagMaterial(name='H87',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S88 = nmag.MagMaterial(name='S88',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H89 = nmag.MagMaterial(name='H89',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S90 = nmag.MagMaterial(name='S90',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H91 = nmag.MagMaterial(name='H91',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S92 = nmag.MagMaterial(name='S92',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H93 = nmag.MagMaterial(name='H93',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S94 = nmag.MagMaterial(name='S94',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H95 = nmag.MagMaterial(name='H95',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S96 = nmag.MagMaterial(name='S96',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
H97 = nmag.MagMaterial(name='H97',
    Ms=M_hard,
    exchange_coupling=A_hard,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
    llg_damping=LLG_damping)
S98 = nmag.MagMaterial(name='S98',
    Ms=M_soft,
    exchange_coupling=A_soft,
    anisotropy=nmag.uniaxial_anisotropy(axis=KA_soft, K1=K_soft),
    llg_damping=LLG_damping)
sim.load_mesh("%s"%mesh_file, [("H1", H1), ("S2", S2), ("H3", H3), ("S4", S4), ("H5", H5), ("S6", S6), ("H7", H7),
    ("S8", S8), ("H9", H9), ("S10", S10), ("H11", H11), ("S12", S12), ("H13", H13), ("S14", S14),
    ("H15", H15), ("S16", S16), ("H17", H17), ("S18", S18), ("H19", H19), ("S20", S20), ("H21", H21),
    ("S22", S22), ("H23", H23), ("S24", S24), ("H25", H25), ("S26", S26), ("H27", H27), ("S28", S28),
    ("H29", H29), ("S30", S30), ("H31", H31), ("S32", S32), ("H33", H33), ("S34", S34), ("H35", H35),
    ("S36", S36), ("H37", H37), ("S38", S38), ("H39", H39), ("S40", S40), ("H41", H41), ("S42", S42),
    ("H43", H43), ("S44", S44), ("H45", H45), ("S46", S46), ("H47", H47), ("S48", S48), ("H49", H49),
    ("S50", S50), ("H51", H51), ("S52", S52), ("H53", H53), ("S54", S54), ("H55", H55), ("S56", S56),
    ("H57", H57), ("S58", S58), ("H59", H59), ("S60", S60), ("H61", H61), ("S62", S62), ("H63", H63),
    ("S64", S64), ("H65", H65), ("S66", S66), ("H67", H67), ("S68", S68), ("H69", H69), ("S70", S70),
    ("H71", H71), ("S72", S72), ("H73", H73), ("S74", S74), ("H75", H75), ("S76", S76), ("H77", H77),
    ("S78", S78), ("H79", H79), ("S80", S80), ("H81", H81), ("S82", S82), ("H83", H83), ("S84", S84),
    ("H85", H85), ("S86", S86), ("H87", H87), ("S88", S88), ("H89", H89), ("S90", S90), ("H91", H91),
    ("S92", S92), ("H93", H93), ("S94", S94), ("H95", H95), ("S96", S96), ("H97", H97), ("S98", S98)],
    unit_length = SI(1e-9,"m"))
# --------------------------------------------------------------------------- #

# Max Apply Field
H_max = 2*ku_hard*1e4/ms_hard
H_max = H_max*1e3/(4*math.pi)  # koe to A/m
print('H_max %f' % H_max)
# set initial magnetisation
sim.set_m([0, 0, 1])
sim.set_params(stopping_dm_dt=2*degrees_per_ns)
# custom save
cube_num = 49
stage_num = 3
M_result = np.zeros((cube_num*2, stage_num, 3))
def my_save(sim):
    for i in range(cube_num):
        mat_index = i+1
        physical_hard_index = mat_index*2-1
        physical_soft_index = mat_index*2
        mat_hard_name = 'H%d' % physical_hard_index
        mat_soft_name = 'S%d' % physical_soft_index
        m_hard = sim.get_subfield_average_siv('M', mat_hard_name)
        m_soft = sim.get_subfield_average_siv('M', mat_soft_name)
        M_result[i*2, sim.id+1] = m_hard
        M_result[i*2+1, sim.id+1] = m_soft
    sim.save_data(fields=['id', 'time', 'step', 'stage_time', 'stage_step', 'H_ext', 'M', 'm'])
# start time
start_time = time.time()
# save initial data
sim.relax(save=[(my_save, at('convergence'))])
# make H_ext = -H_max where x >= 0
def set_H(position):
    # positions unit is nm
    x = position[0] / 1e-9
    y = position[1] / 1e-9
    z = position[2] / 1e-9
    if x < 0:
        return [0, 0, 0]
    return [0, 0, -H_max]
sim.set_H_ext(set_H, unit=SI(1, 'A/m'))
sim.relax(save=[(my_save, at('convergence'))])
print('------make H_ext reserve------')
# make H_ext = H_max where x >= 0
def set_H(position):
    # positions unit is nm
    x = position[0] / 1e-9
    y = position[1] / 1e-9
    z = position[2] / 1e-9
    if x < 0:
        return [0, 0, 0]
    return [0, 0, H_max]
sim.set_H_ext(set_H, unit=SI(1, 'A/m'))
sim.relax(save=[(my_save, at('convergence'))])
# save M_result_2
with open('Result.txt', 'w') as f:
    for i in range(cube_num):
        mat_index = i+1
        physical_hard_index = mat_index*2-1
        physical_soft_index = mat_index*2
        mat_hard_name = 'H%d' % physical_hard_index
        mat_soft_name = 'S%d' % physical_soft_index
        line_hard = [mat_hard_name]
        line_soft = [mat_soft_name]
        for j in range(stage_num):
            m_hard_2 = M_result[i*2, j, 2]
            m_soft_2 = M_result[i*2+1, j, 2]
            line_hard.append(str(m_hard_2))
            line_soft.append(str(m_soft_2))
        f.write('\t'.join(line_hard))
        f.write('\n')
        f.write('\t'.join(line_soft))
        f.write('\n')
# print simulate time
use_time = (time.time() - start_time) / 60
print('Use Time %f min' % use_time)