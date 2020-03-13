ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
uniq_ids = []

for key in ids:
    for id in ids[key]:
        if id not in uniq_ids:
            uniq_ids.append(id)
        else:
            continue
print(uniq_ids)