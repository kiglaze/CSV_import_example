import pandas as pd

def main():
    # Import data/sample_sales.csv
    variable_data_types = {
        "Order ID": int,
        "Customer ID": str,
        "Region": str,
        "Product": str,
        "Category": str,
        "Units": int,
        "UnitPrice": float,
        "Discount": float,
        "Total": float
    }
    sales_data_df = pd.read_csv(
        "./data/sample_sales.csv",
        parse_dates=["Date"],
        dtype=variable_data_types
    )

    # Ensure missing "Discount" values are treated as 0.0.
    sales_data_df["Discount"] = sales_data_df["Discount"].fillna(0.0)

    # Clean the "Region" column to have full region names.
    sales_data_df["Region"] = sales_data_df["Region"].replace({"W": "West", "E": "East", "N": "North", "S": "South"})

    # Make all of the Category column proper case.
    sales_data_df["Category"] = sales_data_df["Category"].str.title()

    # Calculate Total for each row.
    sales_data_df["Total"] = sales_data_df["Units"] * sales_data_df["UnitPrice"] - (sales_data_df["Units"] * sales_data_df["Discount"])
    # Round Total to 2 decimal places.
    sales_data_df["Total"] = sales_data_df["Total"].round(2)

    # Output cleaned data to a new CSV file.
    sales_data_df.to_csv("./data/cleaned_sample_sales.csv", index=False)

    # Print the first 5 rows.
    print(sales_data_df.head())

if __name__ == "__main__":
    main()
