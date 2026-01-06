def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for x in arr:
        idx = int(len(arr) * x)
        buckets[idx].append(x)
    for b in buckets:
        b.sort()
    return [x for b in buckets for x in b]
