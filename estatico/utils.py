from pathlib import Path


def rm_tree(pth):
    pth = Path(pth)
    for child in pth.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()


def retrieve_str_path(path, filename):
    filepath = path / filename
    return str(filepath.resolve())
