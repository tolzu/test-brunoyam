d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
def invert(d):
    return {v:k for k, v in d.items()}
print(invert(d))