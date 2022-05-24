#include <iostream>
#include <algorithm>

using namespace std;

int buckets[1001] = {};

int main()
{

    int N, s, t, b;
    cin >> N;

    while (N--)
    {
        cin >> s >> t >> b;
        for (int i = s; i <= t; ++i)
        {
            buckets[i] += b;
        }
    }

    int ans = 0;
    for (auto b : buckets)
        ans = max(ans, b);

    cout << ans;
}