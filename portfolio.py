
import streamlit as st
from PIL import Image
import io
import base64
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Jameel Ahmad - AI/ML Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# File paths for defaults
DEFAULT_IMAGE_PATH = "mypic.png"
DEFAULT_RESUME_PATH = "resume.pdf"

# Initialize session state with default data
if 'profile_image' not in st.session_state:
    try:
        default_img = Image.open(DEFAULT_IMAGE_PATH)
        buffered = io.BytesIO()
        default_img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.session_state.profile_image = f"data:image/png;base64,{img_str}"
    except:
        st.session_state.profile_image = None
        
if 'resume_file' not in st.session_state:
    try:
        with open(DEFAULT_RESUME_PATH, 'rb') as f:
            st.session_state.resume_file = f.read()
            st.session_state.resume_name = "Jameel_Ahmad_CV.pdf"
    except:
        st.session_state.resume_file = None
        st.session_state.resume_name = None

# Custom CSS with full responsive design
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    /* Remove top padding/margin */
    .block-container {
        padding-top: 10px !important;
        padding-bottom: 1rem !important;
    }
    
    .main .block-container {
        padding-top: 10px !important;
        max-width: 100%;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    .stDecoration {display: none;}
    
    /* Floating animation */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Glow animation */
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 10px rgba(102, 126, 234, 0.5); }
        50% { text-shadow: 0 0 20px rgba(102, 126, 234, 0.8), 0 0 30px rgba(102, 126, 234, 0.6); }
    }
    
    /* Pulse animation */
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Slide in animation */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* AI Tagline Box */
    .ai-tagline {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
        border: 2px solid rgba(102, 126, 234, 0.4);
        border-radius: 20px;
        padding: 1.5rem 2rem;
        text-align: center;
        margin-top: 0;
        margin-bottom: 1rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        animation: pulse 3s ease-in-out infinite;
    }
    
    .ai-tagline h3 {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.8rem;
        font-weight: bold;
        margin: 0;
        animation: glow 2s ease-in-out infinite;
    }
    
    /* Profile Image */
    .profile-img {
        border-radius: 50%;
        border: 6px solid #667eea;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6);
        margin-bottom: 1rem;
        animation: float 3s ease-in-out infinite;
        transition: transform 0.3s ease;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 250px !important;
        height: 250px !important;
        object-fit: cover !important;
        object-position: center 15% !important;
    }

    .profile-img:hover {
        transform: scale(1.15) rotate(0deg);
        animation: none;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.9), 0 0 40px rgba(118, 75, 162, 0.6);
        border-color: #764ba2;
    }
    
    /* Section headers with animation */
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        animation: slideIn 0.6s ease-out;
    }
    
    /* Animated highlight text */
    .highlight-text {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        animation: glow 2s ease-in-out infinite;
    }
    
    /* Cards */
    .custom-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-left: 5px solid #667eea;
        padding: 1.8rem;
        border-radius: 15px;
        margin-bottom: 1.2rem;
        transition: all 0.4s ease;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
        height: 100%;
    }
    
    .custom-card:hover {
        transform: translateX(15px) scale(1.02);
        box-shadow: 0 10px 35px rgba(102, 126, 234, 0.5);
        border-left-color: #764ba2;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
    }
    
    /* Contact cards - equal height */
    .contact-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.12) 0%, rgba(118, 75, 162, 0.12) 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        border: 2px solid rgba(102, 126, 234, 0.3);
        transition: all 0.4s ease;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .contact-card:hover {
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
        border-color: #667eea;
    }
    
    /* Skill tags */
    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        margin: 0.4rem;
        font-size: 0.95rem;
        font-weight: 600;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    
    .skill-tag:hover {
        transform: translateY(-5px) scale(1.1);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Project cards */
    .project-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.12) 0%, rgba(118, 75, 162, 0.12) 100%);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        border: 2px solid rgba(102, 126, 234, 0.3);
        transition: all 0.4s ease;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    }
    
    .project-card:hover {
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
        border-color: #667eea;
    }
    
    /* Text colors */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #ffffff !important;
    }
    
    .stMarkdown p, .stMarkdown li {
        color: #e0e0e0 !important;
        line-height: 1.9;
    }
    
    /* Text inputs */
    .stTextInput input,
    .stTextArea textarea {
        background-color: rgba(30, 30, 50, 0.9) !important;
        color: #ffffff !important;
        border: 2px solid rgba(102, 126, 234, 0.5) !important;
        border-radius: 15px !important;
    }
    
    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 15px rgba(102, 126, 234, 0.5) !important;
        background-color: rgba(40, 40, 70, 0.9) !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.8rem 2.5rem !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100%;
        white-space: nowrap;
    }
    
    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.6) !important;
    }
    
    .stDownloadButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 0.8rem 2rem !important;
        font-weight: bold !important;
    }
    
    /* Navigation container */
    .nav-container {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        justify-content: center;
        margin-bottom: 1rem;
    }
    
    /* Responsive breakpoints */
    @media (max-width: 1200px) {
        .ai-tagline h3 {
            font-size: 1.5rem !important;
        }
        .section-header {
            font-size: 2.3rem !important;
        }
        .profile-img {
            width: 200px !important;
            height: 200px !important;
        }
    }
    
    @media (max-width: 992px) {
        .ai-tagline {
            padding: 1.2rem 1.5rem !important;
        }
        .ai-tagline h3 {
            font-size: 1.3rem !important;
        }
        .section-header {
            font-size: 2rem !important;
        }
        .profile-img {
            width: 180px !important;
            height: 180px !important;
        }
        .custom-card, .project-card {
            padding: 1.5rem !important;
        }
        .stButton > button {
            font-size: 0.9rem !important;
            padding: 0.7rem 1.5rem !important;
        }
    }
    
    @media (max-width: 768px) {
        .ai-tagline {
            padding: 1rem !important;
        }
        .ai-tagline h3 {
            font-size: 1.1rem !important;
        }
        .section-header {
            font-size: 1.8rem !important;
        }
        .profile-img {
            width: 150px !important;
            height: 150px !important;
        }
        .skill-tag {
            font-size: 0.85rem !important;
            padding: 0.5rem 1rem !important;
        }
        .custom-card, .project-card {
            padding: 1.2rem !important;
        }
        .contact-card {
            height: 160px !important;
            padding: 1.5rem !important;
        }
        .stButton > button {
            font-size: 0.85rem !important;
            padding: 0.6rem 1.2rem !important;
        }
    }
    
    @media (max-width: 576px) {
        .ai-tagline {
            padding: 0.8rem !important;
            margin-bottom: 1rem !important;
        }
        .ai-tagline h3 {
            font-size: 0.95rem !important;
        }
        .section-header {
            font-size: 1.5rem !important;
        }
        .profile-img {
            width: 120px !important;
            height: 120px !important;
        }
        .skill-tag {
            font-size: 0.75rem !important;
            padding: 0.4rem 0.8rem !important;
            margin: 0.3rem !important;
        }
        .custom-card, .project-card {
            padding: 1rem !important;
        }
        .contact-card {
            height: 150px !important;
            padding: 1.2rem !important;
        }
        .stButton > button {
            font-size: 0.75rem !important;
            padding: 0.5rem 1rem !important;
        }
        h1 {
            font-size: 1.8rem !important;
        }
        h3 {
            font-size: 1.1rem !important;
        }
        p {
            font-size: 0.95rem !important;
        }
    }
    
    @media (max-width: 400px) {
        .ai-tagline h3 {
            font-size: 0.85rem !important;
        }
        .section-header {
            font-size: 1.3rem !important;
        }
        .profile-img {
            width: 100px !important;
            height: 100px !important;
        }
        .stButton > button {
            font-size: 0.7rem !important;
            padding: 0.4rem 0.8rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# AI Catchy Tagline
st.markdown("""
<div class="ai-tagline">
    <h3>🤖 Transforming Ideas into Intelligent Solutions | Building Tomorrow's AI Today 🚀</h3>
</div>
""", unsafe_allow_html=True)

# Navigation
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        st.session_state.page = "Home"
        st.rerun()
with col2:
    if st.button("💼 Experience", use_container_width=True, key="nav_exp"):
        st.session_state.page = "Experience"
        st.rerun()
with col3:
    if st.button("🎯 Skills", use_container_width=True, key="nav_skills"):
        st.session_state.page = "Skills"
        st.rerun()
with col4:
    if st.button("🚀 Projects", use_container_width=True, key="nav_proj"):
        st.session_state.page = "Projects"
        st.rerun()
with col5:
    if st.button("🎓 Education", use_container_width=True, key="nav_edu"):
        st.session_state.page = "Education"
        st.rerun()
with col6:
    if st.button("📧 Contact", use_container_width=True, key="nav_contact"):
        st.session_state.page = "Contact"
        st.rerun()
with col7:
    if st.button("📄 CV", use_container_width=True, key="nav_cv"):
        st.session_state.page = "CV"
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")

if 'page' not in st.session_state:
    st.session_state.page = "Home"

page = st.session_state.page

# Pages
if page == "Home":
    if st.session_state.profile_image:
        st.markdown(f'<img src="{st.session_state.profile_image}" class="profile-img">', unsafe_allow_html=True)
    else:
        st.markdown('<img src="https://ui-avatars.com/api/?name=Jameel+Ahmad&size=250&background=667eea&color=fff&bold=true&font-size=0.4" class="profile-img">', unsafe_allow_html=True)
    
    st.markdown('<h1 style="color: white; margin: 0; text-align: center;">Jameel Ahmad</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #e0e0e0; margin: 0.5rem 0; text-align: center;"><span class="highlight-text">AI/ML Engineer</span> | <span class="highlight-text">NLP Specialist</span> | <span class="highlight-text">Educator</span></h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: #e0e0e0; text-align: center;">📍 Lahore, Pakistan | 💼 InvoZone</p>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-header">🧠 About Me</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="custom-card">
    <p style="font-size: 1.1rem; color: #e0e0e0; line-height: 1.8;">
    I am an <span class="highlight-text">AI/ML Engineer at InvoZone (Lahore)</span>, passionate about creating data-driven 
    and intelligent systems that solve real-world problems. With a <span class="highlight-text">Master's degree in Artificial 
    Intelligence (MS-AI)</span> from the <span class="highlight-text">University of Sialkot (USKT)</span>, I bring a strong 
    mix of technical expertise and hands-on experience in AI research, NLP, OCR, and ML model deployment.
    </p>
    <p style="font-size: 1.1rem; color: #e0e0e0; line-height: 1.8;">
    Alongside my engineering career, I also have <span class="highlight-text">10 years of teaching experience</span>, 
    mentoring students and professionals in programming, machine learning, and data science.
    </p>
    <p style="font-size: 1.1rem; color: #e0e0e0; line-height: 1.8;">
    I'm passionate about combining knowledge, research, and technology to build <span class="highlight-text">scalable, impactful AI products</span>.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-header">🌱 Currently Exploring</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="custom-card">
        <h4 style="color: #667eea;">🤖 LLM Fine-tuning</h4>
        <p>Fine-tuning and deploying Large Language Models for industry-specific applications</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="custom-card">
        <h4 style="color: #667eea;">🔍 OCR Enhancement</h4>
        <p>Enhancing OCR accuracy with hybrid Computer Vision + NLP pipelines</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="custom-card">
        <h4 style="color: #667eea;">🤝 AI Agents</h4>
        <p>Building AI agents using LangChain and vector-based reasoning systems</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="custom-card">
        <h4 style="color: #667eea;">☁️ Cloud Deployment</h4>
        <p>Cloud-based deployment using Docker and Streamlit Cloud</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Experience":
    st.markdown('<h2 class="section-header">💼 Professional Experience</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
    <h3 style="color: #667eea; margin-bottom: 0.5rem;">💼 AI/ML Engineer</h3>
    <h4 style="color: #a8a8a8; margin-bottom: 1rem;">InvoZone, Lahore | <span class="highlight-text">Current Position</span></h4>
    <ul style="color: #e0e0e0; line-height: 2;">
        <li>Designing and deploying <span class="highlight-text">AI solutions for NLP, OCR, and data automation</span></li>
        <li>Implementing <span class="highlight-text">LangChain and RAG pipelines</span> for LLM-powered applications</li>
        <li>Integrating AI models with APIs, vector databases, and cloud-hosted applications</li>
        <li>Collaborating with cross-functional teams to deliver <span class="highlight-text">production-grade ML pipelines</span></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
    <h3 style="color: #667eea; margin-bottom: 0.5rem;">👨‍🏫 Educator & Mentor</h3>
    <h4 style="color: #a8a8a8; margin-bottom: 1rem;"><span class="highlight-text">10 Years of Teaching Experience</span></h4>
    <ul style="color: #e0e0e0; line-height: 2;">
        <li>Taught and mentored students in <span class="highlight-text">Python, Machine Learning, and Artificial Intelligence</span></li>
        <li>Guided students on academic and real-world AI projects</li>
        <li>Focused on simplifying complex AI concepts through hands-on learning</li>
        <li>Empowered professionals to transition into <span class="highlight-text">AI and data science careers</span></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "Skills":
    st.markdown('<h2 class="section-header">🎯 Skills & Expertise</h2>', unsafe_allow_html=True)
    
    skills_data = {
        "Machine Learning & AI": ["Model Development", "Deep Learning", "Feature Engineering", "Hyperparameter Tuning", "Model Deployment", "Transfer Learning"],
        "Natural Language Processing": ["Custom NER (SpaCy)", "Sentiment Analysis", "Text Classification", "LangChain & RAG", "Transformers", "Embeddings"],
        "OCR & Computer Vision": ["Medical Invoice Extraction", "Image Preprocessing", "Text Recognition", "Document Analysis", "OpenCV"],
        "Data Analysis & Visualization": ["Excel (Advanced)", "Tableau", "Power BI", "Pandas", "Matplotlib", "Seaborn", "EDA", "Statistical Analysis"],
        "Application Development": ["Streamlit Apps", "FastAPI", "REST APIs", "Web Scraping", "HTML/CSS/JS"],
        "Databases": ["PostgreSQL", "MySQL", "SQL", "Vector Databases", "Graph Databases", "Database Design"],
        "Frameworks & Libraries": ["Scikit-learn", "TensorFlow", "PyTorch", "SpaCy", "Hugging Face", "NumPy"],
        "Development Tools": ["PyCharm", "VS Code", "Jupyter Notebook", "Docker", "Git/GitHub", "Linux"]
    }
    
    for category, skills in skills_data.items():
        st.markdown(f'### <span class="highlight-text">{category}</span>', unsafe_allow_html=True)
        skill_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
        st.markdown(f'<div style="margin-bottom: 2rem;">{skill_html}</div>', unsafe_allow_html=True)

elif page == "Projects":
    st.markdown('<h2 class="section-header">🚀 Featured Projects</h2>', unsafe_allow_html=True)
    
    projects = [
        {"title": "🏥 OCR for Medical Invoices", "desc": "AI-powered pipeline extracting structured data from scanned medical documents with high accuracy using deep learning and NLP post-processing.", "tech": ["Python", "OCR", "NLP", "Deep Learning"]},
        {"title": "🏷️ Custom NER Model using SpaCy", "desc": "Domain-specific Named Entity Recognition system improving data labeling accuracy and automation for specialized text analysis.", "tech": ["SpaCy", "NLP", "ML", "Python"]},
        {"title": "💬 AI Chatbot with LangChain & RAG", "desc": "Context-aware conversational AI powered by vector database retrieval and RAG architecture for intelligent responses.", "tech": ["LangChain", "Vector DB", "RAG", "LLM"]},
        {"title": "🕸️ Graph Database Visualizer", "desc": "Interactive Streamlit application for visualizing complex node-edge relationships with dynamic filtering and exploration.", "tech": ["Streamlit", "Graph DB", "Visualization"]},
        {"title": "📝 Automated MCQ Generator", "desc": "NLP-driven system converting educational content into multiple-choice questions with automatic distractor generation.", "tech": ["NLP", "Streamlit", "Python"]},
        {"title": "🌐 Web Scraping & Data Pipeline", "desc": "Custom scrapers collecting structured data from various sources and storing into PostgreSQL/MySQL with automated ETL processes.", "tech": ["BeautifulSoup", "Selenium", "PostgreSQL","MySql"]},
        {"title": "📊 EDA & ML Insights Projects", "desc": "End-to-end data cleaning, visualization, and analysis projects delivering actionable business insights using advanced analytics.", "tech": ["Pandas", "Matplotlib", "Seaborn", "Tableau"]}
    ]
    
    col1, col2 = st.columns(2)
    
    for idx, project in enumerate(projects):
        with col1 if idx % 2 == 0 else col2:
            tech_tags = "".join([f'<span class="skill-tag" style="font-size: 0.8rem; padding: 0.3rem 0.8rem;">{tech}</span>' for tech in project["tech"]])
            st.markdown(f'<div class="project-card"><h3 style="color: #667eea; margin-bottom: 0.5rem;">{project["title"]}</h3><p style="color: #e0e0e0; margin-bottom: 1rem;">{project["desc"]}</p><div>{tech_tags}</div></div>', unsafe_allow_html=True)

elif page == "Education":
    st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card" style="text-align: center; padding: 3rem;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">🎓</div>
        <h2 style="color: #667eea; margin-bottom: 0.5rem;">Master of Science in Artificial Intelligence</h2>
        <h3 class="highlight-text" style="margin-bottom: 1rem;">MS-AI</h3>
        <h4 style="color: #e0e0e0; margin-bottom: 0.5rem;">University of Sialkot (USKT)</h4>
        <p style="color: #a8a8a8;">Pakistan</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-header" style="margin-top: 3rem;">🏆 Certifications & Achievements</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
   
    with col1:
        st.markdown('<div class="custom-card"><h4 style="color: #667eea;">✅ <span class="highlight-text">10 Years Teaching Experience</span></h4><p>Mentored hundreds of students in AI, ML, and Data Science</p></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="custom-card"><h4 style="color: #667eea;">✅ <span class="highlight-text">Production AI Deployment</span></h4><p>Successfully deployed multiple AI solutions in production environments</p></div>', unsafe_allow_html=True)

elif page == "CV":
    st.markdown('<h2 class="section-header">📄 Curriculum Vitae</h2>', unsafe_allow_html=True)
    
    if st.session_state.resume_file:
        st.markdown("""
        <div class="custom-card">
            <h3 class="highlight-text" style="margin-bottom: 1rem;">📄 View & Download My CV</h3>
            <p style="color: #e0e0e0;">Feel free to view and download my curriculum vitae below.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Download Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📥 Download My CV",
                data=st.session_state.resume_file,
                file_name=st.session_state.resume_name or "Jameel_Ahmad_CV.pdf",
                mime="application/pdf" if st.session_state.resume_name.endswith('.pdf') else "application/msword",
                use_container_width=True,
                help="Click to download my CV"
            )
        
        st.markdown("---")
        
        # View Resume (only for PDFs)
        if st.session_state.resume_name and st.session_state.resume_name.endswith('.pdf'):
            st.markdown('### <span class="highlight-text">👁️ Preview CV</span>', unsafe_allow_html=True)
            base64_pdf = base64.b64encode(st.session_state.resume_file).decode('utf-8')
            st.markdown(f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" style="border-radius: 15px; border: 2px solid rgba(102, 126, 234, 0.3); box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);"></iframe>', unsafe_allow_html=True)
        else:
            st.info("📄 Preview is only available for PDF files. Please download to view the document.")
        
    else:
        st.markdown("""
        <div class="custom-card" style="text-align: center; padding: 3rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📄</div>
            <h3 class="highlight-text" style="margin-bottom: 1rem;">CV Not Available Yet</h3>
            <p style="color: #e0e0e0; font-size: 1.1rem; margin-bottom: 1rem;">
            My CV will be available here soon. Please check back later or contact me directly!
            </p>
            <a href="mailto:lifecolorjameel@gmail.com" style="color: #667eea; text-decoration: none; font-weight: bold;">
                📧 Email me for my CV →
            </a>
        </div>
        """, unsafe_allow_html=True)

else:  # Contact
    st.markdown('<h2 class="section-header">📧 Let\'s Connect</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="custom-card">
    <p style="font-size: 1.2rem; color: #e0e0e0; line-height: 1.8;">
    I'm always open to <span class="highlight-text">AI collaborations</span>, <span class="highlight-text">innovative projects</span>, 
    and <span class="highlight-text">research-driven ideas</span>.
    </p>
    <p style="font-size: 1.2rem; color: #e0e0e0; line-height: 1.8;">
    If you're working on something exciting or want to build intelligent systems — <span class="highlight-text">let's connect and make it real!</span>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h2 class="section-header" style="font-size: 2rem; margin-top: 2rem;">✉️ Send Me a Message</h2>', unsafe_allow_html=True)
    
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Your Name *", placeholder="Enter your full name")
            email = st.text_input("Your Email *", placeholder="your.email@example.com")
        
        with col2:
            phone = st.text_input("Phone Number", placeholder="+92 300 1234567")
            subject = st.text_input("Subject *", placeholder="What's this about?")
        
        message = st.text_area("Your Message *", placeholder="Tell me about your project or idea...", height=150)
        
        if st.form_submit_button("🚀 Send Message"):
            if name and email and subject and message:
                mailto = f"mailto:lifecolorjameel@gmail.com?subject={subject}&body=Name: {name}%0D%0AEmail: {email}%0D%0APhone: {phone}%0D%0A%0D%0A{message}"
                st.success("✅ Thank you! Opening your email client...")
                st.markdown(f'<meta http-equiv="refresh" content="0; url={mailto}">', unsafe_allow_html=True)
                st.info("If your email client didn't open, please email directly at: lifecolorjameel@gmail.com")
            else:
                st.error("⚠️ Please fill all required fields (*)")
    
    st.markdown("---")
    st.markdown('### <span class="highlight-text">📞 Contact Information</span>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="contact-card">
        <h4 style="color: #667eea; margin-bottom: 1rem;">📱 Phone Numbers</h4>
        <p style="color: #e0e0e0; margin-bottom: 0.5rem;"><strong>Primary:</strong> <a href="tel:03127139229" style="color: #667eea; text-decoration: none;">0312-7139229</a></p>
        <p style="color: #e0e0e0;"><strong>Secondary:</strong> <a href="tel:03086309698" style="color: #667eea; text-decoration: none;">0308-6309698</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="contact-card">
        <h4 style="color: #667eea; margin-bottom: 1rem;">📧 Email</h4>
        <p style="color: #e0e0e0;"><a href="mailto:lifecolorjameel@gmail.com" style="color: #667eea; text-decoration: none;">lifecolorjameel@gmail.com</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-card">
        <h4 style="color: #667eea; margin-bottom: 1rem;">💼 LinkedIn</h4>
        <p style="color: #e0e0e0;"><a href="https://www.linkedin.com/in/jameel-ahmad-923171248/" target="_blank" style="color: #667eea; text-decoration: none;">Connect on LinkedIn →</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="contact-card">
        <h4 style="color: #667eea; margin-bottom: 1rem;">📘 Facebook</h4>
        <p style="color: #e0e0e0;"><a href="https://web.facebook.com/jameel.ahmad.365612" target="_blank" style="color: #667eea; text-decoration: none;">Connect on Facebook →</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('### <span class="highlight-text">📍 Location</span>', unsafe_allow_html=True)
    st.markdown("""
    <div class="project-card" style="text-align: center;">
    <h3 style="color: #667eea;">📍 Lahore, Pakistan</h3>
    <p style="color: #e0e0e0;">Available for remote opportunities worldwide</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #a8a8a8; padding: 2rem;">
<p>© 2025 Jameel Ahmad. Built with passion for AI & Innovation.</p>
<p class="highlight-text" style="font-size: 1.1rem;">Let's build the future of AI together! 🚀</p>
</div>
""", unsafe_allow_html=True)