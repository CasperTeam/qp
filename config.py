"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = "7113954"
        self.API_HASH: str = "e09df0e45a8585fbbfa98316daa4a834"
        self.SESSION: str = "AQATM0jy5ftdo-feUgnplL9DYRy1IQ7t4SVqOvVmWTe5ujffaj_cSIHw4WzbgylUxlu2_J2iW4jQrrssZDxFrcu-hfMuI_JDN6SMuut-U6cJtwEqHuTaOLHjcyA7mVtujDMy9E3bX6ySLiuoEz2MKSv_wcgiXSFDFLA41sz6KWRMEp7a_YzapGKH6FIp8lf_9TRAlKMxgREkM7_KmZV_QNpGZIfvObvGFq0h1kkEZDVXBLKmnvhFUxrX2Tm24W5CY_uX4TtFtmaO1XE7censDbtZxUnC-VUfFPIIjWyuXthVitMAqeUdBVXOkUwFL2lu4FH_9Fp4le8NLiwLYK2F4-VoZyLfIgA"
        self.SUDOERS: str = "1808004347"
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.QUALITY: str = "high"
        self.PREFIXES: str = "/"
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()


config = Config()
