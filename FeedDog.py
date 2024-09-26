def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()
    i=0
    j=0
    count = 0
    while i < len(hunger_level) and j < len(biscuit_size):
        if hunger_level[i] <= biscuit_size[j]:
            count += 1
            i += 1
            j+= 1
        else:
            j+= 1

    return count

