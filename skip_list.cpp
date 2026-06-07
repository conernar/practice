#include <iostream>
#include <vector>
#include <cstdio>
// 1.Node defination
struct Node {
  int value;
  std::vector<Node*> forward;
  Node(int val, int level) {
    value = val;
    // allocate level + 1 points , default nullptr
    forward.assgin(level + 1, nullptr);
  }
};

// 2.define skip list
class SkipList {
private:
  int max_level;
  int current_level;
  Node* head;

  int randomlevel() {
    int lvl = 0;
    while ((std::rand() % 2 == 1) && lvl < max_level) {
      lvl++;

    }
    return lvl;
  }



public:
  SkipList(int max_lvl) {
    max_level = max_lvl;
    current_level = 0;
    head = new Node(-1, max_level);
  }
  // 3.Search logic
  bool search(int target) {
    Node* curr = head;
    for (int i = current_level; i >= 0; i--) {
      while (curr->forward[i] != nullptr && curr->forward[i]->value < target) {
        curr = curr->forward[i];
      }
    }
    curr = curr->forward[0];
    if (curr != nullptr && curr->value == target) {
      return true;
    }
    return false;
  }

  // 4. Inseart logic
  void insert(int value) {
    
  }

}

int main() {
  return 0;
}
