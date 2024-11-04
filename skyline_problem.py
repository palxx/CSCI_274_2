#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        return divideAndConquer(buildings, 0, buildings.size() - 1);
    }

private:
    vector<vector<int>> divideAndConquer(vector<vector<int>>& buildings, int left, int right) {
        // Base case: If there's no building, return an empty skyline
        if (left > right) return {};

        // Base case: If there's only one building, return its skyline
        if (left == right) {
            int x_start = buildings[left][0];
            int x_end = buildings[left][1];
            int height = buildings[left][2];
            return {{x_start, height}, {x_end, 0}};
        }

        // Divide the range into two halves
        int mid = left + (right - left) / 2;
        vector<vector<int>> leftSkyline = divideAndConquer(buildings, left, mid);
        vector<vector<int>> rightSkyline = divideAndConquer(buildings, mid + 1, right);

        // Merge the two skylines
        return mergeSkylines(leftSkyline, rightSkyline);
    }

    vector<vector<int>> mergeSkylines(const vector<vector<int>>& left, const vector<vector<int>>& right) {
        vector<vector<int>> mergedSkyline;
        int leftHeight = 0, rightHeight = 0, currentHeight = 0;
        int i = 0, j = 0;

        while (i < left.size() && j < right.size()) {
            int x;
            // Choose the smallest x-coordinate
            if (left[i][0] < right[j][0]) {
                x = left[i][0];
                leftHeight = left[i][1];
                i++;
            } else if (left[i][0] > right[j][0]) {
                x = right[j][0];
                rightHeight = right[j][1];
                j++;
            } else {
                x = left[i][0];
                leftHeight = left[i][1];
                rightHeight = right[j][1];
                i++;
                j++;
            }

            // The current height at this x-coordinate is the max of leftHeight and rightHeight
            int maxHeight = max(leftHeight, rightHeight);

            // If the height changes from the previous point, add a new point to the skyline
            if (currentHeight != maxHeight) {
                mergedSkyline.push_back({x, maxHeight});
                currentHeight = maxHeight;
            }
        }

        // Add any remaining points from the left skyline
        while (i < left.size()) {
            mergedSkyline.push_back(left[i]);
            i++;
        }

        // Add any remaining points from the right skyline
        while (j < right.size()) {
            mergedSkyline.push_back(right[j]);
            j++;
        }

        return mergedSkyline;
    }
};
