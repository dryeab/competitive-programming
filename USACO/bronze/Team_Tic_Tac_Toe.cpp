#include <iostream>
#include <unordered_set>

using namespace std;

// char board[3][3];
int row[3][26], col[3][26], diag[2][26];

int main()
{
    char c;
    int index;

    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            cin >> c;
            index = c - 'A';

            row[i][index]++;
            col[j][index]++;

            if (i + j == 2)
                diag[1][index]++;
            if (i - j == 0)
                diag[0][index]++;
        }
    }

    int one = 0, two = 0;
    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 26; ++j)
        {
            if (row[i][j] == 3)
                one++;
            if (col[i][j] == 3)
                one++;
            if (row[i][j] == 2)
                two++;
            if (col[i][j] == 2)
                two++;

            if (i != 2)
            {
                if (diag[i][j] == 3)
                    one++;
                if (diag[i][j] == 2)
                    two++;
            }
        }
    }

    cout << one << endl << two;
}