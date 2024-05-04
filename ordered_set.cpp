#include <bits/stdc++.h>

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;

typedef tree<
    int,  // data type
    null_type,
    less<int>, // less_equal for multiset
    rb_tree_tag,
    tree_order_statistics_node_update>
    ordered_set;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    /*

    methods
        - order_of_key(val) -> returns the number of elements  strictly less than val in the set
        - find_by_order(idx) -> returns the pointer to element at index "idx". Make sure you * to get the element.

    */

    ordered_set t;

    t.insert(0);
    t.insert(1);
    t.insert(1);
    t.insert(5);
    t.insert(10);


    cout << *t.find_by_order(2) << endl;
    cout << t.order_of_key(2) << endl;
}