import pytest

from main import get_all_doc_owners_names, get_doc_owner_name, show_all_docs_info, get_doc_shelf
from main import add_new_doc, delete_doc, move_doc_to_shelf, add_new_shelf



class TestApp:
    def test_owner_name(self):
        assert get_doc_owner_name('11-2') == "Геннадий Покемонов"

    def test_owner_name(self):
        assert get_doc_owner_name('11-2') == "Геннадий Покемонов"

    def test_all_people(self):
        assert get_all_doc_owners_names() == {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'}

    def test_show_all_docs_info(self):
        assert show_all_docs_info() == [('passport', '2207 876234', 'Василий Гупкин'),  ('invoice',
                '11-2', 'Геннадий Покемонов'),  ('insurance', '10006', 'Аристарх Павлов')]

    def test_get_doc_shelf(self):
        assert get_doc_shelf('11-2') == '1'

    def test_add_new_doc(self):
        assert add_new_doc('007', 'letter', 'Mary Poppins', '1') == '1'

    def test_delete_doc(self):
        assert delete_doc('007') == ('007', True)

    def test_move_doc_to_shelf(self):
        assert move_doc_to_shelf('11-2', '2') == '2'

    def test_add_new_shelf(self):
        assert add_new_shelf('4') == ('4', True)








