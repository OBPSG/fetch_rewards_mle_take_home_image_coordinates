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
    return None
