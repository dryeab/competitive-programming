#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(vector<int> &a, vector<int> &b)
{
    return a[0] < b[0];
}

int main()
{
    int s, n;
    cin >> s >> n;

    vector<vector<int>> d(n, vector<int>(2));
    for (int i = 0; i < n; ++i)
    {
        cin >> d[i][0] >> d[i][1];
    }

    sort(d.begin(), d.end(), compare);

    for (int i = 0; i < n; ++i)
    {
        if (s <= d[i][0])
        {
            cout << "NO" << endl;
            return 0;
        }
        s += d[i][1];
    }

    cout << "YES" << endl;
}