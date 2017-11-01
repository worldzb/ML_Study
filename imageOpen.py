from PIL import Image;
import matplotlib.pyplot as plt

img=Image.open('./image/test.png')
plt.figure("dog");
plt.axis('off')
plt.imshow(img)
plt.show()