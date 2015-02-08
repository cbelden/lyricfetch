import requests
import re
from bs4 import BeautifulSoup, Comment


class LyricClient():
    """The Lyric Client retrieves lyrics from Lyric Wikia's API."""

    def __init__(self):
        """Initializes the Lyric Client."""
        pass

    def _get_lyric_url(self, artist, title):
        """Retrieves the url to the webpage that stores the lyrics for the requested song."""

        url_params = {'artist': artist, 'song': title, 'fmt': 'html'}

        try:
            r = requests.get("http://lyrics.wikia.com/api.php", params=url_params)
        except Exception, e:
            raise e

        # Return empty string if lyric request failed
        if r.status_code is not 200:
            return None

        # Read and parse the response
        html = r.text
        soup = BeautifulSoup(html)

        # The first anchor in the response directs to the lyrics page
        # TODO: make this more robost. if lyric wikia changes their api response, this service might break. -Cal
        link = soup.find('a')

        if link:
            return link['href']
        else:
            return None

    def _extract_lyrics(self, lyric_url):
        """Extracts the lyrics from a Lyric Wikia lyrics page."""

        # Parse lyric url response
        r = requests.get(lyric_url)
        soup = BeautifulSoup(r.text)

        # Locate div that stores the lyrics
        lyricbox = soup.find(class_='lyricbox')

        # Return empty string if they lyrics are missing
        if not lyricbox:
            return ''

        # Remove "NewPP limit report" from wiki sites and other HTML comments
        [s.extract() for s in lyricbox(text=lambda text: isinstance(text, Comment))]

        # Remove all script elements
        [s.extract() for s in lyricbox('script')]

        # Extract and store lyrics
        lyrics = ''

        for content in lyricbox.contents:

            tag = content.name

            # Append content if there is no tag (ie. the element is plain text)
            if not tag:

                # Skip line if it's contained in brackets
                if re.match('\[.+\]', content):
                    continue

                lyrics += content + '\n'

        return lyrics

    def get_lyrics(self, artist, title):
        """Retrieves the lyrics for a given song using the Lyric Wikia website."""

        # Unfortunately, when we submit a song lyric request using Lyric Wikia's API,
        # the response contains only a snippet of the song lyrics. A url is also provided,
        # however, for a page that contains the full lyric listing. To retrieve the lyrics,
        # we must get this url, visit the page, and parse the contents for the lyric
        # listing. -Cal

        lyric_url = self._get_lyric_url(artist, title)
        return self._extract_lyrics(lyric_url)


if __name__ == '__main__':

    client = LyricClient()
    print client.get_lyrics('Drake', 'Marvins room')
