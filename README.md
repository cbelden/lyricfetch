#lyricfetch

##About
The lyricfetch Python package retrieves the full lyrics for a song using the Lyric Wikia web service. The main class in lyricfetch, LyricClient, exposes a single method, .get_lyrics(artist, title). In the project root, I've created fetch_some_lyrics.py to illustrate how to use the package. Check out the installation instructions below to get started!

Note: this ish is currently an alpha release (i.e. ready for testing, but no testing has been completed).


##Installing (Mac OS X)
The following instructions describe how to install lyricfetch in a virtual environment. For more
information on virtual environments, this <a href="http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv">blog post</a> might be helfpul. Otherwise, a quick Google search will lead you to numerous sources of info.

Open up a new terminal window. Navigate to a directory where you would like to use lyricfetch. Create a new virtualenv:

    JohnDoe:$ virtualenv venv

Activate the virtual environment:

    JohnDoe:$ source venv/bin/activate

Now you can download the lyricfetch package (from GitHub):

    JohnDoe:$ pip install git+git://github.com/cbelden/lyricfetch.git@master

At this time some other dependencies will also be installed (listed in requirements.txt). To ensure that the package was installed correctly, open up the python interpreter and try to use the service:

    JohnDoe:$ python
    >>> from lyricfetch import LyricClient
    >>> client = LyricClient()
    >>> client.get_lyrics('Drake', 'Marvins room')
    u'Hello? Yeah I just walked in.
    Yeah I'm good... you still working?
    Tonight, right now? Did I go out? Yeah... etc. etc.

And that's it! Now you can quickly get the lyrics to your favorite sad Drake songs. Enjoy or cry or whatever.
