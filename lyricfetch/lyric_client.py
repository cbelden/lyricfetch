import requests
import re
from bs4 import BeautifulSoup


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

        # Return None if lyric request failed
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

        # Extract and store lyrics
        lyrics = ''
        last_tag = None

        for content in lyricbox.contents:

            # Within the lyricbox, the first element(s) consist of an ad contained within
            # a div. Additionally, each line from the lyrics is split by a <br> block. To
            # boot, after the last lyric line, there is a <p> block with some metrics.
            # The div and br blocks have non-None .name values, but both the NavigableText
            # and the <p> tags both have None values for the .name attribute.
            #
            # The following works by assuming that the first non-lyric elements will return
            # a non-None value for name, and the lyrics (text) will always return None. The
            # only time two consecutive None values will occur after the last lyric has been
            # read and the current element is the non-important <p> block. We can break at
            # this point.
            # TODO: follow up with this: if we can get the <p> block to have a non-None
            # .name attribute, we can clean this up quite a bit.

            tag = content.name

            # If last two tags are None, assume we've read all the lyrics
            if not tag and not last_tag:
                break

            # Append content if there is no tag (ie. the element is plain text)
            if not tag:

                # Skip line if it's contained in brackets
                if re.match('\[.+\]', content):
                    continue

                lyrics += content + '\n'

            # Update the last seen tag
            last_tag = tag

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
