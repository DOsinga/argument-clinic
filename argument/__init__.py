#!/usr/bin/env python
from __future__ import print_function

from argparse import ArgumentParser
import inspect
import docstring_parser


def not_empty(value):
    return value and value != inspect.Signature.empty

def entrypoint(func):
    doc = inspect.getdoc(func)
    doc_parsed = docstring_parser.parse(doc)
    sig = inspect.signature(func)
    description = doc_parsed.short_description
    if doc_parsed.long_description:
        description += '\n\n' + doc_parsed.short_description

    parser = ArgumentParser(description=description)

    arg_help = {param.arg_name: param.description for param in doc_parsed.params}
    for par_name, par_info in sig.parameters.items():
        kwargs = {}
        if par_name in arg_help:
            kwargs['help'] = arg_help[par_name]
        if not_empty(par_info.annotation):
            kwargs['type'] = par_info.annotation
        if not_empty(par_info.default):
            kwargs['default'] = par_info.default
        elif par_info.kind == inspect.Parameter.KEYWORD_ONLY:
            kwargs['required'] = True
        arg_name = par_name
        if par_info.kind == inspect.Parameter.KEYWORD_ONLY:
            arg_name = '--' + arg_name
        parser.add_argument(arg_name, **kwargs)
    args = parser.parse_args()

    def wrapper():
        return func(**vars(args))
    return wrapper
