import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from statistics import variance as varn
import time

import os
os.chdir('C:\\Users\Tamim\Stat Project Codes\Input Images')

start=time.time()

def triplet(a,b,c, thres):
    if a >= thres and b >= thres and c >= thres:
        return 255
    else:
        return 0

image=plt.imread('text28.jpeg')

p,q,r=image.shape
Z=np.zeros((p,q), dtype=np.int32)
if image.max() >1:
    for i in range(p):
        for j in range(q):
            Z[i,j] +=triplet(image[i,j][0], image[i,j][1], image[i,j][2], 143)
else:
    for i in range(p):
        for j in range(q):
            Z[i,j] +=triplet(image[i,j][0], image[i,j][1], image[i,j][2], 0.560784)


plt.imshow(Z, cmap='gray', interpolation='hanning')
plt.axis('off')
plt.savefig('rewritten8.jpg', bbox_inches='tight')
img=plt.imread('rewritten8.jpg')

def function(image):
    grayimg=np.dot(image[...,:3],[1/2, 1/4 , 1/4])
    return grayimg

def countvar(image, angle, thres1, thres2):
    rotated_image= ndimage.rotate(image, angle, cval=1)
    grayimg=function(rotated_image)
    (h,w)= grayimg.shape
    ls=[]
    for i in range(h):
        count=0
        for j in range(w-1):
            if thres1 <= abs(grayimg[i, j+1]-grayimg[i,j]) <= thres2:
                count +=1
        ls.append(count)
    var= varn(ls)
    return var

thres1,thres2= 45, 170
fnlist=[countvar(img, 0.5*angle, thres1,thres2) for angle in range(0,360)]
B=max(fnlist)
m= 0.5*fnlist.index(B)

def adjust(angle):
    if angle <= 90:
        return angle
    else:
        return angle + 180

def thikangle(angle):
    if angle <= 90:
        return -angle
    else:
        return 180-angle

fig, ax = plt.subplots(ncols=2, figsize=(20, 20))
ax[0].imshow(image, cmap='gray')
ax[1].imshow(ndimage.rotate(image, adjust(m)), cmap='gray')
plt.show()

end=time.time()

print('Skew about the positive X-axis is about :', thikangle(m), 'degrees')
print(end-start)

