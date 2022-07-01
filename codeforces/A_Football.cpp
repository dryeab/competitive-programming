/*
    https://codeforces.com/problemset/problem/43/A
    Time: O(n)
    Space: O(n)
*/

#include <iostream>
#include <map>

using namespace std;

int main()
{
    int n;
    cin >> n;

    map<string, int> score;

    while (n--)
    {
        string team;
        cin >> team;

        score[team]--;
    }

    string ans = "";
    for (auto it = score.begin(); it != score.end(); ++it)
    {
        if (ans == "" || score[ans] > it->second)
            ans = it->first;
    }

    cout << ans << endl;
}