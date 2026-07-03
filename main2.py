from PetNameGenerator import main
import streamlit as st
st.title("PETS NAME GENERATOR")

animal_type=st.sidebar.selectbox("what is your pet?",("cat","dog","cow","hamster"))

pet_color=st.sidebar.text_area(label=f"what color is your {animal_type}?",max_chars=10)

if pet_color:
    response= main.generate_pet_name(animal_type, pet_color)
    st.text(response)