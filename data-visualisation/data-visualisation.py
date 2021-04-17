import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

categories = ["appliances", "fashion", "luxury_beauty", "music", "prime", "software"]
# categories = ["appliances"]

for category in categories:
    filepath = "./../pre-processed-datasets/" + category + ".csv"

    dfOrig = pd.read_csv(filepath, comment="#")
    df = dfOrig.groupby(['ID']).mean() # Group by Product ID

    print("> Overview of the dataset for category " + category + ":")
    print(df.head())

    print("\n> Distribution of products (per price):")

    print("Min price", df["Price"].min())
    print("Avg price", df["Price"].mean())

    print("Quantile 25 price", df["Price"].quantile(.25))
    print("Median price", df["Price"].median())
    print("Quantile 75 price", df["Price"].quantile(.75))

    print("Max price", df["Price"].max())

    countByPrice = dfOrig.groupby(['Price']).agg(['nunique']) # Group by Price & get unique number of products (ID) & reviews (Review) at this Price

    X = countByPrice.index.values.tolist() # Prices
    Y1 = countByPrice.iloc[:, 1].tolist() # Unique IDs (products) per Price
    Y2 = countByPrice.iloc[:, 3].tolist() # Unique Reviews per Price

    print("Total number of products: ", sum(Y1))
    print("Total number of reviews: ", sum(Y2))

    print("\n> Generating chart...\n\n")

    plt.bar(X, Y1, width=2, label="# Products per price", color="blue", zorder=2)
    plt.bar(X, Y2, width=2, label="# Reviews per price", color="orange", zorder=1)

    plt.yscale('log')
    plt.title("Number of reviews depending on the price — " + category + " category")
    plt.legend()
    plt.xlabel("Price")
    plt.ylabel("Number of reviews (logarithmic scale)")
    
    # Preventing "extreme" outliers in 'fashion' category
    if category == "fashion":
        plt.xlim([0, df["Price"].quantile(.999)])

    plt.show()
    # plt.savefig("./data-visualisation-" + category + ".png")
    plt.clf()


# Exploration, only for test purposes (mean rating per product = f(# of ratings per product))
# for category in categories:
#     filepath = "./../pre-processed-datasets/" + category + ".csv"
#     dfOrig = pd.read_csv(filepath, comment="#")

#     products = dfOrig.groupby(['ID']).agg(['mean', 'count']).sort_values(('Rating', 'count'))
#     print(products.head())

#     X = products[('Rating', 'count')].tolist()
#     Y = products[('Rating', 'mean')].tolist()

#     plt.plot(X, Y, marker='+', label='Category ' + category)

#     plt.title("mean rating = f(# of ratings) for each product")
#     plt.legend()
#     plt.xlabel("Number of ratings")
#     plt.ylabel("Mean rating")

# plt.show()