import numpy as np
import cv2

from Rubik import Rubik

cube = Rubik()
img = cube.visualize()
img = img/255

cv2.imshow("Flattened Rubik's Cube",img)
cv2.waitKey()


rotational_log = cube.randomize()

for key,value in rotational_log.items():
    value = value/255
    value = cv2.putText(value, key, (350,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 1, cv2.LINE_AA)
    cv2.imshow("Flattened Rubik's Cube", value)
    cv2.waitKey()

cv2.destroyAllWindows()