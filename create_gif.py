import imageio.v3 as iio

filenames = ["pic1.jpg", "pic2.jpg"]
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename)) #.imread() method loads an image based on the file path

iio.imwrite("sangam.gif", images, duration = 500, loop = 0)