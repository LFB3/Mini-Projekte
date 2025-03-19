#include <iostream>
#include <vector>

void print(const std::vector<int>& list) {
    for (int i : list) {
        std::cout << i << ", ";
    }
}


int main() {
    int userInput = 0;
    std::vector<int> number;
    while (true) {
        std::cout << "\nPut a number in: ";
        std::cin >> userInput;

        if (userInput == -1) {
            break;
        }

        number.push_back(userInput);
        print(number);
    }

    
    return 0;
}