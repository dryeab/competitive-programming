#include <iostream>
#include <vector>
#include <string>

using namespace std;

void solve()
{
    int n;
    cin >> n;

    vector<int> a(n);
    for (auto &x : a)
        cin >> x;

    if (n % 2)
    {
        cout << "Mike";
    }
    else
    {
        int smallest = 0;
        for (int i = 1; i < n; ++i)
            if (a[i] < a[smallest])
                smallest = i;

        if (smallest % 2 == 0)
            cout << "Joe";
        else
            cout << "Mike";
    }

    cout << endl;
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        solve();
    }
}