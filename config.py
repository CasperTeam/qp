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
        self.SESSION: str = "AQAMcaDuzdFkC0zKVMI2IwHLK7RM0-fUP3pwqv4uldb6NFf8GHRbBUcvF4sTUtJxVneRo1vBm5zOokTdjM4OqkXDDZ2dW3QcDmMYHURGlLs0JSkBVboAXnZjatz7DGo3L2mkZHUkahtuMYMilyJ7wyD8rE_uv4dTRFqZnsmJx9sFEq4cypK6Z3Z9hNgopqxGPT5Mr14-z78Vb-tY5qWPY0Bw5aUzWDiNOPiUuaXRtb3a-LRtf-bMandRhTHH9wLLAMN8W3kqUO_2CKg8Ef1x27-GsUp9vQf9C8qYiA2Zp_OLw1zQH5gNuu6066xn_1nP_FXpRexp_XLj5-IPVtovF1IzZyLfIgA"
        self.SUDOERS: str = "1808004347"
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.QUALITY: str = "high"
        self.PREFIXES: str = "/"
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()


config = Config()
