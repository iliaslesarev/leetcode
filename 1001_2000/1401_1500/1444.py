MOD = 10 ** 9 + 7

def ways(pizza, k):
    rows, cols = len(pizza), len(pizza[0])
    apples = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            apples[i][j] = apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1] + (pizza[i][j] == 'A')
    memo = {}
    def dfs(i, j, pieces, cuts):
        if (i, j, pieces, cuts) in memo:
            return memo[(i, j, pieces, cuts)]
        if pieces == k:
            return 1
        if cuts >= k - 1:
            return 0
        ans = 0
        if k - pieces <= cols - j:
            for r in range(i+1, rows):
                if apples[i][j] - apples[r][j] > 0 and apples[r][j] < apples[i][j]:
                    ans += dfs(r, j, pieces + 1, cuts + 1)
                    ans %= MOD
        if k - pieces <= rows - i:
            for c in range(j+1, cols):
                if apples[i][j] - apples[i][c] > 0 and apples[i][c] < apples[i][j]:
                    ans += dfs(i, c, pieces + 1, cuts + 1)
                    ans %= MOD
        ans += dfs(i, j, pieces, cuts + 1)
        ans %= MOD
        memo[(i, j, pieces, cuts)] = ans
        return ans
    return dfs(0, 0, 1, 0) % MOD

print(ways([".A..A","A.A..","A.AA.","AAAA.","A.AA."], 5)) 