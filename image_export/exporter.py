from PIL import Image
from PIL import ImageDraw

from grid import Grid
from image_export.to_png import ToPNG
from algorithms.binary_tree import BinaryTree
from algorithms.sidewinder import Sidewinder
from algorithms.prims import Prim
from algorithms.kruskals import Kruskal
from algorithms.wilsons import Wilson
from algorithms.recursive import Recursive

def export():
    grid = Grid(30, 20)

    # BinaryTree().generate(grid)

    # Sidewinder().generate(grid)

    # Prim().generate(grid)

    # Wilson().generate(grid)

    kruskal = Kruskal(grid)
    kruskal.generate(grid)

    # Recursive().generate(grid)

    render = ToPNG(grid, 20)
    image = render.render()
    image2 = render.render_color()

if __name__ == '__main__':
    export()