import bpy
import colorsys

import numpy as np
import random
from multiprocessing import Pool
from multiprocessing import cpu_count
from cv2 import cv2



class Cells:
	"""
	This class defines the cells of the CA
	"""

	def __init__(self, image, color_D):
		self.width  = image.width()
		self.height = image.height()
		self.disc = [[0.0
			for i in range(self.width)]
			for j in range(self.height)]

		self.visited = [[0
			for i in range(self.width)]
			for j in range(self.height)]

		self.cells = [["D"
			if image.getPixel_HSV(i,j)[0] == color_D[0] and
			   image.getPixel_HSV(i,j)[1] == color_D[1] and
			   image.getPixel_HSV(i,j)[2] == color_D[2]
			else 'U'
			for i in range(self.width)]
			for j in range(self.height)]

	def setDisc(self, u, v, disc):
		self.disc[v][u] = disc

	def getDisc(self, u, v):
		return self.disc[v][u]


	def increaseVisits(self, u, v):
		self.visited[v][u] += 1

	def setVisited(self, u, v):
		self.visited[v][u] = 1

	def gotVisited(self, u, v):
		if self.visited[v][u] > 0:
			return True
		else:
			return False

	def resetVisited(self):
		self.visited = [[0 for i in range(self.width)]
			for j in range(self.height)]

	def set(self, u, v, state):
		self.cells[v][u] = state

	def get(self, u, v):
		return self.cells[v][u]

	def reset(self):
		self.cells = [[0 for i in range(self.width)]
			for j in range(self.height)]

	def print(self):
		print()
		print("print: ")
		for row in self.cells[::-1]:
			print('[', end='')
			for val in row:
				print('{:1}'.format(val), end='')
			print(']')
		print()

	def printVisits(self):
		print()
		print("printVisits: ")
		for row in self.visited[::-1]:
			print('[', end='')
			for val in row:
				if (val >= 1):
					print('{:2}'.format(val), end='')
				elif (val == 0):
					print('{:2}'.format(' '), end='')
				else:
					print('{:2}'.format('E'), end='')
			print(']')
		print()

	def printDiscs(self):
		print()
		print("printDiscs: ")
		for row in self.disc[::-1]:
			print('[', end='')
			for d in row:
				if (d > 0):
					print('{:2}'.format('+'), end='')
				elif (d < 0):
					print('{:2}'.format('-'), end='')
				else:
					print('{:2}'.format(' '), end='')
			print(']')
		print()



class Image:
	"""
	Pass an image file loaded into Blender when creating an Image-object.
	"""
	def __init__(self, image_file):
		self._img = bpy.data.images[image_file]

	def width(self):
		return self._img.size[0]

	def height(self):
		return self._img.size[1]

	def export_CV(self):
		pixelList = list(self._img.pixels)
		# print("pixelList : ", pixelList)
		# print("len(pixelList): ", len(pixelList))
		rgbPixels = [x for i, x in enumerate(pixelList) if (i+1)%4 != 0]
		a = np.array(rgbPixels)
		# print("a : ", a)
		# print("len(a): ", len(a))
		b = np.reshape(a, (self.height(), self.width(), 3))
		# print("b : ", b)
		# print("len(b): ", len(b))
		rgba = np.ones((self.height(), self.width(), 3), dtype=np.uint8)
		rgba[:,:,:] = np.uint8(b) * 255
		cv_image = np.flip(rgba, axis=[0, 2])
		# print("cv_image: ", cv_image)
		# print("len(cv_image): ", len(cv_image))
		return np.float32(cv_image)

	def import_CV(self, cv_image):
		rgb = np.flip(cv_image, axis=[0, 2])
		rgba = np.ones((self.height(), self.width(), 4), dtype=np.float32)
		rgba[:,:,:-1] = np.float32(rgb) / 255
		self._img.pixels = rgba.flatten()

	def isValidCoord(self, x, y):
		"""
		Returns 'True', if the supplied coordinates
		are in the Image. Otherwhise returns 'False'.
		"""
		if x >= 0 and x < self._img.size[0] and \
		   y >= 0 and y < self._img.size[1]:
			return True
		return False

	def getPixel_RGBA(self, x, y):
		"""
		Gets the pixel's color at 'x' 'y' as RGBA.
		If no valid coords 'x' and 'y' are supplied, then [0,0,0,0] is returned.
		"""
		if self.isValidCoord(x, y):
			index = (y * self.width() + x) * 4
			cell = self._img.pixels[index:index+4]
			return cell
		return [0,0,0,0]

	def getPixel_HSV(self, x, y):
		"""
		Gets the pixel's color at 'x' 'y' as HSV.
		If no valid coords 'x' and 'y' are supplied, then [0,0,0,0] is returned.
		"""
		rgba = self.getPixel_RGBA(x, y)
		hsv  = colorsys.rgb_to_hsv(rgba[0], rgba[1], rgba[2])
		return hsv

	def setPixel_RGBA(self, x, y, RGBA):
		"""
		Sets the pixel's color at 'x' 'y' with RGBA.
		If no valid coords 'x' and 'y' are supplied, then only 'False' is returned.
		"""
		if self.isValidCoord(x, y):
			index = (y * self.width() + x) * 4
			self._img.pixels[index:index+4] = RGBA
			return True
		return False

	def setPixel_HSV(self, x, y, HSV):
		"""
		Sets the pixel's color at 'x' 'y' with HSV.
		If no valid coords 'x' and 'y' are supplied, then only 'False' is returned.
		"""
		rgb  = colorsys.hsv_to_rgb(HSV[0], HSV[1], HSV[2])
		rgba = list(rgb)
		rgba.append(1)
		return self.setPixel_RGBA(x, y, rgba)



def drawCircle(image, color, x, y, radius):
	"""
	draws a circle into image
	"""
	# Reading an image in default mode
	cv_img = (image.export_CV())

	# draw a circle as mask
	center_coordinates = (x, y)
	thickness = 1
	new_img = cv2.circle(cv_img, center_coordinates, radius, color, thickness)

	# write back image with circle into image
	image.import_CV(new_img)



def getCircularNeighborhood(image, x, y, radius):
	"""
	Returns a list of pixels inside a region
	"""
	# Reading an image in default mode
	# cv_img = image.export_CV()

	# create mask with zeros
	mask = np.zeros((image.height(), image.width(), 3), dtype=np.uint8)

	# define a circle as mask
	center_coordinates = (x, y)
	color = (255,255,255)
	thickness = cv2.FILLED
	cv2.circle(mask, center_coordinates, radius, color, thickness)
	n = np.argwhere(mask == (255,255,255))
	return n



def getManhattanNeighborhood(image, cells, x, y, radius):
	lookup = [[1,0],[-1,0],[0,1],[0,-1], [1,1], [-1,-1], [1,-1], [1,-1]] # moore-neighboorhood
	# lookup = [[1,0],[-1,0],[0,1],[0,-1]]
	n = []

	# mark all the pixels as not visited
	cells.resetVisited()

	# create a queue for BFS
	queue = []

	# are valid coords inside the image:
	if image.isValidCoord(x, y) == False:
		return n

	# Mark the source node as
	# visited and enqueue it
	coords = [x,y]
	n = [coords]
	cells.increaseVisits(x, y)
	queue.append(coords)

	while radius >= 0 and queue:
		level_size = len(queue)

		while level_size > 0:
			level_size -= 1

			# dequeue a vertex from queue and print it
			s = queue.pop(0)
			n += [s]

			if not queue:
				radius -= 1

			# get all adjacent pixels of dequeued pixel s
			# if a adjacen has not been visited, then mark it visited and enqueue it
			for l in lookup:
				new_x = s[0] + l[0]
				new_y = s[1] + l[1]

				# are valid coords inside the image:
				if image.isValidCoord(new_x, new_y) == False:
					continue

				# cell got already visited
				if cells.gotVisited(new_x, new_y) == True:
					continue

				coords = [new_x, new_y]
				queue.append(coords)
				cells.setVisited(new_x, new_y)
				# cells.printVisits()
				# print()
		radius -= 1
	return n



def countDCells(image, cells, x, y, radius):
	"""
	Counts the D cells in a given Radius.
	@param cells 	empty cell-set that adds additional info to the image
	@param x 		x pos of the center
	@param y 		y pos of the center
	@param radius	radius
	"""
	cellCount = 0

	regionList = getManhattanNeighborhood(image, cells, x, y, radius)
	# print("regionList: ", regionList)


	for r in regionList:
		# update coords:
		x = r[0]
		y = r[1]

		# get pixel
		cellInfo = cells.get(x, y)
		if cellInfo == "D":
			cellCount += 1

	# print("cellCount: ", cellCount)
	return cellCount


def rgb2hsv(rgb):
	hsv = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
	return list(hsv)


def generate_random(image, rgb_color_D, rgb_color_U):
	# create random image
	color_D = rgb2hsv(rgb_color_D)
	color_U = rgb2hsv(rgb_color_U)
	print("color_D: ", color_D)
	print("color_U: ", color_U)

	for u in range(image.height()):
		for v in range(image.width()):
			rand = random.randint(0,1)
			if rand == 0:
				image.setPixel_HSV(u, v, color_D)
			else:
				image.setPixel_HSV(u, v, color_U)



def CA_young(image, r_activator, r_inhibitor, w, rgb_color_D, rgb_color_U):
	# we need to know the image dimensions
	width  = image.width()
	height = image.height()
	print("Image size: ", width, " x ", height)
	print("w: ", w)

	color_D = rgb2hsv(rgb_color_D)
	color_U = rgb2hsv(rgb_color_U)
	print("color_D: ", color_D)
	print("color_U: ", color_U)

	cells = Cells(image, color_D)
	# cells.printDiscs()
	# cells.print()
	# 1st pass : calculate cells Disc and apply cells-set
	print("1st pass start")
	for u in range(height):
		for v in range(width):
			cells.resetVisited()
			AD = countDCells(image, cells, u, v, r_activator)
			# cells.printVisits()

			cells.resetVisited()
			ID = countDCells(image, cells, u, v, r_inhibitor) - AD
			# cells.printVisits()

			# This computation happens to all cells at the same time,
			# therefore we must defer the setting of the color to a 2nd step.
			disc = AD - w * ID
			cells.setDisc(u, v, disc)
	# debug-output:
	# print("disc = AD - w * ID")
	# print(disc, " = ", AD, " - ", w, " * ", ID)
	# print(disc, " = ", AD, " - ", w * ID)
	# print(disc, " = ", AD - w * ID)
	cells.printDiscs()
	cells.print()
	#cells.printVisits()
	print("2nd pass start")
	# 2nd pass : apply cells to image:
	for u in range(height):
		for v in range(width):
			d = cells.getDisc(u, v)
			if (d > 0):
				cells.set(u, v, "D")
				image.setPixel_HSV(u, v, color_D)
			elif (d < 0):
				cells.set(u, v, "U")
				image.setPixel_HSV(u, v, color_U)
	cells.printDiscs()
	cells.print()
	print("finished")
