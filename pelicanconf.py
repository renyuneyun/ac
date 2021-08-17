#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rui Zhao'
SITENAME = "Rui Zhao's research homepage"
SITEURL = 'http://localhost:8000'

PATH = 'content'

PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['summary']

THEME = './themes/notmyidea'

STATIC_PATHS = ['images', 'pdfs', 'docs']

TIMEZONE = 'Europe/London'

LOCALE = 'en_US'
DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## Blogroll
LINKS = (
        ('AIAI (formerly CISA)', 'http://web.inf.ed.ac.uk/aiai'),
        ('Blog (mainly Chinese)', 'https://blog.ryey.icu'),
        ('Personal projects', 'https://me.ryey.icu/'),
        )
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
#
## Social widget
SOCIAL = (
        ('github', 'https://github.com/renyuneyun/'),
        ('linkedin', 'https://www.linkedin.com/in/zhaoruigh/'),
        ('twitter', 'https://www.twitter.com/zhaoruigh/'),
        ('mastodon', 'https://scholar.social/@ZhaoRui'),
        )
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
