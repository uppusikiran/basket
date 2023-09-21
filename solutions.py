import pandas as pd

def load_fruit_basket(solutions):
    try:
        df = pd.read_csv(solutions)
        return df
    except FileNotFoundError:
        print(f"File '{solutions}' not found.")
        return None

def main(solutions):
    basket = load_fruit_basket(solutions)

    if basket is not None:
        total_fruits = basket['Fruit'].count()
        total_types = basket['Fruit'].nunique()
        fruits_count = basket['Fruit'].value_counts().sort_values(ascending=False)
        
        print(f"Total number of fruit: {total_fruits}")
        print(f"Types of fruit: {total_types}")
        print("The number of each type of fruit in descending order:")
        for fruit, count in fruits_count.items():
            print(f"{fruit}: {count}")
        
        print("The characteristics (size, color, shape, etc.) of each fruit by type:")
        fruit_characteristics = basket.groupby('Fruit')['Characteristics'].apply(lambda x: ', '.join(x.unique()))
        for fruit, characteristics in fruit_characteristics.items():
            print(f"{fruits_count[fruit]} {fruit}s: {characteristics}")

        old_fruits = basket[basket['Days in Basket'] > 3]
        if not old_fruits.empty:
            print("\nHave any fruit been in the basket for over 3 days")
            for fruit, count in old_fruits['Fruit'].value_counts().items():
                print(f"{count} {fruit}s are over 3 days old")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python solution.py <solutions>")
    else:
        solutions = sys.argv[1]
        main(solutions)
