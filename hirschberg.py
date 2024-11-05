# Scoring parameters
match_score = 1
mismatch_penalty = -1
gap_penalty = -2

def calculate_score(a, b):
    if a == b:
        return match_score
    else:
        return mismatch_penalty

# Function to compute alignment score of prefixes with minimal space
def nw_score(X, Y):
    n, m = len(X), len(Y)
    dp = [0] * (m + 1)

    # Initialize DP array for Y sequence
    for j in range(1, m + 1):
        dp[j] = dp[j - 1] + gap_penalty

    # Fill DP array for X sequence
    for i in range(1, n + 1):
        prev = dp[0]
        dp[0] += gap_penalty
        for j in range(1, m + 1):
            temp = dp[j]
            if X[i - 1] == Y[j - 1]:
                dp[j] = max(prev + calculate_score(X[i - 1], Y[j - 1]),
                            dp[j] + gap_penalty,
                            dp[j - 1] + gap_penalty)
            else:
                dp[j] = max(prev + calculate_score(X[i - 1], Y[j - 1]),
                            dp[j] + gap_penalty,
                            dp[j - 1] + gap_penalty)
            prev = temp
    return dp

# Hirschberg's algorithm for sequence alignment with scoring
def hirschberg(X, Y):
    if len(X) == 0:
        return "-" * len(Y), Y, gap_penalty * len(Y)
    elif len(Y) == 0:
        return X, "-" * len(X), gap_penalty * len(X)
    elif len(X) == 1 or len(Y) == 1:
        # Base case: one character in X or Y, solve directly
        align1, align2, score = "", "", 0
        for x in X:
            if x in Y:
                align1, align2 = x, Y[Y.index(x)]
                score += match_score
            else:
                align1, align2 = x, '-'
                score += gap_penalty
        for y in Y:
            if y not in align1:
                align1 += "-"
                align2 += y
                score += gap_penalty
        return align1, align2, score
    else:
        xlen = len(X)
        xmid = xlen // 2

        # Calculate scores from the left half and right half
        scoreL = nw_score(X[:xmid], Y)
        scoreR = nw_score(X[xmid:][::-1], Y[::-1])[::-1]

        # Find the optimal split point in Y
        ysplit = max(range(len(Y) + 1), key=lambda j: scoreL[j] + scoreR[j])

        # Recursive calls to align both halves
        align1_left, align2_left, score_left = hirschberg(X[:xmid], Y[:ysplit])
        align1_right, align2_right, score_right = hirschberg(X[xmid:], Y[ysplit:])

        # Combine results from left and right parts
        align1 = align1_left + align1_right
        align2 = align2_left + align2_right
        total_score = score_left + score_right

        return align1, align2, total_score

# Example usage
X = "CG"
Y = "CA"
align1, align2, total_penalty = hirschberg(X, Y)
print("Alignment 1:", align1)
print("Alignment 2:", align2)
print("Total Penalty:", total_penalty)
