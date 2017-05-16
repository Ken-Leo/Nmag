import math
import time
import numpy as np
import nmag
from nmag.common import degrees_per_ns
from nmag import SI, at

# mesh file
mesh_file = 'singlephase.nmesh.h5'

# height
hard_h = 6.0
# soft_h = 4.0
# Saturation Magnetization -- M
ms_hard = 0.5e6  # 480emu/cc   x 1e3 --->A/m
M_hard = SI(ms_hard, 'A/m')
# M_soft = SI(0.75e6, 'A/m')
# Exchange coupling strength -- A     Formula= 1 erg/cm is 1.0E-5 J/m
A_hard = SI(1.2e-11, "J/m")     # SI(3e-12, "J/m")
# A_hard = SI(1.2e-11, "J/m")
# A_soft = SI(1e-11, "J/m")
# Anisotropy -- K
KA_hard = [0, 0.5, -1]
# KA_soft = [0, 0, -1.0]
# Stability_constant = 55 * 1.38e-23 * 350  # Stability Constant
# Area_constant = 25e-27  # Area Constant = area * 1e-9
# ku_soft = 2.5e5
# ku_hard = (Stability_constant/Area_constant-ku_soft*soft_h)/hard_h
ku_hard = 3.6e5  # 3.6e5
print('ku_hard %f' % ku_hard)
K_hard = SI(ku_hard, "J/m^3")
# K_soft = SI(ku_soft, "J/m^3")
# LLG damping
LLG_damping = 1.0

# create a simulation object
sim = nmag.Simulation()
# --------------------------------------------------------------------------- #
H1 = nmag.MagMaterial(name='H1',
                      Ms=M_hard,
                      exchange_coupling=A_hard,
                      anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                      llg_damping=LLG_damping)
H2 = nmag.MagMaterial(name='H2',
                      Ms=M_hard,
                      exchange_coupling=A_hard,
                      anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                      llg_damping=LLG_damping)
H3 = nmag.MagMaterial(name='H3',
                      Ms=M_hard,
                      exchange_coupling=A_hard,
                      anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                      llg_damping=LLG_damping)
H4 = nmag.MagMaterial(name='H4',
                      Ms=M_hard,
                      exchange_coupling=A_hard,
                      anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                      llg_damping=LLG_damping)
H5 = nmag.MagMaterial(name='H5',
                      Ms=M_hard,
                      exchange_coupling=A_hard,
                      anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                      llg_damping=LLG_damping)
H6 = nmag.MagMaterial(name='H6',
                      Ms=M_hard,
                      exchange_coupling=A_hard,
                      anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                      llg_damping=LLG_damping)
H7 = nmag.MagMaterial(name='H7',
                      Ms=M_hard,
                      exchange_coupling=A_hard,
                      anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                      llg_damping=LLG_damping)
H8 = nmag.MagMaterial(name='H8',
                      Ms=M_hard,
                      exchange_coupling=A_hard,
                      anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                      llg_damping=LLG_damping)
H9 = nmag.MagMaterial(name='H9',
                      Ms=M_hard,
                      exchange_coupling=A_hard,
                      anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                      llg_damping=LLG_damping)
H10 = nmag.MagMaterial(name='H10',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H11 = nmag.MagMaterial(name='H11',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H12 = nmag.MagMaterial(name='H12',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H13 = nmag.MagMaterial(name='H13',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H14 = nmag.MagMaterial(name='H14',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H15 = nmag.MagMaterial(name='H15',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H16 = nmag.MagMaterial(name='H16',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H17 = nmag.MagMaterial(name='H17',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H18 = nmag.MagMaterial(name='H18',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H19 = nmag.MagMaterial(name='H19',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H20 = nmag.MagMaterial(name='H20',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H21 = nmag.MagMaterial(name='H21',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H22 = nmag.MagMaterial(name='H22',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H23 = nmag.MagMaterial(name='H23',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H24 = nmag.MagMaterial(name='H24',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H25 = nmag.MagMaterial(name='H25',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H26 = nmag.MagMaterial(name='H26',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H27 = nmag.MagMaterial(name='H27',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H28 = nmag.MagMaterial(name='H28',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H29 = nmag.MagMaterial(name='H29',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H30 = nmag.MagMaterial(name='H30',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H31 = nmag.MagMaterial(name='H31',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H32 = nmag.MagMaterial(name='H32',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H33 = nmag.MagMaterial(name='H33',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H34 = nmag.MagMaterial(name='H34',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H35 = nmag.MagMaterial(name='H35',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H36 = nmag.MagMaterial(name='H36',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H37 = nmag.MagMaterial(name='H37',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H38 = nmag.MagMaterial(name='H38',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H39 = nmag.MagMaterial(name='H39',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H40 = nmag.MagMaterial(name='H40',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H41 = nmag.MagMaterial(name='H41',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H42 = nmag.MagMaterial(name='H42',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H43 = nmag.MagMaterial(name='H43',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H44 = nmag.MagMaterial(name='H44',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H45 = nmag.MagMaterial(name='H45',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H46 = nmag.MagMaterial(name='H46',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H47 = nmag.MagMaterial(name='H47',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H48 = nmag.MagMaterial(name='H48',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H49 = nmag.MagMaterial(name='H49',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H50 = nmag.MagMaterial(name='H50',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H51 = nmag.MagMaterial(name='H51',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H52 = nmag.MagMaterial(name='H52',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H53 = nmag.MagMaterial(name='H53',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H54 = nmag.MagMaterial(name='H54',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H55 = nmag.MagMaterial(name='H55',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H56 = nmag.MagMaterial(name='H56',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H57 = nmag.MagMaterial(name='H57',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H58 = nmag.MagMaterial(name='H58',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H59 = nmag.MagMaterial(name='H59',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H60 = nmag.MagMaterial(name='H60',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H61 = nmag.MagMaterial(name='H61',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H62 = nmag.MagMaterial(name='H62',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H63 = nmag.MagMaterial(name='H63',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H64 = nmag.MagMaterial(name='H64',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H65 = nmag.MagMaterial(name='H65',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H66 = nmag.MagMaterial(name='H66',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H67 = nmag.MagMaterial(name='H67',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H68 = nmag.MagMaterial(name='H68',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H69 = nmag.MagMaterial(name='H69',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H70 = nmag.MagMaterial(name='H70',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H71 = nmag.MagMaterial(name='H71',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H72 = nmag.MagMaterial(name='H72',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H73 = nmag.MagMaterial(name='H73',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H74 = nmag.MagMaterial(name='H74',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H75 = nmag.MagMaterial(name='H75',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H76 = nmag.MagMaterial(name='H76',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
H77 = nmag.MagMaterial(name='H77',
                       Ms=M_hard,
                       exchange_coupling=A_hard,
                       anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
                       llg_damping=LLG_damping)
# H78 = nmag.MagMaterial(name='H78',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H79 = nmag.MagMaterial(name='H79',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H80 = nmag.MagMaterial(name='H80',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H81 = nmag.MagMaterial(name='H81',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H82 = nmag.MagMaterial(name='H82',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H83 = nmag.MagMaterial(name='H83',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H84 = nmag.MagMaterial(name='H84',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H85 = nmag.MagMaterial(name='H85',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H86 = nmag.MagMaterial(name='H86',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H87 = nmag.MagMaterial(name='H87',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H88 = nmag.MagMaterial(name='H88',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H89 = nmag.MagMaterial(name='H89',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H90 = nmag.MagMaterial(name='H90',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H91 = nmag.MagMaterial(name='H91',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H92 = nmag.MagMaterial(name='H92',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H93 = nmag.MagMaterial(name='H93',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H94 = nmag.MagMaterial(name='H94',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H95 = nmag.MagMaterial(name='H95',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H96 = nmag.MagMaterial(name='H96',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H97 = nmag.MagMaterial(name='H97',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H98 = nmag.MagMaterial(name='H98',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H99 = nmag.MagMaterial(name='H99',
#                        Ms=M_hard,
#                        exchange_coupling=A_hard,
#                        anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                        llg_damping=LLG_damping)
# H100 = nmag.MagMaterial(name='H100',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H101 = nmag.MagMaterial(name='H101',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H102 = nmag.MagMaterial(name='H102',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H103 = nmag.MagMaterial(name='H103',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H104 = nmag.MagMaterial(name='H104',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H105 = nmag.MagMaterial(name='H105',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H106 = nmag.MagMaterial(name='H106',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H107 = nmag.MagMaterial(name='H107',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H108 = nmag.MagMaterial(name='H108',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H109 = nmag.MagMaterial(name='H109',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H110 = nmag.MagMaterial(name='H110',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H111 = nmag.MagMaterial(name='H111',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H112 = nmag.MagMaterial(name='H112',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H113 = nmag.MagMaterial(name='H113',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H114 = nmag.MagMaterial(name='H114',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H115 = nmag.MagMaterial(name='H115',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H116 = nmag.MagMaterial(name='H116',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H117 = nmag.MagMaterial(name='H117',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H118 = nmag.MagMaterial(name='H118',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H119 = nmag.MagMaterial(name='H119',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H120 = nmag.MagMaterial(name='H120',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H121 = nmag.MagMaterial(name='H121',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H122 = nmag.MagMaterial(name='H122',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H123 = nmag.MagMaterial(name='H123',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H124 = nmag.MagMaterial(name='H124',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H125 = nmag.MagMaterial(name='H125',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H126 = nmag.MagMaterial(name='H126',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H127 = nmag.MagMaterial(name='H127',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H128 = nmag.MagMaterial(name='H128',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H129 = nmag.MagMaterial(name='H129',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H130 = nmag.MagMaterial(name='H130',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H131 = nmag.MagMaterial(name='H131',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H132 = nmag.MagMaterial(name='H132',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H133 = nmag.MagMaterial(name='H133',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H134 = nmag.MagMaterial(name='H134',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H135 = nmag.MagMaterial(name='H135',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H136 = nmag.MagMaterial(name='H136',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H137 = nmag.MagMaterial(name='H137',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H138 = nmag.MagMaterial(name='H138',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H139 = nmag.MagMaterial(name='H139',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H140 = nmag.MagMaterial(name='H140',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H141 = nmag.MagMaterial(name='H141',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H142 = nmag.MagMaterial(name='H142',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H143 = nmag.MagMaterial(name='H143',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H144 = nmag.MagMaterial(name='H144',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H145 = nmag.MagMaterial(name='H145',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H146 = nmag.MagMaterial(name='H146',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H147 = nmag.MagMaterial(name='H147',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H148 = nmag.MagMaterial(name='H148',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H149 = nmag.MagMaterial(name='H149',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H150 = nmag.MagMaterial(name='H150',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H151 = nmag.MagMaterial(name='H151',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H152 = nmag.MagMaterial(name='H152',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H153 = nmag.MagMaterial(name='H153',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H154 = nmag.MagMaterial(name='H154',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H155 = nmag.MagMaterial(name='H155',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H156 = nmag.MagMaterial(name='H156',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H157 = nmag.MagMaterial(name='H157',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H158 = nmag.MagMaterial(name='H158',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H159 = nmag.MagMaterial(name='H159',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H160 = nmag.MagMaterial(name='H160',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H161 = nmag.MagMaterial(name='H161',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H162 = nmag.MagMaterial(name='H162',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H163 = nmag.MagMaterial(name='H163',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H164 = nmag.MagMaterial(name='H164',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H165 = nmag.MagMaterial(name='H165',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H166 = nmag.MagMaterial(name='H166',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H167 = nmag.MagMaterial(name='H167',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H168 = nmag.MagMaterial(name='H168',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H169 = nmag.MagMaterial(name='H169',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H170 = nmag.MagMaterial(name='H170',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H171 = nmag.MagMaterial(name='H171',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H172 = nmag.MagMaterial(name='H172',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H173 = nmag.MagMaterial(name='H173',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H174 = nmag.MagMaterial(name='H174',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H175 = nmag.MagMaterial(name='H175',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H176 = nmag.MagMaterial(name='H176',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H177 = nmag.MagMaterial(name='H177',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H178 = nmag.MagMaterial(name='H178',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H179 = nmag.MagMaterial(name='H179',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H180 = nmag.MagMaterial(name='H180',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H181 = nmag.MagMaterial(name='H181',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H182 = nmag.MagMaterial(name='H182',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H183 = nmag.MagMaterial(name='H183',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H184 = nmag.MagMaterial(name='H184',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H185 = nmag.MagMaterial(name='H185',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H186 = nmag.MagMaterial(name='H186',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H187 = nmag.MagMaterial(name='H187',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H188 = nmag.MagMaterial(name='H188',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H189 = nmag.MagMaterial(name='H189',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H190 = nmag.MagMaterial(name='H190',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H191 = nmag.MagMaterial(name='H191',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H192 = nmag.MagMaterial(name='H192',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H193 = nmag.MagMaterial(name='H193',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H194 = nmag.MagMaterial(name='H194',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H195 = nmag.MagMaterial(name='H195',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H196 = nmag.MagMaterial(name='H196',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H197 = nmag.MagMaterial(name='H197',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H198 = nmag.MagMaterial(name='H198',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H199 = nmag.MagMaterial(name='H199',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H200 = nmag.MagMaterial(name='H200',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H201 = nmag.MagMaterial(name='H201',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H202 = nmag.MagMaterial(name='H202',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H203 = nmag.MagMaterial(name='H203',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H204 = nmag.MagMaterial(name='H204',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H205 = nmag.MagMaterial(name='H205',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H206 = nmag.MagMaterial(name='H206',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H207 = nmag.MagMaterial(name='H207',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H208 = nmag.MagMaterial(name='H208',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H209 = nmag.MagMaterial(name='H209',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H210 = nmag.MagMaterial(name='H210',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H211 = nmag.MagMaterial(name='H211',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H212 = nmag.MagMaterial(name='H212',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H213 = nmag.MagMaterial(name='H213',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H214 = nmag.MagMaterial(name='H214',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H215 = nmag.MagMaterial(name='H215',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H216 = nmag.MagMaterial(name='H216',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H217 = nmag.MagMaterial(name='H217',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H218 = nmag.MagMaterial(name='H218',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H219 = nmag.MagMaterial(name='H219',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H220 = nmag.MagMaterial(name='H220',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)
# H221 = nmag.MagMaterial(name='H221',
#                         Ms=M_hard,
#                         exchange_coupling=A_hard,
#                         anisotropy=nmag.uniaxial_anisotropy(axis=KA_hard, K1=K_hard),
#                         llg_damping=LLG_damping)


sim.load_mesh("%s" % mesh_file, [
    ("H1", H1), ("H2", H2), ("H3", H3), ("H4", H4), ("H5", H5), ("H6", H6), ("H7", H7), ("H8", H8), ("H9", H9),
    ("H10", H10), ("H11", H11), ("H12", H12), ("H13", H13), ("H14", H14), ("H15", H15), ("H16", H16), ("H17", H17),
    ("H18", H18), ("H19", H19), ("H20", H20), ("H21", H21), ("H22", H22), ("H23", H23), ("H24", H24), ("H25", H25),
    ("H26", H26), ("H27", H27), ("H28", H28), ("H29", H29), ("H30", H30), ("H31", H31), ("H32", H32), ("H33", H33),
    ("H34", H34), ("H35", H35), ("H36", H36), ("H37", H37), ("H38", H38), ("H39", H39), ("H40", H40), ("H41", H41),
    ("H42", H42), ("H43", H43), ("H44", H44), ("H45", H45), ("H46", H46), ("H47", H47), ("H48", H48), ("H49", H49),
    ("H50", H50), ("H51", H51), ("H52", H52), ("H53", H53), ("H54", H54), ("H55", H55), ("H56", H56), ("H57", H57),
    ("H58", H58), ("H59", H59), ("H60", H60), ("H61", H61), ("H62", H62), ("H63", H63), ("H64", H64), ("H65", H65),
    ("H66", H66), ("H67", H67), ("H68", H68), ("H69", H69), ("H70", H70), ("H71", H71), ("H72", H72), ("H73", H73),
    ("H74", H74), ("H75", H75), ("H76", H76), ("H77", H77)], unit_length=SI(1e-9, "m"))
# --------------------------------------------------------------------------- #
# ("H42", H42), ("H43", H43), ("H44", H44), ("H45", H45), ("H46", H46), ("H47", H47), ("H48", H48), ("H49", H49),
# ("H50", H50), ("H51", H51), ("H52", H52), ("H53", H53), ("H54", H54), ("H55", H55), ("H56", H56), ("H57", H57),
# ("H58", H58), ("H59", H59), ("H60", H60), ("H61", H61), ("H62", H62), ("H63", H63), ("H64", H64), ("H65", H65),
# ("H66", H66), ("H67", H67), ("H68", H68), ("H69", H69), ("H70", H70), ("H71", H71), ("H72", H72), ("H73", H73),
# ("H74", H74), ("H75", H75), ("H76", H76), ("H77", H77), ("H78", H78), ("H79", H79), ("H80", H80), ("H81", H81),
# ("H82", H82), ("H83", H83), ("H84", H84), ("H85", H85), ("H86", H86), ("H87", H87), ("H88", H88), ("H89", H89),
# ("H90", H90), ("H91", H91), ("H92", H92), ("H93", H93), ("H94", H94), ("H95", H95), ("H96", H96), ("H97", H97),
# ("H98", H98), ("H99", H99), ("H100", H100), ("H101", H101), ("H102", H102), ("H103", H103), ("H104", H104),
# ("H105", H105), ("H106", H106), ("H107", H107), ("H108", H108), ("H109", H109), ("H110", H110), ("H111", H111),
# ("H112", H112), ("H113", H113), ("H114", H114), ("H115", H115), ("H116", H116), ("H117", H117), ("H118", H118),
# ("H119", H119), ("H120", H120), ("H121", H121), ("H122", H122), ("H123", H123), ("H124", H124), ("H125", H125),
# ("H126", H126), ("H127", H127), ("H128", H128), ("H129", H129), ("H130", H130), ("H131", H131), ("H132", H132),
# ("H133", H133), ("H134", H134), ("H135", H135), ("H136", H136), ("H137", H137), ("H138", H138), ("H139", H139),
# ("H140", H140), ("H141", H141), ("H142", H142), ("H143", H143), ("H144", H144), ("H145", H145), ("H146", H146),
# ("H147", H147), ("H148", H148), ("H149", H149), ("H150", H150), ("H151", H151), ("H152", H152), ("H153", H153),
# ("H154", H154), ("H155", H155), ("H156", H156), ("H157", H157), ("H158", H158), ("H159", H159), ("H160", H160),
# ("H161", H161), ("H162", H162), ("H163", H163), ("H164", H164), ("H165", H165), ("H166", H166), ("H167", H167),
# ("H168", H168), ("H169", H169), ("H170", H170), ("H171", H171), ("H172", H172), ("H173", H173), ("H174", H174),
# ("H175", H175), ("H176", H176), ("H177", H177), ("H178", H178), ("H179", H179), ("H180", H180), ("H181", H181),
# ("H182", H182), ("H183", H183), ("H184", H184), ("H185", H185), ("H186", H186), ("H187", H187), ("H188", H188),
# ("H189", H189), ("H190", H190), ("H191", H191), ("H192", H192), ("H193", H193), ("H194", H194), ("H195", H195),
# ("H196", H196), ("H197", H197), ("H198", H198), ("H199", H199), ("H200", H200), ("H201", H201), ("H202", H202),
# ("H203", H203), ("H204", H204), ("H205", H205), ("H206", H206), ("H207", H207), ("H208", H208), ("H209", H209),
# ("H210", H210), ("H211", H211), ("H212", H212), ("H213", H213), ("H214", H214), ("H215", H215), ("H216", H216),
# ("H217", H217), ("H218", H218), ("H219", H219), ("H220", H220), ("H221", H221)
# Max Apply Field
H_max = 2 * ku_hard * 1e4 / ms_hard
H_max = H_max * 1e3 / (4 * math.pi)  # koe to A/m
print('H_max %f A/m' % H_max)
# set initial magnetisation
sim.set_m([0, 0, 1])
sim.set_params(stopping_dm_dt=20 * degrees_per_ns)
# custom save
cube_num = 77
stage_num = 2
M_result = np.zeros((cube_num, stage_num, 3))  # create a list of list with 221 elements of matrix(3 x 3)


def my_save(sim):
    for i in range(cube_num):
        # mat_index = i + 1
        # physical_hard_index = mat_index * 2 - 1
        # physical_soft_index = mat_index * 2
        # mat_hard_name = 'H%d' % physical_hard_index
        # mat_soft_name = 'S%d' % physical_soft_index
        mat_hard_name = 'H%d' % (i + 1)
        m_hard = sim.get_subfield_average_siv('M', mat_hard_name)  # obtain M of each cube/grain
        # m_soft = sim.get_subfield_average_siv('M', mat_soft_name)
        M_result[i, sim.id + 1] = m_hard  # id ?
        # M_result[i * 2 + 1, sim.id + 1] = m_soft
    sim.save_data(fields=['id', 'time', 'step', 'stage_time', 'stage_step', 'H_ext', 'M', 'm'])

# start time
start_time = time.time()
# save initial data
sim.relax(save=[(my_save, at('convergence'))])


# make H_ext = -H_max where x >= 0
# need to modify for TDMR

# def set_H(position):      # 01
#     # positions unit is nm
#     x = position[0] / 1e-9
#     y = position[1] / 1e-9
#     z = position[2] / 1e-9
#     if (x < 0) and (x >= -20):
#         return [0, 0, -H_max]
#     elif (x >= 0) and (x <= 20):
#         return [0, 0, H_max]
#     return [0, 0, 0]
#
# sim.set_H_ext(set_H, unit=SI(1, 'A/m'))
# sim.relax(save=[(my_save, at('convergence'))])

# def set_H(position):         # 010101...
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
# sim.set_H_ext(set_H, unit=SI(1, 'A/m'))
# sim.relax(save=[(my_save, at('convergence'))])

def set_H(position):         # 40 x 40nm
    # positions unit is nm   # 1010
    x = position[0] / 1e-9   # 0101
    y = position[1] / 1e-9
    z = position[2] / 1e-9
    if (x < -20) or (y < -20):
        return [0, 0, 0]
    elif (x % 20 >= 10) and (y % 40 < 20):
        return [0, 0, -H_max]
    elif (x % 20 < 10) and (y % 40 >= 20):
        return [0, 0, -H_max]
    elif (x % 20 >= 10) and (y % 40 > 20):
        return [0, 0, H_max]
    elif (x % 20 < 10) and (y % 40 <= 20):
        return [0, 0, H_max]
    return [0, 0, 0]

sim.set_H_ext(set_H, unit=SI(1, 'A/m'))
sim.relax(save=[(my_save, at('convergence'))])
# print('------make H_ext reserve------')

# make H_ext = H_max where x >= 0
# def set_H(position):
#     # positions unit is nm
#     x = position[0] / 1e-9
#     y = position[1] / 1e-9
#     z = position[2] / 1e-9
#     if x < 0:
#         return [0, 0, 0]
#     return [0, 0, H_max]
#
#
# sim.set_H_ext(set_H, unit=SI(1, 'A/m'))
# sim.relax(save=[(my_save, at('convergence'))])

# save M_result_2
with open('Result.txt', 'w') as f:
    for i in range(cube_num):
        mat_index = i + 1
        # physical_hard_index = mat_index * 2 - 1
        # physical_soft_index = mat_index * 2
        mat_hard_name = 'H%d' % mat_index
        # mat_soft_name = 'S%d' % physical_soft_index
        line_hard = [mat_hard_name]
        # line_soft = [mat_soft_name]
        for j in range(2):
            # m_hard_2 = M_result[i * 2, j, 2]
            # m_soft_2 = M_result[i * 2 + 1, j, 2]
            # only one number in the z component in the position of jth row and 2th column
            m_hard_2 = M_result[i, j, 2]
            line_hard.append(str(m_hard_2))
            # line_soft.append(str(m_soft_2))
        f.write('\t'.join(line_hard))
        f.write('\n')
        # f.write('\t'.join(line_soft))
        # f.write('\n')
# print simulate time
use_time = (time.time() - start_time) / 60
print('Use Time %f min' % use_time)
