import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "e_commerce_shopper_behaviour_and_lifestyle.csv"

# загрузка датасета
df = pd.read_csv(file_path)

# вывод базовой информации
print("размер датасета:", df.shape)
print(df.info())
print("первые 5 строк:")
print(df.head())
print("последние 5 строк:")
print(df.tail())

# проверяем пропущенные значения
print("пропущенные значения по колонкам:")
print(df.isnull().sum())

# случайная выборка
df_sample = df.sample(n=10000, random_state=42)

print("основные статистики по выборке:")
print(df_sample.describe())

# визуализация распределений
plt.hist(df_sample["age"], bins=30, color="skyblue", edgecolor="black")
plt.title("распределение возраста покупателей")
plt.xlabel("возраст")
plt.ylabel("количество")
plt.show()

plt.hist(df_sample["income_level"], bins=50, color="lightgreen", edgecolor="black")
plt.title("распределение дохода покупателей")
plt.xlabel("уровень дохода")
plt.ylabel("количество")
plt.show()

plt.boxplot(df_sample["income_level"], vert=False)
plt.title("выбросы дохода покупателей")
plt.show()

# анализ категориальных признаков
for col in df.select_dtypes(include="object").columns:
    print(f"\nраспределение по {col}:")
    print(df_sample[col].value_counts())
    df_sample[col].value_counts().plot(kind="bar", color="orange")
    plt.title(f"распределение по {col}")
    plt.show()

# корреляционная матрица
numeric_cols = df.select_dtypes(include=np.number).columns
corr_matrix = df_sample[numeric_cols].corr()

plt.figure(figsize=(14, 10))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("корреляционная матрица числовых признаков")
plt.show()

# распределение возраста по полу
if "gender" in df_sample.columns and "age" in df_sample.columns:
    plt.figure(figsize=(10,6))
    sns.kdeplot(
        data=df_sample,
        x="age",
        hue="gender",
        fill=True,
        common_norm=False,
        alpha=0.4,
        linewidth=2
    )
    plt.xlabel("возраст")
    plt.ylabel("плотность")
    plt.title("распределение возраста по полу")
    plt.show()

# распределение конверсии по статусу отношений
if "relationship_status" in df_sample.columns and "purchase_conversion_rate" in df_sample.columns:
    plt.figure(figsize=(10,6))
    sns.kdeplot(
        data=df_sample,
        x="purchase_conversion_rate",
        hue="relationship_status",
        fill=True,
        common_norm=False,
        alpha=0.4
    )
    plt.xlabel("конверсия покупок")
    plt.ylabel("плотность")
    plt.title("распределение конверсии покупок по статусу отношений")
    plt.show()

# анализ по дате последней покупки
if "last_purchase_date" in df.columns:
    df["last_purchase_date"] = pd.to_datetime(df["last_purchase_date"])
    purchase_by_gender = df.groupby([df["last_purchase_date"].dt.date, "gender"]).size().unstack()
    plt.figure(figsize=(10,6))
    purchase_by_gender.plot(kind="line", marker="o")
    plt.xlabel("дата")
    plt.ylabel("количество покупок")
    plt.title("покупки по времени и полу")
    plt.tight_layout()
    plt.show()

# вывод гипотез для дальнейшего анализа
print("\nгипотезы для дальнейшего анализа:")
print("1. доход покупателей влияет на частоту покупок")
print("2. тип устройства влияет на средний чек")
print("3. возраст влияет на вероятность покупки определенных категорий товаров")
