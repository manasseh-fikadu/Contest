prices.sort()
    sums=0
    i=0
    count=0
    while sums<=k:
        sums+=prices[i]
        if sums<=k:
            count+=1
        else:
            break
        i+=1
    return count
