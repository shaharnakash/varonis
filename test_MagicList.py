import pytest

from MagicList import MagicList
from Person import Person


@pytest.mark.magic
def test_magic_list_boundary() -> None:

    a = MagicList(Person)
    a[0].age = 5
    assert a[0].age == 5

    a[1].age = 7
    assert a[0].age == 7

    try:
        a[4].age = 11

    except AttributeError as ex:
        assert "'NoneType' object has no attribute 'age'" == str(ex)


