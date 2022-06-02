#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int graph[100000]{};

int main()
{
    int n;
    cin >> n;

    int a, b;
    for (int i = 1; i < n; ++i)
    {
        cin >> a >> b;
        graph[a]++;
        graph[b]++;
    }

    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        ans = max(ans, graph[i] + 1);
    }

    cout << ans;
}