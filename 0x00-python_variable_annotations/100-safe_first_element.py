#!/usr/bin/env python3
""" edit annotation"""


from typing import Any
# The types of the elements of the input are not known


def safe_first_element(lst: Any) -> Any:
    if lst:
        return lst[0]
    else:
        return None
