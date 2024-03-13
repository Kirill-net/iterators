class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.limit = len(self.list_of_list)

    def __iter__(self):
        self.count = 0
        self.list = self.list_of_list[0]
        self.result = iter(self.list)
        return self

    def __next__(self):
        try:
            next_item = next(self.result)
        except StopIteration:
            self.count +=1
            if self.count < self.limit:
                self.list = self.list_of_list[self.count]
                self.result = iter(self.list)
                next_item = next(self.result)
            else:
                raise StopIteration
        return next_item

# list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
# ]
# for i in FlatIterator(list_of_lists_1):
#     print(i)
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()