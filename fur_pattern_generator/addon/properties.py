import bpy

class PropertySettings(bpy.types.PropertyGroup):

	w: bpy.props.FloatProperty(
		name="Incubator Weight w",
		default=0.69,
		min=0.0,
		max=1.0
	)
	color_D: bpy.props.FloatVectorProperty(
		name="color_D",
		subtype="COLOR",
		size=4,
		min=0.0,
		max=1.0,
		default=(0.0, 0.0, 0.0, 1.0)
	)
	color_U: bpy.props.FloatVectorProperty(
		name="color_U",
		subtype="COLOR",
		size=4,
		min=0.0,
		max=1.0,
		default=(1.0, 1.0, 1.0, 1.0)
	)

def register():
	bpy.utils.register_class(PropertySettings)
	bpy.types.Material.my_settings = bpy.props.PointerProperty(type=PropertySettings)

def unregister():
	bpy.utils.unregister_class(PropertySettings)
