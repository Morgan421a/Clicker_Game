import tkinter as tk
from recordstats import load_stats, save_stats


root = tk.Tk() #creates parent window



root.title("Clicker Game")

root.attributes('-zoomed', True)
root.configure(background="light blue")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300")

stats = load_stats()
saved_score = stats.get("p_score", 0)
sc_owned = stats.get("sc_owned", 0)
value = stats["value"]
print("Score:", saved_score)

def score(current_score):
    current_score += value
    saved_score["p_score"] = current_score
    save_stats(saved_score)
    score_label.config(text=f"Score: {current_score}")
    print(current_score)
    return current_score

def strgerclicks(sc_owned):
    if saved_score >= 100:
        sc_owned + 1
        print("Click power increased by 1")
    else:
        print("Not enough points!")



main_button = tk.Button(root, text="click me", command=lambda: score(saved_score)) #Lambda, creates an anonymous function
main_button.pack()

score_label = tk.Label(root, text=f"Score: {saved_score}")
score_label.pack()

stronger_clicks = tk.Button(root, text=f"Stronger clicks : 100 points : {sc_owned}" , command=lambda: strgerclicks(sc_owned))
stronger_clicks.pack()

root.mainloop() #runs main event loop