from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jew=0
        # hashmap = Counter(S)
        hashmap = dict()
        for s in S:
            hashmap[s] = hashmap.get(s, 0) + 1
            print(hashmap)
        for j in J:
            jew += hashmap[j]
        print(jew)
        jew = 0
        for i in list(J):
            for j in list(S):
                if i == j:
                    jew +=1
        print(jew)
        return jew 

if __name__ == "__main__":
    so = Solution()
    J = "aA"
    S = "aAAbbbb"
    so.numJewelsInStones(J,S)
