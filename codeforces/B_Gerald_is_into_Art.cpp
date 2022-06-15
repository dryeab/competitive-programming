#include <iostream>
#include <algorithm>

using namespace std;

int a1, a2, a3, b1, b2, b3;

bool solve(int a2, int b2, int a3, int b3)
{
    if (a2 + a3 <= a1 && max(b2, b3) <= b1)
        return true;
    if (b2 + b3 <= b1 && max(a2, a3) <= a1)
        return true;

    return false;
}

int main()
{

    cin >> a1 >> b1;
    cin >> a2 >> b2;
    cin >> a3 >> b3;

    if (solve(a2, b2, a3, b3) || solve(b2, a2, a3, b3) || solve(a2, b2, b3, a3) || solve(b2, a2, b3, a3))
        cout << "Yes";
    else
        cout << "No";
}