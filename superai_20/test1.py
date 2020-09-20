# Test 1
#

import numpy as np

a = np.arange(100)
a.reshape(10,10)
print(a)

b = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(b)




# def convimg(img,conv):
#     img_shape = img.shape
#     conv_shape = conv.shape
#     return np.array([[np.sum(img[i:i+conv_shape[0],j:j+conv_shape[1]]*conv) for j in range(img_shape[1]-conv_shape[1]+1)] for i in range(img_shape[0]-conv_shape[0]+1)])
