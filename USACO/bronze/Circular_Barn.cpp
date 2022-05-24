#include <iostream>
#include <vector>

using namespace std;

int main()
{

    int n, ri;
    cin >> n;

    vector<int> v;

    while (n--)
    {
        cin >> ri;
        v.push_back(ri);
    }

    int ans = 1e9;

    for (int i = 0; i < v.size(); ++i)
    {
        int dis = 1, j = (i + 1) % v.size(), total = 0;
        while (j != i)
        {
            total += v[j] * dis;
            dis++;
            j = (j + 1) % v.size();
        }
        ans = min(ans, total);
    }

    cout << ans;
}