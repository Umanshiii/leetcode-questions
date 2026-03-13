def largestRectangle(h):
    n = len(h)
    ans = 0

    for i in range(n):
        height = h[i]
        width = 0

        for j in range(i, n):
            height = min(height, h[j])
            width += 1
            ans = max(ans, height * width)

    return ans
