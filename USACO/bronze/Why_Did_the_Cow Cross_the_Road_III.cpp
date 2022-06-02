#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

    int n;
    cin >> n;

    vector<pair<int, int>> t;
    int a, b;
    for (int i = 0; i < n; ++i)
    {
        cin >> a >> b;
        t.push_back(make_pair(a, b));
    }

    sort(t.begin(), t.end());

    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        if (t[i].first > ans)
        {
            ans = t[i].first;
        }
        ans += t[i].second;
    }

    cout << ans;
}