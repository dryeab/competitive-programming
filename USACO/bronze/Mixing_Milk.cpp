#include <iostream>

using namespace std;

int main()
{
    int change, j, i;
    int x[3], capacity[3];

    for (int i = 0; i < 3; ++i)
    {
        cin >> capacity[i];
        cin >> x[i];
    }

    for (int k = 0; k < 100; k++)
    {
        i = k % 3;
        j = (i + 1) % 3;
        change = min(capacity[j] - x[j], x[i]);
        x[i] -= change;
        x[j] += change;
    }

    for (auto i : x)
        cout << i << endl;

    return 0;
}