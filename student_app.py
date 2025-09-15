import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Loading the environment variables to the program
load_dotenv()

# Initializing the model 
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

st.header("AI Tutor for Computer Science & Engineering Subjects 📔📚")

# the root class for selecting the topic of the subject
class Select_subject_name:
    def C_programming(self):
        return st.selectbox("Select C topic", [
            "Introduction to C programming",
            "Keywords and Identifiers",
            "Data Types",
            "Operators and Expressions",
            "Input and Output",
            "Control Structures",
            "Arrays",
            "Pointers",
            "Functions",
            "Storage Classes",
            "Structures and Unions",
            "Dynamic Memory Allocation",
            "File Handling",
            "Preprocessor Directives",
            "Error Handling and Debugging"
        ])
    def machine_learning(self):
        return st.selectbox("Select Machine Learning Topic",[
            'Introduction to Machine Leaning',
            'Types of Machine Leanring',
            'Supervised Learning',
            'Unsupervised Learning',
            'Reinforcement Learning',
            'Ensemble Learning',
            'Hyper-parameter Tuning',
    # ---------- Supervised Learning ----------
            "Linear Regression",
            "Ridge Regression",
            "Lasso Regression",
            "Polynomial Regression",
            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "Gradient Boosting",
            "AdaBoost",
            "XGBoost",
            "LightGBM",
            "K-Nearest Neighbors (KNN)",
            "Support Vector Machine (SVM)",
            "Naive Bayes (Gaussian, Multinomial, Bernoulli)",
            "Extra Trees Classifier/Regressor",
            
            # ---------- Unsupervised Learning ----------
            "K-Means Clustering",
            "Hierarchical Clustering (Agglomerative, Divisive)",
            "DBSCAN",
            "Principal Component Analysis (PCA)",
            "Independent Component Analysis (ICA)",
            "t-SNE",
            # ---------- Reinforcement Learning ----------
            "Q-Learning",
            # ---------- Ensemble Methods ----------
            "Bagging",
            "Boosting",
            "Stacking",
            "Voting Classifier"
    ]
    )
        
    def Cpp_Programming(self):
        return st.selectbox("Select C++ topic", [
            "Object-Oriented Concepts",
            "Classes and Objects",
            "Constructors and Destructors",
            "Inheritance",
            "Polymorphism",
            "Operator Overloading",
            "File Handling",
            "Templates and Exception Handling"
        ])
        
    def Digital_Electronics(self):
        return st.selectbox("Select Digital Electronics topic", [
            "Number Systems and Codes",
            "Boolean Algebra",
            "Logic Gates",
            "Combinational Circuits",
            "Sequential Circuits",
            "Flip-Flops",
            "Registers and Counters",
            "Memory Devices"
        ])

    def Computer_Organization(self):
        return st.selectbox("Select Computer Organization topic", [
            "Basic Structure of Computers",
            "Machine Instructions and Programs",
            "Basic Processing Unit",
            "Microprogrammed Control",
            "Memory System",
            "Cache and Virtual Memory",
            "Input / Output Organization",
            "Pipelining and RISC/CISC"
        ])

    def Data_Structures(self):
        return st.selectbox("Select Data Structures topic", [
            "Introduction and Complexity",
            "Arrays and Linked Lists",
            "Stacks and Queues",
            "Trees (Binary, AVL, Heap)",
            "Graphs and Traversals",
            "Searching Techniques",
            "Sorting Techniques",
            "Hashing"
        ])

    def Operating_System(self):
        return st.selectbox("Select OS topic", [
            "Introduction to Operating Systems",
            "System Structures",
            "Process Management",
            "CPU Scheduling",
            "Deadlocks",
            "Memory Management",
            "Virtual Memory",
            "File Systems",
            "I/O Systems"
        ])

    def DBMS(self):
        return st.selectbox("Select DBMS topic", [
            "Introduction to DBMS",
            "Data Models and ER Model",
            "Relational Model",
            "SQL Queries",
            "Normalization",
            "Transaction Management",
            "Concurrency Control",
            "Recovery System",
            "Database Security"
        ])

    def Software_Engineering(self):
        return st.selectbox("Select SE topic", [
            "Software Development Life Cycle",
            "Process Models (Waterfall, Agile, Spiral)",
            "Requirement Analysis",
            "Software Design",
            "Coding and Testing",
            "Software Project Management",
            "Risk Management",
            "Software Maintenance"
        ])

    def Computer_Networks(self):
        return st.selectbox("Select Networking topic", [
            "Introduction to Data Communication",
            "OSI Model and TCP/IP",
            "Transmission Media",
            "Switching Techniques",
            "Error Detection and Correction",
            "Data Link Protocols",
            "IP Addressing and Routing",
            "Transport Layer Protocols",
            "Application Layer (HTTP, FTP, DNS)"
        ])

    def Web_Technology(self):
        return st.selectbox("Select Web Tech topic", [
            "HTML Basics",
            "CSS Styling",
            "JavaScript Fundamentals",
            "DOM Manipulation",
            "Forms and Validations",
            "PHP Basics",
            "Database Connectivity with PHP",
            "Web Security Basics"
        ])

    def Java_Programming(self):
        return st.selectbox("Select Java topic", [
            "Introduction to Java",
            "Classes and Objects",
            "Constructors and Inheritance",
            "Polymorphism",
            "Interfaces and Packages",
            "Exception Handling",
            "Multithreading",
            "File Handling",
            "Networking",
            "JDBC"
        ])

    def Artificial_Intelligence(self):
        return st.selectbox("Select AI topic", [
            "Introduction to AI",
            "Search Techniques",
            "Knowledge Representation",
            "Reasoning and Inference",
            "Expert Systems",
            "Natural Language Processing",
            "Machine Learning Basics",
            "AI Applications"
        ])

# ---------- Inherited class ----------
class Subject_selection(Select_subject_name):
    def run(self):
        subject_name = st.selectbox("Select your subject name", [
            "Programming in C",
            "Digital Electronics",
            "Computer Organization",
            "Data Structures",
            "C++ Programming",
            "Operating System",
            "Database Management System (DBMS)",
            "Software Engineering",
            "Computer Networks",
            "Web Technology",
            "Java Programming",
            "Artificial Intelligence",
            "Machine Learning"
        ])

        # Map subjects to methods
        topic_name = None
        if subject_name == "Programming in C":
            topic_name = self.C_programming()
        elif subject_name == "Digital Electronics":
            topic_name = self.Digital_Electronics()
        elif subject_name == "Computer Organization":
            topic_name = self.Computer_Organization()
        elif subject_name == "Data Structures":
            topic_name = self.Data_Structures()
        elif subject_name == "C++ Programming":
            topic_name = self.Cpp_Programming()
        elif subject_name == "Operating System":
            topic_name = self.Operating_System()
        elif subject_name == "Database Management System (DBMS)":
            topic_name = self.DBMS()
        elif subject_name == "Software Engineering":
            topic_name = self.Software_Engineering()
        elif subject_name == "Computer Networks":
            topic_name = self.Computer_Networks()
        elif subject_name == "Web Technology":
            topic_name = self.Web_Technology()
        elif subject_name == "Java Programming":
            topic_name = self.Java_Programming()
        elif subject_name == "Artificial Intelligence":
            topic_name = self.Artificial_Intelligence()
        elif subject_name == "Machine Learning":
            topic_name = self.machine_learning()


        # Explanation style & length
        explanation_style = st.selectbox("Choose Explanation Style:", ["Simple","Theory", "Theory with Code", "Code Heavy"])
        explanation_length = st.selectbox("Choose Explanation Length:", ["Short", "Medium", "Long"])

        # Generate AI explanation
        if topic_name and st.button("Generate Explanation"):
            template_string = """
            Explain the topic '{topic}' from subject '{subject}' with the following style and length:
            Explanation Style: {style}
            Explanation Length: {length}
            Include relevant formulas, examples, and code snippets if needed.
            """
            prompt_template = PromptTemplate(
                input_variables=["subject", "topic", "style", "length"],
                template=template_string
            )

            final_prompt = prompt_template.invoke({
                "subject": subject_name,
                "topic": topic_name,
                "style": explanation_style,
                "length": explanation_length
            })

            with st.spinner("Generating explanation..."):
                result = model.invoke(final_prompt)

            st.write(result.content)

# --------- Run the app ---------
app = Subject_selection()
app.run()
