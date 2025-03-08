from typing import get_origin, get_args, Union

def check_allowed_types(obj, allowed_types):
    """올바른 타입인지 확인하는 함수"""
    # origin_type = get_origin(allowed_types)  # 제네릭 타입의 기본 타입 가져오기
    # if origin_type == Union:
    #     allowed_types = get_args(allowed_types)
    # elif origin_type is not None:
    #     allowed_types = origin_type  # 기본 타입으로 변경

    # if type(obj) not in allowed_types:
    #     raise TypeError(f"Invalid type: expected {allowed_types}, got {type(obj)}")
    pass