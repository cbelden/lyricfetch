#lyricfetch
The lyricfetch Python package retrieves the full lyrics for a song using the Lyric Wikia web service.
The fetch_some_lyrics.py file illustrates how to use the package. Additionally, I've included the correct syntax
below because it's just that easy.

    from lyricfetch import LyricClient
    
    client = LyricClient()
    lyrics = client.get_lyrics('Drake', 'Marvins Room')

And that's it!
