/**
 * https://leetcode.com/problems/my-calendar-i/
 * Time: O(NlogN)
 * Space: O(N)
 */

class MyCalendar {
public:
    map<int, int> events;

    MyCalendar() {
        events.clear();
    }

    bool book(int start, int end) {

        end--;

        if (events.count(start))
            return false;

        auto i = events.upper_bound(start);

        if (i != events.begin() && prev(i)->second >= start)
            return false;

        if (i != events.end() && i->first <= end)
            return false;

        events[start] = end;

        return true;
    }
};