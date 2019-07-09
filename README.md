metacritic-py
==============

A wrapper for the Metacritic website
---------------------------------------

*metacritic-py* is a scraper, written in Python, for the PS4 games of the Metacritic website.  
You can retrieve all the general information of a game (e.g. title, user and critics score) and the user reviews to be used as a starting point to gain insights on the game.

Features
--------

- Supports and tested under Python 3.4.3 and 3.7.3
- Implements the methods to retrieve general information on a game and store the users' reviews to be used to calculate useful statistics

Installation
------------

You can install *metacriticapi* using one of the following methods:

- Use pip: 
```pip install git+https://github.com/AntoG87/metacriticapi.git```
- Download the `source from Github`_ and install it yourself. In this case use the following command to install the libraries included in the requirements.txt text file:
```
pip install -r https://github.com/AntoG87/metacriticapi/master/requirements.txt
```
 
How it works
------------
First, import the library:

.. code-block:: python

    >>> import metacriticapi as mc

To search all the games including a particular string use the Search method. The example below shows all the games including the string 'batman':

```python
    >>> s = mc.Search()
    >>> games = s.games('batman')
    >>> games
    {'games': {'Batman: Arkham Knight': 'batman-arkham-knight',
    'Batman: Return to Arkham': 'batman-return-to-arkham',
    'Batman: The Enemy Within - Episode 5: Same Stitch': 'batman-the-enemy-within---episode-5-same-stitch',
    'Batman: The Telltale Series': 'batman-the-telltale-series',
    'Batman: Arkham VR': 'batman-arkham-vr',
    'LEGO Batman 3: Beyond Gotham': 'lego-batman-3-beyond-gotham',
    'Batman: The Enemy Within - The Telltale Series': 'batman-the-enemy-within---the-telltale-series',
    'Batman: The Enemy Within - Episode 4: What Ails You': 'batman-the-enemy-within---episode-4-what-ails-you',
    'Batman: Arkham Knight - Season of Infamy: Most Wanted': 'batman-arkham-knight---season-of-infamy-most-wanted',
    'Batman: The Enemy Within - Episode 1: The Enigma': 'batman-the-enemy-within---episode-1-the-enigma'}}
```

Once we have retrieved the desired game, we pick the slug (e.g. 'batman-return-to-arkham' for 'Batman: Return to Arkham') and we use the method info of the class Games to retrieve the general information.
You can then access to the a particular attribute as shown in the example below:

```python
    >>> games = mc.Games('batman-return-to-arkham')
    >>> game = games.info()
    {'title': 'Batman: Return to Arkham',
    'general': {'Rating:': 'T',
    'Developer:': 'Rocksteady Studios, Virtuos',
    'Genre(s):': 'Miscellaneous, Compilation'},
    'scores': {'critics': '73', 'users': '8.0'},
    'release_date': 'Oct 18, 2016'}
    >>> game['scores']['critics']
    '73'
```

Finally, you can retrieve all the users' reviews, which are stored in a list:

```python
    >>> reviews = game.user_reviews()
    [('Oct 20, 2016', '8'),
    ('Oct 29, 2016', '8'),
    ('Feb 26, 2017', '9'),
    ('Dec 10, 2016', '8'),
    ('May  6, 2017', '5'),
    ('Oct 30, 2016', '9'),
    ('Oct 19, 2016', '10'),
    ('Oct 28, 2016', '4'),
    ('Nov 16, 2016', '10'),
    ('Oct 26, 2016', '7'),
    ('May  2, 2017', '8'),
    ('Dec  7, 2016', '10'),
    ('Jul  5, 2018', '8'),
    ('Jun  4, 2019', '7'),
    ('Jan  5, 2017', '7'),
    ('Nov 14, 2018', '8'),
    ('Oct 19, 2017', '10'),
    ('Jun 22, 2019', '1')]
```

You can use the dates and single scores to calculated useful distribution and statistics to gain additional insight on how the game is being reviewed by gamers. 

All the methods shown so far can work if the user is behind a proxy. All you have to do is instantiatin a proxy and pass it to the methods as demonstrated in the example below:

```python    
    >>> proxies = {'http': 'http://my-proxy/', 'https': 'https://my-proxy/'}
    >>> games = s.games('batman', proxies=proxies)
    >>> game = games.info(proxies=proxies)
    >>> reviews = game.user_reviews(proxies=proxies)
```
