import pytest

from main import document_add, document_del, document_move, add_shelf, del_shelf


TEST_DATA_DOC_ADDED = ([[
    ["10008", "insurance", "Геннадий Покемонов", '3'],
    [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "insurance", "number": "10008", "name": "Геннадий Покемонов"}
    ],
    {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': ['10008']
    }
]])

TEST_DATA_DOC_DEL = ([[
    ["10006"],
    [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"}
    ],
    {
        '1': ['2207 876234', '11-2'],
        '2': [],
        '3': []
    }
]])

TEST_DATA_DOC_MOVE = ([[
    ["10006", '3'],
    [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ],
    {
        '1': ['2207 876234', '11-2'],
        '2': [],
        '3': ['10006']
    }
]])

TEST_DATA_ADD_SHELF = ([[
    ['4'],
    [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ],
    {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': [],
        '4': []
    }
]])


class TestWorkingDocumentCatalogPy:

    @pytest.mark.parametrize('list_document, list_before, dist_before', TEST_DATA_DOC_ADDED)
    def test_doc_added(self, list_document, list_before, dist_before):
        number, type_document, people, shelf = list_document
        list_after, dist_after = document_add(number, type_document, people, shelf)
        assert list_before == list_after
        assert dist_before[shelf] == dist_after
        document_del(number)

    @pytest.mark.parametrize('list_document, list_before, dist_before', TEST_DATA_DOC_DEL)
    def test_document_del(self, list_document, list_before, dist_before):
        result, list_after, dist_after, document_delete, shelf_document = document_del(list_document[0])
        assert list_before == list_after
        assert dist_before[shelf_document] == dist_after
        document_add(document_delete["number"], document_delete["type"], document_delete["name"], shelf_document)

    @pytest.mark.parametrize('list_document, list_before, dist_before', TEST_DATA_DOC_MOVE)
    def test_document_move(self, list_document, list_before, dist_before):
        number, shelf = list_document
        result, list_after, dist_after, restore_shelf = document_move(number, shelf)
        assert list_before == list_after
        assert dist_before[shelf] == dist_after
        document_move(number, restore_shelf)

    @pytest.mark.parametrize('list_shelf, list_before, dist_before', TEST_DATA_ADD_SHELF)
    def test_add_shelf(self, list_shelf, list_before, dist_before):
        list_after, dist_after = add_shelf(list_shelf[0])
        assert list_before == list_after
        assert dist_before[list_shelf[0]] == dist_after
        del_shelf(list_shelf[0])
