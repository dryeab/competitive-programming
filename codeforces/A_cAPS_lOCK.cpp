#include <iostream>

using namespace std;

bool isMistake(string s)
{
    for (int i = 1; i < s.size(); ++i)
    {
        if (s[i] >= 97)
            return false;
    }
    return true;
}

int main()
{
    string s;
    cin >> s;

    if (isMistake(s))
    {
        string ans = "";

        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] >= 97)
                ans += s[i] - 32;
            else
                ans += s[i] + 32;
        }
        cout << ans << endl;
    }
    else
    {
        cout << s << endl;
    }
}