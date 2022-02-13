import streamlit as st

import seaborn as sns

import matplotlib.pyplot as plt

import pandas as pd

from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

import pickle

st.title('Penguin Classifier')

st.write("This app uses 6 inputs to predict the species of penguin using"
         " a model built on the Palmer's Penguin's dataset. Use the form below"
         "to get started!")

penguin_file = st.file_uploader('Upload your own penguin data')

if penguin_file is None:

    rf_pickle = open('random_forest_penguin.pickle','rb')

    map_pickle = open('output_penguin.pickle','rb')

    rfc = pickle.load(rf_pickle)

    unique_penguin_mapping = pickle.load(map_pickle)

    rf_pickle.close()

    map_pickle.close()
    
else:
    
    penguin_df = pd.read_csv('penguins.csv')

    penguin_df.dropna(inplace = True)

    output = penguin_df['species']

    features = penguin_df[['island', 'bill_length_mm',  'bill_depth_mm',  'flipper_length_mm',  'body_mass_g', 'sex']]

    features = pd.get_dummies(features)


    output, unique_penguin_mapping = pd.factorize(output)

    x_train, x_test, y_train, y_test = train_test_split(
    features, output, test_size=.8
    )

    rfc = RandomForestClassifier(random_state =15)

    rfc.fit(x_train, y_train)

    y_pred = rfc.predict(x_test)

    score = accuracy_score(y_pred, y_test)

    st.write('We trained a Random Forest model on these data,'
             ' it has a score of {}!Use the'
             'inputs below to try out the model!'.format(score))
    fig, ax = plt.subplots()

    ax = sns.barplot(rfc.feature_importances_, features.columns)

    plt.title('Which features are the most important for species prediction?')

    plt.xlabel('Importance')

    plt.ylabel('Feature')

    plt.tight_layout()

    fig.savefig('feature_importance.png')

    st.write('We used a machine learning(Random Forest) model to'
             ' predict the species, the features used in this prediction'
             ' are ranked by relative importance below.')
    st.image('feature_importance.png')



with st.form('user_inputs'):
    island = st.selectbox('Penguin Island',options= ['Biscoe','Dream','Torgerson'])

    sex = st.selectbox('Sex',options = ['Female','Male'])

    bill_length = st.number_input('Bill Length(mm)', min_value = 0)

    bill_depth = st.number_input('Bill Depth(mm)', min_value = 0)

    flipper_length = st.number_input('Flipper Length(mm)', min_value = 0)

    body_mass = st.number_input('Body Mass(g)', min_value = 0)

    st.form_submit_button()

    island_biscoe, island_dream, island_torgerson = 0,0,0

    if island == 'Biscoe':
    
        island_biscoe = 1
    
    elif island == 'Dream':
    
        island_dream = 1
    
    elif island == 'Torgerson':
    
        island_torgerson = 1
    
    sex_female, sex_male = 0,0

    if sex == 'Female':

        sex_female = 1
    
    elif sex =='Male':

        sex_male =1
        
new_prediction = rfc.predict([[bill_length, bill_depth,
                               flipper_length, body_mass,
                               island_biscoe,island_dream,
                               island_torgerson,sex_female, sex_male]])

prediction_species = unique_penguin_mapping[new_prediction][0]

st.write('We predict your penguin is of the {} species'.format(prediction_species))

penguin_df = pd.read_csv('penguins.csv')
st.write('Below are the histograms for each continuous variable'
         'separated by penguin species. The vertical line'
         'represents your the inputted value')

fig, ax = plt.subplots()

ax = sns.displot(x = penguin_df['bill_length_mm'],

                 hue = penguin_df['species'])

plt.axvline(bill_length)

plt.title('Bill Length by Species')

st.pyplot(ax)

fig, ax = plt.subplots()

ax = sns.displot(x = penguin_df['bill_depth_mm'],

                 hue = penguin_df['species'])

plt.axvline(bill_depth)

plt.title('Bill Depth by Species')

st.pyplot(ax)

fig, ax = plt.subplots()

ax = sns.displot(x = penguin_df['flipper_length_mm'],
                 hue = penguin_df['species'])

plt.axvline(flipper_length)

plt.title('Flipper Length by Species')

st.pyplot(ax)




#print('Our accuracy score for this model is {}'.format(score))

#rf_pickle = open('random_forest_penguin.pickle','wb')

#pickle.dump(rfc,rf_pickle)

#rf_pickle.close()

#output_pickle = open('output_penguin.pickle','wb')

#pickle.dump(uniques,output_pickle)

#output_pickle.close()

