#VERSION: 1.00
#AUTHORS: Boris Nagaev (bnagaev@gmail.com)
# This plugin is licensed under the GNU GPL Version 2.

from novaprinter import prettyPrinter
from helpers import retrieve_url, download_file
import re

hit_pattern = re.compile(r'''<a href=".+">(?P<name>.+)</a>\s*
\s*</td>\s*
\s*<td class="dl">\s*
\s*<b class="sd">(?P<seeds>.*)</b> \| <b class="lc">(?P<leech>.+)</b>\s*
\s*<br/>\s*
\s*<a href="(?P<link>.+)">(?P<size>.+)</a>\s*''')
tag = re.compile(r'<.*?>')

class tfile(object):
    url = 'http://tfile.ru';
    name = 'tfile.ru'
    supported_categories = {'all': 0,
                            'movies': 37,
                            'tv': 1068,
                            'music': 67,
                            'games': 98,
                            'anime': 175,
                            'software': 118,
                            'pictures': 1075,
                            'books': 195}
    query_pattern = '%(url)s/forum/ssearch.php?f=%(f)i&q=%(q)s'

    def __init__(self):
        pass

    def search(self, what, cat='all'):
        params = {}
        params['url'] = self.url
        params['q'] = what
        params['f'] = self.supported_categories[cat]
        dat = retrieve_url(self.query_pattern % params)
        for hit in hit_pattern.finditer(dat):
            d = hit.groupdict()
            d['link'] = self.url + d['link']
            d['engine_url'] = self.url
            d['name'] = tag.sub('', d['name'])
            prettyPrinter(d)

