#include <iostream>

using namespace std;

int index(string s, int start, char x)
{
    for (int i = start; i < s.size(); ++i)
    {
        if (s[i] == x)
            return i;
    }

    return -1;
}

int main()
{
    string s;
    cin >> s;

    int start = -1;
    for (char x : (string) "hello")
    {
        start = index(s, start + 1, x);
        if (start == -1)
        {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
}