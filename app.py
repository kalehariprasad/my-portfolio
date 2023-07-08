import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# Page functions



def home():
    st.title("kale Hari Prasad")
    image=Image.open('image.jpg')
    st.image(image,width=200,)
    st.markdown("""
               
        As a Data Scientist, I am driven by a passion for delivering impactful results. With expertise in predictive modeling and API development, I possess a strong command of Python and a wealth of practical knowledge in various aspects of the data science workflow. My skills encompass data preprocessing, feature engineering, model selection, and performance assessment, allowing me to create robust and accurate predictive models.

        Throughout my career, I have demonstrated a track record of developing innovative solutions that drive business growth and enhance customer satisfaction. By leveraging my technical skills and domain knowledge, I have successfully tackled complex challenges and delivered actionable insights to stakeholders. I thrive in collaborative settings, actively engaging with cross-functional teams to understand business requirements and align data science efforts with organizational goals.

        One of my key strengths lies in my ability to effectively communicate complex technical concepts to non-technical stakeholders. I understand the importance of clear and concise communication in driving data-driven decision-making. Whether it's presenting findings, explaining model outputs, or discussing project progress, I ensure that information is conveyed in a manner that is easily understandable and relevant to the audience.

        In addition to my technical prowess, I possess a strong sense of curiosity and a desire to continuously learn and stay up-to-date with the latest advancements in the field of data science. This allows me to adapt quickly to new technologies, tools, and methodologies, ensuring that my solutions are at the forefront of industry standards.
     """)
    

def projects():
    st.title("Projects")
    st.header('Employee promotion prediction')
    st.markdown(""""
                I worked diligently to develop a Python-based movie recommendation system by leveraging the TMDB API. The first step involved collecting comprehensive movie data from the API, including titles, genres, posters, and cast information. This rich dataset served as the foundation for our recommendation system, ensuring a diverse and extensive collection of movies to work with.

To efficiently manipulate and analyze the movie data, I utilized popular libraries such as pandas and NumPy. These libraries provided powerful tools for data manipulation, enabling us to preprocess and organize the movie features effectively. By leveraging these tools, I ensured that the data was in a suitable format for further analysis and recommendation generation.

For the recommendation algorithm, I employed scikit-learn, a widely-used machine learning library. Using scikit-learn, I calculated similarity measures between movies based on their respective features. In particular, I utilized cosine similarity to determine the similarity between movies, considering factors such as genre, cast, and other relevant attributes. This allowed the system to identify and suggest similar movies based on their feature similarities.

The developed recommendation system enabled users to receive movie suggestions based on their preferences. By analyzing the comprehensive movie data collected from the TMDB API and leveraging efficient data manipulation techniques, the system was able to generate accurate and relevant recommendations. The cosine similarity calculations facilitated a robust and effective recommendation process, ensuring that users received suggestions that closely matched their interests.

Overall, through the integration of the TMDB API, Python libraries such as pandas and NumPy for data manipulation, and scikit-learn for similarity calculations, I successfully developed a powerful movie recommendation system. This system allowed users to discover new movies based on the similarities between their features, providing an enhanced movie-watching experience.
                
                
                """)
    if st.button('Open Promotion Prediction'):
         link = "https://kalehariprasad-employee-promotion-predictions-app-7x6ya6.streamlit.app/"
         st.markdown(f'<a href="{link}" target="_blank">Open Promotion Prediction</a>', unsafe_allow_html=True)
        

        

                
    st.header("Movie Recommendations system")
    st.markdown("""
                I worked diligently to develop a Python-based movie recommendation system by leveraging the TMDB API. The first step involved collecting comprehensive movie data from the API, including titles, genres, posters, and cast information. This rich dataset served as the foundation for our recommendation system, ensuring a diverse and extensive collection of movies to work with.

                To efficiently manipulate and analyze the movie data, I utilized popular libraries such as pandas and NumPy. These libraries provided powerful tools for data manipulation, enabling us to preprocess and organize the movie features effectively. By leveraging these tools, I ensured that the data was in a suitable format for further analysis and recommendation generation.

                For the recommendation algorithm, I employed scikit-learn, a widely-used machine learning library. Using scikit-learn, I calculated similarity measures between movies based on their respective features. In particular, I utilized cosine similarity to determine the similarity between movies, considering factors such as genre, cast, and other relevant attributes. This allowed the system to identify and suggest similar movies based on their feature similarities.

                The developed recommendation system enabled users to receive movie suggestions based on their preferences. By analyzing the comprehensive movie data collected from the TMDB API and leveraging efficient data manipulation techniques, the system was able to generate accurate and relevant recommendations. The cosine similarity calculations facilitated a robust and effective recommendation process, ensuring that users received suggestions that closely matched their interests.

                Overall, through the integration of the TMDB API, Python libraries such as pandas and NumPy for data manipulation, and scikit-learn for similarity calculations, I successfully developed a powerful movie recommendation system. This system allowed users to discover new movies based on the similarities between their features, providing an enhanced movie-watching experience.
                """)
    if st.button("Open Movie Recommendation System"):
       link = "https://kalehariprasad-movie-recommendatios-app2-bgkvok.streamlit.app/"
       st.markdown(f'<a href="{link}" target="_blank">Open Movie Recommendation System</a>', unsafe_allow_html=True)

    
    st.header("College admission prediction system")
    st.markdown("""
                I embarked on the development of a machine learning model to accurately predict student admission, working diligently on the project. The first step was to implement essential data preprocessing techniques to ensure the quality and reliability of the data. I performed feature scaling to eliminate any potential bias that could arise from varying scales of input variables. Additionally, I employed imputation techniques to handle missing data, ensuring that valuable information was not lost during the modeling process.

                To provide seamless accessibility to the application, I deployed the model using Streamlit Cloud. This deployment platform facilitated an intuitive web interface that allowed users to easily interact with the application. Leveraging Streamlit Cloud's capabilities, I ensured that the model was readily accessible to a wide range of users, providing a user-friendly and convenient experience.

                To enhance the efficiency and maintainability of the solution, I utilized scikit-learn pipelines. By incorporating pipelines into the workflow, I streamlined the data preprocessing and modeling process. This approach not only improved efficiency but also made it easier to organize and manage the various steps involved in the solution.

                Throughout the development process, I approached the project with great care and attention to detail. I focused on implementing essential data preprocessing techniques, deploying the model using Streamlit Cloud, and leveraging scikit-learn pipelines to optimize the workflow. By devoting my expertise and efforts to the project, I successfully developed a robust model that accurately predicted student admission. The final solution provided valuable insights for decision-making in student admissions, catering to the requirements of the project in a comprehensive manner.
                """)
    if st.button("College admission predictio System"):
        
        link = "https://kalehariprasad-college-predictions-app-utbfvp.streamlit.app/"
        st.markdown(f'<a href="{link}" target="_blank">College admission prediction System</a>', unsafe_allow_html=True)

  
                
    st.title('Logistics price prediction')
    st.markdown("""
                As part of a collaborative effort with my team members, we embarked on the development of a machine learning model using pipelines to predict consignment prices. Our first step was to gather requirements and understand the problem at hand, ensuring that we had a clear vision of the desired solution. With a well-defined plan in place, we proceeded to design and implement the model, leveraging the power of various machine learning algorithms and techniques.

               Throughout the development process, we maintained open communication and shared our expertise to ensure a robust and accurate model. We conducted thorough data analysis, preprocessing, and feature engineering to extract relevant information from the dataset, enhancing the model's predictive capabilities. The pipeline architecture allowed us to streamline the workflow, ensuring efficient data transformation and model training.

               To provide easy and user-friendly access to our solution, we opted to deploy the model using Streamlit Cloud. This platform enabled us to create an intuitive web application where users could input relevant consignment information and obtain accurate price predictions. Streamlit Cloud's deployment capabilities facilitated the seamless integration of our model, providing a smooth and interactive experience for end-users.

               Overall, our collaboration and systematic approach to developing, deploying, and deploying the model using pipelines and Streamlit Cloud resulted in a powerful and accessible solution for predicting consignment prices. By leveraging the collective expertise of our team and employing user-friendly tools, we aimed to deliver a high-quality product that met the needs of our target audience.
               """ )
               
    if st.button('open logistic price prediction'):
        link= "https://kalehariprasad-logistics-price-prediction-app1-m8w5oi.streamlit.app/"
        st.markdown(f'<a href="{link}" target="_blank">logistic price prediction</a>', unsafe_allow_html=True)

  
def Education ():
    st.title("Education")
    st.subheader('B.tech')
    st.markdown("""
                ABR college college of engineerinig &technology

                B.tech(Electrical and Electronics engineering) - 2018-2021

                cgpa 6.9/10
                """)
    st.subheader("Diploma")
    st.markdown("""
                ABR college college of engineerinig &technology
                
                Diploma(Electrical and Electronics engineering) - 2015 -2018
                
                72.75%
                """)
    st.subheader("SSC")
    st.markdown("""
                ZPHS Chennipadu
                
                SSC 2014 -2015
                
                cgpa -8.8/10
                """)
                
def Experience():
    st.title('Experience')
    st.subheader("Data Scientist intern - Oasis infobyte")
    st.markdown("""
                
                
               Throughout my journey as a Data Scientist intern, I have successfully developed end-to-end projects, showcasing my expertise in various aspects of the field. One such project involved tackling an email classification problem. From data preprocessing to model evaluation, I leveraged Python to handle the entire pipeline. By employing feature engineering techniques and selecting appropriate models, I achieved effective email classification, providing valuable insights for improved productivity and organization.

               Additionally, I conducted Exploratory Data Analysis (EDA) on unemployment in India, gaining valuable insights into the factors contributing to the country's employment landscape. Through visualizations, statistical analysis, and data exploration, I provided meaningful and actionable information to stakeholders, facilitating informed decision-making.

               To ensure seamless integration and usability, I developed APIs for both end-to-end projects. This allowed for easy integration with existing systems and provided a user-friendly interface for accessing the functionalities of the projects. By creating APIs, I prioritized the ease of use and smooth integration of the developed solutions.

               Throughout the projects, I maintained a strong focus on business growth and customer experience improvement. By understanding the unique needs and requirements of the stakeholders, I designed and implemented predictive models that effectively addressed their specific challenges. For instance, I successfully developed models for classifying iris species and classifying emails, showcasing my ability to deliver accurate and valuable predictions.
                """)
    if st.button("Oasis infoByte certificate"):
        link="https://drive.google.com/file/d/1e1pDzdhNCRJ5eLQxA0ZIEv_6lnFuYMFy/view?usp=sharing"
        st.markdown(f'<a href="{link}" target="_blank">Oasis infoByte certificate</a>', unsafe_allow_html=True)

    st.subheader("Project Intern - iNeuron. AI")
    st.markdown("""
                In my role as a Data Scientist project intern, I have played a crucial role in conducting thorough data cleaning, preprocessing, and analysis. By meticulously cleaning and preparing the data, I ensured its quality and reliability, laying the foundation for the development of accurate and robust machine learning models. Through exploratory data analysis (EDA), I gained valuable insights into the data, identifying patterns and trends that informed the subsequent modeling process.

                As part of the development process, I actively contributed to designing, implementing, and evaluating machine learning model algorithms. By staying abreast of the latest advancements in the field, I leveraged a diverse range of algorithms and techniques to address specific problem statements. This involved feature selection, engineering, and model training, ensuring the models were tailored to the specific requirements of the tasks at hand.

                To optimize the performance of the models, I conducted rigorous performance analysis and fine-tuned model parameters. By assessing metrics such as accuracy, precision, recall, and F1 score, I iteratively refined the models, maximizing their predictive capabilities. This iterative process allowed me to identify the optimal configurations for the models, enhancing their overall performance.

                Collaboration played a crucial role in my work, as I closely collaborated with team members to seamlessly integrate machine learning models into larger software systems. By coordinating with software engineers and developers, I ensured the successful deployment and functionality of the models within the larger system architecture. This collaborative effort ensured that the models were efficiently integrated and delivered their intended value to end-users.
                """)
    if st.button("iNeuron. AI certificate"):
        link="https://drive.google.com/file/d/1e6Kmbh3wXSZ2YDHinr1FyHnQ5N8pvfdE/view?usp=sharing"
        st.markdown(f'<a href="{link}" target="_blank">iNeuron. AI certificate</a>', unsafe_allow_html=True)
                
                
                
def Resume ():
    st.title("Resume")
    link ="https://drive.google.com/file/d/1rZNlaBwXU4IVYz0OaWYDC8qE2-nffZb1/view?usp=sharing"
    st.markdown(f'<a href="{link}" target="_blank"> Resume </a>', unsafe_allow_html=True)




def certification():
    st.title('my certifications')
    st.markdown("""
                Machine Learning Certification Course for Beginners
                """)
    if st.button("show credential"):
        link="https://drive.google.com/file/d/1ZcoQpNAHQ3RF57djmdSuR0_ttup2DwdL/view?usp=sharing"
        st.markdown(f'<a href="{link}" target="_blank"> certificate</a>', unsafe_allow_html=True)
def skills():
    st.title("skils")
    st.subheader("Programing Langauges")
    
    st.markdown("- Python\n- MySQL")
    st.subheader("Python Libraries")
    st.markdown("- Pandas\n- NumPy\n- Scikit-learn\n- Machine Learning Algorithms\n- NLP")
    st.subheader("Data Visualization")
    st.markdown("- Matplotlib\n- seaborn")
    st.subheader("Web Development")
    st.markdown("- streamlit")
    st.subheader("Version Control")
    st.markdown("- Git\n- GitHub")
def contact():
    st.title(" contact details")
    st.markdown("""
                phone- +916302051580
                
                
                
                Email     -  hariprasad9693@gmail.com
                
                Linkedin  -  https://www.linkedin.com/in/hari-prasad-kale-896701236/
                
                Github    -  https://github.com/kalehariprasad
                
                
                
                
                """)
    # Add content for the about page

# Main app
def main():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Go to", ["Home", "Education","Experience","Projects","certification","skills","Resume", "contact"])

    # Render the selected page
    if selected_page == "Home":
        home()
    elif selected_page=="Education":
        Education()   
    elif selected_page == "Experience":
        Experience()
    elif selected_page == "Projects":
        projects()
    elif selected_page == "certification":
        certification()
    elif selected_page == "skills":
        skills()
    elif selected_page =="Resume":
        Resume()
    elif selected_page == "contact":
        contact()

if __name__ == "__main__":
    main()

