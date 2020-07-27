import time 
import cv2
import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image
print('Imports complete')

cap = cv2.VideoCapture(0)
prev = []
run = True

frames = []
fps_list = []
while run:
    bef = time.time()
    ret, current = cap.read()
    grey = np.asarray(cv2.cvtColor(current, cv2.COLOR_BGR2GRAY))
    if prev == []:
        pass
    else:
        modified = 255-(grey - prev)
        modified[modified > 200] = 0
        cv2.imshow('Motion', modified)
    time.sleep(0.022)
    prev = grey
    aft = time.time()
    fps_list.append(1/(aft-bef))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        run = False

x = [i+1 for i in range(len(fps_list))]
plt.plot(x, fps_list, color = 'orange', linewidth = 0.8)
plt.title(f'{round(np.average(fps_list),1)}')
plt.show()