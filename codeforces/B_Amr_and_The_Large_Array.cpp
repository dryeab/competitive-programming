#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int M = 10e6 + 5;

int start[M] = {}, last[M], freq[M] = {};

int main()
{

    int n, mf = 0, val, l = 1, r = n;
    cin >> n;

    for (int i = 1; i <= n; ++i)
    {
        cin >> val;

        if (!start[val])
            start[val] = i;

        last[val] = i;

        freq[val]++;

        mf = max(mf, freq[val]);

        if (freq[i] >= mf)
        {
            if (r - l > last[i] - start[i])
            {
                l = start[i];
                r = last[i];
            }
        }
    }

    cout << l << " " << r << endl;
}

/*

const int M = 10e6 + 5;

int tFreq[M] = {}, sFreq[M] = {};

int main()
{
    int n, mf = 0;
    cin >> n;

    vector<int> a(n);
    for (int &x : a)
    {
        cin >> x;
        tFreq[x]++;
        mf = max(mf, tFreq[x]);
    }

    int l = 0, r = 0, al = 0, ar = n - 1;
    while (r < n)
    {
        sFreq[a[r]]++;
        while (sFreq[a[r]] >= mf)
        {
            if (ar - al > r - l)
            {
                ar = r;
                al = l;
            }
            sFreq[a[l]]--;
            l++;
        }

        r++;
    }

    cout << al + 1 << " " << ar + 1 << endl;
}
*/