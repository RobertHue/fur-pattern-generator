import bpy


class PropertySettings(bpy.types.PropertyGroup):
    r_activator: bpy.props.IntProperty(  # type: ignore
        name="Radius Of Activator", default=3, min=0, max=10
    )
    r_inhibitor: bpy.props.IntProperty(  # type: ignore
        name="Radius Of Inhibitor", default=6, min=0, max=10
    )
    w: bpy.props.FloatProperty(  # type: ignore
        name="Inhibitor Weight w", default=0.42, min=0.0, max=1.0
    )
    color_D: bpy.props.FloatVectorProperty(  # type: ignore
        name="color_D",
        subtype="COLOR",
        size=4,
        min=0.0,
        max=1.0,
        default=(0.0, 0.0, 0.0, 1.0),
    )
    color_U: bpy.props.FloatVectorProperty(  # type: ignore
        name="color_U",
        subtype="COLOR",
        size=4,
        min=0.0,
        max=1.0,
        default=(1.0, 1.0, 1.0, 1.0),
    )


def register():
    bpy.utils.register_class(PropertySettings)
    bpy.types.Material.my_settings = bpy.props.PointerProperty(
        type=PropertySettings
    )


def unregister():
    bpy.utils.unregister_class(PropertySettings)
