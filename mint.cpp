#include <bits/stdc++.h>
#define ll long long
using namespace std;

template<int P>
int norm(int x) {
    if (x < 0) {
        x += P;
    }
    if (x >= P) {
        x -= P;
    }
    return x;
}

template<class T>
T power(T a, long long b) {
    T res = 1;
    for (; b; b /= 2, a *= a) {
        if (b % 2) {
            res *= a;
        }
    }
    return res;
}

template<int P>
struct Mint {
    int x;
    Mint(int x = 0) : x(norm<P>(x)) {}
    Mint(long long x) : x(norm<P>(x % P)) {}

    int val() const {
        return x;
    }
    Mint operator-() const {
        return Mint(norm<P>(P - x));
    }
    Mint inv() const {
        assert(x != 0);
        return power(*this, P - 2);
    }
    Mint &operator*=(const Mint &rhs) {
        x = (long long)(x) * rhs.x % P;
        return *this;
    }
    Mint &operator+=(const Mint &rhs) {
        x = norm<P>(x + rhs.x);
        return *this;
    }
    Mint &operator-=(const Mint &rhs) {
        x = norm<P>(x - rhs.x);
        return *this;
    }
    Mint &operator/=(const Mint &rhs) {
        return *this *= rhs.inv();
    }
    friend Mint operator*(const Mint &lhs, const Mint &rhs) {
        Mint res = lhs;
        res *= rhs;
        return res;
    }
    friend Mint operator+(const Mint &lhs, const Mint &rhs) {
        Mint res = lhs;
        res += rhs;
        return res;
    }
    friend Mint operator-(const Mint &lhs, const Mint &rhs) {
        Mint res = lhs;
        res -= rhs;
        return res;
    }
    friend Mint operator/(const Mint &lhs, const Mint &rhs) {
        Mint res = lhs;
        res /= rhs;
        return res;
    }
    friend istream &operator>>(istream &is, Mint &a) {
        long long v;
        is >> v;
        a = Mint(v);
        return is;
    }
    friend ostream &operator<<(ostream &os, const Mint &a) {
        return os << a.val();
    }
};

const int MOD = 998244353;
using mint = Mint<MOD>;

void solve(){
  
}

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t = 1;
    cin >> t;
    
    while (t--){
      solve();
    }
    
    return 0;
}
