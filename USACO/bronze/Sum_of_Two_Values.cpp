#include <iostream>
#include <map>

using namespace std;

int main()
{
    map<int, int> m;
    
    int n, x;
    cin >> n >> x;

    int temp;
    for (int i = 0; i <= n; ++i)
    {
        if (i == n)
        {
            cout << "IMPOSSIBLE";
            break;
        }
        cin >> temp;
        if (m[x - temp])
        {
            cout << m[x - temp] << " " << i + 1;
            break;
        }
        m[temp] = i + 1;
    }
}