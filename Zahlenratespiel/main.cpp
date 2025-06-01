#include <iostream>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <algorithm> // für tolower

void printhighscore(int easy, int medium, int hard) {
    // Highscores anzeigen
    std::cout << "\n=== Highscores ===\n";
    if (easy != 0) {std::cout << "Easy: " << easy << " tries\n";}
    if (medium != 0) {std::cout << "Medium: " << medium << " tries\n";}
    if (hard != 0) {std::cout << "Hard: " << hard << " tries\n";}
    
}

int getSafeInt(const std::string& prompt) {
    int value;
    while (true) {
        std::cout << prompt;
        if (std::cin >> value) {
            return value; // Wenn die Eingabe erfolgreich war, geben wir die Zahl zurück.
        } else {
            std::cout << "Invalid input! Please enter a number.\n";
            std::cin.clear(); // Setzt den Fehlerzustand von cin zurück.
            std::cin.ignore(10000, '\n'); // Überspringt die fehlerhafte Eingabe im Puffer.
        }
    }
}

int getSafeString(const std::string& prompt) {
    std::string value;
    while (true) {
        std::cout << prompt;
        if (std::cin >> value) {
            return value; // Wenn die Eingabe erfolgreich war, geben wir die Zahl zurück.
        } else {
            std::cout << "Invalid input! Please enter a Word.\n";
            std::cin.clear(); // Setzt den Fehlerzustand von cin zurück.
            std::cin.ignore(10000, '\n'); // Überspringt die fehlerhafte Eingabe im Puffer.
        }
    }
}

int main() {
    // Konstanten für die Bereiche
    const int EASY_MAX = 50;
    const int MEDIUM_MAX = 100;
    const int HARD_MAX = 200;

    // Zufallsgenerator initialisieren
    srand(time(0));

    std::cout << "Welcome to the number guessing game!\n";
    std::cout << "I'm thinking of a number in a range you choose.\n";
    std::cout << "Try to guess it!\n";

    // Highscores
    int highscoreeasy = 0, highscoremedium = 0, highscorehard = 0;
    std::string playagain;

    do {
        std::string difficulty;
        int randomNumber = 0;
        int maxNumber = 0;

        // Schwierigkeit wählen
        while (true) {
            difficulty = getSafeString("Choose difficulty ([1] easy {1-50}, [2] medium {1-100}, [3] hard {1-200}): ");
            std::transform(difficulty.begin(), difficulty.end(), difficulty.begin(), ::tolower); // klein schreiben

            if (difficulty == "easy" or difficulty == "1") {
                maxNumber = EASY_MAX;
                break;
            } else if (difficulty == "medium" or difficulty == "2") {
                maxNumber = MEDIUM_MAX;
                break;
            } else if (difficulty == "hard" or difficulty == "3") {
                maxNumber = HARD_MAX;
                break;
            } else {
                std::cout << "Invalid input! Please enter easy, medium or hard.\n";
            }
        }

        // Zufallszahl
        randomNumber = rand() % maxNumber + 1;

        // Spiel starten
        int tries = 0, guess = 0;

        while (true) {
            tries++;
            oss << "Guess the number between 1 and " << maxNumber << ": ";
            int guess = getSafeInt(oss.str());

            if (guess == randomNumber) {
                std::cout << "Congratulations! You guessed the number in " << tries << " tries!\n";

                // Highscore prüfen
                if (difficulty == "easy" && (highscoreeasy == 0 || tries < highscoreeasy)) {
                    highscoreeasy = tries;
                    std::cout << "New highscore for easy!\n";
                } else if (difficulty == "medium" && (highscoremedium == 0 || tries < highscoremedium)) {
                    highscoremedium = tries;
                    std::cout << "New highscore for medium!\n";
                } else if (difficulty == "hard" && (highscorehard == 0 || tries < highscorehard)) {
                    highscorehard = tries;
                    std::cout << "New highscore for hard!\n";
                }

                break;
            } else if (guess < randomNumber) {
                std::cout << "Too small!\n";
            } else {
                std::cout << "Too big!\n";
            }
        }

        // Noch ein Spiel?
        std::cout << "Play again? (y/n): ";
        std::cin >> playagain;
        std::transform(playagain.begin(), playagain.end(), playagain.begin(), ::tolower); // Eingabe klein

        while (playagain != "y" && playagain != "n") {
            std::cout << "Invalid input! Please enter y or n: ";
            std::cin >> playagain;
            std::transform(playagain.begin(), playagain.end(), playagain.begin(), ::tolower);
        }

    } while (playagain == "y");

    printhighscore(highscoreeasy, highscoremedium, highscorehard);
    std::cout << "Thank you for playing!\n";
    return 0;
}
