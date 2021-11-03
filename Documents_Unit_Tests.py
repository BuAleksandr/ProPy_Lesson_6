import unittest
import Documents


class TestDocuments(unittest.TestCase):

    def test_search_person(self):
        self.assertEqual(Documents.search_person('2207 876234'), "Василий Гупкин")

    def test_add_new_doc(self):
        self.assertEqual(Documents.adding_to_the_archive('паспорт', '123', 'Геннадий Букин', '1'),
                         'паспорт с номером 123 с именем Геннадий Букин добавлен в каталог и перечень полок')

    def test_delete_doc(self):
        self.assertEqual(Documents.delete_document('123'), 'Документ с номером 123 удален с полки 1')


if __name__ == '__main__':
    unittest.main()
