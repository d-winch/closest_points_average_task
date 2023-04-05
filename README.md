# Average X Y Coordinate Task

The main file contains a utility function for working with points in 2D space.\
The test file contains a number of example pytest tests.

**Author:** David Winch\
**Date:** April 5th, 2023

## Functions
`closest_points_average(coord, point_list, point_count)`\
Computes the average x and y of the closest points to a given coordinate in a list.

`coord`: A Point representing the (x, y) coordinates of the reference point.\
`point_list`: A list of Points representing the (x, y) coordinates of the points to consider.
`point_count`: An integer representing the number of closest points to consider.\
`return`: A tuple representing the (x, y) coordinates of the average of the closest points.


### Notes
I changed the function from using a global point list to taking one as a parameter.\
I also added the `point_count` variable so that the code could be used to calculate based on n closest points.

I also assumed in the example running of the code that it should not consider the given reference point in the list of points, so I made a copy of the point list and removed the reference point before running the function, as below.

```
for i in range(0, 30, 5):
    points_without_coord = copy.copy(points)
    points_without_coord.remove(points[i])  # Remove the point we're comparing to
    print(
        f"{points[i]} -> {closest_points_average(points[i], points_without_coord, 3)}"
    )
```
