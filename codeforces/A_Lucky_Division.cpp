#include <iostream>

using namespace std;

bool isLucky(int i)
{
    while (i)
    {
        if (i % 10 != 4 && i % 10 != 7)
            return false;
        i /= 10;
    }

    return true;
}
int main()
{
    int n;
    cin >> n;

    for (int i = 4; i < 1000; ++i)
    {
        if (isLucky(i) && n % i == 0)
        {
            cout << "YES" << endl;
            return 0;
        }
    }

    cout << "NO" << endl;
}