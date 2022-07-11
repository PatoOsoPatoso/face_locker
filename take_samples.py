import os
import cv2
import shutil
from pathlib import Path

db_path = str(Path(os.path.dirname(os.path.realpath(__file__)) + '/database').resolve())

directions = [' DE FRENTE - ENTER  ', 'HACIA ARRIBA - ENTER', 'HACIA ABAJO - ENTER ', 'LA IZQUIERDA - ENTER', 'LA DERECHA - ENTER']

def check_database():
    if not os.path.exists(db_path):
        os.mkdir(db_path)

def check_name():
    names = os.listdir(db_path)

    option = input("Give me the name: ")

    if not option:
        print("[ERROR] - There has to be a name to proceed..")
        exit(1)

    if option in names:
        print("[ERROR] - The name can't be in use.")
        exit(1)
    
    os.mkdir(Path(db_path + f"/{option}").resolve())

    return option

def main():
    check_database()

    option = check_name()

    cam = cv2.VideoCapture(0)

    start = False
    cont = 1
    step = 0

    while True:
        _, frame = cam.read()
        _, aux = cam.read()

        cv2.putText(aux, directions[step], (140, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 250), 2, cv2.LINE_AA)

        cv2.putText(aux, f"{cont-1}/100", (280, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 250, 250), 2, cv2.LINE_AA)

        cv2.imshow('aux', aux)

        if step == 4 and cont == 101:
            print("Todo completado, hasta luego!")
            exit()

        if cont == 101:
            start = False
            cont = 1
            step += 1

        if start:
            cv2.imwrite(str(Path(db_path + f'/{option}/{step}_{cont}.png').resolve()), frame)
            cont += 1

        if cv2.waitKey(1) == 13 and cont == 1:
            start = True
        
        if cv2.waitKey(1) == 27:
            shutil.rmtree(str(Path(db_path + f'/{option}').resolve()))
            print("Operación cancelada con éxito!")
            exit()


if __name__ == "__main__":
    main()