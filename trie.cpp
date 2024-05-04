#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

class TrieNode {
   public:
    TrieNode *children[26] = {NULL};
    bool isEnd = false;
};

class Trie {
   public:
    TrieNode *root;

    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode *iter = root;
        for (auto &c : word) {
            int idx = c - 'a';
            if (!iter->children[idx])
                iter->children[idx] = new TrieNode();
            iter = iter->children[idx];
        }
    }

    bool find(string word) {
        TrieNode *iter = root;
        for (auto &c : word) {
            int idx = c - 'a';
            if (!iter->children[idx])
                return false;
            iter = iter->children[idx];
        }
        return iter->isEnd;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
}