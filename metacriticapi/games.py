from .base import Metacritic
import time
 
class Games(Metacritic):   
    URLs = {'info': 'https://www.metacritic.com/game/playstation-4/{slug}/details',
            'user_reviews':'https://www.metacritic.com/game/playstation-4/{slug}/user-reviews?page={{page}}'}
    XPATH_QUERIES = {'info':{'product_details': "//div[@class='product_details']//tr", 
                             'critics_score': "//span[@itemprop='ratingValue']//text()",
                             'users_score': "//div[contains(@class,'metascore_w user large game')]//text()",
                             'release_date':"//li[@class='summary_detail release_data']/span[2]//text()",
                             'title': "//div[@class='product_title']/a/h1/text()"},
                    'user_reviews':{'vote':"//li[contains(@class,'user_review')]//div[contains(@class,'metascore')]//text()",
                                    'date':"//li[contains(@class,'user_review')]//div[@class='date']/text()"}}
          

    def __init__(self, slug=0): 
        super(Games, self).__init__()
        self.slug = slug
     
    def _get_product_details(self, html):
        details = self._apply_xpath_query('info', 'product_details', html)
        product_details = {}
        for tr in details:
            children = tr.getchildren()
            attr = children[0].text.strip()           
            value = children[1].xpath(".//text()")[0].replace(" "*44," ").strip()            
            product_details[attr] = value    
        return product_details
         
    def _get_product_scores(self, html):
        critics = self._apply_xpath_query('info', 'critics_score', html)
        if critics:
            critics = critics[0]     
        else:
            critics = 'tbd'
        users = self._apply_xpath_query('info', 'users_score', html)
        if users:
            users = users[0]
        else:
            users = 'tbd'
        scores = {'critics': critics, 'users':users}
        return scores              

    def _get_title(self, html):
        title = self._apply_xpath_query('info', 'title', html)[0]        
        return title

    def _get_releasedate(self, html):
        release_date = self._apply_xpath_query('info', 'release_date', html)[0]
        return release_date

    def _get_review_dates(self,html):
        review_date = self._apply_xpath_query('user_reviews', 'date', html)
        return review_date

    def _get_review_votes(self,html):
        review_votes = self._apply_xpath_query('user_reviews', 'vote', html)
        return review_votes   

    def info(self, **kwargs):        
        path = self._get_slug_path('info')
        slug_html = self._GET(path, kwargs)
        product_details = self._get_product_details(slug_html)
        scores = self._get_product_scores(slug_html)
        title = self._get_title(slug_html)
        release_date = self._get_releasedate(slug_html)
        info = {'title':title, 'general': product_details, 'scores':scores, 'release_date': release_date}
        return info      
     
    def user_reviews (self, cap=9999, **kwargs):
        searchComplete = False
        page = 0
        all_reviews = []     
        while not searchComplete:            
            path = self._get_slug_path('user_reviews').format(page=page)
            slug_html = self._GET(path, kwargs)        
            dates = self._get_review_dates(slug_html)
            votes = self._get_review_votes(slug_html)
            if not(dates or votes) or (len(all_reviews)==cap):
                searchComplete = True
                if cap:
                    all_reviews = all_reviews[:cap]
            else:                
                page_reviews = [(k,v) for k, v in zip(dates, votes)]
                all_reviews+=page_reviews
                page+=1
                time.sleep(0.5)
        return all_reviews  
     
    def __repr__(self):
        return "<class_%s: %s>" % ("Games", self.slug)
 