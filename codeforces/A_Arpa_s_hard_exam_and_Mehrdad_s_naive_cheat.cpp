/*
    https://codeforces.com/problemset/problem/742/A
    Time: O(log(n))
*/

#include <iostream>

using namespace std;

int pow(int b, int e, int mod)
{
    if (e == 0)
        return 1;

    int res;

    if (e % 2)
        res = b * pow(b, e - 1, mod);
    else
    {
        int temp = pow(b, e / 2, mod);
        res = temp * temp;
    }

    return res % mod;
}

int main()
{
    int n;
    cin >> n;

    if (n == 0)
        cout << 1 << endl;
    else
        cout << pow(8, n, 10) % 10 << endl;
}