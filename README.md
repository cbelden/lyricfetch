#lyricfetch
The lyricfetch Python package retrieves the full lyrics for a song using the Lyric Wikia web service.
The fetch_some_lyrics.py file illustrates how to use the package. Additionally, I've included its contents below:

    from lyricfetch import LyricClient
    
    client = LyricClient()
    lyrics = client.get_lyrics('Drake', 'Marvins Room')

And that's it! Now you can quickly get the lyrics to your favorite sad Drake songs. Enjoy or cry or whatever.
