/*
    https://leetcode.com/problems/maximum-units-on-a-truck/
    Time: O(n*log(n))
    Space: O(1)
*/

class Solution
{
public:
    static bool compare(vector<int> &box1, vector<int> &box2)
    {
        return box1[1] > box2[1];
    }

    int maximumUnits(vector<vector<int>> &boxTypes, int truckSize)
    {
        sort(boxTypes.begin(), boxTypes.end(), compare);

        int res = 0;
        for (auto box : boxTypes)
        {
            int num = box[0], unit = box[1];
            if (truckSize <= 0)
                break;
            res += min(num, truckSize) * unit;
            truckSize -= num;
        }

        return res;
    }
};

/*
    https://leetcode.com/problems/maximum-units-on-a-truck/
    Time: O(n)
    Space: O(n)
*/

class Solution
{
public:
    int maximumUnits(vector<vector<int>> &boxTypes, int truckSize)
    {

        int count[1001] = {};

        for (auto box : boxTypes)
        {
            count[box[1]] += box[0];
        }

        int res = 0;
        for (int i = 1000; i >= 0; --i)
        {
            if (truckSize <= 0)
                break;
            res += min(count[i], truckSize) * i;
            truckSize -= count[i];
        }

        return res;
    }
};