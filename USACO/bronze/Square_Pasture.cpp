#include <iostream>
#include <algorithm>

using namespace std;

struct Rect
{
    int x1, x2, y1, y2;
};

int main()
{
    Rect a, b;

    cin >> a.x1 >> a.y1 >> a.x2 >> a.y2;
    cin >> b.x1 >> b.y1 >> b.x2 >> b.y2;

    int Dy = max(b.y2, a.y2) - min(b.y1, a.y1);
    int Dx = max(b.x2, a.x2) - min(b.x1, a.x1);

    int M = max(Dx, Dy);

    cout << M * M;

    return 0;
}