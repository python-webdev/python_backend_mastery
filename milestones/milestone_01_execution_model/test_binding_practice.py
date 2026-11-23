from binding_practice import trace_bindings


def test_trace_binding():
    result = trace_bindings()
    assert set(result) == {"first_value", "second_value", "same_object"}


def test_trace_bindings_identity():
    result = trace_bindings()
    assert result["same_object"] is False
