#!/usr/bin/env python

from distutils.core import setup


setup(name='LyricFetch',
      version='1.0',
      description='Lyric Fetcher Tool',
      author='Cal Belden',
      author_email='calvinbelden@gmail.com',
      packages=['lyricfetch'],
      install_requires=['beautifulsoup4 (==4.3.2)',
                        'requests (==2.3.0)',
                        'wsgiref (==0.1.2)'])
