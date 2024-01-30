import pandas as pd
import streamlit as st
import pickle

columns = [
    'Berlin', 'Hamburg', 'Munich', 'Koeln', 'Essen',
    'Stuttgart', 'Dortmund', 'Duesseldorf', 'Bremen', 'Nuernberg',
    'Hannover', 'Leipzig', 'Duisburg', 'Dresden', 'Wandsbek', 'Bochum',
    'Wuppertal', 'Marienthal', 'Moenchengladbach', 'Augsburg', 'Chemnitz',
    'Krefeld', 'Kiel', 'Magdeburg', 'Oberhausen', 'Freiburg', 'Luebeck',
    'Bremerhaven', 'Erfurt', 'Harburg', 'Hagen', 'Rostock', 'Mainz',
    'Saarbruecken', 'Hamm', 'Herne', 'Muelheim', 'Heidelberg', 'Paderborn',
    'Darmstadt', 'Wuerzburg', 'Regensburg', 'Recklinghausen', 'Goettingen',
    'Heilbronn', 'Ulm', 'Bottrop', 'Bergedorf', 'Offenbach', 'Remscheid',
]


def main():
    st.title("Installs Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Installs Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    data = {}
    for col in columns:
        data[col] = int(st.text_input(col, "0"))

    if st.button("Predict"):
        dataset = pd.DataFrame(data, index=[0])
        model = pickle.load(open('model.pkl', 'rb'))
        prediction = model.predict(dataset)

        st.success('Installs on spendings: {}'.format(int(prediction[0])))


if __name__ == '__main__':
    main()
