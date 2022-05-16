import numpy as np
import cv2

from Rubik import Rubik

cube = Rubik()
img = cube.visualize()
img = img/255

cv2.imshow("Flattened Rubik's Cube",img)
cv2.waitKey()
cv2.destroyAllWindows()