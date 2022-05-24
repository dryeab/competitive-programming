#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int x, y, m, ans = 0;

    cin >> x >> y >> m;

    for (int i = 0; i * x <= m; ++i)
    {
        int j = (m - i * x) / y;
        ans = max(ans, i * x + j * y);
    }

    cout << ans;
}