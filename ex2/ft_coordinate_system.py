import math


def parse_coords(coords_str: str) -> tuple:
    if not coords_str:
        raise ValueError("No coordinates provided!")
    lst = [int(x) for x in coords_str.split(",")]
    if len(lst) != 3:
        raise ValueError(f"Expected 3 coordinates, got {len(lst)}")
    return tuple(lst)


def calc_distance(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def show_coords(coords_str: str, is_first: bool = False) -> None:
    try:
        position = parse_coords(coords_str)
        dist = calc_distance((0, 0, 0), position)
        if is_first:
            print(f"Position created: {position}")
        else:
            print(f'Parsing coordinates: "{coords_str}"')
            print(f"Parsed position: {position}")
        print(f"Distance between (0, 0, 0) and {position}: {round(dist, 2)}")
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{coords_str}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")


def show_unpacking(coords_str: str) -> None:
    try:
        x, y, z = parse_coords(coords_str)
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    show_coords("10,20,5", True)
    print()
    show_coords("3,4,0")
    print()
    show_coords("abc,def,ghi")
    print()
    show_unpacking("3,4,0")
