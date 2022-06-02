#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

string cows[7] = {"Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"};

map<string, int> p;
map<int, vector<string>> rp;

int main()
{
    int n;
    cin >> n;

    string cow;
    int q;

    for (int i = 0; i < n; ++i)
    {
        cin >> cow >> q;
        p[cow] += q;
    }

    for (string cow : cows)
    {
        rp[p[cow]].push_back(cow);
    }

    int i = 1;
    for (auto [q, _] : rp)
    {

        if (i == 2)
        {
            if (rp[q].size() > 1)
                cout << "tie";
            else
                cout << rp[q][0];
            break;
        }

        i += 1;
    }
}