#include <iostream>

using namespace std;

int count[] = {0, 0};

int main()
{
    int n;
    cin >> n;

    while (n--)
    {
        int i;
        cin >> i;

        count[i % 2]++;
    }

    int ans = 0, turn = 0;

    while (count[0] || count[1])
    {
        if (turn == 0)
        {
            if (count[0] > 0)
            {
                ans++;
                count[0]--;
            }
            else
            {
                if (count[1] == 1)
                {
                    ans--;
                    break;
                }
                ans++;
                count[1] -= 2;
            }
        }
        else
        {

            if (count[1] == 0)
                break;

            ans++;
            count[1]--;
        }

        turn = (turn + 1) % 2;
    }

    cout << ans;
}