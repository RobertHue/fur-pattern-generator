import cProfile
import subprocess
from fpg.generator.cells import Cells
import os


def main() -> None:
    x_res = 100
    y_res = 100
    cells = Cells(res=(x_res, y_res))
    cells.randomize()
    cells.develop(3, 6, w=0.5)


if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    profiler_output_file = "cells_develop.cprofile"
    profiler_file_path = os.path.join(script_directory, profiler_output_file)
    cProfile.run("main()", filename=profiler_file_path)
    subprocess.run(["snakeviz", profiler_file_path])
