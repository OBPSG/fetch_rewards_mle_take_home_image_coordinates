from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pydantic.types import Json
import calculator
import json
from typing import List, Tuple

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/image_coordinates/")
async def intro():
    return {"message": "Use Postman, a similar web API driver, or navigate to the /docs# endpoint to make a POST request"}


@app.post("/image_coordinates")
async def calculate(input: calculator.Point_Set_Dimensions):
    """
    Method that handles POST Requests for image coordinate calculation
    The expected format for the JSON object of the request body is as follows:
    {
        //corner points
        "p1": {
            "x": integer for the x coodinate
            "y": integer for the y coordinate
        },
        "p2" : {
            "x": integer for the x coodinate
            "y": integer for the y coordinate
        },
        "p3": {
            "x": integer for the x coodinate
            "y": integer for the y coordinate
        },
        "p4": {
            "x": integer for the x coodinate
            "y": integer for the y coordinate
        }

        dimensions; {
            "height": integer representing the number of pixel rows in the image grid
            "width": integer representing the number of pixel columns in the image grid
        }
    }
    """
    bounds_tuple = calculator.min_max_xy([
        (input.p1.x, input.p1.y),
        (input.p2.x, input.p2.y),
        (input.p3.x, input.p3.y),
        (input.p4.x, input.p4.y)])

    result = calculator.generate_points(
        bounds_tuple[0],
        bounds_tuple[1],
        bounds_tuple[2],
        bounds_tuple[3],
        input.dimensions.width,
        input.dimensions.height
        )

    return result