def trace_bindings() -> dict:
    first = [10, 20]
    second = first
    first = [30, 40]

    return {
        "first_value": first,
        "second_value": second,
        "same_object": first is second,
    }
