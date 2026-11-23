from binding_practice import trace_bindings


def test_trace_bindings():
    result = trace_bindings()
    assert set(result) == {"first_value", "second_value", "same_object"}
    assert result["first_value"] == [30, 40]
    assert result["second_value"] == [10, 20]
    assert result["same_object"] is False
