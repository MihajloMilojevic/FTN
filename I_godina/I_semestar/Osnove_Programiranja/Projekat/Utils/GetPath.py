import os


def get_relative_path(path_from_root: list[str]) -> str:
    path = os.path.dirname(__file__)
    path = os.path.join(path, "..")
    for p in path_from_root:
        path = os.path.join(path, p)
    # print(path)
    return path
