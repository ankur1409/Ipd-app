import streamlit as st

# Function to display the About section
def show_about():
    st.subheader("About")
    st.write("Welcome to [Your Company/Project Name], where we are breaking communication barriers with innovative technology. Our platform specializes in sign language to text and speech conversion, empowering individuals with hearing and speech impairments to communicate seamlessly in real-time.")
    st.write("Harnessing the power of advanced AI, machine learning, and gesture recognition, our solution translates sign language into written and spoken words, fostering inclusivity and accessibility in everyday interactions. Whether it's in classrooms, workplaces, healthcare, or social settings, our technology bridges the gap between the hearing and non-hearing communities.")
# Function to simulate camera functionality
def open_camera():
    st.write("Camera functionality to be implemented.")

# Main application
def main():
    # Set the title of the app
    st.title("Sign Language Recognition")

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
