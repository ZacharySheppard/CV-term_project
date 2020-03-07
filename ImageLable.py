import os

augmented = True
folder = "up"

if augmented:
    file = "/home/mark/Documents/Term 8/Image Processing/ImageLable/" + folder + "/" + 'augmented/'
else:
    file = "/home/mark/Documents/Term 8/Image Processing/ImageLable/" + folder + "/"

i = 0

for filename in os.listdir(file):
    if filename == 'augmented':
        continue
    name = folder + str(i) + ".png"
    source = file + filename
    name = file + name
    os.rename(source, name)
    i += 1
