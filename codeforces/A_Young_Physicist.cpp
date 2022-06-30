#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    int x = 0, y = 0, z = 0, a, b, c;
    while (n--)
    {
        cin >> a >> b >> c;
        x += a;
        y += b;
        z += c;
    }

    if (x == 0 && y == 0 && z == 0)
        cout << "YES";
    else
        cout << "NO";
    cout << endl;
}