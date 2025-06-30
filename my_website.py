
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Shubham Mantri - Data Scientist",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .main {
        padding-top: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    .hero-section {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        text-align: center;
        color: white;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 300;
        margin-bottom: 1rem;
        opacity: 0.9;
    }
    
    .skill-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    
    .skill-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .project-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(238, 90, 36, 0.4);
    }
    
    .experience-timeline {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border-left: 4px solid #4ecdc4;
    }
    
    .contact-button {
        background: linear-gradient(135deg, #4ecdc4 0%, #2980b9 100%);
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
        transition: all 0.3s ease;
        border: none;
        font-weight: 600;
    }
    
    .contact-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    .sidebar .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    
    .animated-text {
        animation: fadeInUp 1s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Sidebar Navigation
st.sidebar.title("🎯 Navigation")
st.sidebar.markdown("---")

# Navigation buttons with proper session state handling
if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.page = "Home"
if st.sidebar.button("💼 Experience", use_container_width=True):
    st.session_state.page = "Experience"
if st.sidebar.button("🚀 Projects", use_container_width=True):
    st.session_state.page = "Projects"
if st.sidebar.button("🎯 Skills", use_container_width=True):
    st.session_state.page = "Skills"
if st.sidebar.button("📈 Achievements", use_container_width=True):
    st.session_state.page = "Achievements"
if st.sidebar.button("📞 Contact", use_container_width=True):
    st.session_state.page = "Contact"

# Get current page
page = st.session_state.page

# Main content based on selection
if page == "Home":
    # Hero Section
    st.markdown("""
    <div class="hero-section animated-text">
        <h1 class="hero-title">Shubham Mantri</h1>
        <p class="hero-subtitle">Data Scientist III | AI/ML Expert | Innovation Driver</p>
        <p style="font-size: 1.2rem; margin-top: 1rem;">
            🚀 Transforming data into intelligent solutions with cutting-edge AI/ML technologies
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>5+</h3>
            <p>Years Experience</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>15+</h3>
            <p>Clients Onboarded</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>99.4%</h3>
            <p>Best Model Accuracy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>35%</h3>
            <p>Revenue Impact</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # About Section
    st.markdown("""
    <div class="project-card animated-text">
        <h2 style="color: #4ecdc4; margin-bottom: 1rem;">🎯 About Me</h2>
        <p style="font-size: 1.1rem; line-height: 1.8; color: white;">
            I'm a passionate Data Scientist with expertise in developing innovative AI/ML solutions that drive business value. 
            Currently working as Data Scientist III at Jio Platforms Limited, I specialize in Generative AI, Computer Vision, 
            and Fraud Detection systems. My work has contributed to significant revenue increases and successful client onboarding 
            across multiple organizations.
        </p>
        <p style="font-size: 1.1rem; line-height: 1.8; color: white; margin-top: 1rem;">
            💡 <strong>Specializations:</strong> Agentic RAG, Multimodal AI, Behavioral Biometrics, Fraud Detection, 
            Computer Vision, and Predictive Analytics.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Experience":
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 2rem;'>💼 Professional Journey</h1>", unsafe_allow_html=True)
    
    # Experience Timeline
    experiences = [
        {
            "company": "Jio Platforms Limited (JPL)",
            "role": "Data Scientist III",
            "period": "August 2024 - Present",
            "projects": [
                "Intelligent PDF Query Chatbot using Agentic RAG",
                "Attribute-Based Image and User Input Style Mapping"
            ],
            "achievements": "88% accuracy in visual pattern matching"
        },
        {
            "company": "Bureau, Inc.",
            "role": "Data Scientist",
            "period": "April 2022 - July 2024",
            "projects": [
                "Device Intelligence Solution for Fraud Detection",
                "Behavior Biometrics Solution for Bot Detection"
            ],
            "achievements": "99.4% accuracy, 27% revenue increase, 10+ clients onboarded"
        },
        {
            "company": "Spinny",
            "role": "Data Scientist",
            "period": "March 2021 - March 2022",
            "projects": [
                "Car Procurement Price Prediction Using Hybrid ML Models"
            ],
            "achievements": "15% RMSE reduction"
        }
    ]
    
    for exp in experiences:
        projects_html = "".join([f"<li>{project}</li>" for project in exp['projects']])
        st.markdown(f"""
        <div class="experience-timeline animated-text">
            <h3 style="color: #4ecdc4; margin-bottom: 0.5rem;">{exp['company']}</h3>
            <h4 style="color: #ff6b6b; margin-bottom: 0.5rem;">{exp['role']}</h4>
            <p style="color: #a0a0a0; margin-bottom: 1rem; font-weight: 600;">{exp['period']}</p>
            <p style="color: white; margin-bottom: 1rem;"><strong>Key Projects:</strong></p>
            <ul style="color: white; margin-bottom: 1rem;">
                {projects_html}
            </ul>
            <p style="color: #4ecdc4; font-weight: 600;">🎯 {exp['achievements']}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Projects":
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 2rem;'>🚀 Featured Projects</h1>", unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Intelligent PDF Query Chatbot using Agentic RAG",
            "description": "Developed a sophisticated chatbot using Agentic Retrieval-Augmented Generation to query PDF documents efficiently, providing concise and accurate responses from document content.",
            "tech": ["llamaindex", "transformers", "openai", "gradio"],
            "algorithms": ["Naive RAG", "Agentic RAG", "Multimodal RAG"],
            "impact": "Enhanced document querying efficiency",
            "category": "Generative AI"
        },
        {
            "title": "Device Intelligence Solution for Fraud Detection",
            "description": "Developed a comprehensive solution assigning unique IDs to devices using hybrid rule-based and ML models to detect fraud indicators like emulators, VPNs, and rooting.",
            "tech": ["scikit-learn", "pandas", "numpy", "keras", "tensorflow"],
            "algorithms": ["Random Forest", "Multi-Layered Perceptron", "Rule-based Logic"],
            "impact": "99.4% accuracy, 27% revenue increase, 10+ clients onboarded",
            "category": "Fraud Detection"
        },
        {
            "title": "Behavior Biometrics Solution",
            "description": "Built an advanced behavioral biometrics solution using touch, motion, and pointer data to detect bot activity and Account Takeover (ATO) frauds with high accuracy.",
            "tech": ["scikit-learn", "tensorflow", "keras", "numpy"],
            "algorithms": ["Isolation Forest", "ECOD", "CNN Outlier Model"],
            "impact": "97% accuracy in bot detection, 92% recall in ATO fraud detection",
            "category": "Behavioral Analytics"
        },
        {
            "title": "Visual Pattern Recognition System",
            "description": "Created an AI system that identifies user-defined attributes such as patterns or textures in images by analyzing input images and user descriptions.",
            "tech": ["openai", "gradio", "rembg"],
            "algorithms": ["Generative AI", "Computer Vision"],
            "impact": "88% accuracy in matching visual patterns",
            "category": "Computer Vision"
        }
    ]
    
    for project in projects:
        # Create technology tags
        tech_tags = ""
        for tech in project['tech']:
            tech_tags += f'<span style="background: rgba(255, 107, 107, 0.2); color: #ff6b6b; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block;">{tech}</span>'
        
        # Create algorithm tags
        algo_tags = ""
        for algo in project['algorithms']:
            algo_tags += f'<span style="background: rgba(78, 205, 196, 0.2); color: #4ecdc4; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.9rem; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block;">{algo}</span>'
        print('$'*50)
        print(tech_tags)
        print('!'*50)
        print(algo_tags)
        print('$'*50)

        # Create the project card HTML
        project_html = f"""
        <div class="project-card animated-text" style="background: rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 2rem; margin-bottom: 2rem; border: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <h3 style="color: #4ecdc4; margin: 0; font-size: 1.4rem;">{project['title']}</h3>
                <span style="background: linear-gradient(135deg, #ff6b6b, #ee5a24); color: white; padding: 0.3rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">{project['category']}</span>
            </div>
            <p style="color: white; font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">{project['description']}</p>
            <div style="margin-bottom: 1rem;">
                <h4 style="color: #4ecdc4; margin-bottom: 0.5rem; font-size: 1.1rem;">🧠 Algorithms:</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                    {algo_tags}
                </div>
            </div>
            <div style="margin-bottom: 1rem;">
                <h4 style="color: #4ecdc4; margin-bottom: 0.5rem; font-size: 1.1rem;">🛠️ Technologies:</h4>
                <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                    {tech_tags}
                </div>
            </div>
            <div style="background: rgba(78, 205, 196, 0.1); border-radius: 10px; padding: 1rem; border-left: 4px solid #4ecdc4;">
                <h4 style="color: #4ecdc4; margin: 0 0 0.5rem 0; font-size: 1.1rem;">🎯 Impact & Results:</h4>
                <p style="color: white; margin: 0; font-weight: 600;">{project['impact']}</p>
            </div>
        </div>
        """
        
        st.markdown(project_html, unsafe_allow_html=True)

elif page == "Skills":
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 2rem;'>🎯 Technical Expertise</h1>", unsafe_allow_html=True)
    
    # Skills data for visualization
    skills_data = {
        'AI/ML Frameworks': ['TensorFlow', 'Keras', 'Scikit-learn', 'PyTorch', 'Transformers'],
        'Generative AI': ['OpenAI API', 'LlamaIndex', 'RAG Systems', 'Multimodal AI', 'Gradio'],
        'Data Science': ['Pandas', 'NumPy', 'Plotly', 'Seaborn', 'Matplotlib'],
        'Algorithms': ['Random Forest', 'CNN', 'Isolation Forest', 'Decision Trees', 'Neural Networks'],
        'Tools & Platforms': ['Tableau', 'Superset', 'Git', 'Docker', 'AWS'],
        'Specializations': ['Fraud Detection', 'Computer Vision', 'NLP', 'Behavioral Analytics', 'Predictive Modeling']
    }
    
    # Create skill proficiency chart
    skill_levels = {
        'Machine Learning': 95,
        'Deep Learning': 90,
        'Generative AI': 88,
        'Computer Vision': 85,
        'NLP': 82,
        'Data Visualization': 90,
        'Python': 95,
        'Statistical Analysis': 88,
        'Fraud Detection': 92,
        'MLOps': 78
    }
    
    # Skills radar chart
    fig = go.Figure()
    
    categories = list(skill_levels.keys())
    values = list(skill_levels.values())
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        fillcolor='rgba(78, 205, 196, 0.3)',
        line_color='rgba(78, 205, 196, 1)',
        line_width=3,
        name='Skill Level'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='rgba(255, 255, 255, 0.3)',
                tickcolor='white'
            ),
            angularaxis=dict(
                gridcolor='rgba(255, 255, 255, 0.3)',
                tickcolor='white'
            )
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Skills categories
    col1, col2, col3 = st.columns(3)
    
    skills_columns = [
        ['AI/ML Frameworks', 'Generative AI'],
        ['Data Science', 'Algorithms'],
        ['Tools & Platforms', 'Specializations']
    ]
    
    for idx, col in enumerate([col1, col2, col3]):
        with col:
            for category in skills_columns[idx]:
                skill_tags = "".join([f'<span style="background: rgba(255, 107, 107, 0.2); color: #ff6b6b; padding: 0.4rem 0.8rem; border-radius: 15px; font-size: 0.85rem; display: inline-block; margin-bottom: 0.5rem; margin-right: 0.5rem;">{skill}</span>' for skill in skills_data[category]])
                
                st.markdown(f"""
                <div class="skill-card">
                    <h3 style="color: #4ecdc4; margin-bottom: 1rem;">{category}</h3>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                        {skill_tags}
                    </div>
                </div>
                """, unsafe_allow_html=True)

elif page == "Achievements":
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 2rem;'>📈 Key Achievements</h1>", unsafe_allow_html=True)
    
    # Achievement metrics visualization
    metrics_data = {
        'Metric': ['Model Accuracy', 'Revenue Increase', 'Clients Onboarded', 'RMSE Reduction', 'Bot Detection Accuracy'],
        'Value': [99.4, 35, 15, 15, 97],
        'Project': ['Device Intelligence', 'Combined Impact', 'Multiple Projects', 'Car Price Prediction', 'Behavior Biometrics']
    }
    
    df = pd.DataFrame(metrics_data)
    
    # Create bar chart
    fig = px.bar(
        df, 
        x='Metric', 
        y='Value', 
        color='Project',
        title='Key Performance Metrics Across Projects',
        color_discrete_sequence=['#4ecdc4', '#ff6b6b', '#45b7d1', '#96ceb4', '#feca57']
    )
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        title_font_size=20,
        title_x=0.5
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Achievement cards
    achievements = [
        {
            "icon": "🎯",
            "title": "99.4% Model Accuracy",
            "description": "Achieved exceptional accuracy in fraud detection using hybrid ML models",
            "impact": "Device Intelligence Solution"
        },
        {
            "icon": "📈",
            "title": "35% Revenue Impact",
            "description": "Combined revenue increase across projects at Bureau Inc.",
            "impact": "Multiple Client Onboarding"
        },
        {
            "icon": "🤖",
            "title": "97% Bot Detection",
            "description": "High accuracy in behavioral biometrics for bot detection",
            "impact": "ATO Fraud Prevention"
        },
        {
            "icon": "🎨",
            "title": "88% Pattern Matching",
            "description": "Visual pattern recognition in images with AI",
            "impact": "Computer Vision Innovation"
        }
    ]
    
    col1, col2 = st.columns(2)
    
    for i, achievement in enumerate(achievements):
        col = col1 if i % 2 == 0 else col2
        with col:
            st.markdown(f"""
            <div class="project-card" style="text-align: center;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">{achievement['icon']}</div>
                <h3 style="color: #4ecdc4; margin-bottom: 1rem;">{achievement['title']}</h3>
                <p style="color: white; font-size: 1.1rem; line-height: 1.6; margin-bottom: 1rem;">{achievement['description']}</p>
                <div style="background: rgba(255, 107, 107, 0.2); border-radius: 10px; padding: 0.8rem;">
                    <p style="color: #ff6b6b; font-weight: 600; margin: 0;">{achievement['impact']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif page == "Contact":
    st.markdown("<h1 style='text-align: center; color: white; margin-bottom: 2rem;'>📞 Let's Connect</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card" style="text-align: center;">
        <h2 style="color: #4ecdc4; margin-bottom: 2rem;">Ready to collaborate on your next AI project?</h2>
        <p style="color: white; font-size: 1.2rem; line-height: 1.8; margin-bottom: 2rem;">
            I'm always excited to discuss new opportunities, innovative projects, and ways to leverage AI/ML 
            for business growth. Whether you're looking for fraud detection solutions, generative AI applications, 
            or advanced analytics, let's talk!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact buttons
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0;">
            <a href="https://www.linkedin.com/in/shubham-mantri-13697b107" target="_blank" 
               style="background: linear-gradient(135deg, #0077b5 0%, #005885 100%); 
                      color: white; padding: 1rem 2rem; border-radius: 25px; 
                      text-decoration: none; display: inline-block; font-weight: 600;
                      transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(0,119,181,0.4);">
                💼 LinkedIn Profile
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0;">
            <a href="mailto:shubham.mantri@email.com" 
               style="background: linear-gradient(135deg, #4ecdc4 0%, #2980b9 100%); 
                      color: white; padding: 1rem 2rem; border-radius: 25px; 
                      text-decoration: none; display: inline-block; font-weight: 600;
                      transition: all 0.3s ease; box-shadow: 0 5px 15px rgba(78,205,196,0.4);">
                📧 Email Me
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    # What I can help with section
    st.markdown("""
    <div style="background: rgba(78, 205, 196, 0.1); border-radius: 15px; padding: 2rem; margin-top: 2rem;">
        <h3 style="color: #4ecdc4; margin-bottom: 1rem; text-align: center;">🚀 What I Can Help With:</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Create service cards
    col1, col2, col3, col4 = st.columns(4)
    
    services = [
        {"title": "🤖 Generative AI Solutions", "desc": "RAG systems, chatbots, content generation"},
        {"title": "🛡️ Fraud Detection", "desc": "ML-based fraud prevention systems"},
        {"title": "👁️ Computer Vision", "desc": "Image analysis, pattern recognition"},
        {"title": "📊 Predictive Analytics", "desc": "Business intelligence, forecasting"}
    ]
    
    for i, (col, service) in enumerate(zip([col1, col2, col3, col4], services)):
        with col:
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.05); padding: 1.5rem; border-radius: 15px; 
                        margin: 1rem 0; text-align: center; height: 150px; display: flex; 
                        flex-direction: column; justify-content: center;
                        transition: all 0.3s ease; border: 1px solid rgba(255,255,255,0.1);">
                <h4 style="color: #ff6b6b; margin-bottom: 0.8rem; font-size: 1rem;">{service['title']}</h4>
                <p style="color: white; font-size: 0.85rem; line-height: 1.4; margin: 0;">{service['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 2rem; background: rgba(0,0,0,0.2); border-radius: 15px;">
    <p style="color: #a0a0a0; font-size: 0.9rem;">
        ⚡ Built with Streamlit | 🚀 Designed for Impact | 💡 Powered by AI
    </p>
    <p style="color: #4ecdc4; font-weight: 600; margin-top: 1rem;">
        "Turning Data into Intelligent Solutions, One Algorithm at a Time"
    </p>
</div>
""", unsafe_allow_html=True)
