
import streamlit as st

# Function to display the About section
def show_about():
    st.subheader("About")
    st.write("Welcome to our project, where we are breaking communication barriers with innovative technology.")
    st.write("Our platform specializes in sign language to text and speech conversion, empowering individuals with hearing and speech impairments to communicate seamlessly in real-time.")
    st.write("Harnessing the power of advanced AI, machine learning, and gesture recognition, our solution translates sign language into written and spoken words, fostering inclusivity and accessibility in everyday interactions.")
    st.write("Whether it's in classrooms, workplaces, healthcare, or social settings, our technology bridges the gap between the hearing and non-hearing communities.")

# Function to simulate camera functionality
def open_camera():
    st.write("Camera functionality to be implemented.")

# Main application
def main():
    # Set the title of the app
    st.set_page_config(page_title="Sign Language Recognition", page_icon=":sign_language:", layout="wide")
    
    # Logo
    logo = "logo.png"  # Replace with the path to your logo image
    st.image(logo, width=10, use_column_width=False)  # Set width to 300 pixels

    # Header
    st.title("Sign Language Recognition")
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Empowering Communication</h2>", unsafe_allow_html=True)

    # Text input box for user input
    text_input = st.text_area("Converted Text:", height=100)

    # Button to open camera (placeholder)
    if st.button("Open Camera"):
        open_camera()

    # About section
    if st.button("About"):
        show_about()

# Run the app
if __name__ == "__main__":
    main()
