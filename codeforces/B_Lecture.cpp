#include <iostream>
#include <map>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    map<string, string> mp;
    string a, b;

    while (m--)
    {
        cin >> a >> b;
        mp[a] = b;
    }

    string c;
    while (n--)
    {
        cin >> c;
        if (mp[c].size() < c.size())
            c = mp[c];
        cout << c << " \n"[n == 0];
    }
}