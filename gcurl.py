import pycurl
from StringIO import StringIO
import os

c= pycurl.Curl()
c.setopt(c.URL, 'https://www.google.co.in/search?client=opera&hs=jwL&ei=vrIfWs2QMsrYvASh5r3QCQ&q="index+of"+inurl%3Awp-content+inurl%3Awww.roadbang.com&oq="index+of"+inurl%3Awp-content+inurl%3Awww.roadbang.com&gs_l=psy-ab.3...1521440.1523177.0.1523621.9.9.0.0.0.0.104.790.8j1.9.0....0...1c.1.64.psy-ab..0.0.0....0.72hNtZ8wXpY&num=10')
c.perform()
