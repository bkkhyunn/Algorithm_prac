def solution(genres, plays):
    answer = []
    playlist = {genre:{} for genre in set(genres)}
    total = {genre:0 for genre in set(genres)}
    for i, (g, p) in enumerate(zip(genres, plays)):
        playlist[g][i] = p
        total[g] += p
    for g in sorted(total, key=total.get, reverse=True):
        for i in sorted(playlist[g], key=playlist[g].get, reverse=True)[:2]:
            answer.append(i)
    return answer