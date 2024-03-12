class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.count1 = 0
        self.count2 = 0
        self.limit1 = len(self.list_of_list)
        # print('---')
        return self

    def __next__(self):
        if self.count1 < self.limit1:
            self.list = self.list_of_list[self.count1]
            self.limit2 = len(self.list)
            # print('count1=', self.count1)
            if self.count2 < self.limit2 - 1:
                # print('count2=', self.count2)
                item = self.list[self.count2]
                self.count2 += 1
                return item
            else:
                item = self.list[self.count2]
                self.count2 = 0
                self.count1 += 1
                return item
        else:
            raise StopIteration
# list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
# ]
# for i in FlatIterator(list_of_lists_1):
#     print(i)
#
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