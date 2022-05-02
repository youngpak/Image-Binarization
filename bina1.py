import numpy as np

from PIL import Image

import matplotlib.pyplot as plt
path = '002.jpg'

image_pil = Image.open(path)
image = np.array(image_pil)

image.shape


#이미지 range 확인
np.min(image), np.max(image)


image_pil = Image.open(path).convert("L")
image_bw = np.array(image_pil)

plt.imshow(image_bw,'gray')
plt.show()