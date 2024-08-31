import json
import os
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from dotenv import load_dotenv
import utils

# Load environment variables
load_dotenv()

# Load JSON data
try:
    with open('assets/data.json') as file:
        my_info = json.load(file)
except FileNotFoundError:
    st.error("JSON file not found.")
    my_info = {}

# Load PDF data
try:
    with open('assets/nj_resume.pdf', 'rb') as file:
        pdf_data = file.read()
except FileNotFoundError:
    st.error("PDF file not found.")
    pdf_data = None

# Load Images
try:
    img_photo = Image.open('images/self.jpeg')
except FileNotFoundError as e:
    st.error(f"Image file not found: {e}")
    img_photo = None

# Lottie animations
lottie_animation = 'https://assets10.lottiefiles.com/packages/lf20_O2ci8jA9QF.json'
lottie_getintouch = 'https://assets5.lottiefiles.com/private_files/lf30_T12D5w.json'

# Set up Streamlit page configuration
st.set_page_config(page_title='Nithin Jashua', page_icon='🙌', layout='wide')

# Define custom CSS for profile image animation and button styling
css = """
<style>
body {
    background: #FFFFFF; /* Changed background color to pure white */
    font-family: 'Quicksand', sans-serif;
    color: black; /* Changed text color to black for better contrast */
}

.container {
    display: flex;
    align-items: flex-start;
    gap: 40px;
    padding: 20px;
}

.avatar-container {
    width: 230px; /* Increased size */
    height: 250px; /* Increased size */
    position: relative;
}

.avatar {
    overflow: hidden;
    border-radius: 50%;
    border: solid 3px rgba(0,150,136,0.3);
    width: 100%;
    height: 100%;
    background-size: cover;
    cursor: pointer;
}

.avatar img {
    width: 100%;
    height: 100%;
}

.pulse {
    width: 250px; /* Match avatar size */
    height: 270px; /* Match avatar size */
    border-radius: 50%;
    background: rgba(0,150,136,0.2);
    position: absolute;
    top: 0;
    left: 0;
    border: solid 2px #00796B;
    z-index: 1;
    animation: pulse-animation 2s infinite;
}

.name {
    position: fixed;
    top: calc(50% + 110px);
    text-align: center;
    left: 50%;
    transform: translateX(-50%);
    text-transform: uppercase;
    color: black; /* Changed text color to black */
    background: rgba(0,150,136,0.2);
    border: solid 2px #00796B;
    padding: 5px 10px;
    opacity: 0;
    transition: opacity 0.5s;
}

.info {
    color: black; /* Changed text color to black */
    text-transform: uppercase;
    position: fixed;
    right: 10px;
    bottom: 10px;
    font-size: 10px;
    opacity: 0.5;
}

/* Animation */
@keyframes pulse-animation {
    0% {
        transform: scale(1);
        opacity: 0.2;
    }
    50% {
        transform: scale(1.1);
        opacity: 0.4;
    }
    100% {
        transform: scale(1);
        opacity: 0.2;
    }
}

/* Contact Form Styles */
form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
    max-width: 400px;
    margin: 0 auto;
}

input, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #00796B;
    border-radius: 5px;
    font-family: 'Quicksand', sans-serif;
}

button {
    padding: 10px;
    color: skyblue;
    border: 2px solid skyblue;
    font-size: 16px;
    cursor: pointer;
    text-transform: uppercase;
    font-weight: bold;
    background: none;
    transition: background-color 0.3s ease, color 0.3s ease;
}

button:hover {
    background-color: skyblue;
    color: #FFFFFF; /* Changed text color to white for contrast */
}
</style>
"""

# Apply custom CSS
st.markdown(css, unsafe_allow_html=True)

# Main content
with st.container():
    left, right = st.columns([1, 3], gap='small')

    with left:
        if img_photo:
            # Convert the image to base64 and display with new animation styles
            img_base64 = utils.convert_image_to_base64(img_photo)
            st.markdown(f'''
            <div class="avatar-container">
                <div class="pulse"></div>
                <div class="avatar">
                    <img src="data:image/jpeg;base64,{img_base64}" alt="Profile Picture">
                </div>
                <div class="name">{my_info.get('name', 'Name')}</div>
            </div>
            ''', unsafe_allow_html=True)

    with right:
        st.subheader(my_info.get('header', ''))
        st.title(my_info.get('title', ''))
        st.write(my_info.get('about_me', ''))
        if pdf_data:
            st.download_button(
                label="📄 Download Resume",
                data=pdf_data,
                file_name='nithin_burugu.pdf',
                mime="application/octet-stream",
                key='download_resume'
            )

st.write('---')
st.header('Connect with me...')
c1, c2, c3, c4 = st.columns(4)

with st.container():
    c1.write(my_info.get('github', ''))
    c2.write(my_info.get('linkedin', ''))
    c3.write(my_info.get('instagram', ''))
    c4.write(my_info.get('leetcode', ''))

with st.container():
    st.write('---')
    interests, animation = st.columns([2, 3], gap='small')

    with interests:
        st.write('''
        ## My interests are:
        * Django web development and creating CRUD operations.
        * Backend development using Django REST Framework.
        * Designing and developing RESTful APIs.
        * Working with databases like MySQL, Snowflake.
        * Exploring machine learning projects and applications.
        * Enjoying nature through solo hikes and photography.
        ''')

    with animation:
        st_lottie(
            utils.load_data_from_url(lottie_animation),
            height=300,
            key='animation'
        )

st.write('---')
st.header('My Projects')

# Projects section
projects = [
    {
        "image_path": 'images/turismapp.png',
        "title": 'Tourism Website',
        "description": '''
        Developed a tourism website where users can browse through content, videos, and images of popular destinations.
        * Implemented a mobile-friendly layout using HTML block elements, inline elements, and CSS3 properties such as background, flex, and CSS box model properties.
        * Included a carousel for multiple images of a destination using Bootstrap carousel and embedded virtual tour videos using Bootstrap components.
        Technologies used: HTML, CSS, Bootstrap
        ''',
        "link": 'https://turismapp.ccbp.tech'
    },
    {
        "image_path": 'images/todoapp.png',
        "title": 'Todos Application',
        "description": '''
        A robust task tracking system with CRUD capabilities designed to simplify task management.
        * Created with HTML, CSS, and Bootstrap to provide a user-friendly interface.
        * Dynamic UI updates via JavaScript event listeners and DOM operations for seamless CRUD functionality.
        * Ensured task persistence with local storage methods to prevent data loss.
        Technologies used: HTML, CSS, JS, Bootstrap
        ''',
        "link": 'https://todosapp2022.ccbp.tech'
    },
    {
        "image_path": 'images/nxtrendzapp.png',
        "title": 'Nxt Trendz (ECommerce Clone)',
        "description": '''
        Developed an e-commerce platform inspired by Amazon and Flipkart.
        * Built pages for Login, Products, and Product details using React Router, React components, form inputs, and event handlers.
        * Implemented secure authentication and authorization with JWT tokens and REST API calls.
        Technologies used: React JS, JS, CSS, Bootstrap, Routing, REST API Calls, Local Storage, JWT Token.
        ''',
        "link": 'https://nxttrendzapp.ccbp.tech'
    }
]

for project in projects:
    with st.container():
        st.write('---')
        image_col, text_col = st.columns((1, 2))
        with image_col:
            try:
                st.image(project['image_path'])
            except FileNotFoundError:
                st.error(f"Image file not found: {project['image_path']}")
        with text_col:
            st.subheader(project['title'])
            st.write(project['description'])
            st.write(f"[Click here to view the project]({project['link']})")
