/**
 * http://www.usaco.org/index.php?page=viewproblem2&cpid=965
 * Time: O(N)
 * Space: O(N)
 */

#include <bits/stdc++.h>

using namespace std;

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("lineup.in", "r", stdin);
    freopen("lineup.out", "w", stdout);

    int n;
    cin >> n;

    map<string, set<string>> adj;
    map<string, int> indegree;
    set<string> visited;

    for (int i = 0; i < n; ++i) {
        string x, y, z;
        cin >> x >> z >> z >> z >> z >> y;
        adj[x].insert(y);
        adj[y].insert(x);
        indegree[x]++, indegree[y]++;
    }

    vector<string> cows, res;

    cows.push_back("Beatrice");
    cows.push_back("Belinda");
    cows.push_back("Bella");
    cows.push_back("Bessie");
    cows.push_back("Betsy");
    cows.push_back("Blue");
    cows.push_back("Buttercup");
    cows.push_back("Sue");

    for (string cow : cows) {
        while (!visited.count(cow) && indegree[cow] < 2) {
            res.push_back(cow);
            visited.insert(cow);
            for (string another : adj[cow]) {
                if (!visited.count(another)) {
                    cow = another;
                    indegree[cow]--;
                    break;
                }
            }
        }
    }

    for (string x : res)
        cout << x << "\n";
}