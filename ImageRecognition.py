# ImageRecognition using Cluster Analysis (Minkovsky formula) V1.0
import time
start_time = time.time()
from PIL import Image #impor from Pilow package 
import numpy

im_1 = Image.open("15.jpg")  #opening image as Image class
print("Image 1: ", im_1.format, im_1.size, im_1.mode) #image file format, image size in pixels, image "mode"
im_2 = Image.open("15_modification.jpg")
print("Image 2: ", im_2.format, im_2.size, im_2.mode)
print('\n')

#im_1.show() #showing the image in Windows Photo


def image_comparsion(im_1, im_2):
	if im_1.size != im_2.size:
		if im_1.size > im_2.size:
			im_1 = im_1.resize((im_2.size),Image.ANTIALIAS) #downsize the image with an ANTIALIAS filter
		else:
			im_2 = im_2.resize((im_1.size),Image.ANTIALIAS)

	imArr_1 = numpy.array(im_1.getdata()).reshape(im_1.size[0], im_1.size[1], -1)
	imArr_2 = numpy.array(im_2.getdata()).reshape(im_2.size[0], im_2.size[1], -1)
	#Table with 3 colour digits inside (RGB)

	width, height = im_1.size
	r_coef = 2 #coef fo Minkovsky formula

	r_picture_difference = 0
	g_picture_difference = 0
	b_picture_difference = 0

	for i in range(width):
		for j in range(height):
			r_pixel_difference = numpy.average((imArr_1[i][j][0] - imArr_2[i][j][0])**r_coef)
			g_pixel_difference = numpy.average((imArr_1[i][j][1] - imArr_2[i][j][1])**r_coef)
			b_pixel_difference = numpy.average((imArr_1[i][j][2] - imArr_2[i][j][2])**r_coef)

			r_picture_difference += r_pixel_difference
			g_picture_difference += g_pixel_difference
			b_picture_difference += b_pixel_difference
	r_picture_difference **= 1/r_coef
	g_picture_difference **= 1/r_coef
	b_picture_difference **= 1/r_coef
	print("R: %d ; G: %d ; B: %d" % (r_picture_difference, g_picture_difference, b_picture_difference))
	max_difference = (width * height * 255**r_coef)**(1/r_coef)
	print("Relative values - R: %d%%; G: %d%% ; B: %d%%" % (((r_picture_difference/max_difference)*100), 
													  ((g_picture_difference/max_difference)*100), 
													  ((b_picture_difference/max_difference)*100)))

image_comparsion(im_1,im_2)


print("--- %s seconds ---" % (time.time() - start_time))