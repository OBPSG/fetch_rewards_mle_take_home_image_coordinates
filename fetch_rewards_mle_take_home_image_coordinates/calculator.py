from pydantic import BaseModel

class Point(BaseModel):
    x: float
    y: float

class Dimensions(BaseModel):
    height: int
    width: int

class Point_Set_Simensions(BaseModel):
    p1: Point
    p2: Point
    p3: Point
    p4: Point
    dimensions: Dimensions

def generate_points(min_x: float, max_x: float, min_y: float, max_y: float, num_cols: int, num_rows: int):
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
