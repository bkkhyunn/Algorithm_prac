from collections import defaultdict
def solution(genres, plays):
    answer = []
    playlist = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in playlist:
            playlist[genre] = [play, (i, play)]
        else:
            playlist[genre][0] += play
            playlist[genre].append((i, play))
    
    while playlist:
        genre = max(playlist, key=lambda x: playlist[x][0])
        #print(playlist[genre][1:])
        
        answer += [value[0] for i, value in enumerate(sorted(playlist[genre][1:], key=lambda x: x[1], reverse=True)) if i < 2]
        
        del playlist[genre]
    return answer