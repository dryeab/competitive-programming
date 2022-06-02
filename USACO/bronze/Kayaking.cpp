#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>

using namespace std;

int w[101];
int n;

int calculate(int i, int j)
{
    int l = 0, r = 1, ans = 0;

    while (r < 2 * n)
    {

        if (l == i || l == j)
            l++;
        else if (r <= l || r == i || r == j)
            r++;
        else
        {
            ans += w[r] - w[l];
            l = r + 1;
            r++;
        }
    }

    return ans;
}

int main()
{

    cin >> n;

    for (int i = 0; i < 2 * n; ++i)
    {
        cin >> w[i];
    }

    sort(w, w + (2 * n));

    int ans = (int)1e6;

    for (int i = 0; i < 2 * n; ++i)
    {
        for (int j = 0; j < 2 * n; ++j)
        {
            if (i != j)
                ans = min(ans, calculate(i, j));
        }
    }

    cout << ans;
}