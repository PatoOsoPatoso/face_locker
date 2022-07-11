import os
import cv2
import pickle
import face_recognition
from pathlib import Path
from imutils import paths
from alive_progress import alive_bar

print("[INFO] - Cargando imágenes...")
imagePaths = list(paths.list_images(str(Path(os.path.dirname(os.path.realpath(__file__)) + '/database').resolve())))

knownEncodings = []
knownNames = []

with alive_bar(len(imagePaths), dual_line=True, title='[INFO] - Procesando imagenes') as bar:
    for (i, imagePath) in enumerate(imagePaths):
        name = imagePath.split(os.path.sep)[-2]
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model="cnn")
        encodings = face_recognition.face_encodings(rgb, boxes)
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)
        bar()

print("[INFO] - Serializando encodings...")
data = {"encodings": knownEncodings, "names": knownNames}
f = open("face_encodings", "wb")
f.write(pickle.dumps(data))
f.close()

print("[+] - Todas las operaciones finalizadas exitosamente")
