/**
 * https://codeforces.com/problemset/problem/82/A
 * Time:
 * Space:
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    string Q[] = {"Sheldon", "Leonard", "Penny", "Rajesh", "Howard"};

    for (int round = 1;; round = round << 1) {
        for (int i = 0; i < 5; ++i) {
            n -= round;
            if (n <= 0) {
                cout << Q[i];
                return 0;
            }
        }
    }
}
