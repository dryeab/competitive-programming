#include <iostream>
#include <map>
#include <string>
#include <cstdlib>

using namespace std;

map<string, int> m = {
    {"Ox", 1}, {"Tiger", 2}, {"Rabbit", 3}, {"Dragon", 4}, {"Snake", 5}, {"Horse", 6}, {"Goat", 7}, {"Monkey", 8}, {"Rooster", 9}, {"Dog", 10}, {"Pig", 11}, {"Rat", 12}};

map<string, int> year = {{"Bessie", 0}};
map<string, string> zodiac = {{"Bessie", "Ox"}};

void calculate(string dxn, string first, string last)
{
    string zl = zodiac[last], zf = zodiac[first];
    int i = m[zf], j = m[zl], dif;

    if (dxn == "previous")
    {
        if (j < i)
            dif = 12 - (i - j);
        else
            dif = j - i;

        dif = -dif;
    }
    else
    {
        if (i < j)
            dif = 12 - (j - i);
        else
            dif = i - j;
    }

    year[first] = year[last] + dif;
}

int main()
{
    string first, dxn, z, last, _;

    int n;
    cin >> n;

    while (n--)
    {
        for (int i = 0; i < 8; ++i)
        {
            if (i == 0)
                cin >> first;
            else if (i == 3)
                cin >> dxn;
            else if (i == 4)
                cin >> z;
            else if (i == 7)
                cin >> last;
            else
                cin >> _;
        }

        zodiac[first] = z;
        calculate(dxn, first, last);

        if (first == "Elsaie")
            break;
    }

    cout << abs(year["Bessie"] - year["Elsie"]);
}