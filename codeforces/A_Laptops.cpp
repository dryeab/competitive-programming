/**
 * https://codeforces.com/problemset/problem/456/A
 * Time: O(n)
 * Space: O(n)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, a, b;
    cin >> n;

    // vector<pair<int, int>> order(n + 1, {-1, -1});

    // for (int i = 0; i < n; ++i) {
    //     cin >> a >> b;
    //     if (order[a].first == -1 || order[a].first > b)
    //         order[a].first = b;
    //     if (order[a].second == -1 || order[a].second < b)
    //         order[a].second = b;
    // }

    // int msf = 0, right = 0;
    // for (int i = 1; i <= n; ++i) {
    //     if (order[i].first != -1) {
    //         if (order[i].first < msf) {
    //             right = 1;
    //             break;
    //         }
    //         msf = max(msf, order[i].second);
    //     }
    // }

    vector<pair<int, int>> pq;
    for (int i = 0; i < n; ++i) {
        cin >> a >> b;
        pq.push_back(make_pair(a, b));
    }

    sort(pq.begin(), pq.end());

    int right = 0;
    for (int i = 1; i < n; ++i) {
        if (pq[i - 1].first != pq[i].first && pq[i].second < pq[i - 1].second) {
            right = 1;
            break;
        }
    }

    cout << (right ? "Happy Alex" : "Poor Alex");
}