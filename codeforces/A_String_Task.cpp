#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
    string res = "", s;
    cin >> s;

    for (char x : s)
    {
        if (x < 97)
            x += 32;

        switch (x)
        {
        case 'a':
            break;
        case 'e':
            break;
        case 'i':
            break;
        case 'o':
            break;
        case 'u':
            break;
        case 'y':
            break;
        default:
            res += ".";
            res += x;
        }
    }

    cout << res << endl;
}