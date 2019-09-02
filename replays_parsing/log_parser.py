from typing import List

from replays_fetching.replay_fetcher import ReplayFetcher

import re


class LogParser:
    def __init__(self):
        self.replay_fetcher = ReplayFetcher()

    def get_parsed_replay_logs(self) -> List[str]:
        return self.__parse_replay_logs()

    def __parse_replay_logs(self) -> List[str]:
        logs = []
        replays = self.replay_fetcher.get_replays()
        for replay in replays:
            logs.append(replay['log'])
        return self.__parse_logs(logs)

    def __parse_logs(self, logs) -> List[str]:
        # TODO [DanicPy]: Parse logs before returning!
        null = None
        string = logs
        x = string["log"].split("\n")
        pattern1 = r"\|j\|"
        pattern2 = r"\|c\|"
        pattern3 = r"\|l\|"
        pattern4 = r"\|n\|"
        pattern5 = r"\|inactive\|"
        battle = []
        for i in range(len(x)):
            if not re.match(pattern1, x[i]) and not re.match(pattern2, x[i]) and not re.match(pattern3,x[i]) \
                    and not re.match(pattern4, x[i]) and not re.match(pattern5, x[i]):
                battle.append(x[i])

        return battle
