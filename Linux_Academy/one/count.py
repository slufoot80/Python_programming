count = 0
while count < 10:
    if count % 2 != 0:
        count += 1
        continue
    print("We are counting odd numbers %s" % count)
    count += 1
    #elif count % 2 != 0:
    #    count += 1
    #    continue
    #print("We are counting odd numbers %s" % count)
    #count += 1
