# Disease-checker

🩺 Intelligent Disease Symptoms Checker (IDSC)
Welcome to the Intelligent Disease Symptoms Checker (IDSC)  a simple, offline tool made with Python that helps you check your symptoms and see what illness you might be dealing with. Whether you're feeling unwell or just curious, IDSC is here to guide you with basic health insights, especially in places where seeing a doctor right away isn’t always easy.

📖 What's Inside?
•	✨ What is IDSC?
•	🧰 What Can It Do?
•	🦠 Which Illnesses Can It Check?
•	⚙️ How It Works
•	📦 How to Set It Up
•	💡 Example Use
•	🔒 A Friendly Warning
•	🤝 Want to Help?
•	🙏 Thanks & Credits

✨ What is IDSC?
IDSC is a Python command-line application that gives you a first-level health checkup. You choose your symptoms from a list, and it tells you how closely they match a known disease like malaria, COVID-19, or pneumonia.
It won’t replace a doctor, but it can give you a heads-up on whether you should just rest or go see a healthcare professional.

🧰 What Can It Do?
Here’s what makes IDSC useful:
✅ Symptom selection made easy — Pick symptoms by number
🧠 Smart matching — Tells you how likely your symptoms match a disease
📊 Simple results — You’ll see either Positive (if symptoms match well) or Negative
💻 Works offline — No internet? No problem. It runs right from your computer
🧍‍♂️ Personalized output — Adds your name, age, and results into a mini-report

🦠 Which Illnesses Can It Check?
IDSC currently checks for:
1.	Diarrhea
2.	Malaria
3.	COVID-19
4.	Dengue
5.	Chikungunya
6.	Typhoid
7.	Influenza (Flu)
8.	Chickenpox
9.	Pneumonia
Each one has its own list of symptoms. Just pick the ones you're feeling and let IDSC do the rest.

⚙️ How It Works
Here’s the basic flow:
1.	You’ll be asked to enter your name and age
2.	Choose the disease you want to check
3.	Select symptoms from a numbered list (just type the numbers)
4.	The app calculates how many of your symptoms match
5.	If you match 60% or more of the listed symptoms → Positive
6.	Otherwise → Negative

📦 How to Set It Up
🐍 You’ll need Python 3 installed. 

💡 Example Use
$ python disease_checker.py

Enter Patient Name:
Amina Bello

Enter Patient Age:
22

1. Diarrhea
2. Malaria
3. COVID-19
...
Enter a disease number:
2

1. Chills
2. Headache
3. Vomiting
...
Enter any symptoms:
1
2
4
9

Test Result:
Patient name: Amina Bello  
Patient age: 22  
Disease name: Malaria  
Status: Positive ✅

 A Friendly Warning
This tool gives basic suggestions, not medical advice.
If you feel seriously unwell, or your symptoms are getting worse, please see a healthcare professional. This is a guide, not a doctor on your computer.

🤝 Want to Help?
Contributions are welcome! You can:
•	Improve the code
•	Add new diseases or symptoms
•	Make a graphical (GUI) version
•	Translate it for other languages
To contribute:
1.	Fork the project
2.	Make your changes
3.	Open a pull request
4.	Let’s build it better, together 


Thanks & Credits
Big thanks to:
•	Developers who believe in open health tools
•	Communities with limited healthcare access — this project is for you
•	Tools like Symptomate and Ada Health for inspiration


