#include <iostream>

using namespace std;

int limit[100];

int main()
{

    int n, m;
    cin >> n >> m;

    int x = 0, l, sl, sp;

    for (int i = 0; i < 100;)
    {
        cin >> l >> sl;
        while (l--)
        {
            limit[i] = sl;
            i++;
        }
    }

    int ans = 0;

    for (int i=0; i < 100;){
        cin >> l >> sp;
        while (l--){
            ans = max(ans, sp - limit[i]);
            i++;
        }
    }

    cout << ans;

    return 0;
}