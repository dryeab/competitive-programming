#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{

    int n;
    string a, b;

    cin >> n >> a >> b;

    int l = 0, r = 0, ans = 0;
    
    while (r <= n)
    {
        if (r == n || a[r] == b[r])
        {
            ans += min(1, r - l);
            l = r + 1;
        }
        r++;
    }

    cout << ans;
}