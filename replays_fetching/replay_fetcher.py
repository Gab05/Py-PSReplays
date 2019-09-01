from typing import List
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

BASE_URL = 'https://replay.pokemonshowdown.com/'
REPLAY_FORMAT = '.json'


class ReplayFetcher:
    def __init__(self):
        pass

    def get_replays(self) -> List[dict]:
        replays = []
        for replayId in self.__get_replay_ids():
            replays.append(self.__fetch_replay_of_id(replayId))
        return replays

    def __get_replay_ids(self) -> List[str]:
        # TODO [Gab05]: find a way to effectively fetch competitive replay ids
        return [
            'doublesou-232753081'
        ]

    def __fetch_replay_of_id(self, replay_id) -> dict:
        url = BASE_URL + replay_id + REPLAY_FORMAT
        return dict(self.__fetch_document_of_url(url))

    def __fetch_document_of_url(self, url: str) -> str:
        request = Request(url)
        request.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) '
                                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                                         'Chrome/72.0.3626.121 Safari/537.36')
        response = BeautifulSoup(urlopen(request), 'html.parser').get_text()
        return json.loads(response)
