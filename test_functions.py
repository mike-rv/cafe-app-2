import pytest
import extra_functions as x
import cafe_app as a
import file_handlers as fh
from io import StringIO


@pytest.mark.parametrize(
    'dict_record, expected',
    [({"id": "1", "name": "coke", "price": "1.0"}, {"id": "co1e", "name": "coke", "price": "1.0"}
    ) ,
    ({"id": "3", "name": "popcorn", "price": "5.0"}, {"id": "po3n", "name": "popcorn", "price": "5.0"}
    )]
)
def test_id_generator(dict_record, expected):
    assert x.id_generator(dict_record) == expected
    


def test_exit_main_menu(monkeypatch):
    inputs = StringIO('0\n')
    monkeypatch.setattr('sys.stdin', inputs)
    assert a.main_menu() == None

def test_enter_sub_menu_exit_exit(monkeypatch):
    inputs = StringIO('1\n0\n0\n')
    monkeypatch.setattr('sys.stdin', inputs)
    assert a.main_menu() == None


class TestCsvFunctions:
    def test_is_csv_empty(self):
        assert fh.is_csv_empty('file_not_empty.csv') == False

    def test_is_csv_not_empty(self):
        assert fh.is_csv_empty('file_empty.csv') == True

