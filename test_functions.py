import pytest
from pytest import MonkeyPatch
import extra_functions as x
import cafe_app as a
import file_handlers as fh
from io import StringIO
from unittest import mock

@pytest.mark.parametrize(
    'dict_record, expected',
    [({"id": "", "name": "coke", "price": "1.0"}, {"id": "ce", "name": "coke", "price": "1.0"}
    ) ,
    ({"id": "", "name": "popcorn", "price": "5.0"}, {"id": "pn", "name": "popcorn", "price": "5.0"}
    )]
)
def test_id_generator_create_happy_path(dict_record, expected):
    assert x.id_generator_create(dict_record) == expected
    
@pytest.mark.parametrize(
    'dict_record, expected',
    [({"id": "", "name": "coke", "price": 1}, {"id": "ce", "name": "coke", "price": "1.0"}
    ) ,
    ({"id": "", "name": "popcorn", "cost": "5.0"}, {"id": "pn", "name": "popcorn", "price": "5.0"}
    )]
)
def test_id_generator_create_bad_path(dict_record, expected):
    with pytest.raises(AssertionError):
        assert x.id_generator_create(dict_record) == expected
        
@mock.patch("builtins.print", return_value="{'id': 'co1e', 'name': 'coke', 'price': '1.0'}")
def test_print_whole_list(monkeypatch: MonkeyPatch): 
    list_type = []
    expected = "{'id': 'co1e', 'name': 'coke', 'price': '1.0'}"
    assert x.print_whole_list(list_type) == expected
    
@mock.patch("builtins.print", return_value={'customer_name': 'Max', 'customer_address': 'Thun_project/cafe_app_project_2 (main)derdome, Desert Apocalypse', 'customer_phone_number': '035435435', 'product_id_index': '', 'courier_id': '', 'status': 'preparing'})
def test_orders_list(monkeypatch: MonkeyPatch):
    expected = {'customer_name': 'Max', 'customer_address': 'Thun_project/cafe_app_project_2 (main)derdome, Desert Apocalypse', 'customer_phone_number': '035435435', 'product_id_index': '', 'courier_id': '', 'status': 'preparing'}
    assert x.print_orders_list() == expected

def test_create_temp_dict_happy_path():
    menu_type = "product"
    temp_dict = {}
    expected = {"id": "", "name": "", "price": ""}
    assert x.create_temp_dict(menu_type, temp_dict) == expected
    
def test_create_temp_dict_bad_path():
        with pytest.raises(AssertionError):
            menu_type = "mayonaisse"
            temp_dict = {}
            expected = {"id": "", "name": "", "price": ""}
            assert x.create_temp_dict(menu_type, temp_dict) == expected

def test_create_name_happy_path():
    temp_dict = {"id": "", "name": "", "price": ""}
    input_name = "coke"
    expected = {"id": "", "name": "coke", "price": ""}
    assert x.create_name(temp_dict, input_name) == expected

def test_create_name_bad_path():
        with pytest.raises(AssertionError):
            temp_dict = {"id": "", "name": "", "price": ""}
            input_name = 12345
            expected = {"id": "", "name": "coke", "price": ""}
            assert x.create_name(temp_dict, input_name) == expected
            
def test_create_phone_num_bad_path():
    with pytest.raises(AssertionError):
        temp_dict = {"id": "", "name": "coke", "phone_number": ""}
        input_name = "cheese"
        expected = {"id": "", "name": "coke", "phone_number": "0800123321"}
        assert x.create_phone_num(temp_dict, input_name) == expected
    
def test_sort_temp_dict():
    temp_dict = { "name": "coke", "phone_number": "", "id": ""}
    expected = {"id": "", "name": "coke", "phone_number": ""}
    assert x.sort_temp_dict(temp_dict) == expected

def test_sort_temp_dict_bad_path():
    with pytest.raises(AssertionError):
        temp_dict = { "name": "coke", "phone_number": "", "id": ""}
        expected = {"id": "", "name": "coke" }
        assert x.sort_temp_dict(temp_dict) == expected    
    
def test_create_phone_num():
    temp_dict = {"id": "", "name": "coke", "phone_number": ""}
    input_name = "0800123321"
    expected = {"id": "", "name": "coke", "phone_number": "0800123321"}
    assert x.create_phone_num(temp_dict, input_name) == expected
    
def test_create_phone_num_bad_path():
    with pytest.raises(AssertionError):
        temp_dict = {"id": "", "name": "coke", "phone_number": ""}
        input_name = 800123321
        expected = {"id": "", "name": "coke", "phone_number": "800123321"}
        assert x.create_phone_num(temp_dict, input_name) == expected
    
def test_append_dict_to_list():
    temp_dict = {"id": "ce", "name": "coke", "price": 1.0}
    list_type = []
    expected = [{"id": "ce", "name": "coke", "price": 1.0}]
    assert x.append_to_dict_to_list(list_type, temp_dict) == expected
    
def test_append_dict_to_list_bad_path():
    with pytest.raises(AttributeError):
        temp_dict = {"id": "ce", "name": "coke", "price": 1.0}
        list_type = {}
        expected = [{"id": "ce", "name": "coke", "price": 1.0}]
        assert x.append_to_dict_to_list(list_type, temp_dict) == expected

def test_update_price():
    list_type = [{"id": "ce", "name": "coke", "price": 1.0}]
    index = 0
    key = "price"
    input_info = '5.0'
    expected = '5.0'
    assert x.update_price(list_type, index, key, input_info) == expected
    
def test_update_price_bad_path():
    with pytest.raises(AssertionError):
        list_type = [{"id": "ce", "name": "coke", "price": 1.0}]
        index = 0
        key = "price"
        input_info = 5.0
        expected = '5.0'
        assert x.update_price(list_type, index, key, input_info) == expected
    
def test_update_record():
    list_type = [{"id": "ce", "name": "coke", "price": 1.0}]
    index = 0
    key = "name"
    input_info = 'chips'
    expected = 'chips'
    assert x.update_price(list_type, index, key, input_info) == expected
    
def test_update_record_bad_path():
    with pytest.raises(IndexError):
        list_type = [{"id": "ce", "name": "coke", "price": 1.0}]
        index = 3
        key = "name"
        input_info = 'chips'
        expected = 'chips'
        assert x.update_price(list_type, index, key, input_info) == expected
    
def test_id_generator_update():
    list_type = [{"id": "", "name": "coke", "price": 1.0}]
    index = 0
    expected = [{"id": "ce", "name": "coke", "price": 1.0}]
    assert x.id_generator_update(list_type, index) == expected
    
def test_id_generator_update_bad_path():
    with pytest.raises(IndexError):
        list_type = [{"id": "", "name": "coke", "price": 1.0}]
        index = 4
        expected = [{"id": "ce", "name": "coke", "price": 1.0}]
        assert x.id_generator_update(list_type, index) == expected
    
def test_delete_record():
    list_type = [{"id": "ce", "name": "coke", "price": 1.0}]
    index = 0
    expected = None
    assert x.delete_record(list_type, index) == expected
    
def test_delete_record_bad_path():
    with pytest.raises(IndexError):
        list_type = [{"id": "ce", "name": "coke", "price": 1.0}]
        index = 2
        expected = None
        assert x.delete_record(list_type, index) == expected
    
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
        assert fh.is_csv_empty('data/file_not_empty.csv') == False
    
    def test_is_csv_empty_bad_path(self):
        with pytest.raises(AssertionError):
            assert fh.is_csv_empty('data/file_not_empty.csv') == True

    def test_is_csv_not_empty(self):
        assert fh.is_csv_empty('data/file_empty.csv') == True
        
    def test_is_csv_not_empty_bad_path(self):
        with pytest.raises(AssertionError):
            assert fh.is_csv_empty('data/file_empty.csv') == False

