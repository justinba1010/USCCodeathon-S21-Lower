/* Copyright 2021
** Justin Baum
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

vector<int> solution(vector<string> &lock, string &key, int n, int k) {
    // Time: O(k)
    // Here n <= 26
    // Space: O(1)
    if (n == 0) return {0, 0};
    vector<int> counts = vector<int>(n, 0);
    for (int i = 0; i < k; ++i) {
        char curr_key = key[i];
        int index = lock[i].find(curr_key);
        for (int j = 0; j < n; ++j) {
            // Add distances for each column
            counts[j] += min((j - index + n) % n, (index - j + n) % n);
        }
    }
    auto x = min_element(counts.begin(), counts.end());
    return {distance(counts.begin(), x), *x};
}

int main(void) {
    int n, k;
    cin >> n >> k;
    string key;
    cin >> key;
    vector<string> lock;
    for (int i = 0; i < k; ++i) {
        string l;
        cin >> l;
        lock.push_back(l);
    }
    auto s = solution(lock, key, n, k);
    cout << s[0] << " " << s[1] << endl;
    return 0;
}
