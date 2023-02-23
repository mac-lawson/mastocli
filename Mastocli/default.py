from mastodon import Mastodon
import html
from html.parser import HTMLParser
import time
from colorama import Fore, Back
email = ""
password = ""

# Subclass HTMLParser to extract only plain text
class HTMLPlainTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)


# Mastodon.create_app(
#     'mastocli',
#     api_base_url = 'https://infosec.exchange',
#     to_file = 'pytooter_clientcred.secret'
# )
def tl():
    mastodon = Mastodon(client_id = 'pytooter_clientcred.secret',)
    mastodon.log_in(
        email,
        password,
        to_file = 'pytooter_usercred.secret'
        )
    # mastodon.toot('Testing the python api!')
    # tl = Mastodon.timeline_local(max_id=None, min_id=None, since_id=None, limit=None, only_media=False)
            
    timeline = mastodon.timeline_home(limit=5)
    for toot in timeline:
        # Parse the HTML and extract plain text
        parser = HTMLPlainTextParser()
        parser.feed(toot['content'])
        content = ''.join(parser.text)
        # Unescape any HTML entities
        content = html.unescape(content)
        print(Back.BLACK + Fore.RED + content + Back.RESET + Fore.RESET)
        # time.sleep(1)

# In this version of the script, the HTMLPlainTextParser class is a subclass of HTMLParser that overrides the handle_data() method to extract only the plain text from the HTML. The feed() method is then used to parse the HTML content of each toot and extract only the plain text.

# The plain text is then unescaped using the html.unescape() method to convert any HTML entities to their corresponding characters. Finally, the plain text is printed to the command line without any HTML tags.

# With these modifications, the script will print the Mastodon timeline with

def toot(message):
    mastodon = Mastodon(client_id = 'pytooter_clientcred.secret',)
    mastodon.log_in(
        email,
        password,
        to_file = 'pytooter_usercred.secret'
        )
    mastodon.toot(message)