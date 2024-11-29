import pandas as pd
import matplotlib.pyplot as plt

#чтение данных, сохранения в CSV и построения гистограммы
def process_titanic_data(parquet_file, output_csv):
    #чтение данных из parquet файла
    data = pd.read_parquet(parquet_file)

    #сохранение данных в формат CSV
    data.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"Данные успешно сохранены в файл: {output_csv}")

    #проверка структуры данных
    print("Первые строки данных:")
    print(data.head())

    #построение гистограммы
    plot_survival_by_class(data)

#построение гистограммы
def plot_survival_by_class(data):
    #группировка данных по классу билета и статусу выживаемости для дальнейшего графика
    survival_data = data.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)

    #нормализация данных для отображения в процентах
    survival_percent = survival_data.div(survival_data.sum(axis=1), axis=0) * 100

    #построение графика
    survival_percent.plot(kind='bar', stacked=True, color=["skyblue", "lightcoral"], figsize=(10, 6))
    plt.title("Выживаемость пассажиров Титаника", fontsize=14)
    plt.xlabel("Класс билета", fontsize=12)
    plt.ylabel("Процент пассажиров", fontsize=12)
    plt.legend(["Выжил", "Не выжил"], loc="upper left", fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(ticks=range(len(survival_percent.index)), labels=["Первый класс", "Второй класс", "Третий класс"], rotation=0)
    plt.show()

parquet_file = "titanic.parquet"
output_csv = "titanic.csv"

process_titanic_data(parquet_file, output_csv)



"""import pandas as pd   вариант без применения функций крч легче
import matplotlib.pyplot as plt

data = pd.read_parquet("titanic.parquet") #чтение данных из файла .parquet

data.to_csv("titanic.csv", index=False)  #сохранение данных в формате CSV
print("Данные сохранены в файл titanic.csv")

#группировка данных по классу билета и статусу выживаемости
survival_data = data.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)

#преобразование в проценты
survival_percent = survival_data.div(survival_data.sum(axis=1), axis=0) * 100

#построение гистограммы
survival_percent.plot(
    kind='bar',
    stacked=True,
    color=["skyblue", "lightcoral"],
    figsize=(8, 5)  рандомные параметры вкусовщина
)

#настройка графика
plt.title("Выживаемость пассажиров Титаника")
plt.xlabel("Класс билета")
plt.ylabel("Процент пассажиров")
plt.xticks(ticks=range(len(survival_percent.index)), labels=["Первый", "Второй", "Третий"], rotation=0)
plt.legend(["Выжил", "Не выжил"], loc="upper left")
plt.tight_layout()

# Показать график
plt.show()"""
