def solution(k, tangerine):
    sizes = sorted(tangerine)
    counts = []
    previous = None

    for size in sizes:
        if size == previous:
            counts[-1] += 1
        else:
            counts.append(1)
        previous = size

    counts.sort(reverse=True)

    for kinds, count in enumerate(counts, 1):
        k -= count
        if k <= 0:
            return kinds