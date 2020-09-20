# Test 1
import numpy as np

a = np.arange(100)
a.reshape(10,10)
b = np.array([[1,0,0],[0,1,0],[0,0,1]])
def conv(oimg,filt):
  fh,fw = filt.shape
  ih,iw = oimg.shape 
  newimg=[]
  for j in range(0,ih-fh+1):
    newrow=[] #Column loop
    for i in range(0,iw-fw+1):
      #Row loop
      sumimg = oimg[j:j+fh,i:i+fw]
      sumcov = (sumimg*filt).sum()
      #print(sumcov)
      newrow.append(sumcov)
    newimg.append(newrow)  
  return newimg
 
 conv(a,b)



# def convimg(img,conv):
#     img_shape = img.shape
#     conv_shape = conv.shape
#     return np.array([[np.sum(img[i:i+conv_shape[0],j:j+conv_shape[1]]*conv) for j in range(img_shape[1]-conv_shape[1]+1)] for i in range(img_shape[0]-conv_shape[0]+1)])
