class Solution:
    def frequencySort(self, s: str) -> str:
        # Time Complexity: O(nlogm)
        # Heap can also be used to sort 
        countChar = {}
        # res = ""

        for i in range(len(s)):
            if s[i] in countChar:
                countChar[s[i]] += 1 
            else:
                countChar[s[i]] = 1 
            
            # sortedcountChar = [x:x for lambda]
        
        sortedDict = dict(sorted(countChar.items(), key = lambda item: item[1], reverse = True))

        # print(sortedDict)

        res = "".join([k * v for k,v in sortedDict.items()])

        return res 
        