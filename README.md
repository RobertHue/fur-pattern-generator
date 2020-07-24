# fur_pattern_generator
This is a blender add-on for generating fur textures.

You can generate textures with it, that use a Cellular Automata to simulate
the stripes and dots on animals such as leopards and tigers.

The algorithm used for it is the one defined by David Young, that is based on cellular automata:
- https://users.math.yale.edu/public_html/People/frame/Fractals/Panorama/Biology/Leopard/Leopard.html
- https://users.math.yale.edu/public_html/People/frame/Fractals/CA/welcome.html



## future goals:
This project is *still under development*.

### User-Friendly
- the user is able to use a menu to alter the weighting or the shape of
activator/inhibator
- register/unregister functions to install the addon

### Quality-Assurance
- tests, that verify the proper functioning

### Features
- Image UV-Editor Side-Menu entry

## Development

### Coding Conventions used:
- https://www.gdquest.com/docs/guidelines/best-practices/blender-python/
- https://realpython.com/absolute-vs-relative-python-imports/

### Visual Studio Code

I recommend that you use Visual Studio Code, because it offers convenient
development features such as autocomplete, syntax highlighting, integration
with version control systems and other tools that make development faster
and easier:

- https://b3d.interplanety.org/en/using-microsoft-visual-studio-code-as-external-ide-for-writing-blender-scripts-add-ons/
- https://youtu.be/q06-hER7Y1Q
- https://medium.com/@m3lles/how-to-hide-unwanted-folders-and-files-in-visual-studio-code-2bb0f39c4251

### Install pip

1. Download `get-pip.py` and store it inside your blender-python folder
2. Execute the pip-installer:

`./python.exe get-pip.py`

### Install fake-bpy

To get rid of following pylint(import-error)
> Unable to import 'bpy'

- Install fake-bpy:

`./python.exe -m pip install fake-bpy-module-2.83`
