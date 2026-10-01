class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strs:
            sorteds = "".join(sorted(s))
            dd[sorteds].append(s)
        return list(dd.values())