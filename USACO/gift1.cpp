/*
ID: dryeab1
LANG: C++
PROG: gift1
*/

#include <bits/stdc++.h>

using namespace std;

int main() {

    ofstream fout("gift1.out");
    ifstream fin("gift1.in");

    int np;
    fin >> np;

    map<string, int> money;
    vector<string> order;
    string name;

    for (int i = 0; i < np; ++i) {
        fin >> name;
        order.push_back(name);
    }

    int m, ng;
    for (int i = 0; i < np; ++i) {

        fin >> name;
        fin >> m >> ng;

        if (ng) {
            money[name] -= (m / ng) * ng;
            for (int j = 0; j < ng; ++j) {
                fin >> name;
                money[name] += m / ng;
            }
        }
    }

    for (auto name : order)
        fout << name << " " << money[name] << endl;

    return 0;
}