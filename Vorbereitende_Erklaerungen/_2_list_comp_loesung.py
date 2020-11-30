def most_common_tags(self):
    all_tags_flat = [tag for game in self.steam_discount_list if game['tag_list'] is not None for tag in game['tag_list']]
    occur = [[tag, all_tags_flat.count(tag)] for tag in set(all_tags_flat)]
    self.most_common_tags = sorted(occur, key = lambda x: x[1], reverse=True)


# Zerlegung der folgenden List-Comprehension VORWÄRTS
# all_tags_flat = [tag for game in self.steam_discount_list if game['tag_list'] is not None for tag in game['tag_list']]

# 1. 
for game in self.steam_discount_list:
    pass

# 2.
for game in self.steam_discount_list:
    if game['tag_list'] is not None:
        pass

# 3.
for game in self.steam_discount_list:
    if game['tag_list'] is not None:
        for tag in game['tag_list']:
            pass

# 4. pass mit dem Ausdruck ersetzten
new_list = []
for game in self.steam_discount_list:
    if game['tag_list'] is not None:
        for tag in game['tag_list']:
            new_list.append(tag)


# Zerlegung der folgenden List-Comprehension RÜCKWÄRTS
# all_tags_flat = [tag for game in self.steam_discount_list if game['tag_list'] is not None for tag in game['tag_list']]

# 1. 
for tag in game['tag_list']:
    pass

# 2.
if game['tag_list'] is not None:
    for tag in game['tag_list']:
        pass

# 3.
for game in self.steam_discount_list:
    if game['tag_list'] is not None:
        for tag in game['tag_list']:
            pass

# 4. 'pass' mit dem Ausdruck ersetzten, welcher als List-Element eingetragen werden soll.
new_list = []
for game in self.steam_discount_list:
    if game['tag_list'] is not None:
        for tag in game['tag_list']:
            new_list.append(tag)

# Wenn ihr dieses File mit einem Linter anschaut seht iht, dass ab Schritt 3 nur noch das Argument self nicht definiert ist. 
# In den vorhergehenden Schritten ist der Bezeichner game nicht definiert, da dieser erst in der äußersten Schale aus der discount_list gezogen wird.