from pathlib import Path


def open_file(file_path: Path):

    try:
        f = open(file_path, "r")
        contents = f.read()
    except Exception as e:
        raise RuntimeError(f"It was not possible to load {file_path}")
    else:
        f.close()
    return contents
