# This file is only here to avoid the following error inside VSC:
#
# ImportError: attempted relative import with no known parent package
#
# This happens due to blender not calling this addon as a package
# See: https://napuzba.com/a/import-error-relative-no-parent
#

print(
    f"""
	__file__={__file__:<35}
	__name__={__name__:<20}
	__package__={__package__!s:<20}
	"""
)
