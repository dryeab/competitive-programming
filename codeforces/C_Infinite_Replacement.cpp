#include <iostream>

using namespace std;

void solve()
{
    string s, t;
    cin >> s >> t;

    if (t == "a")
    {
        cout << 1 << endl;
        return;
    }

    for (char c : t)
    {
        if (c == 'a')
        {
            cout << -1 << endl;
            return;
        }
    }

    cout << (1ll << s.size()) << endl;
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