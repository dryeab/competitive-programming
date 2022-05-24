#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

/*
    Bessie - 1
    Elsie - 2
    Mildred - 3
*/

int change[100][2]{};

vector<string> cows{"Bessie", "Elsie", "Mildred"};

vector<int> output = {7, 7, 7};

int ans = 0; // final answer store

void change_output(int ch[])
{
    int index = ch[0];

    bool was_there = (output[index] == max({output[0], output[1], output[2]}));

    output[index] += ch[1]; // changed

    bool is_here = (output[index] == (output[index] == max({output[0], output[1], output[2]})));

    if (is_here != was_there)
        ans++;
}

int main()
{
    int N;
    cin >> N;

    int day, c, index;
    string cow;

    while (N--)
    {
        cin >> day >> cow >> c;
        index = find(cows.begin(), cows.end(), cow) - cows.begin();
        change[day][0] = index;
        change[day][1] = c;
    }

    for (int i = 0; i < 100; ++i)
    {
        if (change[i][0])
        {
            change_output(change[i]);
        }
    }

    cout << ans;
}