#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int m = classroom.size();
        int n = classroom[0].size(); 
        
        int start_r = -1, start_c = -1;
        vector<pair<int, int>> litter_positions;
        
        int litter_idx[20][20];
        for(int i = 0; i < 20; ++i) {
            for(int j = 0; j < 20; ++j) {
                litter_idx[i][j] = -1;
            }
        }

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (classroom[r][c] == 'S') {
                    start_r = r;
                    start_c = c;
                } else if (classroom[r][c] == 'L') {
                    litter_idx[r][c] = litter_positions.size();
                    litter_positions.push_back({r, c});
                }
            }
        }

        int total_litter = litter_positions.size();
        int target_mask = (1 << total_litter) - 1;
        int num_masks = 1 << total_litter;
        vector<int> max_energy_state(m * n * num_masks, -1);
        auto get_index = [&](int r, int c, int mask) {
            return (r * n + c) * num_masks + mask;
        };
        struct State {
            int r, c, mask, curr_energy, moves;
        };
        queue<State> q;
        
        int initial_mask = 0;
        if (classroom[start_r][start_c] == 'L') {
            initial_mask |= (1 << litter_idx[start_r][start_c]);
        }

        q.push({start_r, start_c, initial_mask, energy, 0});
        max_energy_state[get_index(start_r, start_c, initial_mask)] = energy;

        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        while (!q.empty()) {
            State curr = q.front();
            q.pop();

            // Goal check
            if (curr.mask == target_mask) {
                return curr.moves;
            }

            if (curr.curr_energy == 0) continue;

            for (int i = 0; i < 4; ++i) {
                int nr = curr.r + dr[i];
                int nc = curr.c + dc[i];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc] != 'X') {
                    int next_energy = curr.curr_energy - 1;
                    int next_mask = curr.mask;

                    if (classroom[nr][nc] == 'L') {
                        next_mask |= (1 << litter_idx[nr][nc]);
                    }
                    
                    if (classroom[nr][nc] == 'R') {
                        next_energy = energy;
                    }

                    int idx = get_index(nr, nc, next_mask);
                    if (next_energy > max_energy_state[idx]) {
                        max_energy_state[idx] = next_energy;
                        q.push({nr, nc, next_mask, next_energy, curr.moves + 1});
                    }
                }
            }
        }

        return -1;
    }
};
