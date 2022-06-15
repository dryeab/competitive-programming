#include <iostream>

using namespace std;

int visited[202][202] = {};

bool check(int x, int y)
{

    int dxn[][2] = {{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}};

    for (int i = 0; i < 4; ++i)
    {
        int x2 = dxn[i][0], y2 = dxn[i][1];
        if (visited[x2][y2] && (visited[x][y] - visited[x2][y2] - 1))
            return false;
    }

    return true;
}

int main()
{
    string path;
    cin >> path;

    int x = 101, y = 101;
    visited[x][y] = 1;

    for (int i = 0; i < path.size(); ++i)
    {
        char d = path[i];
        if (d == 'L')
            x--;
        if (d == 'R')
            x++;
        if (d == 'U')
            y++;
        if (d == 'D')
            y--;

        if (visited[x][y])
        {
            cout << "BUG";
            return 0;
        }

        visited[x][y] = i + 2;

        if (!check(x, y))
        {
            // cout << x << " " << y << endl;
            cout << "BUG";
            return 0;
        }
    }

    cout << "OK";
}