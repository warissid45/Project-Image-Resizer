image resizer project

import cv2

scale_percent = int(input("Enter scale percent: "))
image = cv2.imread('imagegrad.jpg')
cv2.imshow('title', image)

destination = 'ImageResizerProject.png'
new_width = int(image.shape[1]*scale_percent/100)
new_height = int(image.shape[0]*scale_percent/100)

new = (new_width, new_height)

output = cv2.resize(image, new)
cv2.imwrite(destination, output)
cv2.waitKey(0)



