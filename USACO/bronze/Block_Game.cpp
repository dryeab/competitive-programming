#include <iostream>

using namespace std;

int soln[26] = {};

int main()
{
    int N;
    cin >> N;

    while (N--)
    {
        int c1[26] = {}, c2[26] = {};

        string word1, word2;
        cin >> word1 >> word2;

        for (auto x : word1)
            c1[x - 'a']++;
        for (auto x : word2)
            c2[x - 'a']++;

        for (int i = 0; i < 26; ++i)
            soln[i] += max(c1[i], c2[i]);
    }

    for (auto i : soln)
        cout << i << endl;
}