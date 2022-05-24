#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

    int n, k;
    vector<int> diamonds;

    cin >> n >> k;

    while (n--)
    {
        int d;
        cin >> d;
        diamonds.push_back(d);
    }

    sort(diamonds.begin(), diamonds.end());

    int i = 0, j = 0, ans = 0;

    while (j < diamonds.size())
    {

        while (diamonds[j] - diamonds[i] > k)
            i++;

        while (j < diamonds.size() && diamonds[j] - diamonds[i] <= k)
        {
            j++;
        }

        ans = max(ans, j - i);
    }

    cout << max(ans, j - i);
}