    #include <bits/stdc++.h>

    typedef long long ll;

    using namespace std;

    /*

    */

    void solve() {
        int n;
        cin >> n;

        map<int, int> cnt;

        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;

            int d = 2;
            while (d * d <= x) {
                while (x % d == 0)
                    cnt[d]++, x /= d;
                d++;
            }

            if (x > 1) {
                cnt[x]++;
            }
        }

        for (auto [a, b] : cnt) {
            if (b % n) {
                cout << "NO\n";
                return;
            }
        }

        cout << "YES\n";
    }

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(0);

        int t = 1;
        cin >> t;

        while (t--) {
            solve();
        }
    }