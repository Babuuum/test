from scr import person_search, spot_search, add_new, del_from_base
import pytest

person_number = [("2207 876234", "Василий Гупкин"), ("11-2", "Геннадий Покемонов"), ("10006", "Аристарх Павлов")]
spot_number = [("2207 876234", "1"), ("11-2", "1"), ("10006", "2"), ("1", ("документа под номером 1 в базе нет"))]
new_result = [("number", "type", "name", "5", "5 полки не существует"), ("number", "type", "name", "3", "новый документ создан")]
del_result = [("11-2", "документ успешно удален"),("1", "Документа под номером 1 нет в базе данных!")]

class Test_func:

    @classmethod
    def setup_Class(cls):
        print("setUpClass")

    def setup(self):
        print("method setup")

    @pytest.mark.parametrize("number, result", person_number)
    def test_person_search(self, number, result):
        assert person_search(number) == result

    @pytest.mark.parametrize("number, spot", spot_number)
    def test_spot_search(self, number, spot):
        assert spot_search(number) == spot

    @pytest.mark.parametrize("number, type, name, spot, result", new_result)
    def test_show_all(self, number, type, name, spot, result):
        assert add_new(number, type, name, spot) == result

    @pytest.mark.parametrize("number, result", del_result)
    def test_del(self, number, result):
        assert del_from_base(number) == result
        
    def teardown(self):
        print("method teardown")

    @classmethod
    def teardown_class(cls):
        print("tearDownClass")