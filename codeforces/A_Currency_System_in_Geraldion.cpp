#include <iostream>
#include <algorithm>

using namespace std;

int a[1000];

int main()
{
    int n, x;
    cin >> n;

    for (int i = 0; i < n; ++i)
    {
        cin >> x;
        if (x == 1)
        {
            cout << -1;
            return 0;
        }
    }

    cout << 1;
}