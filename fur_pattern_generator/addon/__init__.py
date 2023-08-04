import bpy

print(
    """
	__file__={0:<35}
	__name__={1:<20}
	__package__={2:<20}
	""".format(
        __file__, __name__, str(__package__)
    )
)

from . import fur_pattern_generator, operators, panels, properties


def register():
    operators.register()
    panels.register()
    properties.register()


def unregister():
    operators.unregister()
    panels.unregister()
    properties.unregister()
