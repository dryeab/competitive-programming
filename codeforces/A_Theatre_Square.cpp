#include <iostream>

using namespace std;

int main()
{
    int n, m, a;
    cin >> n >> m >> a;

    int x = (n / a) + (n % a ? 1 : 0);
    int y = (m / a) + (m % a ? 1 : 0);

    cout << (long long)x * y << endl;
}