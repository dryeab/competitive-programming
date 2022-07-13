/**
 * https://codeforces.com/problemset/problem/550/C
 * Time: O(n^3)
 * Space: O(n)
 */

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

void solve(vector<int> &nums) {

    int n = nums.size();

    for (int i = 0; i < n; ++i) {

        if (nums[i] % 8 == 0) {
            cout << "YES \n"
                 << nums[i];
            return;
        }

        for (int j = i + 1; j < n; ++j) {
            if ((nums[i] * 10 + nums[j]) % 8 == 0) {
                cout << "YES \n"
                     << (nums[i] * 10 + nums[j]);
                return;
            }
            for (int k = j + 1; k < n; ++k) {
                if ((nums[i] * 100 + nums[j] * 10 + nums[k]) % 8 == 0) {
                    cout << "YES \n"
                         << (nums[i] * 100 + nums[j] * 10 + nums[k]);
                    return;
                }
            }
        }
    }
    cout << "NO";
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<int> nums;

    string s;
    cin >> s;

    for (int i = 0; i < s.size(); ++i) {
        nums.push_back(s[i] - '0');
    }

    solve(nums);
}