import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'C:\Users\devah\Desktop\Images\IMG_20250817_172832_270.jpg')

padded_img = cv2.copyMakeBorder(img, 50, 50, 100, 100, cv2.BORDER_CONSTANT, value=(0, 0, 0))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(padded_img, cv2.COLOR_BGR2RGB))
plt.title("Padded with Black")
plt.show()


