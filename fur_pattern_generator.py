import bpy
import colorsys
import numpy as np
import random
from multiprocessing import Pool
from multiprocessing import cpu_count


class Cells:
	"""
	This class defines the cells of the CA
	"""

	def __init__(self, image):
		self.width  = image.width()
		self.height = image.height()
		
		self.visited = [[0 
			for i in range(self.width)] 
			for j in range(self.height)]
			
		self.cells = [["D" if image.getPixel_HSV(i,j)[2] < 0.2 else 'U' 
			for i in range(self.width)] 
			for j in range(self.height)]

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
		for row in self.cells[::-1]:
			print('[', end='')
			for val in row:
				print('{:1}'.format(val), end='')
			print(']')
		print()
		
	def printVisits(self):
		print()
		for row in self.visited[::-1]:
			print('[', end='')
			for val in row:
				print('{:1}'.format(val), end='')
			print(']')
		print()



class Image:
	"""
	Pass an image file loaded into Blender when creating an Image-object.
	"""
	def __init__(self, image_file):
		self.img = bpy.data.images[image_file]
		
	def width(self):
		return self.img.size[0]
	
	def height(self):
		return self.img.size[1]
		
	def isValidCoord(self, x, y):
		"""
		Returns 'True', if the supplied coordinates 
		are in the Image. Otherwhise returns 'False'.
		"""
		if x >= 0 and x < self.img.size[0] and \
		   y >= 0 and y < self.img.size[1]:
			return True
		return False

	def getPixel_RGBA(self, x, y):
		"""
		Gets the pixel's color at 'x' 'y' as RGBA.
		If no valid coords 'x' and 'y' are supplied, then [0,0,0,0] is returned.
		"""
		if self.isValidCoord(x, y):
			index = (y * self.width() + x) * 4
			cell = self.img.pixels[index:index+4]
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
			self.img.pixels[index:index+4] = RGBA
			return True
		return False
	 
	def setPixel_HSV(self, x, y, HSV):
		""" 
		Sets the pixel's color at 'x' 'y' with HSV.
		If no valid coords 'x' and 'y' are supplied, then only 'False' is returned.
		"""
		rgb  = colorsys.hsv_to_rgb(HSV[0], HSV[1], HSV[2])
		rgba = [v for v in rgb]
		rgba.append(1)
		return self.setPixel_RGBA(x, y, rgba)



def countDCells(image, cells, x, y, mh_radius):
	"""
	Counts the D cells in a given Radius.
	@param cells 		empty cell-set that adds additional info to the image
	@param x 			x pos of the center
	@param y 			y pos of the center
	@param mh_radius	manhattan radius
	"""
	cellCount = 0
	
	# cell got already visited
	if cells.gotVisited(x, y) == True:
		return 0
	
	# is valid coords:
	if image.isValidCoord(x, y) == False:
		return 0	
	
	# recursion break-condition
	if mh_radius < 0:
		return 0
		
	# get pixel
	cellInfo = cells.get(x, y)
	if cellInfo == "D":
#		print("D-Cell at : (", x, ", ", y, ")", " inside r: ", mh_radius)
		cellCount += 1
#	else:
#		print("U-Cell at : (", x, ", ", y, ")", " inside r: ", mh_radius)
		
	# set cell to visited
	cells.increaseVisits(x, y) 
	
	# print("hsv: ", HSV)
	stillToVisit = []
	lookup = [ [1,0], [-1,0], [0,1], [0,-1] ]
	
	if mh_radius == 0:
		return cellCount
	
	for l in lookup:		
		loc_x = x + l[0]
		loc_y = y + l[1]
#		print("look at : (", loc_x, ", ", loc_y, ")")
		
		# stop at border; no wrap-around!!!
		# and if cell is still unvisited
		if  image.isValidCoord(loc_x, loc_y) and \
			cells.gotVisited(loc_x, loc_y) == False:
#			print("investigate at : (", loc_x, ", ", loc_y, ")")
			
			# remember still to visit pixels
			stillToVisit.append([loc_x, loc_y])
#			cellCount += countDCells(img, cells, loc_x, loc_y, mh_radius-1)

	# visit remembered pixels with smaller radius and increase cellCount
	for s in stillToVisit:
		# recursion:
		cellCount += countDCells(image, cells, s[0], s[1], mh_radius-1)
		#print("~ cellCount : ", cellCount)
	return cellCount



def CA_young(image):
	width  = image.width()
	height = image.height()
	
	# we need to know the image dimensions
	print ("Image size: ", width, " x ", height)

	cells = Cells(image)
	# 1st pass : calculate cells Disc and apply cells-set
	print("1st pass start")
	for u in range(height):
		for v in range(width):
#			print("### visit pixel: (", u, ", ", v, ")")
			cells.resetVisited()
			AD = countDCells(image, cells, u, v, 3)
#			cells.printVisits()
			cells.resetVisited()
			ID = countDCells(image, cells, u, v, 6) - AD
#			cells.printVisits()
			w=0.69
			Disc = AD - w * ID
			
			if (Disc > 0):
#				print("### formula: ", Disc, " = ", AD, " - ", w, " * ", ID)
				cells.set(u, v, "D")
			elif (Disc < 0):
#				print("### formula: ", Disc, " = ", AD, " - ", w, " * ", ID)
				cells.set(u, v, "U")
					
	print("2nd pass start")
	# 2nd pass : apply cells to image:
	for u in range(height):
		for v in range(width):
			if cells.get(u, v) == "D":
				image.setPixel_HSV(u, v, [0,0,0])
			elif cells.get(u, v) == "U":
				image.setPixel_HSV(u, v, [0.05,0.8,1.0] )
			
#	cells.print()



if __name__ == "__main__":

	image = Image("Image.png")

	# create random image
	for u in range(image.height()):
		for v in range(image.width()):
			image.setPixel_HSV(u, v, [0,0,random.randint(0,1)])
				
	CA_young(image)
	
	
	
	
	print("FINISHED")
	