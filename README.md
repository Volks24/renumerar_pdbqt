renumera los archivos pdbqt.dum para usar en bias_docking en autodock GPU
Uso: python dummy_pdbqt.py <archivo_entrada>.pdbqt

input
REMARK  4 active torsions:
REMARK  status: ('A' for Active; 'I' for Inactive)
REMARK    1  A    between atoms: C3_4329  and  C10_4336 
REMARK    2  A    between atoms: C10_4336  and  C1'_4337 
REMARK    3  A    between atoms: C4'_4340  and  N4'_4348 
REMARK    4  A    between atoms: N1'_4343  and  C11_4344 
ROOT
HETATM    1  C1' SU2 A1001       8.751   1.717  -8.855  1.00 54.37     0.000 A 
HETATM    2  C2' SU2 A1001      10.093   1.464  -9.109  1.00 58.87     0.002 A 
HETATM    3  C3' SU2 A1001      10.492   0.289  -9.748  1.00 60.77     0.017 A 
HETATM    4  C4' SU2 A1001       9.555  -0.660 -10.144  1.00 62.10     0.056 A 
HETATM    5  C5' SU2 A1001       8.211  -0.402  -9.884  1.00 57.95     0.017 A 
HETATM    6  C6' SU2 A1001       7.812   0.774  -9.247  1.00 56.28     0.002 A 
HETATM   26  CM  SU2 A1001       9.152   0.530  -9.498  1.00  0.00     0.000 AC
ENDROOT
BRANCH   1   7
HETATM    7  C10 SU2 A1001       8.350   3.008  -8.149  1.00 47.02     0.005 C 
BRANCH   7   8

output
REMARK  4 active torsions:
REMARK  status: ('A' for Active; 'I' for Inactive)
REMARK    1  A    between atoms: C3_4329  and  C10_4336 
REMARK    2  A    between atoms: C10_4336  and  C1'_4337 
REMARK    3  A    between atoms: C4'_4340  and  N4'_4348 
REMARK    4  A    between atoms: N1'_4343  and  C11_4344 
ROOT
HETATM    1  C1' SU2 A1001       8.751   1.717  -8.855  1.00 54.37     0.000 A 
HETATM    2  C2' SU2 A1001      10.093   1.464  -9.109  1.00 58.87     0.002 A 
HETATM    3  C3' SU2 A1001      10.492   0.289  -9.748  1.00 60.77     0.017 A 
HETATM    4  C4' SU2 A1001       9.555  -0.660 -10.144  1.00 62.10     0.056 A 
HETATM    5  C5' SU2 A1001       8.211  -0.402  -9.884  1.00 57.95     0.017 A 
HETATM    6  C6' SU2 A1001       7.812   0.774  -9.247  1.00 56.28     0.002 A 
HETATM    7  CM  SU2 A1001       9.152   0.530  -9.498  1.00  0.00     0.000 AC
ENDROOT
BRANCH     1   8
HETATM    8  C10 SU2 A1001       8.350   3.008  -8.149  1.00 47.02     0.005 C 
BRANCH     8   9
