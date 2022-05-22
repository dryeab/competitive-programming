#include <iostream>
#include <vector>

using namespace std;

int main()
{

    int m, n, k;

    cin >> m >> n >> k;

    char c;
    vector<vector<string>> store(m, vector<string>(n));

    for (int i = 0; i < m; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> c;
            store[i][j] = string(k, c);
        }

        for (int j = 0; j < k; ++j)
        {
            for (int l = 0; l < n; ++l)
            {
                cout << store[i][l];
            }
            cout << endl;
        }
    }

    return 0;
}