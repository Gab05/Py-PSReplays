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
        battle = []
        for log in logs:
            log_lines = log.split("\n")
            pattern = r"\|switch|move|turn|win|faint\|"

            # keep what starts with this pattern
            for line_number in range(len(log_lines)):
                if re.match(pattern, log_lines[line_number]):
                    battle.append(log_lines[line_number])
        return battle

    def __parse_logs_with_battle_output(self, logs):
        null = None
        splitted_battle_log = logs["log"].split("\n")
        pattern1 = r"\|j\|"
        pattern2 = r"\|c\|"
        pattern3 = r"\|l\|"
        pattern4 = r"\|n\|"
        pattern5 = r"\|inactive\|"
        battle = []
        # only keeping what doesn't start with those patterns
        for i in range(len(splitted_battle_log)):
            if not re.match(pattern1, splitted_battle_log[i]) and not re.match(pattern2, splitted_battle_log[i]) and not re.match(pattern3,splitted_battle_log[i]) \
                    and not re.match(pattern4, splitted_battle_log[i]) and not re.match(pattern5, splitted_battle_log[i]):
                battle.append(splitted_battle_log[i])
            return battle
