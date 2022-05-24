#include <iostream>

using namespace std;

int enter[26]{}, leave[26]{};

int main()
{
    char cow;
    for (int i = 1; i < 53; ++i)
    {
        cin >> cow;
        cow -= 'A';
        if (!enter[cow])
            enter[cow] = i;
        else
            leave[cow] = i;
    }

    int ans = 0;
    for (int i = 0; i < 26; ++i)
    {
        for (int j = 0; j < 26; ++j)
        {
            if (enter[i] < enter[j] && enter[j] < leave[i] && leave[j] > leave[i])
                ans++;
        }
    }

    cout << ans;
}