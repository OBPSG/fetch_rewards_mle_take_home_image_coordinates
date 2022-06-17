from typing import List, Tuple
from pydantic import BaseModel

class Point(BaseModel):
    x: float
    y: float

class Dimensions(BaseModel):
    height: int
    width: int

class Point_Set_Dimensions(BaseModel):
    p1: Point
    p2: Point
    p3: Point
    p4: Point
    dimensions: Dimensions

class Output(BaseModel):
    points: List[List[Tuple[float, float]]]

def min_max_xy(points):
    """
    This function takes in a list of four point tuples that represent the corner points of an image area rectangle
    ex: [(0, 0), (3, 0), (0, 3), (3, 3)]
    and returns a tuple containing the minimum and maximum x and y coordinates
    """
    return (min(points[0][0], points[1][0], points[2][0], points[3][0]),
            max(points[0][0], points[1][0], points[2][0], points[3][0]),
            min(points[0][1], points[1][1], points[2][1], points[3][1]),
            max(points[0][1], points[1][1], points[2][1], points[3][1])
    )


def generate_points(min_x: float, max_x: float, min_y: float, max_y: float, num_cols: int, num_rows: int):
    """
    Function generate_points is called after min_max_xy
    Takes in a set of four floats representing the minimum and maximum x and y coordinates,
    plus a pair of ints for the number of rows and columns in the pixel grid
    and returns a two-dimensional list of point tuples for the final pixel coordinates
    """
    point_set = []
    x_step = (max_x - min_x)/(num_cols - 1)
    y_step = (max_y - min_y)/(num_rows - 1) 
    y_pos = min_y
    for i in range(num_rows):
        point_set.append([])
        x_pos = min_x
        for j in range(num_cols):
            point_tuple = (x_pos, y_pos)
            point_set[i].append(point_tuple)
            x_pos += x_step
        y_pos += y_step

    return point_set
