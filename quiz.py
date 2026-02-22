# Code logic By Ayush Prabhakhar

import tkinter as tk
import json, os, random

FILE="quiz_questions.json"
TIME_PER_Q=15

def ensure_file():
    if not os.path.exists(FILE):
        data=[
            {"question":"What is the capital of France?","choices":["Berlin","Madrid","Paris","Rome"],"answer":2},
            {"question":"Which planet is known as the Red Planet?","choices":["Earth","Mars","Jupiter","Venus"],"answer":1},
            {"question":"2 + 2 * 2 = ?","choices":["6","8","4","10"],"answer":0},
            {"question":"Largest ocean on Earth?","choices":["Atlantic","Indian","Arctic","Pacific"],"answer":3},
            {"question":"Who wrote Hamlet?","choices":["Shakespeare","Tolstoy","Hemingway","Dickens"],"answer":0},
            {"question":"Fastest land animal?","choices":["Lion","Tiger","Cheetah","Leopard"],"answer":2},
            {"question":"Primary gas in Earth's atmosphere?","choices":["Oxygen","Nitrogen","CO2","Hydrogen"],"answer":1},
            {"question":"Which language is used for web styling?","choices":["HTML","Python","CSS","C++"],"answer":2}
        ]
        try:
            with open(FILE,"w",encoding="utf-8") as f: json.dump(data,f,indent=2)
        except: pass

def load_questions():
    try:
        with open(FILE,"r",encoding="utf-8") as f:
            q=json.load(f)
            valid=[]
            for i in q:
                if isinstance(i,dict) and "question" in i and "choices" in i and "answer" in i and len(i["choices"])==4:
                    valid.append(i)
            if valid: return valid
    except: pass
    return []

def start_quiz():
    global questions,index,correct,wrong,after_id,time_left
    for w in end_frame.winfo_children(): w.destroy()
    end_frame.pack_forget()
    quiz_frame.pack(fill="both",expand=True)
    questions=load_questions()
    random.shuffle(questions)
    index=0
    correct=0
    wrong=0
    load_q()

def load_q():
    global time_left,after_id
    if index>=len(questions):
        show_result()
        return
    q=questions[index]
    q_label.config(text=q["question"])
    for i,b in enumerate(btns):
        b.config(text=f"{chr(65+i)}.  {q['choices'][i]}",bg="#f0f0f0",fg="black",state="normal")
    prog.config(text=f"{index+1} / {len(questions)}")
    score_lbl.config(text=f"Score: {correct}")
    time_left=TIME_PER_Q
    update_timer()

def update_timer():
    global time_left,after_id
    timer_lbl.config(text=f"Time: {time_left}s")
    if time_left<=0:
        auto_wrong()
        return
    time_left-=1
    after_id=root.after(1000,update_timer)

def auto_wrong():
    global wrong
    wrong+=1
    show_correct(None)

def answer(i):
    show_correct(i)

def show_correct(chosen):
    global index,correct,wrong,after_id
    try: root.after_cancel(after_id)
    except: pass
    q=questions[index]
    for b in btns: b.config(state="disabled")
    right=q["answer"]
    for i,b in enumerate(btns):
        if i==right: b.config(bg="#28a745",fg="white")
    if chosen is not None:
        if chosen==right:
            correct+=1
        else:
            wrong+=1
            btns[chosen].config(bg="#dc3545",fg="white")
    root.after(1100,next_q)

def next_q():
    global index
    index+=1
    load_q()

def show_result():
    quiz_frame.pack_forget()
    end_frame.pack(fill="both",expand=True)
    total=correct+wrong
    pct=int((correct/total)*100) if total else 0
    tk.Label(end_frame,text="Quiz Finished",font=("Arial",24,"bold")).pack(pady=20)
    tk.Label(end_frame,text=f"Correct Answers: {correct}",font=("Arial",14)).pack(pady=3)
    tk.Label(end_frame,text=f"Wrong Answers: {wrong}",font=("Arial",14)).pack(pady=3)
    tk.Label(end_frame,text=f"Percentage Score: {pct}%",font=("Arial",16,"bold")).pack(pady=10)
    tk.Button(end_frame,text="Restart Quiz",command=start_quiz,font=("Arial",12),width=18,height=2).pack(pady=10)

ensure_file()

root=tk.Tk()
root.title("Quiz Game By Ayush Prabhakhar")
root.geometry("650x520")

quiz_frame=tk.Frame(root,padx=20,pady=20)
quiz_frame.pack(fill="both",expand=True)

top=tk.Frame(quiz_frame)
top.pack(fill="x")
score_lbl=tk.Label(top,text="Score: 0",font=("Arial",11,"bold"))
score_lbl.pack(side="left")
prog=tk.Label(top,text="0/0",font=("Arial",11))
prog.pack(side="right")

timer_lbl=tk.Label(quiz_frame,text="Time",font=("Arial",12,"bold"))
timer_lbl.pack(anchor="e",pady=(5,0))

q_label=tk.Label(quiz_frame,text="",wraplength=600,font=("Arial",18,"bold"),justify="left")
q_label.pack(pady=20,anchor="w")

btns=[]
for i in range(4):
    b=tk.Button(
        quiz_frame,
        text="",
        height=2,
        anchor="w",
        padx=15,
        font=("Arial",13),
        relief="raised",
        bd=2,
        command=lambda i=i:answer(i)
    )
    b.pack(fill="x",pady=6,ipady=6)
    btns.append(b)

end_frame=tk.Frame(root,padx=20,pady=20)

questions=[]
start_quiz()

root.mainloop()