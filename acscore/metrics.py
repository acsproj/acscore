from .metric.file_length import FileLength
from .metric.function_name_case import FunctionNameCase
from .metric.nesting_loops import NestingLoops
from .metric.class_name_case import ClassNameCase
from .metric.indent_type import IndentType
from .metric.quotes_type import QuotesType
from .metric.spaces_near_round_brackets import SpacesNearRoundBrackets
from .metric.spaces_near_braces import SpacesNearBraces
from .metric.spaces_near_square_brackets import SpacesNearSquareBrackets
from .metric.import_order import ImportOrder
from .metric.blank_before_function import BlankBeforeFunction
from .metric.blank_before_class import BlankBeforeClass
from .metric.blank_before_method import BlankBeforeMethod

IMPLEMENTED_METRICS = [
    FileLength.__name__,
    FunctionNameCase.__name__,
    NestingLoops.__name__,
    ClassNameCase.__name__,
    IndentType.__name__,
    QuotesType.__name__,
    SpacesNearRoundBrackets.__name__,
    SpacesNearBraces.__name__,
    SpacesNearSquareBrackets.__name__,
    ImportOrder.__name__,
    BlankBeforeFunction.__name__,
    BlankBeforeClass.__name__,
    BlankBeforeMethod.__name__,
]
