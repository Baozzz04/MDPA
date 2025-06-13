import math

def min_split_with_frequency_difference(arr):
    n = len(arr)
    dp = [math.inf] * (n + 1)
    dp[0] = 0
    prev = [-1] * (n + 1)

    for i in range(1, n + 1):
        freq = {}
        for j in range(i - 1, -1, -1):
            elem = arr[j]
            freq[elem] = freq.get(elem, 0) + 1
            length = i - j

            if len(freq) == 0:
                f1, f2 = 0, 0
            elif len(freq) == 1:
                f1 = list(freq.values())[0]
                f2 = 0
            else:
                sorted_freqs = sorted(freq.values(), reverse=True)
                f1 = sorted_freqs[0]
                f2 = sorted_freqs[1]

            if f1 - f2 >= 0.6 * length:
                if dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

    if dp[n] == math.inf:
        return -1, []

    subarrays = []
    idx = n

    while idx > 0:
        j = prev[idx]
        subarray = arr[j:idx]
        subarrays.append(subarray)
        idx = j

    subarrays.reverse()

    return dp[n], subarrays
