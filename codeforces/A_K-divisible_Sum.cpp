#include <iostream>

using namespace std;

void solve()
{
    long long n, k;
    cin >> n >> k;

    if (n > k)
        k = k * (n / k) + (n % k ? k : 0);

    cout << (k / n + (k % n ? 1 : 0)) << endl;
}

int main()
{
    int t;
    cin >> t;

    while (t--)
        solve();
}