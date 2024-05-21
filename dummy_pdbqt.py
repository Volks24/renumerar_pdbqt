import sys
import os
import shutil

def renumber_pdbqt(input_file, output_file):
    # Leer el archivo PDBQT original
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    atom_counter = 0
    atom_indices = {}
    new_lines = []

    # Primero, renumerar los átomos y registrar los nuevos índices
    for line in lines:
        if line.startswith('ATOM') or line.startswith('HETATM'):
            # Incrementar el contador de átomos
            atom_counter += 1
            old_index = int(line[6:11].strip())
            atom_indices[old_index] = atom_counter

            # Modificar el índice en la línea
            new_line = line[:6] + f'{atom_counter:>5}' + line[11:]
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    # Ahora, actualizar las referencias en las líneas BRANCH
    final_lines = []
    for line in new_lines:
        if line.startswith('BRANCH'):
            parts = line.split()
            old_branch_indices = [int(parts[1]), int(parts[2])]
            new_branch_indices = [atom_indices[old_branch_indices[0]], atom_indices[old_branch_indices[1]]]
            new_line = f"BRANCH   {new_branch_indices[0]:>3} {new_branch_indices[1]:>3}\n"
            final_lines.append(new_line)
        else:
            final_lines.append(line)

    # Escribir el archivo PDBQT renumerado
    with open(output_file, 'w') as f:
        f.writelines(final_lines)

if __name__ == "__main__":
    # Verifica que se haya pasado un argumento (el archivo de entrada)
    if len(sys.argv) != 2:
        print("Uso: python script.py <archivo_entrada>")
        sys.exit(1)
    
    input_file = sys.argv[1]

    # Verifica si el archivo de entrada existe
    if not os.path.isfile(input_file):
        print(f"Error: el archivo {input_file} no existe.")
        sys.exit(1)

    # Define el nombre del archivo de respaldo y del archivo de salida
    base_name = os.path.splitext(input_file)[0]
    old_file = f"{base_name}_old.pdbqt"
    output_file = input_file

    # Renombra el archivo de entrada
    shutil.copy(input_file, old_file)
    
    # Llama a la función de renumeración
    renumber_pdbqt(old_file, output_file)

    print(f"El archivo {input_file} ha sido procesado y guardado como {output_file}")
    print(f"El archivo original ha sido renombrado a {old_file}")
