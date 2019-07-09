from .base import Metacritic

class Search(Metacritic):
    URLs = {'search': 'https://www.metacritic.com/search/game/{slug}/results?plats[72496]=1&search_type=advanced'}
    XPATH_QUERIES = {'results':{'games':"//h3[@class='product_title basic_stat']/a"}}

    def __init__(self):
        super(Search, self).__init__()

    def _get_all_games(self, html):
        games = self._apply_xpath_query('results', 'games', html)
        return games

    def games(self, query='', **kwargs):
        self.slug = query
        path = self._get_slug_path('search')
        slug_html = self._GET(path, kwargs)
        games = self._get_all_games(slug_html)
        results = {'games':{game.text.strip():game.attrib['href'].split("/")[-1] for game in games}}
        return results