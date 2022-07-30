#include <bits/stdc++.h>

using namespace std;

vector<int> pi(const string &s) {

    int n = s.size();
    vector<int> pi_s(n);

    for (int i = 1, j = 0; i < n; ++i) {

        while (j > 0 && s[j] != s[i])
            j = pi_s[j - 1];

        if (s[i] == s[j])
            j++;

        pi_s[i] = j;
    }

    return pi_s;
}

int kmp(string &s, string &p) {

    int n = s.size(), m = p.size();
    string new_string = p + "#" + s; // -#- can be any character that doesn't appear both in p and s
    vector<int> pi_p = pi(new_string);

    for (int i = m + 1; i < n + m + 1; ++i)
        if (pi_p[i] == m)
            return i - (m + 1) - m + 1;

    return -1;
}

int main() {
    string x = "amalgamation", p = "amat";
    cout << kmp(x, p);
}