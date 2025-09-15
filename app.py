import streamlit as st

st.header("Welcome to my website")

# ---------- Base class ----------
class Select_subject_name:
    def C_programming(self):
        st.selectbox("Select C topic", [
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

    def Digital_Electronics(self):
        st.selectbox("Select Digital Electronics topic", [
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
        st.selectbox("Select Computer Organization topic", [
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
        st.selectbox("Select Data Structures topic", [
            "Introduction and Complexity",
            "Arrays and Linked Lists",
            "Stacks and Queues",
            "Trees (Binary, AVL, Heap)",
            "Graphs and Traversals",
            "Searching Techniques",
            "Sorting Techniques",
            "Hashing"
        ])

    def Cpp_Programming(self):
        st.selectbox("Select C++ topic", [
            "Object-Oriented Concepts",
            "Classes and Objects",
            "Constructors and Destructors",
            "Inheritance",
            "Polymorphism",
            "Operator Overloading",
            "File Handling",
            "Templates and Exception Handling"
        ])

    def Operating_System(self):
        st.selectbox("Select OS topic", [
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
        st.selectbox("Select DBMS topic", [
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
        st.selectbox("Select SE topic", [
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
        st.selectbox("Select Networking topic", [
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
        st.selectbox("Select Web Tech topic", [
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
        st.selectbox("Select Java topic", [
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
        st.selectbox("Select AI topic", [
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
        # ---------- Step 1: Select subject ----------
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
        ])


        # ---------- Step 3: Display topic selectbox based on chosen subject ----------
        if subject_name == "Programming in C":
            self.C_programming()
        elif subject_name == "Digital Electronics":
            self.Digital_Electronics()
        elif subject_name == "Computer Organization":
            self.Computer_Organization()
        elif subject_name == "Data Structures":
            self.Data_Structures()
        elif subject_name == "C++ Programming":
            self.Cpp_Programming()
        elif subject_name == "Operating System":
            self.Operating_System()
        elif subject_name == "Database Management System (DBMS)":
            self.DBMS()
        elif subject_name == "Software Engineering":
            self.Software_Engineering()
        elif subject_name == "Computer Networks":
            self.Computer_Networks()
        elif subject_name == "Web Technology":
            self.Web_Technology()
        elif subject_name == "Java Programming":
            self.Java_Programming()
        elif subject_name == "Artificial Intelligence":
            self.Artificial_Intelligence()
        # ---------- Step 2: Select explanation style & length ----------
        explanation_style = st.selectbox("Choose Explanation Style:", ["Simple", "Theory is code", "Code Heavy"])
        explanation_length = st.selectbox("Choose Explanation Length:", ["Short", "Medium", "Long"])
        
        


# --------- Run the app ---------
app = Subject_selection()
app.run()
