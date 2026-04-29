from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


DATA_PATH = Path("vgsales.csv")
FIGURES_DIR = Path("figures")
REPORT_TEXT_PATH = Path("eda_summary.txt")

FIGURES_DIR.mkdir(exist_ok=True)
plt.style.use("ggplot")


def save_current_figure(filename):
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()


def print_and_store(lines, text=""):
    print(text)
    lines.append(str(text))


def horizontal_bar(values, labels, color):
    positions = np.arange(len(labels))
    plt.barh(positions, values, color=color)
    plt.yticks(positions, labels)
    plt.gca().invert_yaxis()


summary = []

df = pd.read_csv(DATA_PATH)
df = df.rename(columns={"Global Sales": "Global_Sales"})

print_and_store(summary, "Лабораторная работа 3/ EDA датасета продаж видеоигр")
print_and_store(summary, "-" * 60)
print_and_store(summary, f"Размер датасета: {df.shape[0]} строк, {df.shape[1]} столбцов")
print_and_store(summary, "\nТипы данных:")
print_and_store(summary, df.dtypes)
print_and_store(summary, "\nПервые 5 строк:")
print_and_store(summary, df.head())
print_and_store(summary, "\nПоследние 5 строк:")
print_and_store(summary, df.tail())
print_and_store(summary, "\nПропущенные значения:")
print_and_store(summary, df.isnull().sum())

df["Global_Sales"] = df["Global_Sales"].fillna(
    df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum(axis=1)
)

df["Year"] = df["Year"].astype(int)

numeric_cols = ["Year", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
categorical_cols = ["Platform", "Genre", "Publisher"]

print_and_store(summary, "\nОсновные статистики:")
print_and_store(summary, df[numeric_cols].describe())

print_and_store(summary, "\nУникальные значения категориальных признаков:")
for col in categorical_cols:
    print_and_store(summary, f"{col}: {df[col].nunique()} уникальных значений")
    print_and_store(summary, df[col].value_counts().head(10))

# 1. Выпуски игр по годам.
games_by_year = df.groupby("Year").size()
plt.figure(figsize=(12, 6))
games_by_year.plot(kind="line", marker="o", color="steelblue")
plt.title("Количество выпущенных игр по годам")
plt.xlabel("Год")
plt.ylabel("Количество игр")
save_current_figure("01_games_by_year.png")

# 2. Топ платформ по глобальным продажам.
platform_sales = df.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
horizontal_bar(platform_sales.values, platform_sales.index, "cornflowerblue")
plt.title("Топ-10 платформ по глобальным продажам")
plt.xlabel("Глобальные продажи, млн копий")
plt.ylabel("Платформа")
save_current_figure("02_top_platforms.png")

# 3. Продажи по жанрам.
genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
horizontal_bar(genre_sales.values, genre_sales.index, "mediumseagreen")
plt.title("Глобальные продажи по жанрам")
plt.xlabel("Глобальные продажи, млн копий")
plt.ylabel("Жанр")
save_current_figure("03_genre_sales.png")

# 4. Распределение глобальных продаж.
plt.figure(figsize=(10, 6))
plt.hist(df["Global_Sales"], bins=60, color="orange", edgecolor="black")
plt.title("Распределение глобальных продаж игр")
plt.xlabel("Глобальные продажи, млн копий")
plt.ylabel("Количество игр")
save_current_figure("04_global_sales_distribution.png")

# 5. Boxplot продаж для поиска выбросов.
plt.figure(figsize=(10, 4))
plt.boxplot(df["Global_Sales"], vert=False, patch_artist=True, boxprops={"facecolor": "lightcoral"})
plt.title("Выбросы в глобальных продажах")
plt.xlabel("Глобальные продажи, млн копий")
save_current_figure("05_global_sales_boxplot.png")

# 6. Региональные продажи по жанрам.
regional_by_genre = df.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()
regional_by_genre = regional_by_genre.loc[genre_sales.index]
regional_by_genre.plot(kind="bar", stacked=True, figsize=(12, 7))
plt.title("Региональная структура продаж по жанрам")
plt.xlabel("Жанр")
plt.ylabel("Продажи, млн копий")
plt.xticks(rotation=45, ha="right")
save_current_figure("06_regional_sales_by_genre.png")

# 7. Корреляционная матрица числовых признаков.
corr_matrix = df[numeric_cols].corr()
plt.figure(figsize=(9, 7))
plt.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(label="Корреляция")
plt.xticks(np.arange(len(numeric_cols)), numeric_cols, rotation=45, ha="right")
plt.yticks(np.arange(len(numeric_cols)), numeric_cols)
for i in range(len(numeric_cols)):
    for j in range(len(numeric_cols)):
        plt.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}", ha="center", va="center", color="black")
plt.title("Корреляционная матрица числовых признаков")
save_current_figure("07_correlation_matrix.png")

# 8. Динамика продаж по основным регионам.
sales_by_year = df.groupby("Year")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum()
plt.figure(figsize=(12, 6))
for col in sales_by_year.columns:
    plt.plot(sales_by_year.index, sales_by_year[col], label=col)
plt.title("Динамика региональных продаж по годам")
plt.xlabel("Год")
plt.ylabel("Продажи, млн копий")
plt.legend()
save_current_figure("08_regional_sales_by_year.png")

# 9. Топ издателей.
publisher_sales = df.groupby("Publisher")["Global_Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
horizontal_bar(publisher_sales.values, publisher_sales.index, "mediumpurple")
plt.title("Топ-10 издателей по глобальным продажам")
plt.xlabel("Глобальные продажи, млн копий")
plt.ylabel("Издатель")
save_current_figure("09_top_publishers.png")

# Выбросы по IQR.
q1 = df["Global_Sales"].quantile(0.25)
q3 = df["Global_Sales"].quantile(0.75)
iqr = q3 - q1
upper_bound = q3 + 1.5 * iqr
outliers = df[df["Global_Sales"] > upper_bound]

print_and_store(summary, "\nАнализ выбросов по Global_Sales:")
print_and_store(summary, f"Q1 = {q1:.2f}, Q3 = {q3:.2f}, IQR = {iqr:.2f}")
print_and_store(summary, f"Граница выбросов: больше {upper_bound:.2f} млн копий")
print_and_store(summary, f"Количество выбросов: {len(outliers)}")
print_and_store(summary, "Топ-5 игр по глобальным продажам:")
print_and_store(summary, df.sort_values("Global_Sales", ascending=False).head(5)[["Name", "Platform", "Year", "Genre", "Global_Sales"]])

print_and_store(summary, "\nНаблюдения:")
print_and_store(summary, f"Самый продаваемый жанр: {genre_sales.index[0]}")
print_and_store(summary, f"Лидирующая платформа по продажам: {platform_sales.index[0]}")
print_and_store(summary, f"Лидирующий издатель по продажам: {publisher_sales.index[0]}")
print_and_store(summary, "Продажи в Северной Америке сильнее всего связаны с глобальными продажами.")

print_and_store(summary, "\nГипотезы для дальнейшей проверки:")
print_and_store(summary, "1. Жанр игры влияет на глобальные продажи.")
print_and_store(summary, "2. Платформа влияет на коммерческий успех игры.")
print_and_store(summary, "3. Региональные предпочтения отличаются: продажи в Японии распределены по жанрам иначе, чем в Северной Америке и Европе.")

REPORT_TEXT_PATH.write_text("\n".join(map(str, summary)), encoding="utf-8")
print("\nГрафики сохранены в папку figures")
print(f"Сводка сохранена в файл {REPORT_TEXT_PATH}")

input("Нажмите Enter для завершения...")