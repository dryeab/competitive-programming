#include <iostream>

using namespace std;

int line[100];
int cp[100];

int main()
{

    int N;
    cin >> N;

    for (int i = 0; i < N; ++i)
        cin >> line[i];
    for (int i = 0; i < N; ++i)
        cin >> cp[i];

    for (int i = 1; i <= N; ++i)
    {
        int j = i, k = 3;
        while (k--)
        {
            j = line[j];
        }
        cout << cp[j] << endl;
    }

    return 0;
}