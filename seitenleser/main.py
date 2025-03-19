from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import keyboard

# 🔹 Öffne Chrome sichtbar
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# 🔹 Webseite laden
driver.get("https://oxelf.github.io/typehero/")
time.sleep(1)  # Warte, bis die Seite geladen ist

# 🔹 "content"-Element finden
content = driver.find_element(By.CLASS_NAME, "content")

# 🔹 Alle Elemente in "content" finden
elements = content.find_elements(By.XPATH, "./*")

# 🔹 Wörter und Leerzeichen speichern
extracted_text = []

for element in elements:
    if "spacer" in element.get_attribute("class"):
        extracted_text.append(" ")  # Spacer als Leerzeichen speichern
    elif "word" in element.get_attribute("class"):
        letters = element.find_elements(By.CLASS_NAME, "letter")
        word_text = "".join([letter.text for letter in letters])
        extracted_text.append(word_text)

# 🔹 Finalen Text zusammenfügen
final_text = "".join(extracted_text)
print("Extrahierter Text:", final_text)

# 🔹 Funktion für Tastenkombination
def write_text():
    for i in range(len(final_text)):
        buchstabe = final_text[i]
        pyautogui.write(buchstabe)  # Langsam schreiben, um Fehler zu vermeiden

# 🔹 Tastenkombination setzen (Strg + Alt + R)
keyboard.add_hotkey("ctrl+alt+c", write_text)
print("Drücke Strg + Alt + C, um den Text einzufügen.")

# 🔹 Warte auf Tastendrücke, Browser bleibt offen
keyboard.wait()
