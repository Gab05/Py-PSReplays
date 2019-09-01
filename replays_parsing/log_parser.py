from typing import List

from replays_fetching.replay_fetcher import ReplayFetcher


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
        return logs
