#include <iostream>
#include <algorithm>

using namespace std;

int main()
{

    int a, b, c, d;

    cin >> a >> b;
    cin >> c >> d;

    if (c < a)
    {
        swap(a, c);
        swap(b, d);
    }

    if (c >= b)
        cout << (b - a) + d - c;
    else
        cout << max(b, d) - a;

    return 0;
}