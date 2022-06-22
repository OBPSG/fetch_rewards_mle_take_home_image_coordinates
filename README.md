---
# Author: Andrew Beaudrie#
# Date: 6/9/2022# 
# For: Fetch Rewards Machine Learning Apprenticeship Application#
## Project Overview: Image Pixel Coordinate Calculator ##
## https://fetch-hiring.s3.amazonaws.com/machine-learning-engineer/image-coordinates.html ##
---
Description: A Web API that accepts POST Requests for calculating pixel coordinates for rendering an image. It takes requests that include floating-point coordinates representing the bounding corners of  the image, and a pair of integers for the number of pixel rows and pixel columns in the image to be rendered. It returns a matrix (nested 2D JSON array) of points as the result.

Details: The web service is made in Python using FastAPI with Pydantic for model-based validation of inputs and formatting of outputs.
The Docker image is built using the official Python 3.9 image as its base.

To build a local copy of the Docker Image, simply use the build command in the docker CLI using the dockerfile provided.
When running the container, make certain to publish port 8000 inside the container and map it to 8000 outside.
And to make POST Request, use either Postman, a similar web API driver, or the Swagger UI by navigating to the //docs# endpoint in a browser.
The expected format for the JSON object of the request body is as follows:
```
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
```

To run the App outside of a container, navigate to the src directory and use the following command:
```
uvicorn main:app --reload
```
Per the Uvicorn docuementation, the --reload flag should only be used in development environments.

To run the unit tests, open the solution file (.sln) in Visual Studio. Then, in the solution explorer, right-click the calculator_test module and select "Start without debugging"