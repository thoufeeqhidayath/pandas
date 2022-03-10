
def _calculate_percentage(df_a):
    print("columns",df_a.columns)
    print("sele",df_a[df_a.columns]>1) #check values in columns are greateer

    sum_of_rows = df_a[df_a.columns].sum(axis=1)
    print("________sum________________")
    print(sum_of_rows)
    print("________________________")
    print("________divide________________")
    df_a[df_a.columns] = df_a[df_a.columns].div(sum_of_rows, axis=0)
    print("________________________")


    df_a[df_a.columns] = df_a[df_a.columns].multiply(100)
    return df_a



data = {
    "old_a":{"a":1,"b":3,"c":8},
    "old_b": {"a": 4, "b": 9, "c": 6},
    "old_c": {"a": 6, "b": 2, "c": 2}


}
import pandas as pd

df = pd.DataFrame(data)
_calculate_percentage(df)
print(df.head(5))