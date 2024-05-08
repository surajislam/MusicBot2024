from MahakXMusic.core.bot import Anony
from MahakXMusic.core.dir import dirr
from MahakXMusic.core.git import git
from MahakXMusic.core.userbot import Userbot
from MahakXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
