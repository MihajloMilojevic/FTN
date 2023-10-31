import os

def GetRelativePath(path_from_root: list[str]) -> str:
    cur_path = os.path.dirname(__file__)
    file_path = "\\".join(path_from_root);
    new_path = os.path.relpath(f'.\\{file_path}', cur_path)
    return new_path