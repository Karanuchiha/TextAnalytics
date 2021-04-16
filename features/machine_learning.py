from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def features_importances(dataset_name):
    print('Applying machine learning to csv:', dataset_name)
    df = pd.read_csv("final_datasets/" + dataset_name, comment="#")
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df = df.dropna().reset_index(drop=True)
    df = df.sort_values('price').reset_index(drop=True)

    columns = list(df.columns)

    columns.remove('ID')
    columns.remove('rating')
    columns.remove('review')
    columns.remove('product')
    columns.remove('price')

    X = []
    y = df['price']

    for i in range(len(df)):
        features = []
        for col in columns:
            features.append(df[col][i])
        
        X.append(features)
    X = pd.DataFrame(X, index=None, columns=columns)

    importances = []
    n_trials = 10

    for i in range(n_trials):
        model = RandomForestRegressor(random_state=i).fit(X, y)
        importance = model.feature_importances_
        importances.append(importance)

    final_importance = []
    for col_i in range(len(columns)):
        sum = 0
        for trial_i in range(n_trials):
            sum += importances[trial_i][col_i]
        
        final_importance.append(sum/n_trials)
    
    for i,v in enumerate(final_importance):
        print('Feature: %s, Importance: %.5f' % (columns[i],v))
    
    #plt.bar([x for x in range(len(final_importance))], final_importance)
    #plt.show()

    df_all_features = pd.DataFrame(data=[final_importance], index=None, columns=columns)
    df_all_features.to_csv('features_importances/' + 'all_features_' + dataset_name, index=False)

    importances_grouped = []
    l2sca = 0
    lca = 0
    for i in range(len(columns)):
        if(columns[i].startswith('l2sca')):
            l2sca += final_importance[i]
        elif(columns[i].startswith('lca')):
            lca += final_importance[i]
        else:
            importances_grouped.append(final_importance[i])

    importances_grouped.append(l2sca)
    importances_grouped.append(lca)

    for i in range(4):
        print('Feature: %s, Importance: %.5f' % (columns[i], importances_grouped[i]))

    print('Feature: l2sca, Importance: %.5f' % (importances_grouped[4]))
    print('Feature: lca, Importance: %.5f' % (importances_grouped[5]))

    #plt.bar([x for x in range(len(importances_grouped))], importances_grouped)
    #plt.show()

    df_grouped_features = pd.DataFrame(data=[importances_grouped], index=None, columns=[columns[0], columns[1],
                                                                                columns[2], columns[3], 'l2sca', 'lca'])
    df_grouped_features.to_csv('features_importances/' + 'grouped_features_' + dataset_name, index=False)




    ## Testing performance
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=10)
    y_test.sort_index(inplace=True)
    X_test.sort_index(inplace=True)

    model = LinearRegression().fit(X_train, y_train)
    predictions = model.predict(X_test)

    y_test = np.array(y_test)
    predictions = np.array(predictions)

    abs_errors = [abs(predictions[i] - y_test[i]) for i in range(len(predictions))]
    abs_errors = np.array(abs_errors)

    print('Mean Error', abs_errors.mean())
    print('Median Error', np.median(abs_errors))
    print()
    print('Mean Price', y_test.mean())
    print('Median Price', np.median(y_test))
    print()
    print('Mean Predicted Price', predictions.mean())
    print('Median Predicted Price', np.median(predictions))
    
    plt.plot([i for i in range(len(y_test))], y_test, label='Training data')
    plt.plot([i for i in range(len(predictions))], predictions, label='Predictions')
    plt.ylabel("Price")
    plt.legend()
    plt.savefig('features_importances/' + 'linear_regression_' + dataset_name.split(".csv")[0])
    plt.clf()

    r_squared = polyfit(y_test, predictions, 1)['determination']
    return r_squared

def polyfit(x, y, degree):
    results = {}

    coeffs = np.polyfit(x, y, degree)

     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results

def compose_r_2_csv():
    r_2 = []

    r_2.append(features_importances('result_appliances.csv'))
    r_2.append(features_importances('result_fashion.csv'))
    r_2.append(features_importances('result_luxury_beauty.csv'))
    r_2.append(features_importances('result_prime.csv'))
    r_2.append(features_importances('result_software.csv'))
    r_2.append(features_importances('result_music.csv'))

    df_grouped_features = pd.DataFrame(data=[r_2], index=None, columns=['result_appliances', 'result_fashion',
                                    'result_luxury_beauty', 'result_prime', 'result_software', 'result_music'])
    df_grouped_features.to_csv('r_2_values.csv', index=False)

compose_r_2_csv()