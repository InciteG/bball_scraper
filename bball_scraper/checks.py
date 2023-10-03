from typing import Dict, Iterable, List, Optional, Set, Tuple, Union

def check_value(
    value_name: str,
    value,
    valid_values: List
):
    if value not in valid_values:
        raise ValueError(f"{value_name} must be one of {valid_values}" )
    else:
        pass

def check_not_value(
    value_name: str,
    value,
    invalid_values: List
):
    if value in invalid_values:
        raise ValueError(f"{value_name} cannot be {invalid_values}" )
    else:
        pass