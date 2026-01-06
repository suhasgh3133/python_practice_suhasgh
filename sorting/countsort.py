def counting_sort(arr):
    max_val = max(arr)
    count = [0]*(max_val+1)
    for x in arr:
        count[x] += 1
    res = []
    for i in range(len(count)):
        res.extend([i]*count[i])
    return res
