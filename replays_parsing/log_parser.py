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

    def __parse_logs(self, logs) -> List[list]:
        battles = []
        pattern = r"\|switch|move|turn|win|faint\|"
        for log in logs:
            battle = []
            log_lines = log.split("\n")
            # keep what starts with this pattern
            for line_number in range(len(log_lines)):
                if re.match(pattern, log_lines[line_number]):
                    battle.append(log_lines[line_number])
            battles.append(battle)
        return battles

    def __parse_logs_with_battle_output(self, logs):
        pattern = r"\|j|c|l|n|inactive\|"
        battles = []
        for log in logs:
            battle = []
            log_lines = log.split("\n")
            # keep what starts with this pattern
            for line_number in range(len(log_lines)):
                if not re.match(pattern, log_lines[line_number]):
                    battle.append(log_lines[line_number])
            battles.append(battle)
        return battles

