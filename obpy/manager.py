from typing import List
import ast


class TransformationsManager:
    transformations: List[ast.NodeTransformer] = []

    def __init__(self, tree: ast.AST):
        self.tree = tree

    @classmethod
    def register_transformer(cls, transformer: ast.NodeTransformer):
        cls.transformations.append(transformer)
        return transformer

    def apply_transformations(self) -> ast.AST:
        for transformation in self.transformations:
            self.tree = ast.fix_missing_locations(transformation().visit(self.tree))
        return self.tree
