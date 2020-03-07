import os

folder = '/home/mark/Documents/Term 8/Image Processing/ImageLable/all/'
arr = []

for filename in os.listdir(folder):

    name, file_extension = os.path.splitext(filename)
    if 'down' in name:
        arr.append(0)

    elif 'up' in name:
        arr.append(1)

    elif 'go' in name:
        arr.append(2)

    elif 'stop' in name:
        arr.append(3)

    elif 'okay' in name:
        arr.append(4)

print(arr)
