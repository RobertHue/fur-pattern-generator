# fur_pattern_generator

![Python](https://img.shields.io/badge/python-3.10+-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build](https://github.com/RobertHue/fur_pattern_generator/actions/workflows/ci-test.yml/badge.svg?branch=master)](https://github.com/RobertHue/fur_pattern_generator/actions/workflows/ci-test.yml)

With this blender add-on you can generate textures in the shape of the stripes
and dots on animals, such as leopards and tigers.

The algorithm used for it is the one defined by David Young. It is based on
cellular automata and is simulating the pigment-cells (melanocytes) inside of
mammals, that are sending out activator and inhibitor genes into their
neighborhood cells:

- https://users.math.yale.edu/public_html/People/frame/Fractals/Panorama/Biology/Leopard/Leopard.html
- http://ccl.northwestern.edu/netlogo/models/Fur

## Table of Contents

- [fur\_pattern\_generator](#fur_pattern_generator)
  - [Table of Contents](#table-of-contents)
  - [Repository structure](#repository-structure)
  - [Getting Started](#getting-started)
    - [Installation prerequisites](#installation-prerequisites)
  - [Usage](#usage)
  - [Development](#development)
    - [Good to know](#good-to-know)
    - [Coding Conventions](#coding-conventions)
    - [Visual Studio Code](#visual-studio-code)
      - [Hints](#hints)

## Repository structure

The repository is structured as follows:

- `.vscode/`: workspace configuration for [VSCode]
- `fpg/`: Python package containing the modules of the fur pattern generator
- `tests/`: contains unit tests for this project (still TBD)
- `poetry.lock`: lock file for [Poetry]
- `pyproject.toml`: configuration file for [Poetry]
- `README.md`: the README file that you are reading right now

## Getting Started

### Installation prerequisites

- [Git]
- [VSCode]
- [Python] (see `pyproject.toml` for it's version)
- Install [Poetry], as follows:

   ```console
   python -m pip install --upgrade pip
   python -m pip install --user pipx
   python -m pipx ensurepath
   pipx install poetry
   ```

To install these dependencies, just execute the following command:

   ```console
   poetry install
   ```

## Usage

Go into UV-Editor and create an image by hitting `New Image`.
It is recommended to choose low resolution, because the algorithm is not yet optimized enough.

After that you can generate a `Random Noise` or let the CA young pattern generator run by hitting `CA Young`:

![example](docs/example.png)

---

## Development

This section serves rather as a knowledge-base for developers,
who want to test this addon. So have fun and fiddle with it.

### Good to know

- https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Addons
- https://docs.blender.org/api/2.83/bpy.props.html

### Coding Conventions

- https://www.gdquest.com/docs/guidelines/best-practices/blender-python/
- https://realpython.com/absolute-vs-relative-python-imports/
- https://b3d.interplanety.org/en/class-naming-conventions-in-blender-2-8-python-api/

### Visual Studio Code

I recommend that you use Visual Studio Code, because it offers convenient
development features such as autocomplete, syntax highlighting, integration
with version control systems and other tools that make development faster
and easier:

- https://b3d.interplanety.org/en/using-microsoft-visual-studio-code-as-external-ide-for-writing-blender-scripts-add-ons/
- https://youtu.be/q06-hER7Y1Q
- https://medium.com/@m3lles/how-to-hide-unwanted-folders-and-files-in-visual-studio-code-2bb0f39c4251

#### Hints

- Please install the recommended plugins for VSCode (located in `.vscode/settings.json`).

- For testing changes in your addon really quick, just reload the addon with F1:

   ```console
   Blender: Reload Addons`
   ```

- For debugging your addon, you can also use normal or conditional break-points.

[Git]: https://git-scm.com/downloads
[Python]: https://www.python.org/
[VSCode]: https://code.visualstudio.com/
[Poetry]: https://python-poetry.org/
