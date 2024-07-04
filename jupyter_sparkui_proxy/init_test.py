import pytest

def test_import_class():
    try:
        from jupyter_sparkui_proxy import SparkUIHandler
    except ImportError:
        pytest.fail("Failed to import SparkUIHandler from jupyter_sparkui_proxy")
