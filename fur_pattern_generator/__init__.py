# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
	"name" : "fur_pattern_generator",
	"author" : "RobertHue",
	"description" : "",
	"blender" : (2, 80, 0),
	"version" : (0, 0, 1),
	"location" : "",
	"warning" : "",
	"category" : "Generic"
}

print("""
	__file__={0:<35}
	__name__={1:<20}
	__package__={2:<20}
	"""
	.format(__file__,__name__,str(__package__))
)

from . import addon


def register():
	addon.register()


def unregister():
	addon.unregister()

# if __name__ == "__main__":
# 	obj = bpy.context.object
# 	if obj:
# 		me = obj.data
# 		if me.uv_textures.active is not None:
# 			for tf in me.uv_textures.active.data:
# 				if tf.image:
# 					img = tf.image.name
# 					print(img)
# 	# image = Image("Image.png")

# 	# # create random image
# 	# for u in range(image.height()):
# 	# 	for v in range(image.width()):
# 	# 		image.setPixel_HSV(u, v, [0,0,random.randint(0,1)])

# 	# CA_young(image)

# 	print("FINISHED")
