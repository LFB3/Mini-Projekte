#include <string>
#include <iostream>
using namespace std;

int main() {
    double solution = 0.0; // double für Nachkommastellen
    double firstNumber = 0.0;
    double secondNumber = 0.0;
    string operation = "";

    while (true) {
        cout << "First Number (or 0 to stop): ";
        cin >> firstNumber;

        if (firstNumber == 0) { // einfacher und korrekt
            break;
        }

        cout << "Second Number: ";
        cin >> secondNumber;

        cout << "Enter operation (+, -, *, /): ";
        cin >> operation;

        if (operation == "+") {
            solution = firstNumber + secondNumber;
            cout << "The result is: " << solution << endl;
        } else if (operation == "-") {
            solution = firstNumber - secondNumber;
            cout << "The result is: " << solution << endl;
        } else if (operation == "*") {
            solution = firstNumber * secondNumber;
            cout << "The result is: " << solution << endl;
        } else if (operation == "/") {
            if (secondNumber == 0) {
                cout << "Error: Division by zero is not allowed!" << endl;
            } else {
                solution = firstNumber / secondNumber;
                cout << "The result is: " << solution << endl;
            }
        } else {
            cout << "Invalid operation!" << endl;
        }
    }

    cout << "Program ended." << endl;
    return 0;
}
