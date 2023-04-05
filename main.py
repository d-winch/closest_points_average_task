"""
This file contains a utility function to work with points in 2D space.
This module can be imported and used in other Python scripts for working with 2D points.

Author: David Winch
Date: April 5th, 2023

Functions:
- closest_points_average(coord, point_list, point_count): Computes the average of the closest points to a given coordinate in a list.
"""

import copy
import math

Point = tuple[float, float]


def closest_points_average(
    coord: Point, point_list: list[Point], point_count: int
) -> Point:
    """
    This function takes a coordinate, a list of points, and a number of points to consider, and returns the average (x, y) coordinates of the closest points to the given coordinate in the list.

    :param coord: A Point representing the (x, y) coordinates of the reference point.
    :type coord: tuple[float, float]
    :param point_list: A list of Points representing the (x, y) coordinates of the points to consider.
    :type point_list: list[tuple[float, float]]
    :param point_count: An integer representing the number of closest points to consider.
    :type point_count: int
    :return: A tuple representing the (x, y) coordinates of the average of the closest points.
    :rtype: tuple[float, float]
    """
    points_w_distances = [(p, math.dist(coord, p)) for p in point_list]
    points_w_distances.sort(key=lambda x: x[1])
    closest_points = points_w_distances[:point_count]
    avg_x = sum(p[0][0] for p in closest_points) / point_count
    avg_y = sum(p[0][1] for p in closest_points) / point_count
    return (avg_x, avg_y)


if __name__ == "__main__":
    points: list[Point] = [
        (8.7, 1.6),
        (7.6, 7.2),
        (9.6, 8.4),
        (9.6, 0.7),
        (1.4, 8.6),
        (5.4, 8.9),
        (7.9, 6.6),
        (5.9, 1.4),
        (8.3, 8.5),
        (1.9, 4.9),
        (8.3, 7.8),
        (7.2, 5.8),
        (7.0, 3.0),
        (1.2, 7.5),
        (8.8, 2.6),
        (9.7, 5.7),
        (2.5, 5.5),
        (1.1, 4.9),
        (5.1, 0.8),
        (5.5, 1.1),
        (6.6, 7.7),
        (3.1, 9.3),
        (1.0, 2.4),
        (3.2, 8.4),
        (8.1, 7.3),
        (0.9, 9.3),
        (4.4, 2.8),
        (8.8, 0.8),
        (2.3, 8.4),
        (1.3, 8.5),
    ]

    for i in range(0, 30, 5):
        points_without_coord = copy.copy(points)
        points_without_coord.remove(points[i])  # Remove the point we're comparing to
        print(
            f"{points[i]} -> {closest_points_average(points[i], points_without_coord, 3)}"
        )
