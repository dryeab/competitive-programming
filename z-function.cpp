#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

/*

    - Find a vector, z, of length n such that z[i] is the length of the longest
      prefix of s such that s[i:i+z[i]] is equal to s[:z[i]]
    - The main idea is to keep track of the rightmost substring that is the prefix
      of the string
    - For more: https://cp-algorithms.com/string/z-function.html
*/

vector<int> zfunc(string& s) {
    int n = s.size();
 
    vector<int> z(n);
    int l = 0, r = 0; // [l, r] - the rightmost substring that feats with prefix of s
    for (int i = 1; i < n; ++i) {
        if (r > i) {
            z[i] = min(z[i - l], r - i + 1);
        }
        while (i + z[i] < n && s[i + z[i]] == s[z[i]]) {
            z[i]++;
        }
        if (i + z[i] - 1 >= r) {
            r = i + z[i] - 1, l = i;
        }
    }
 
    return z;
}