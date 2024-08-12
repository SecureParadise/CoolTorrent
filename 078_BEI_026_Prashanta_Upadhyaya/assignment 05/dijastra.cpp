// This is simple dijastra problem to find shortest path in a 3*3 matrix from (0,0) to (2,2) 
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>

using namespace std;

// Function to find the shortest path in a grid using Dijkstra's algorithm
int shortestPathInMatrix(const vector<vector<int>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();

    // Min-heap to store (distance, row, col)
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> minHeap;

    // Initialize distance array with infinity
    vector<vector<int>> dist(rows, vector<int>(cols, INT_MAX));
    dist[0][0] = matrix[0][0];
    minHeap.push(make_tuple(dist[0][0], 0, 0));

    // Directions for moving in the grid
    vector<int> directions = {-1, 0, 1, 0, 0, -1, 0, 1};  // Up, Down, Left, Right

    while (!minHeap.empty()) {
        tuple<int, int, int> current = minHeap.top();
        minHeap.pop();

        int currentDist = std::get<0>(current);
        int row = std::get<1>(current);
        int col = std::get<2>(current);

        // Check if we have reached the destination
        if (row == rows - 1 && col == cols - 1) {
            return currentDist;
        }

        // Explore the neighbors
        for (int i = 0; i < 4; ++i) {
            int newRow = row + directions[i * 2];
            int newCol = col + directions[i * 2 + 1];

            // Check if the new position is within bounds
            if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
                int newDist = currentDist + matrix[newRow][newCol];
                if (newDist < dist[newRow][newCol]) {
                    dist[newRow][newCol] = newDist;
                    minHeap.push(make_tuple(newDist, newRow, newCol));
                }
            }
        }
    }

    // If there is no path, return -1 or some indication of failure
    return -1;
}

int main() {
    vector<vector<int>> matrix = {
        {1, 2, 99},
        {4, 3, 1},
        {7, 6, 1}
    };

    int result = shortestPathInMatrix(matrix);
    if (result != -1) {
        cout << "The shortest path distance is: " << result << endl;
    } else {
        cout << "No path found." << endl;
    }

    return 0;
}
