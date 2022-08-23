class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class TestIntegerList(TestCase):
    def test_constructor(self):
        intlist = IntegerList(1, 2, 3, 4, 5, 'a')
        self.assertEqual([1, 2, 3, 4, 5], intlist._IntegerList__data)

    def test_get_data(self):
        intlist = IntegerList(1, 2, 3, 4, 5, 'a')
        self.assertEqual([1, 2, 3, 4, 5], intlist.get_data())

    def test_add_element_not_int_raises(self):
        intlist = IntegerList(1, 2, 3, 4, 5, 'a')
        with self.assertRaises(ValueError) as ex:
            intlist.add('b')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_element(self):
        intlist = IntegerList(1, 2, 3, 4, 5, 'a')
        intlist.add(6)
        self.assertEqual([1, 2, 3, 4, 5, 6], intlist.get_data())

    def test_remove_index_index_out_of_range_raises(self):
        intlist = IntegerList(1, 2, 3, 'a')
        with self.assertRaises(IndexError) as ex:
            intlist.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        intlist = IntegerList(1, 2, 3)
        removed = intlist.remove_index(0)
        self.assertEqual(1, removed)

    def test_element_is_removed_from_list_after_remove_index(self):
        intlist = IntegerList(1, 2, 3)
        intlist.remove_index(0)
        self.assertEqual([2, 3], intlist.get_data())

    def test_get_raises(self):
        intlist = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            intlist.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get(self):
        intlist = IntegerList(1, 2, 3)
        result = intlist.get(0)
        self.assertEqual(1, result)

    def test_insert_index_out_of_range_raises(self):
        intlist = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            intlist.insert(5, 1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_element_not_an_integer_raises(self):
        intlist = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ex:
            intlist.insert(0, 'a')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert(self):
        intlist = IntegerList(1, 2, 3)
        intlist.insert(0, 0)
        self.assertEqual([0, 1, 2, 3], intlist.get_data())

    def test_get_biggest(self):
        intlist = IntegerList(1, 2, 3)
        result = intlist.get_biggest()
        self.assertEqual(3, result)

    def test_get_index(self):
        intlist = IntegerList(1, 2, 3)
        result = intlist.get_index(1)
        self.assertEqual(0, result)


if __name__ == "__main__":
    main()



