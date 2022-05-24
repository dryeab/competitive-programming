#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int loc[1001];
char dxn[1001];

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> dxn[i] >> loc[i];
    }

    int ans = n;

    for (int i = 0; i < n; ++i)
    {
        int liers = 0;
        for (int j = 0; j < n; ++j)
        {
            if (dxn[i] == dxn[j])
                continue;
            if (dxn[i] == 'G' && loc[j] >= loc[i])
                continue;
            if (dxn[i] == 'L' && loc[j] <= loc[i])
                continue;
            liers++;
        }
        ans = min(ans, liers);
    }

    cout << ans << endl;
}