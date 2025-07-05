import pathlib
import cv2

# Charge le modèle de détection faciale
cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
clf = cv2.CascadeClassifier(str(cascade_path))

# Initialise la webcam
camera = cv2.VideoCapture(0)

try:
    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Détection des visages
        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)  # Parenthèse fermante ajoutée ici
        
        # Dessine un rectangle autour des visages
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        cv2.imshow("Détection Faciale", frame)
        
        # Quitter avec la touche 'q'
        if cv2.waitKey(1) == ord('q'):
            break

finally:
    camera.release()
    cv2.destroyAllWindows()
