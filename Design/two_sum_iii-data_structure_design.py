class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numCounts = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.numCounts[number] = self.numCounts.get(number, 0) + 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key in self.numCounts.keys():
            target = value - key;
            if target in self.numCounts:
                if key == target and self.numCounts[key] < 2:
                    continue
                return True
        return False
