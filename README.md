# 🧠 Python Quiz Game (GUI)

A professional **Quiz Game built with Python and Tkinter** featuring a clean graphical interface, countdown timer, randomized questions, score tracking, and automatic JSON question management.

This application runs entirely with the Python standard library — no external packages required.

---

## ✨ Features

✅ Graphical user interface  
✅ Large readable question display  
✅ Four clearly visible answer buttons  
✅ Countdown timer for each question  
✅ Automatic move when time expires  
✅ Correct answer highlighted in green  
✅ Wrong answer highlighted in red  
✅ Randomized question order every run  
✅ Live score display  
✅ Progress indicator (Question X / Total)  
✅ Final results screen with percentage  
✅ Restart quiz without closing the program  
✅ Auto-creates JSON question file if missing  
✅ Handles invalid or broken JSON safely  

---

## 🖥️ Requirements

- Python 3.x installed  
- No external libraries needed  

Tkinter comes bundled with standard Python installations.

---

## 📂 Project Structure

quiz-game/
│
├── quiz_game.py  
├── questions.json   (auto-generated if missing)  
└── README.md  

---

## ▶️ How To Run

1. Download or clone the project  

2. Open terminal in the project folder  

3. Run:

python quiz_game.py

---

## 📝 Question File Format

The program loads questions from:

questions.json

If the file does not exist, it is automatically created with example questions.

Each question follows this format:

{
  "question": "Your question here",
  "choices": ["A", "B", "C", "D"],
  "answer": "Correct choice text"
}

---

## 🎮 How To Play

1. Launch the program  
2. Read the question carefully  
3. Click one of the four answer buttons  
4. Watch the timer — unanswered questions count as wrong  
5. See your final score at the end  
6. Click **Restart Quiz** to play again  

---

## 📊 Scoring System

- Correct answers counted  
- Wrong answers counted  
- Final percentage calculated automatically  

---

## 🛡️ Error Handling

The program safely handles:

- Missing question file  
- Corrupted JSON data  
- Empty question lists  
- Invalid formats  

---

## 👨‍💻 Developer

Created by **Ayush Prabhakar**  
GitHub: https://github.com/ayushprabhakar38  

---

## 🛠️ Support

For support, feature requests, or bug reports:

- 📧 Email: ayushprabhakar38@gmail.com  
- 🐙 GitHub: https://github.com/ayushprabhakar38  
- 🌐 Website: https://ayushprabhakharpy.vercel.app/  

---

## 📜 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

## 🧾 Version History

### v1.0.0
- Initial release  
