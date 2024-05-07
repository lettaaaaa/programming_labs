from bisect import bisect_left


def find_triplet_sum(a, x):
    a.sort()
    lo, hi = 0, len(a) - 1
    while lo + 1 < hi:
        i = bisect_left(a, x - a[lo] - a[hi], lo + 1, hi)  # binary search
        assert lo < i
        triplet_sum = a[lo] + a[i] + a[hi]
        if i == hi or triplet_sum < x:  # sum is too small
            lo += 1
        elif triplet_sum > x:  # sum is too big
            hi -= 1
        else:  # found
            assert lo < i < hi and triplet_sum == x
            return True
    return False


"""if __name__ == '__main__':
    N = list(map(int, input().split()))
    P = int(input())
    print(find_triplet_sum(N, P))"""
