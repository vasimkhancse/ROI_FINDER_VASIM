"""
Rectangle Area Calculation Module
Calculates the area of a rectangle ROI: Area = width * height (px² / px2).
"""


def calculate_area(coordinates):
    """
    Calculate rectangle area:
    width = max(x) - min(x)
    height = max(y) - min(y)
    Area = width * height (px²)
    """
    xs = [p[0] for p in coordinates]
    ys = [p[1] for p in coordinates]

    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    area = width * height

    return area, width, height
