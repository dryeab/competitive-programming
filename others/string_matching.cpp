/*
    https://cses.fi/problemset/task/1753
    Time: O(n + m)
    Space: O(n + m)
*/

#include <bits/stdc++.h>

using namespace std;

vector<int> pi(string &p) {

    int m = p.size();
    vector<int> pi_p(m);

    for (int i = 1, j = 0; i < m; ++i) {

        while (j > 0 && p[i] != p[j])
            j = pi_p[j - 1];

        if (p[i] == p[j])
            j++;

        pi_p[i] = j;
    }

    return pi_p;
}

int kmp(string &s, string &p) {

    string n = p + "#" + s;
    vector<int> pi_s = pi(n);

    int res = 0;
    for (int x : pi_s)
        res += x == p.size();

    return res;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    string s, p;
    cin >> s >> p;

    cout << kmp(s, p) << endl;
}