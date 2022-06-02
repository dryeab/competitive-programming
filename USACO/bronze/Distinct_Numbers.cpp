#include <iostream>
#include <unordered_set>

using namespace std;

int main()
{
    int n;
    cin >> n;

    unordered_set<int> s;

    int temp;
    while (n--)
    {
        cin >> temp;
        s.insert(temp);
    }

    cout << s.size();
}