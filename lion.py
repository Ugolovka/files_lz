import re
from collections import Counter
import pandas as pd
from docx import Document

# Функция для чтения текста из .docx файла
def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)

# Функция для анализа текста
def analyze_text_from_docx(file_path):
    text = read_docx(file_path).lower()
    
    # Удаление лишних символов и разделение на слова
    words = re.findall(r'\b\w+\b', text)
    
    # Подсчет частоты слов
    word_count = Counter(words)
    total_words = sum(word_count.values())
    
    # Подсчет частоты букв
    letters = re.findall(r'[а-яёa-z]', text)  # Подходит для русского и английского текста
    letter_count = Counter(letters)
    total_letters = sum(letter_count.values())
    
    # Форматирование таблицы по словам
    word_stats = [
        {"Слово": word, "Частота встреч в раз": count, "Частота встреч в %": round((count / total_words) * 100, 2)}
        for word, count in word_count.items()
    ]
    word_df = pd.DataFrame(word_stats)
    
    # Форматирование таблицы по буквам
    letter_stats = [
        {"Буква": letter, "Частота встреч в раз": count, "Частота встреч в %": round((count / total_letters) * 100, 2)}
        for letter, count in letter_count.items()
    ]
    letter_df = pd.DataFrame(letter_stats)
    
    return word_df, letter_df

# Сохранение статистики в файл
def save_statistics_to_file(word_df, letter_df):
    word_df.to_csv("word_statistics.csv", index=False, encoding="utf-8-sig")
    letter_df.to_csv("letter_statistics.csv", index=False, encoding="utf-8-sig")
    print("Статистика успешно сохранена в файлы word_statistics.csv и letter_statistics.csv.")

# Основной код
file_path = "lion.docx"  # Укажите имя вашего .docx файла
word_df, letter_df = analyze_text_from_docx(file_path)

# Печать результатов
print("Статистика по словам:")
print(word_df)
print("\nСтатистика по буквам:")
print(letter_df)

# Сохранение результатов в файл
save_statistics_to_file(word_df, letter_df)