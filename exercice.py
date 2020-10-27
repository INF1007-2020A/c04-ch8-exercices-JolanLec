#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def comparaison_fichier(file1, file2):
    if file1 != file2:
        with open(file1, 'r', encoding= "utf-8") as f1, open(file2, 'r', encoding="urf-8") as f2:
            for index, line1 in enumerate(f1):
                line2= f2.readline()

                if line1 != line2:
                    print("les fichiers sont différents! À la ligne {index + 1 }, on a:")
                    print(line1)
                    print("et on a:")
                    print(line2)
                    break

def triple_les_espaces(input_file, output_file):
    with open(input_file, 'r', encoding= "utf-8") as in_file, open(outpu_file, 'w', encoding="utf-8") as out_file:
        for line in in_file:
            words= line.split()
            line_triple = "   ".join(words)
            out_file.write(line_triple)
            # ou juste comme ca:
            # out_file.write(line.replace(" ", "   "))

def note_lettre(file_path, result_file_path):
    with open(file_path, 'r', encoding= "utf-8") as f, open(result_file_path.txt, 'w', encoding= "utf-8") as f_correspondance:
        notes_pourcentage = f.readlines()

    for note in notes_pourcentage:
        for key, value in PERCENTAGE_TO_LETTER.items():
            if value[0] <= note <= value[]




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
