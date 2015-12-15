"""
utility functions for gridcells
"""

# set some global vars
from pydhdt import EPSG_CODE

def gridcell2poly(cellcntr, cellsize):
    """
    Create a postGIS WKT Polygon geometry for a grid cell.  The cell
    center is given as a list of X and Y values.  The cell size is a
    list of dX and dY values.  The returned value is a string.

    Here's an example WKT Polygon string:

    ST_Polygon(
      ST_GeomFromText(
      'LINESTRING(75.15 29.53,77 29,77.6 29.5, 75.15 29.53)'),
      4326);

    (I've added line breaks to make this readable.)
    """
    xcntr, ycntr = cellcntr
    deltax, deltay = cellsize

    points = [[xcntr-deltax, ycntr+deltay], [xcntr+deltax, ycntr+deltay],
              [xcntr+deltax, ycntr-deltay], [xcntr-deltax, ycntr-deltay],
              [xcntr-deltax, ycntr+deltay]]

    coordlist = ["{0} {1}".format(x[0], x[1]) for x in points]
    coordstr = ",".join(coordlist)
    wktstr = "ST_Polygon(ST_GeomFromText('LINESTRING({0}),{1})".format(
        coordstr, EPSG_CODE)

    return wktstr

