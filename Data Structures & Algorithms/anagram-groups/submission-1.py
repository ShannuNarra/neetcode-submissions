class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for eachstring in strs:
            key=''.join(sorted(eachstring))
            res[key].append(eachstring)
        return list(res.values())