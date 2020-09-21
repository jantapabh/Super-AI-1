import numpy as np

# arr = ([0, 1, 2],[3,4,5],[6,7,8]) #สร้างอาเรย์ 3*3
# print(arr) #แสดงค่า
# a = arr[0:1]
# print(a)

# //CODE1

# size = 16
# filter_row = 3
# filter_col = 5

# img = np.random.randint(0, 10, size=(size,size))
# filter = np.random.randint(0, 10, size=(filter_row,filter_col))

# res = np.zeros(shape=(size - filter_row + 1, size - filter_col + 1))

# for i in range(size - filter_row + 1):
#   for j in range(size - filter_col + 1):
#     res[i,j] = np.multiply(img[i:i+filter_row, j:j+filter_col], filter).sum()

# res

#CODE2

def conv(img, kernel):
    (img_h, img_w) = img.shape
    (kernel_h, kernel_w) = kernel.shape
    img_temp = np.zeros((img_h - kernel_h + 1, img_w - kernel_w + 1), dtype='int16')
    for i in range(img_h - kernel_h + 1):
        for j in range(img_w - kernel_w + 1):
            roi = img[i:i+kernel_h, j:j+kernel_w]
            value = (roi * kernel).sum()
            img_temp[i, j] = value
    return img_temp
img_filtered = conv(img,kernel)
img_filtered
