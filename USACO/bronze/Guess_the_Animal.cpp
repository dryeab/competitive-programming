#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main()
{

    int n;
    cin >> n;

    unordered_map<string, int> counter;
    vector<vector<string>> chars(n);

    string name, chr;
    int n_chars;

    for (int i = 0; i < n; ++i)
    {
        cin >> name >> n_chars;
        while (n_chars--)
        {
            cin >> chr;
            if (counter.find(chr) == counter.end())
                counter[chr] = 0;

            chars[i].push_back(chr);
            counter[chr]++;
        }
    }

    int ans = 0;
    for (vector<string> animal : chars)
    {
        int x = 0;
        for (string chr : animal)
        {
            cout << "counter of " << chr << " is " << counter[chr] << endl;

            if (counter[chr] > 1)
                x++;
        }

        ans = max(ans, x);
    }

    cout << ans;
}