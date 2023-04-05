import pytest
from main import closest_points_average, Point


def test_closest_points_average_simple():
    points: list[Point] = [(0.0, 0.0), (1.0, 1.0), (2.0, 2.0)]
    coord: Point = (0, 1)
    x, y = closest_points_average(coord=coord, point_list=points, point_count=3)
    assert x == 1
    assert y == 1


def test_closest_points_float():
    points: list[Point] = [(8.8, 0.8), (8.8, 2.6), (9.6, 0.7)]
    coord: Point = (8.7, 1.6)
    x, y = closest_points_average(coord=coord, point_list=points, point_count=3)
    assert x == pytest.approx(9.06, 0.1)
    assert y == pytest.approx(1.36, 0.1)


def test_closest_points_average_with_negative_values():
    points: list[Point] = [(-1.0, -1.0), (1.0, 1.0), (0.0, 0.0)]
    coord: Point = (0, 0)
    x, y = closest_points_average(coord=coord, point_list=points, point_count=3)

    assert x == 0
    assert y == 0


def test_closest_points_average_with_same_points():
    points: list[Point] = [(1.0, 1.0), (1.0, 1.0), (1.0, 1.0)]
    coord: Point = (1, 1)
    x, y = closest_points_average(coord=coord, point_list=points, point_count=3)

    assert x == 1
    assert y == 1


def test_closest_points_average_recurring():
    points: list[Point] = [(0.0, 0.0), (1.0, 1.0), (3.0, 3.0)]
    coord: Point = (0, 1)
    x, y = closest_points_average(coord=coord, point_list=points, point_count=3)

    assert x == pytest.approx(1.3, 0.2)
    assert y == pytest.approx(1.3, 0.2)


def test_closest_points_average_given_points():
    points: list[Point] = [
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
    coord: Point = (8.7, 1.6)
    x, y = closest_points_average(coord=coord, point_list=points, point_count=3)
    assert x == pytest.approx(9.06, 0.1)
    assert y == pytest.approx(1.36, 0.1)
