/**
 * https://codeforces.com/problemset/problem/1234/B1
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, k, id, last;
    cin >> n >> k;

    queue<int> q;
    set<int> inside;

    for (int i = 0; i < n; ++i) {
        cin >> id;
        if (inside.count(id))
            continue;

        if (q.size() == k) {
            last = q.front();
            q.pop();
            inside.erase(last);
        }

        q.push(id);
        inside.insert(id);
    }

    vector<int> res;
    while (!q.empty()) {
        last = q.front();
        q.pop();
        res.push_back(last);
    }

    cout << res.size() << endl;

    while (res.size()) {
        last = res[res.size() - 1];
        res.pop_back();
        cout << last << " ";
    }
}