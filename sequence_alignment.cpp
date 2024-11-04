// CPP program to implement sequence alignment
// problem.
#include <bits/stdc++.h>

using namespace std;

// function to find out the minimum penalty
void getMinimumPenalty(string x, string y, int pxy, int pgap)
{
	int i, j; // initialising variables
	
	int m = x.length(); // length of gene1
	int n = y.length(); // length of gene2
	
	// table for storing optimal substructure answers
	int dp[n+m+1][n+m+1] = {0};

	// initialising the table 
	for (i = 0; i <= (n+m); i++)
	{
		dp[i][0] = i * pgap;
		dp[0][i] = i * pgap;
	} 

	// calculating the minimum penalty
	for (i = 1; i <= m; i++)
	{
		for (j = 1; j <= n; j++)
		{
			if (x[i - 1] == y[j - 1])
			{
				dp[i][j] = dp[i - 1][j - 1];
			}
			else
			{
				dp[i][j] = min({dp[i - 1][j - 1] + pxy , 
								dp[i - 1][j] + pgap , 
								dp[i][j - 1] + pgap });
			}
		}
	}
	
	// Printing the final answer
	cout << "Minimum Penalty in aligning the genes = ";
	cout << dp[m][n] << "\n";
	return;
}

// Driver code
int main(){
	// input strings
	string gene1 = "PALETTE";
	string gene2 = "PALATE";
	
	// initialising penalties of different types
	int misMatchPenalty = 3;
	int gapPenalty = 2;

	// calling the function to calculate the result
	getMinimumPenalty(gene1, gene2, 
		misMatchPenalty, gapPenalty);
	return 0;
}
