from replays_fetching.replay_fetcher import ReplayFetcher

replay_fetcher = ReplayFetcher()
replays = replay_fetcher.get_replays()

for index in range(len(replays)):
    print('Replay #{0}: '.format(index) + str(replays[index]))
