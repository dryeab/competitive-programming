#include <iostream>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int p[20];

int solve(int i, int n, int first, int second)
{
    if (i == n)
    {
        return abs(second - first);
    }

    return min(solve(i + 1, n, first + p[i], second), solve(i + 1, n, first, second + p[i]));
}

int main()
{

    int n;
    cin >> n;

    for (int i = 0; i < n; ++i)
    {
        cin >> p[i];
    }

    cout << solve(0, n, 0, 0);
}