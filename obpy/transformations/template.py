from .. import TransformationsManager
import ast


@TransformationsManager.register_transformer
class _(ast.NodeTransformer):
    def visit_AST(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Add(self, node: ast.AST) -> ast.AST:
        return node

    def visit_And(self, node: ast.AST) -> ast.AST:
        return node

    def visit_AnnAssign(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Assert(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Assign(self, node: ast.AST) -> ast.AST:
        return node

    def visit_AsyncFor(self, node: ast.AST) -> ast.AST:
        return node

    def visit_AsyncFunctionDef(self, node: ast.AST) -> ast.AST:
        return node

    def visit_AsyncWith(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Attribute(self, node: ast.AST) -> ast.AST:
        return node

    def visit_AugAssign(self, node: ast.AST) -> ast.AST:
        return node

    def visit_AugLoad(self, node: ast.AST) -> ast.AST:
        return node

    def visit_AugStore(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Await(self, node: ast.AST) -> ast.AST:
        return node

    def visit_BinOp(self, node: ast.AST) -> ast.AST:
        return node

    def visit_BitAnd(self, node: ast.AST) -> ast.AST:
        return node

    def visit_BitOr(self, node: ast.AST) -> ast.AST:
        return node

    def visit_BitXor(self, node: ast.AST) -> ast.AST:
        return node

    def visit_BoolOp(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Break(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Bytes(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Call(self, node: ast.AST) -> ast.AST:
        return node

    def visit_ClassDef(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Compare(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Constant(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Continue(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Del(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Delete(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Dict(self, node: ast.AST) -> ast.AST:
        return node

    def visit_DictComp(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Div(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Ellipsis(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Eq(self, node: ast.AST) -> ast.AST:
        return node

    def visit_ExceptHandler(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Expr(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Expression(self, node: ast.AST) -> ast.AST:
        return node

    def visit_ExtSlice(self, node: ast.AST) -> ast.AST:
        return node

    def visit_FloorDiv(self, node: ast.AST) -> ast.AST:
        return node

    def visit_For(self, node: ast.AST) -> ast.AST:
        return node

    def visit_FormattedValue(self, node: ast.AST) -> ast.AST:
        return node

    def visit_FunctionDef(self, node: ast.AST) -> ast.AST:
        return node

    def visit_FunctionType(self, node: ast.AST) -> ast.AST:
        return node

    def visit_GeneratorExp(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Global(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Gt(self, node: ast.AST) -> ast.AST:
        return node

    def visit_GtE(self, node: ast.AST) -> ast.AST:
        return node

    def visit_If(self, node: ast.AST) -> ast.AST:
        return node

    def visit_IfExp(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Import(self, node: ast.AST) -> ast.AST:
        return node

    def visit_ImportFrom(self, node: ast.AST) -> ast.AST:
        return node

    def visit_In(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Index(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Interactive(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Invert(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Is(self, node: ast.AST) -> ast.AST:
        return node

    def visit_IsNot(self, node: ast.AST) -> ast.AST:
        return node

    def visit_JoinedStr(self, node: ast.AST) -> ast.AST:
        return node

    def visit_LShift(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Lambda(self, node: ast.AST) -> ast.AST:
        return node

    def visit_List(self, node: ast.AST) -> ast.AST:
        return node

    def visit_ListComp(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Load(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Lt(self, node: ast.AST) -> ast.AST:
        return node

    def visit_LtE(self, node: ast.AST) -> ast.AST:
        return node

    def visit_MatMult(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Match(self, node: ast.AST) -> ast.AST:
        return node

    def visit_MatchAs(self, node: ast.AST) -> ast.AST:
        return node

    def visit_MatchClass(self, node: ast.AST) -> ast.AST:
        return node

    def visit_MatchMapping(self, node: ast.AST) -> ast.AST:
        return node

    def visit_MatchOr(self, node: ast.AST) -> ast.AST:
        return node

    def visit_MatchSequence(self, node: ast.AST) -> ast.AST:
        return node

    def visit_MatchSingleton(self, node: ast.AST) -> ast.AST:
        return node

    def visit_MatchStar(self, node: ast.AST) -> ast.AST:
        return node

    def visit_MatchValue(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Mod(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Module(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Mult(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Name(self, node: ast.AST) -> ast.AST:
        return node

    def visit_NameConstant(self, node: ast.AST) -> ast.AST:
        return node

    def visit_NamedExpr(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Nonlocal(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Not(self, node: ast.AST) -> ast.AST:
        return node

    def visit_NotEq(self, node: ast.AST) -> ast.AST:
        return node

    def visit_NotIn(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Num(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Or(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Param(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Pass(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Pow(self, node: ast.AST) -> ast.AST:
        return node

    def visit_RShift(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Raise(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Return(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Set(self, node: ast.AST) -> ast.AST:
        return node

    def visit_SetComp(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Slice(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Starred(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Store(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Str(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Sub(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Subscript(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Suite(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Try(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Tuple(self, node: ast.AST) -> ast.AST:
        return node

    def visit_TypeIgnore(self, node: ast.AST) -> ast.AST:
        return node

    def visit_UAdd(self, node: ast.AST) -> ast.AST:
        return node

    def visit_USub(self, node: ast.AST) -> ast.AST:
        return node

    def visit_UnaryOp(self, node: ast.AST) -> ast.AST:
        return node

    def visit_While(self, node: ast.AST) -> ast.AST:
        return node

    def visit_With(self, node: ast.AST) -> ast.AST:
        return node

    def visit_Yield(self, node: ast.AST) -> ast.AST:
        return node

    def visit_YieldFrom(self, node: ast.AST) -> ast.AST:
        return node

    def visit_alias(self, node: ast.AST) -> ast.AST:
        return node

    def visit_arg(self, node: ast.AST) -> ast.AST:
        return node

    def visit_arguments(self, node: ast.AST) -> ast.AST:
        return node

    def visit_boolop(self, node: ast.AST) -> ast.AST:
        return node

    def visit_cmpop(self, node: ast.AST) -> ast.AST:
        return node

    def visit_comprehension(self, node: ast.AST) -> ast.AST:
        return node

    def visit_excepthandler(self, node: ast.AST) -> ast.AST:
        return node

    def visit_expr(self, node: ast.AST) -> ast.AST:
        return node

    def visit_expr_context(self, node: ast.AST) -> ast.AST:
        return node

    def visit_keyword(self, node: ast.AST) -> ast.AST:
        return node

    def visit_match_case(self, node: ast.AST) -> ast.AST:
        return node

    def visit_mod(self, node: ast.AST) -> ast.AST:
        return node

    def visit_operator(self, node: ast.AST) -> ast.AST:
        return node

    def visit_pattern(self, node: ast.AST) -> ast.AST:
        return node

    def visit_slice(self, node: ast.AST) -> ast.AST:
        return node

    def visit_stmt(self, node: ast.AST) -> ast.AST:
        return node

    def visit_type_ignore(self, node: ast.AST) -> ast.AST:
        return node

    def visit_unaryop(self, node: ast.AST) -> ast.AST:
        return node

    def visit_withitem(self, node: ast.AST) -> ast.AST:
        return node
