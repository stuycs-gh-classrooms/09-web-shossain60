def lists2dict(g0, g1):
    return dict(zip(g0, g1))


def better_hitters(team, cutoff):
    return [player for player, average in team.items() if average >= cutoff]



def word_counts(s):
    words = s.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
