import copy
import math

Point = tuple[float, float]


def closest_points_average(
    coord: Point, point_list: list[Point], point_count: int
) -> Point:
    list_p = [(p, math.dist(coord, p)) for p in point_list]
    list_p.sort(key=lambda x: x[1])
    closest_points = list_p[:point_count]
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
        points_without_coord.remove(points[i])
        print(
            f"{points[i]} -> {closest_points_average(points[i], points_without_coord, 3)}"
        )
