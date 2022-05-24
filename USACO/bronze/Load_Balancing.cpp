#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int lx[1000]{}, ly[1000]{};
int n;

int M(int a, int b)
{
    int one = 0, two = 0, three = 0, four = 0;
    for (int i = 0; i < n; ++i)
    {
        if (lx[i] <= a && ly[i] <= b)
            one++;
        if (lx[i] <= a && ly[i] > b)
            two++;
        if (lx[i] > a && ly[i] <= b)
            three++;
        if (lx[i] > a && ly[i] > b)
            four++;
    }

    return max({one, two, three, four});
}
int main()
{
    cin >> n;

    for (int i = 0; i < n; ++i)
    {
        cin >> lx[i] >> ly[i];
    }

    int ans = 1e6;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cout << lx[i] << " " << ly[j] << " " << M(lx[i], ly[j]) << endl;
            ans = min(ans, M(lx[i], ly[j]));
        }
    }

    cout << ans;

}