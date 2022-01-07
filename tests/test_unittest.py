import unittest

from main import document_add, document_del, document_move, add_shelf, del_shelf


class TestWorkingDocumentCatalog(unittest.TestCase):

    def test_doc_added(self):
        documents_first = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "insurance", "number": "10008", "name": "Геннадий Покемонов"}
        ]
        directories_first = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': ['10008']
        }
        documents_second, directories_second = document_add("10008", "insurance", "Геннадий Покемонов", '3')
        self.assertListEqual(documents_first, documents_second)
        self.assertListEqual(directories_first['3'], directories_second)
        document_del("10008")

    def test_document_del(self):
        documents_first_true = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
        ]
        directories_first_true = {
            '1': ['2207 876234', '11-2'],
            '2': [],
            '3': []
        }
        documents_first_false = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        directories_first_false = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': []
        }
        result, documents_second, directories_second, document_delete, shelf_document = document_del("10006")
        if result:
            self.assertListEqual(documents_first_true, documents_second)
            self.assertListEqual(directories_first_true['2'], directories_second)
            document_add("10006", "insurance", "Аристарх Павлов", '2')
        else:
            self.assertListEqual(documents_first_false, documents_first_false)
            self.assertListEqual(directories_first_false['2'], directories_first_false['2'])

    def test_document_move(self):
        documents_first = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        directories_first = {
            '1': ['2207 876234', '11-2'],
            '2': [],
            '3': ['10006']
        }
        result, documents_second, directories_second, restore_shelf = document_move("10006", '3')
        self.assertListEqual(documents_first, documents_second)
        self.assertListEqual(directories_first['3'], directories_second)
        document_move("10006", '2')

    def test_add_shelf(self):
        documents_first = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        directories_first = {
            '1': ['2207 876234', '11-2'],
            '2': ['10006'],
            '3': [],
            '4': []
        }
        documents_second, directories_second = add_shelf('4')
        self.assertListEqual(documents_first, documents_second)
        self.assertListEqual(directories_first['4'], directories_second)
        del_shelf('4')


if __name__ == '__main__':
    unittest.main()

