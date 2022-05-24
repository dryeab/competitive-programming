#include <iostream>
#include <vector>

using namespace std;

int main(){

    vector<int> x, y;

    int n, p;
    cin >> n;

    for (int i=0; i < 2*n; ++i){
        cin >> p;
        if (i < n)
            x.push_back(p);
        else
            y.push_back(p);
    }

    int ans = 0;
    for (int i=0; i<n; ++i){
        for (int j=i+1; j < n; ++j){
            int d1 = x[i] - x[j], d2 = y[i] - y[j];
            ans = max(ans, d1 * d1 + d2 * d2);
        }
    }

    cout << ans;

}