# This file is only here to avoid the following error inside VSC:
#
# ImportError: attempted relative import with no known parent package
#
# This happens due to blender not calling this addon as a package
# See: https://napuzba.com/a/import-error-relative-no-parent
#

print("""
	__file__={0:<35}
	__name__={1:<20}
	__package__={2:<20}
	"""
	.format(__file__,__name__,str(__package__))
)

import fur_pattern_generator
