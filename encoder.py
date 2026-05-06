import pandas as pd


def classify_columns(df, onehot_max=10):
    """
    DataFrame sütunlarını növlərinə görə qruplaşdırır.

    Qaydalar:
    - numeric sütunlar -> numeric
    - unique dəyəri 2 olan categorical sütunlar -> binary
    - unique dəyəri 3 ilə onehot_max arası olanlar -> onehot
    - ondan böyük olanlar -> cardinal
    """

    result = {
        "numeric": [],
        "binary": [],
        "onehot": [],
        "cardinal": []
    }

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            result["numeric"].append(col)
        else:
            unique_count = df[col].nunique(dropna=True)

            if unique_count == 2:
                result["binary"].append(col)
            elif 3 <= unique_count <= onehot_max:
                result["onehot"].append(col)
            else:
                result["cardinal"].append(col)

    return result


def suggest_encoding(df, onehot_max=10):
    """
    Hər sütun üçün uyğun encoding tipini təklif edir.
    """

    plan = {}

    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            plan[col] = "numeric"
        else:
            unique_count = df[col].nunique(dropna=True)

            if unique_count == 2:
                plan[col] = "binary encoding"
            elif 3 <= unique_count <= onehot_max:
                plan[col] = "one-hot encoding"
            else:
                plan[col] = "cardinal / other encoding"

    return plan


def rare_encode_column(df, col, threshold=0.05):
    """
    Verilən sütunda az istifadə olunan kateqoriyaları 'Rare' ilə əvəz edir.

    threshold=0.05 -> 5%-dən az görünənlər Rare olacaq
    """

    frequencies = df[col].value_counts(normalize=True)
    rare_values = frequencies[frequencies < threshold].index

    df[col] = df[col].apply(lambda x: "Rare" if x in rare_values else x)
    return df


def rare_encode_dataframe(df, columns, threshold=0.05):
    """
    Birdən çox sütunda rare encoding edir.
    """

    for col in columns:
        df = rare_encode_column(df, col, threshold)

    return df