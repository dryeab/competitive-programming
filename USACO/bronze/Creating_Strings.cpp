#include <iostream>
#include <vector>

using namespace std;

string s;
vector<string> perms;
int counter[26]{};

void permute(string perm)
{
    if (perm.size() == s.size())
    {
        perms.push_back(perm);
        return;
    }

    for (int i = 0; i < 26; ++i)
    {
        if (counter[i])
        {
            counter[i]--;
            permute(perm + (char)('a' + i));
            counter[i]++;
        }
    }
}

int main()
{

    cin >> s;

    for (char c : s)
        counter[c - 'a']++;

    permute("");

    cout << perms.size() << endl;
    for (auto perm : perms)
    {
        cout << perm << endl;
    }
}
