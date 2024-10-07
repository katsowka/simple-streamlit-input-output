import streamlit as st
from data import (
    regions,
    min_age,
    max_age,
    get_mean_claim
)


def configure_page() -> None:
    st.set_page_config(page_title="Super Simple Streamlit App", layout="wide")


def configure_overview() -> None:
    st.markdown("## Simple App - Insurance Claims by Region and Age")
    st.markdown(
        "This [simple app](https://github.com/katsowka/simple-streamlit-input-output)\
        takes two inputs and uses a static csv file to generate an output, \
        which gets displayed."
    )

    st.markdown(
        "Specifically, it calculates the **number of claims** and **average claim \
        value** for people from a selected **region** and of a selected **age**, based on \
        [data](https://github.com/premrpinto/Insurance-dataset/tree/main) recorded in a \
        hypothetical sample of insurance claims."
    )


def inputs_outputs() -> None:

    # input form
    with st.form("input_form"):
        st.markdown("### Inputs")
        st.write("Choose the region and age of person for whom you want insurance \
                 claims data.")
        selected_region = st.selectbox('REGION:', regions)
        selected_age = st.slider('AGE:', min_age, max_age) 
        st.form_submit_button('submit inputs')

    # outside of form
    num_claims, mean_claim = get_mean_claim(selected_region=selected_region, selected_age=selected_age)
    st.markdown("### Output")
    st.write(f"number of claims:  {num_claims}\n\naverage claim amount: £{mean_claim:.2f}")
              

def main() -> None:
    configure_page()
    configure_overview()
    inputs_outputs()


if __name__ == "__main__":
    main()
