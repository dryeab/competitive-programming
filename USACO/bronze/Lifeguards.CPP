#include <iostream>

using namespace std;

int count[1001]{}, interval[100][2];

int main()
{

    int n;
    cin >> n;

    for (int i = 0; i < n; ++i)
    {
        cin >> interval[i][0] >> interval[i][1];

        for (int j = interval[i][0]; j < interval[i][1]; ++j)
            count[j]++;
    }

    int total = 0;
    for (int c : count)
        total += c > 0;

    int ans = 1005;
    for (int i = 0; i < n; ++i)
    {
        int x = 0;
        for (int j = interval[i][0]; j < interval[i][1]; ++j)
        {
            if (count[j] == 1)
                x++;
        }

        ans = min(ans, x);
    }

    cout << total - ans;
}