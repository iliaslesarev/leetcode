# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from typing import List


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        base_domain: str = startUrl.split("/")[2]
        base_prefix: str = f"http://{base_domain}"
        working_stack = [startUrl]
        visited_urls = {startUrl}
        while len(working_stack) != 0:
            next_url = working_stack.pop()
            crawling_results = htmlParser.getUrls(next_url)
            for result in crawling_results:
                if result.startswith(base_prefix) and result not in visited_urls:
                    working_stack.append(result)
                    visited_urls.add(result)
        return list(visited_urls)
