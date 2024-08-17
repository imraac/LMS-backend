




import re
import json
from app import app, db
from models import Course, Question

def get_youtube_thumbnail_url(video_url):
    youtube_id_match = re.search(r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|v\/|embed\/|user\/\S+\/\S+\/|embed\/|\S+\/\S+\/|v\/)|youtu\.be\/|youtube\.com\/(?:playlist\?list=|embed\/|v\/|watch\?v=))([a-zA-Z0-9_-]{11})', video_url)
    if youtube_id_match:
        video_id = youtube_id_match.group(1)
        return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return None

def seed_database():
    with app.app_context():
        db.create_all()
        
        # Seed Courses
        courses = [
            {
                "title": "Introduction to Python",
                "description": "Learn the basics of Python programming, including syntax, data structures, and basic algorithms.",
                "video": "https://www.youtube.com/watch?v=rfscVS0vtbw",
                "tech_stack": "Python,Flask,SQLAlchemy",
                "what_you_will_learn": json.dumps([
                    "Understand Python syntax and semantics",
                    "Implement basic algorithms and data structures",
                    "Work with Flask to create web applications"
                ])
            },
            {
                "title": "Mastering JavaScript",
                "description": "Dive deep into JavaScript and learn how to build dynamic, responsive web applications.",
                "video": "https://www.youtube.com/watch?v=PkZNo7MFNFg",
                "tech_stack": "JavaScript,React,Node.js,Express",
                "what_you_will_learn": json.dumps([
                    "Advanced JavaScript concepts and ES6 features",
                    "Building single-page applications with React",
                    "Backend development with Node.js and Express"
                ])
            },
            {
                "title": "Full-Stack Web Development",
                "description": "A comprehensive course covering both front-end and back-end web development technologies.",
                "video": "https://www.youtube.com/watch?v=Q33KBiDriJY",
                "tech_stack": "HTML,CSS,JavaScript,Python,Django,PostgreSQL",
                "what_you_will_learn": json.dumps([
                    "Design and build full-stack web applications",
                    "Implement responsive design using HTML and CSS",
                    "Develop RESTful APIs with Django and PostgreSQL"
                ])
            },
            {
                "title": "Data Science with Python",
                "description": "Explore the world of data science using Python, including data analysis, visualization, and machine learning.",
                "video": "https://www.youtube.com/watch?v=ua-CiDNNj30",
                "tech_stack": "Python,Pandas,NumPy,Matplotlib,Scikit-learn",
                "what_you_will_learn": json.dumps([
                    "Data manipulation and analysis with Pandas",
                    "Data visualization with Matplotlib and Seaborn",
                    "Machine learning algorithms and model evaluation"
                ])
            },
            {
                "title": "Data Science with SQL and Python",
                "description": "Dive into data science and analytics with this comprehensive course on SQL and Python.",
                "video": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
                "tech_stack": "SQL,Python,Pandas",
                "what_you_will_learn": json.dumps([
                    "Writing complex SQL queries",
                    "Data manipulation and analysis with Python and Pandas",
                    "Building data pipelines and dashboards"
                ])
            },
            {
                "title": "Machine Learning Mastery",
                "description": "Explore the world of machine learning and build intelligent systems using Python.",
                "video": "https://www.youtube.com/watch?v=GwIo3gDZCVQ",
                "tech_stack": "Python,Scikit-Learn,TensorFlow",
                "what_you_will_learn": json.dumps([
                    "Understanding machine learning algorithms",
                    "Data preprocessing and model training",
                    "Building neural networks with TensorFlow"
                ])
            },
            {
                "title": "Full-Stack Web Development",
                "description": "Become a full-stack web developer with comprehensive training in front-end and back-end technologies.",
                "video": "https://www.youtube.com/watch?v=srvUrASNj0s",
                "tech_stack": "HTML,CSS,JavaScript,Node.js,MongoDB",
                "what_you_will_learn": json.dumps([
                    "Building responsive websites with HTML, CSS, and JavaScript",
                    "Server-side development with Node.js",
                    "Working with databases using MongoDB"
                ])
            },
            {
                "title": "Advanced React Development",
                "description": "Master the art of building modern, scalable web applications with React.",
                "video": "https://www.youtube.com/watch?v=N3AkSS5hXMA",
                "tech_stack": "React,Redux,Firebase",
                "what_you_will_learn": json.dumps([
                    "State management with Redux",
                    "Building real-time applications with Firebase",
                    "Optimizing React applications for performance"
                ])
            },
            {
                "title": "Mobile App Development with Flutter",
                "description": "Gain expertise in developing mobile applications with Flutter and Dart.",
                "video": "https://www.youtube.com/watch?v=x0uinJvhNxI",
                "tech_stack": "Flutter,Dart,Firebase",
                "what_you_will_learn": json.dumps([
                    "Building cross-platform mobile apps with Flutter",
                    "Managing state in Flutter applications",
                    "Integrating Firebase for backend services"
                ])
            }
        ]
        
        for course_data in courses:
            thumbnail_url = get_youtube_thumbnail_url(course_data["video"])
            if not thumbnail_url:
                thumbnail_url = "https://example.com/image/default_thumbnail.jpg"
            
            course = Course(
                title=course_data["title"],
                description=course_data["description"],
                image=thumbnail_url,
                video=course_data["video"],
                tech_stack=course_data["tech_stack"],
                what_you_will_learn=course_data["what_you_will_learn"]
            )
            db.session.add(course)
        
        # Seed Questions
        questions = [
            # HTML
            {
                "question_text": "What is the correct HTML element for inserting a line break?",
                "category": "html",
                "options": [
                    "<break>",
                    "<lb>",
                    "<br>",
                    "<line>"
                ],
                "correct_answer": "<br>"
            },
            {
                "question_text": "Which HTML tag is used to define an internal style sheet?",
                "category": "html",
                "options": [
                    "<style>",
                    "<script>",
                    "<link>",
                    "<css>"
                ],
                "correct_answer": "<style>"
            },
            # CSS
            {
                "question_text": "How do you change the font size of an element in CSS?",
                "category": "css",
                "options": [
                    "font-size: 16px;",
                    "text-size: 16px;",
                    "font: 16px;",
                    "size: 16px;"
                ],
                "correct_answer": "font-size: 16px;"
            },
            {
                "question_text": "Which CSS property controls the text color?",
                "category": "css",
                "options": [
                    "color",
                    "text-color",
                    "font-color",
                    "background-color"
                ],
                "correct_answer": "color"
            },
            # JavaScript
            {
                "question_text": "How do you declare a variable in JavaScript?",
                "category": "javascript",
                "options": [
                    "var myVar;",
                    "variable myVar;",
                    "declare myVar;",
                    "let myVar;"
                ],
                "correct_answer": "var myVar;"
            },
            {
                "question_text": "Which method is used to write text to the console in JavaScript?",
                "category": "javascript",
                "options": [
                    "console.write()",
                    "console.log()",
                    "log.console()",
                    "print.console()"
                ],
                "correct_answer": "console.log()"
            },
            # React
            {
                "question_text": "What method is used to update the state in a React component?",
                "category": "react",
                "options": [
                    "this.setState()",
                    "this.updateState()",
                    "this.modifyState()",
                    "this.changeState()"
                ],
                "correct_answer": "this.setState()"
            },
            {
                "question_text": "Which hook is used to handle side effects in a React functional component?",
                "category": "react",
                "options": [
                    "useState",
                    "useEffect",
                    "useContext",
                    "useReducer"
                ],
                "correct_answer": "useEffect"
            },
            # Redux
            {
                "question_text": "What is the purpose of Redux middleware?",
                "category": "redux",
                "options": [
                    "To handle async actions",
                    "To manage local component state",
                    "To update the store directly",
                    "To trigger actions"
                ],
                "correct_answer": "To handle async actions"
            },
            {
                "question_text": "Which function is used to create a Redux store?",
                "category": "redux",
                "options": [
                    "createStore()",
                    "configureStore()",
                    "initializeStore()",
                    "createReduxStore()"
                ],
                "correct_answer": "createStore()"
            }
        ]

        for question_data in questions:
            question = Question(
                question_text=question_data["question_text"],
                category=question_data["category"],
                options=json.dumps(question_data["options"]),
                correct_answer=question_data["correct_answer"]
            )
            db.session.add(question)
        
        db.session.commit()

if __name__ == "__main__":
    seed_database()
