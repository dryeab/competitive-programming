/*
    https://codeforces.com/problemset/problem/500/A
    Time: O(n)
    Space: O(n)
*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, t;
    cin >> n >> t;

    vector<int> a(n - 1);
    for (int &x : a)
        cin >> x;

    vector<bool> isPossible(n);
    isPossible[0] = true;

    for (int i = 0; i < n - 1; ++i)
        if (isPossible[i])
            isPossible[i + a[i]] = true;

    cout << (isPossible[t - 1] ? "YES" : "NO") << endl;
}