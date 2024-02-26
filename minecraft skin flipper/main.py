from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import sizes as s
import functions as fun

img = np.asarray(Image.open('skin.png'))
img = s.size(img, 'alex')
img['body_front'] = fun.flip(img['body_front'], 'x')
plt.imshow(img['body_front'])
plt.show()
