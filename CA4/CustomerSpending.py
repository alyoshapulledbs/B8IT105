# -*- coding: utf-8 -*-
"""
Module       : B8IT105 - Programming For Big Data
Assignment   : CA4 - DataFrames using Pandas
Student Code : 10541255
Student Name : Alyosha Pulle
"""

# The data is sourced from - https://archive.ics.uci.edu/ml/datasets/Wholesale+customers
# Have included dataset in submission in case URL goes offline. 

import pandas as pd
import matplotlib.pyplot as plt

class CustomerSpending():
    # Opens repository and provides access to data frame and some visualisations.
    
    def __init__(self):
        # Set environment Load in the data from URL.
        self.__set_environment()
        self.__df_spending = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv')
        self.__product_categories = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicatessen']

    def __set_environment(self):
        plt.close('all')
        pd.set_option('max_columns', None)
        plt.rcParams["figure.figsize"] = (10, 10)

    def get_df_spending(self):
        # Accessor to the dataset.
        return self.__df_spending

    def nan_count(self):
        # Give # of NaNs in dataset.
        return pd.isna(self.__df_spending).sum().sum()

    def clean_data(self):
        # Fix typo in column name.
        self.__df_spending.rename(columns={'Delicassen':'Delicatessen'}, inplace=True)
        
        # Convert Channel and Region to categoricals.
        self.__df_spending['Channel'] = self.__df_spending['Channel'].astype('category')
        self.__df_spending['Channel'].cat.categories = ['Horeca', 'Retail']
        
        self.__df_spending['Region'] = self.__df_spending['Region'].astype('category')
        self.__df_spending['Region'].cat.categories = ['Lisbon', 'Oporto', 'Other Region']

        # Calculate total sales.
        self.__df_spending['Total'] = (self.__df_spending['Fresh'] + self.__df_spending['Milk'] +
             self.__df_spending['Grocery'] + self.__df_spending['Frozen'] +
             self.__df_spending['Detergents_Paper'] + self.__df_spending['Delicatessen'])
        
    def show_summary(self):
        # Print a summary of the data
        print('\n## The shape of the data ##')
        print(self.__df_spending.shape)      
        print('\n## The top 5 rows ##')
        print(self.__df_spending.head())
        print('\n## The column data types ##')
        print(self.__df_spending.dtypes)
        print('\n## Basic statistics ##')
        print(self.__df_spending.describe())

    def plot_summary_counts(self):
        # Total Observations Collected In Region By Channel
        df_totals = (self.__df_spending.loc[:, ['Region','Channel','Total']]
                                        .groupby(['Region','Channel'])
                                        .size()
                                        .unstack(1))
        plt.figure();
        df_totals.plot.bar()
        plt.title('Total Observations Collected In Region By Channel')
        plt.ylabel('Observations')
        plt.show()
        
    def plot_summary_spending_totals(self):
        # Total Annual Spending In Region By Channel
        df_totals = (self.__df_spending.loc[:, ['Region','Channel','Total']]
                                        .groupby(['Region','Channel'])
                                        .sum()
                                        .unstack(1))
        plt.figure();
        df_totals.plot.bar()
        plt.title('Total Annual Spending In Region By Channel')
        plt.ylabel('Annual Spending')
        plt.show()

    def plot_distribution(self, channel='Horeca', region='All'):
        # Annual Spending Distribution By Product Category
        # Filtered by Channel and optionally Region
        if region == 'All':
            regionText = 'All Regions'
            df_distribution = self.__df_spending[self.__df_spending['Channel'] == channel]
        else:
            regionText = region
            df_distribution = self.__df_spending[(self.__df_spending['Channel'] == channel) & 
                                                 (self.__df_spending['Region'] == region)]
        plt.figure();
        df_distribution.boxplot(column=self.__product_categories, showmeans=True)
        plt.title('Annual Spending Distribution By Product Category\nFor {0} In {1}'.format(channel, regionText))
        plt.xlabel('Product Categories')
        plt.ylabel('Annual Spending')
        plt.show()


def main():
    cs = CustomerSpending()
    print('\n### Summary on Raw Data')
    cs.show_summary()
    print('\n### Summary on Cleaned Data')
    cs.clean_data()
    cs.show_summary()
    
    cs.plot_summary_counts()
    cs.plot_summary_spending_totals()
    
    cs.plot_distribution()      # Horeca
    cs.plot_distribution(channel='Retail')
    
    cs.plot_distribution(region='Lisbon')      # Horeca
    cs.plot_distribution(channel='Retail', region='Lisbon')

if __name__ == '__main__':
    main()
