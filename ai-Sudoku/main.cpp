#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <chrono>

const int SIZE = 9;
const int EMPTY = 0;

// Hilfsfunktion: Überprüft, ob eine Zahl in der Zeile gültig ist
bool isInRow(const std::vector<std::vector<int>>& board, int row, int num) {
    for (int col = 0; col < SIZE; col++) {
        if (board[row][col] == num) {
            return true;
        }
    }
    return false;
}

// Hilfsfunktion: Überprüft, ob eine Zahl in der Spalte gültig ist
bool isInCol(const std::vector<std::vector<int>>& board, int col, int num) {
    for (int row = 0; row < SIZE; row++) {
        if (board[row][col] == num) {
            return true;
        }
    }
    return false;
}

// Hilfsfunktion: Überprüft, ob eine Zahl im 3x3-Block gültig ist
bool isInBox(const std::vector<std::vector<int>>& board, int startRow, int startCol, int num) {
    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
            if (board[startRow + row][startCol + col] == num) {
                return true;
            }
        }
    }
    return false;
}

// Prüft, ob eine Zahl an die Position (row, col) gesetzt werden darf
bool isValidMove(const std::vector<std::vector<int>>& board, int row, int col, int num) {
    return !isInRow(board, row, num) &&
           !isInCol(board, col, num) &&
           !isInBox(board, row - row % 3, col - col % 3, num);
}

// Backtracking-Algorithmus zum Erstellen eines vollständigen Sudoku-Bretts
bool fillBoard(std::vector<std::vector<int>>& board, int row, int col) {
    if (row == SIZE - 1 && col == SIZE) {
        return true;
    }
    if (col == SIZE) {
        row++;
        col = 0;
    }
    if (board[row][col] != EMPTY) {
        return fillBoard(board, row, col + 1);
    }

    for (int num = 1; num <= SIZE; num++) {
        if (isValidMove(board, row, col, num)) {
            board[row][col] = num;
            if (fillBoard(board, row, col + 1)) {
                return true;
            }
            board[row][col] = EMPTY; // Rückgängigmachen (Backtracking)
        }
    }
    return false;
}

// Erstellt ein vollständiges Sudoku-Brett
void generateFullSudoku(std::vector<std::vector<int>>& board) {
    std::srand(std::time(0));

    // Startet mit einem leeren Brett
    board.assign(SIZE, std::vector<int>(SIZE, EMPTY));

    // Füllt das Brett mit Backtracking
    fillBoard(board, 0, 0);
}

// Löscht zufällige Zahlen, um ein Rätsel zu erstellen
void removeNumbers(std::vector<std::vector<int>>& board, int difficulty) {
    int cellsToRemove = difficulty;
    while (cellsToRemove > 0) {
        int row = std::rand() % SIZE;
        int col = std::rand() % SIZE;

        if (board[row][col] != EMPTY) {
            board[row][col] = EMPTY;
            cellsToRemove--;
        }
    }
}

// Zeigt das Sudoku-Brett in der Konsole an
void printBoard(const std::vector<std::vector<int>>& board) {
    for (int row = 0; row < SIZE; row++) {
        if (row % 3 == 0 && row != 0) {
            std::cout << "---------------------\n";
        }
        for (int col = 0; col < SIZE; col++) {
            if (col % 3 == 0 && col != 0) {
                std::cout << "| ";
            }
            if (board[row][col] == EMPTY) {
                std::cout << ". ";
            } else {
                std::cout << board[row][col] << " ";
            }
        }
        std::cout << "\n";
    }
}

// Hauptfunktion
int main() {
    std::vector<std::vector<int>> board;
    int difficulty;

    std::cout << "Choose difficulty (20 = Easy, 40 = Medium, 55 = Hard): ";
    std::cin >> difficulty;
    auto start = std::chrono::high_resolution_clock::now();
    generateFullSudoku(board);
    removeNumbers(board, difficulty);
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "\nGenerated Sudoku:\n";
    printBoard(board);
    std::chrono::duration<double> duration = end - start;
    std::cout << "Time taken: " << duration.count() << " seconds" << std::endl;
    return 0;
}
