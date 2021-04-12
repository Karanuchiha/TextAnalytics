import numpy as np
import pandas as pd
import sys
import random
from features_extractor import extract_features_from_text

def create_dataframe(preprocessed_dataset_name):
    print('Creating the final csv for:', preprocessed_dataset_name)
    df = pd.read_csv("preprocessed_datasets/" + preprocessed_dataset_name, comment="#")

    indices = [i for i in range(len(df))]
    indices_to_use = []

    random.seed(0)
    for i in range(1600):
        random_index = random.randrange(len(indices))
        indices_to_use.append(indices[random_index])
        del indices[random_index]

    final_dataset_list = []
    count = 1
    for i in indices_to_use:
        print('Processing review: ' + str(count) + '/1600')
        count += 1
        ID = df['ID'][i]
        rating = df['Rating'][i]
        review = df['Review'][i]
        product = df['Product'][i]
        price = df['Price'][i]

        try:
            features = extract_features_from_text(review)
        except:
            continue
        l2sca_features = [features['l2sca'][i] for i in features['l2sca']]
        lca_features = [features['lca'][i] for i in features['lca']]

        review_features_list = [ID, rating, review, product, price, features['ttr'], features['words_per_t_unit'],
            features['words_per_clauses'],features['flesch_reading_ease']]
        review_features_list.extend(l2sca_features)
        review_features_list.extend(lca_features)

        final_dataset_list.append(review_features_list)
    
    feature_names = ['ID', 'rating', 'review', 'product', 'price', 'ttr', 'words_per_t_unit',
                        'words_per_clauses', 'flesch_reading_ease']

    l2sca_feature_names = ['l2sca_' + i for i in features['l2sca']]
    lca_features_names = ['lca_' + i for i in features['lca']]

    feature_names.extend(l2sca_feature_names)
    feature_names.extend(lca_features_names)

    final_dataset_list = final_dataset_list[:1500]
    final_df = pd.DataFrame(data=final_dataset_list, index=None, columns=feature_names)
    final_df.to_csv('final_datasets/' + preprocessed_dataset_name,index=False)
    print('Final csv for:', preprocessed_dataset_name, 'created')


create_dataframe('result_appliances.csv')
create_dataframe('result_fashion.csv')
create_dataframe('result_luxury_beauty.csv')
create_dataframe('result_prime.csv')
create_dataframe('result_software.csv')
create_dataframe('result_music.csv')
