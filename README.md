Description :

Ce projet implémente un système de détection faciale en temps réel utilisant la webcam. Il repose sur la cascade de Haar d'OpenCV pour identifier les visages et les encadrer avec des rectangles colorés. Le programme affiche également un compteur du nombre de visages détectés.

Fonctionnalités :

- Capture vidéo en direct depuis la webcam

- Détection faciale via le classifieur Haar Cascade

- Encadrement des visages en vert lime (limegreen)

- Affichage du compteur en bleu ciel (deepskyblue)

- Arrêt propre avec la touche q

Technologies Utilisées :

- Python 3

- OpenCV (cv2) pour le traitement d'image

- Matplotlib pour la conversion des couleurs


Comment ça marche ?

Le programme initialise la webcam et configure la résolution.

Chaque image est convertie en niveaux de gris pour la détection.

Les visages détectés sont entourés de rectangles et numérotés.

Un compteur en temps réel indique le nombre de visages.

L'application s'arrête proprement lors de l'appui sur q.
