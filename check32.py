"""CS 32 helper library for Act I, Scene II"""


def check_arg(arg: object, ttype: type, arg_name: str):
    if not isinstance(arg, ttype):
        raise TypeError(
            f"The argument {arg_name} is of type {type(arg)}, but this function requires {ttype}"
        )
