import bpy
from bpy.utils import register_class, unregister_class

print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(
	__file__,__name__,str(__package__)))

from . import fur_pattern_generator, operators

classes = (
	operators.FUR_PATTERN_GENERATOR_OT_ca_young,
	operators.FUR_PATTERN_GENERATOR_OT_generate_random
)

def register():
	for cls in classes:
		register_class(cls)

def unregister():
	for cls in classes:
		unregister_class(cls)
