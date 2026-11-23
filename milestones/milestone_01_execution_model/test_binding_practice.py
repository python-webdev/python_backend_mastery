from binding_practice import trace_binding


def test_trace_binding():
    result = trace_binding()
    assert result["first_value"] == [30, 40]
    assert result["second_value"] == [10, 20]


def test_trace_bindings_identity():
    result = trace_binding()
    assert result["same_object"] is False
