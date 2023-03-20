import importlib
from pathlib import Path
import argparse
import ast
from . import TransformationsManager


def main():
    parser = argparse.ArgumentParser(
        prog=Path(__file__).parent.name, description="Python obfuscator"
    )
    parser.add_argument("file")
    arguments = parser.parse_args()

    for file in (Path(__file__).resolve().parent / "transformations").glob("*.py"):
        importlib.import_module(
            f".transformations.{file.name[:-3]}", package=__package__
        )

    t_manager = TransformationsManager(
        tree=ast.parse(
            open(arguments.file).read(),
            file,
        )
    )
    t_manager.apply_transformations()
    print(ast.unparse(t_manager.tree))


if __name__ == "__main__":
    exit(main())
