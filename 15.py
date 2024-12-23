def del_enem(people,enemies):
    res = []
    for enemy in enemies:
        for i in range (0,len(people)-1):
            if people[i] == enemy:
                res.append(people[i])

    return res

print(del_enem(['paul','simon','ashley'], ['paul', 'simon']))