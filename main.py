import random


class SortedList:

    def __init__(self, lst=None):
        if lst is None:
            lst = []
        self.lst = lst

    def __str__(self):
        return self.lst.__str__()

    def sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
        l_nums = [n for n in nums if n < q]

        e_nums = [q] * nums.count(q)
        b_nums = [n for n in nums if n > q]
        return self.sort(l_nums) + e_nums + self.sort(b_nums)

    def of(self, lst):
        if isinstance(lst, [].__class__) | isinstance(lst, ().__class__):
            try:
                self.lst = self.sort(lst)
            except TypeError as t:
                print(t)
                self.lst = lst
        elif isinstance(lst, {}.__class__):
            print("{}")
        else:
            self.lst = lst


sl = SortedList()
l = ("aasdf", "fdsf", "cgasd", "basd", "tade", "zead", "abeef")
sl.of(l)

print(sl)
