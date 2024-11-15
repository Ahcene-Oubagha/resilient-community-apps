#
# Unit tests for fn_splunk_integration/components/function_utils.py
#
#   100% code coverage
#
from resilient_lib import IntegrationError
from fn_splunk_integration.util.function_utils import make_query_string, make_item_dict

def test_query_string():
    print("Testing query string substitution....")
    input_string = "index = %param1% source=%param2% AND %param3%=%param4%"
    params = ["_internal", "*splunkd*", "clientip", "127.0.0.1"]

    query = make_query_string(input_string, params)
    expect = "index = _internal source=*splunkd* AND clientip=127.0.0.1"

    assert query == expect

def test_make_item_dict():
    print("Testing make_item_dict")
    params = ["field1", "value1",
              "field2", "value2",
              "field3", "value3"]

    item_dict = make_item_dict(params)
    assert item_dict["field1"] == params[1] and item_dict["field2"] == params[3] and item_dict["field3"] == params[5]

    # Test wrong number of params
    try:
        make_item_dict(["p1","p2","p3"])
        assert False
    except IntegrationError:
        assert True

    # Test null key
    try:
        item_dict = make_item_dict(["p1", "p2",
                        None, "p4",
                        "p5", "p6"])
        assert item_dict["p1"] == "p2" and item_dict["p5"] == "p6"
        assert "p4" not in item_dict
    except IntegrationError:
        assert False

    # Test null value
    try:
        item_dict = make_item_dict(["p1", None])
        assert not item_dict["p1"]
    except:
        assert False
