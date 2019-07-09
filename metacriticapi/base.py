from lxml import etree
import requests
 
class Metacritic(object):
    """
    Provides an abstract base class to retrieve betting odds and results
    """    
    URLs = {}
    XPATH_QUERIES = {}

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def _get_path(self, key):
        return self.URLs[key]

    def _get_xpath_query(self, key, xpath):
        return self.XPATH_QUERIES[key][xpath]

    def _apply_xpath_query(self, key, xpath, seed):
        xpath_query = self._get_xpath_query(key, xpath)
        details = seed.xpath(xpath_query)
        return details        

    def _get_slug_path(self, key):
        return self._get_path(key).format(slug=self.slug)

    def _get_proxy(self, params):
        if 'proxies' in params:
            return params['proxies']    
        else:
            return None

    def _request(self, method, path, params=None):
        proxies = self._get_proxy(params)
        response = requests.request(method, path, params=params, headers=self.headers, proxies=proxies)    
        html = etree.HTML(response.content)
        return html         

    def _GET(self, path, params=None):
        response = self._request('GET', path, params=params)
        return response    
     
