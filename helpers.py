# it'll take headlines(list, which might contain duplicates n all), n it'll return unique headlines list

def remove_duplicates(headlines):
    return list(set(headlines))

# set aint ordered.

# valid headlines ( skippin all empty strings or adds )
def filter_headlines(headlines):
    return [h for h in headlines if len(h) > 15]

# it limits headlines to 15 or jus how much we want.
def limit_headlines(headlines_list, limit = 15):
    return headlines_list[:limit]
