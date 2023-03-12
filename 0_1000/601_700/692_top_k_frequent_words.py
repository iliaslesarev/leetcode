import heapq

from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)

        heap = [(-freq, word) for word, freq in c.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


print(Solution().topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2) == ['i', 'love'])
print(Solution().topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4) == ['the', 'is', 'sunny', 'day'])
print(Solution().topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=3))
print(Solution().topKFrequent(words=["akjkun","hobievq","ibbb","jhw","pxwsurrun","hxfwhrjm","pxwsurrun","wjo","pxwsurrun","wfetx","ydp","qfazmji","qfazmji","llvabr","uaq","kyj","uaq","wuzvu","nze","qznvdw","wjo","uaq","qfazmji","uaq","hxfwhrjm","ftmcuyb","rmjim","omx","omx","jgqdwle","ehoc","nze","jgqdwle","kyj","erkc","wfetx","wjo","wjo","rmldehuuff","wfetx","qznvdw","jhw","jhw","pxwsurrun","rmldehuuff","omx","yhriclj","pxwsurrun","kyj","erkc","wfetx","pxwsurrun","gukcclzd","llvabr","cpgyk","jhw","llvabr","qfazmji","llvabr","yhriclj","zvefqcz","fiwdfgzs","pqpozde","nze","qfazmji","qznvdw","kyj","ydp","wuzvu","erkc","qznvdw","yhriclj","akjkun","rmjim","moeuarod","hvxg","nze","rmldehuuff","jhw","rmldehuuff","wjo","cpgyk","omx","hlak","kyj","hxfwhrjm","qfazmji","gukcclzd","pqpozde","wfetx","wahno","cpgyk","nze","ibbb","wjo","wuzvu","kyj","kyj","zvefqcz","rmjim","erkc","llvabr","omx","hobievq","pxwsurrun","wahno","akjkun","jgqdwle","nze","ftmcuyb","wuzvu","hxfwhrjm","ibbb","wfetx","akjkun","omx","hxfwhrjm","hlak","rmldehuuff","hxfwhrjm","jhw","pxwsurrun","omx","wjo","hlak","zvefqcz","ehoc","wuzvu","pqpozde","cgwncxeof","jhw","hlak","usaq","wqnez","qznvdw","ibbb","erkc","wfetx","hlak","cpgyk","hxfwhrjm","wuzvu","jaar","hlak","wahno","hlak","ibbb","nze","omx","wfetx","erkc","kyj","pqpozde","hlak","nze","wjo","cgwncxeof","uaq","kyj","wahno","cgwncxeof","hlak","rmldehuuff","hlak","wfetx","wahno","kyj","yhriclj","nze","jgqdwle","fiwdfgzs","jhw","wuzvu","wfetx","ibbb","ydp","hobievq","rmjim","ehoc","jhw","hobievq","rmldehuuff","wuzvu","gukcclzd","wuzvu","jhw","qfazmji","wjo","qfazmji","wuzvu","ehoc","omx","nze","jgqdwle","pxwsurrun","omx","gukcclzd","jaar","uaq","qznvdw","ibbb","hxfwhrjm"], k=24))