#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> x;

int calculate(int i)
{
    int l = i, r = i, rad = 1;
    while (l && x[l] - rad <= x[l - 1] && r < x.size() - 1 && x[r] + rad >= x[r + 1])
    {
        rad++;
        l--;
        r++;
    }

    return r - l + 1;
}

int main()
{
    int n;
    cin >> n;

    int p;
    for (int i = 0; i < n; ++i)
    {
        cin >> p;
        x.push_back(p);
    }

    sort(x.begin(), x.end());

    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        ans = max(ans, calculate(i));
    }

    cout << ans;
}