# ImageRecognition using Cluster Analysis Minkovsky formula with coef = 2

import time
start_time = time.time() #just a thing to note time, this method is kinda slow
from PIL import Image #import from Pilow package 
import numpy


# input comparable images here
im_1 = Image.open("4.jpg")        
im_2 = Image.open("4_similar.jpg")
print('\n')
print("...")



def image_comparsion(im_1, im_2):
	if im_1.size != im_2.size:
		if im_1.size > im_2.size:
			im_1 = im_1.resize((im_2.size),Image.ANTIALIAS) #downsize the image with an ANTIALIAS filter
		else:
			im_2 = im_2.resize((im_1.size),Image.ANTIALIAS)
		print("Pictures were resized")

	imArr_1 = numpy.array(im_1.getdata()).reshape(im_1.size[0], im_1.size[1], -1)
	imArr_2 = numpy.array(im_2.getdata()).reshape(im_2.size[0], im_2.size[1], -1)
	#Table with 3 colour digits inside (RGB)

	width, height = im_1.size
	coef = 2 #coef fo Minkovsky formula

	r_picture_difference = 0
	g_picture_difference = 0
	b_picture_difference = 0

	for i in range(width):
		for j in range(height):
			r_pixel_difference = numpy.average((imArr_1[i][j][0] - imArr_2[i][j][0])**coef)
			g_pixel_difference = numpy.average((imArr_1[i][j][1] - imArr_2[i][j][1])**coef)
			b_pixel_difference = numpy.average((imArr_1[i][j][2] - imArr_2[i][j][2])**coef)

			r_picture_difference += r_pixel_difference
			g_picture_difference += g_pixel_difference
			b_picture_difference += b_pixel_difference
	r_picture_difference **= 1/coef
	g_picture_difference **= 1/coef
	b_picture_difference **= 1/coef
	print("R: %d ; G: %d ; B: %d" % (r_picture_difference, g_picture_difference, b_picture_difference))
	max_difference = (width * height * 255**coef)**(1/coef)
	r_relat = (r_picture_difference/max_difference)*100
	g_relat = (g_picture_difference/max_difference)*100
	b_relat = (b_picture_difference/max_difference)*100
	print("Relative values - R: %d%%; G: %d%% ; B: %d%%" % (r_relat, g_relat, b_relat))
	print('\n')

	if r_relat == 0 and g_relat == 0 and b_relat == 0:
		print("Pictures are duplicates")
	elif r_relat <= 30 and g_relat <= 30 and b_relat <= 30:
		print("Not good, not terrible. Images are similar")
	else:
		print("This is different images")

image_comparsion(im_1,im_2)


print("--- %s seconds ---" % (time.time() - start_time))
