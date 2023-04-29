class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)

        mapping = {p[0]: p for p in pieces}

        i = 0
        while i < n:
            if arr[i] not in mapping:
                return False

            target_piece = mapping[arr[i]]
            for x in target_piece:
                if x != arr[i]:
                    return False
                i += 1

        return True