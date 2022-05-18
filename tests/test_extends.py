import pytest

from compose_viz.extends import Extends


def test_extend_init_normal() -> None:
    try:
        Extends(service_name="frontend", from_file="tests/in/000001.yaml")

        assert True
    except Exception as e:
        assert False, e


def test_extend_init_without_from_file() -> None:
    try:
        Extends(service_name="frontend")

        assert True
    except Exception as e:
        assert False, e


def test_extend_init_without_service_name() -> None:
    with pytest.raises(TypeError):
        Extends(from_file="tests/in/000001.yaml")  # type: ignore
