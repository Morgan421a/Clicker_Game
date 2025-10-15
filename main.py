import tkinter as tk
from recordstats import load_stats, save_stats

root = tk.Tk()
root.title("Clicker Game")
root.attributes('-zoomed', True)
root.configure(background="light blue")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300")

# Load the full stats dict
stats = load_stats()
print("Loaded stats:", stats)

def score():
    stats["p_score"] += stats.get("value", 1)
    save_stats(stats)
    score_label.config(text=f"Score: {stats['p_score']}")
    print(stats["p_score"])

def strgerclicks():
    if stats["p_score"] >= 100:
        stats["p_score"] -= 100
        stats["value"] += 1
        save_stats(stats)
        print("Click power increased by 1")
        stronger_clicks.config(text=f"Stronger clicks : 100 points : {stats['value']}")
        score_label.config(text=f"Score: {stats['p_score']}")
    else:
        print("Not enough points!")

# GUI Elements
main_button = tk.Button(root, text="click me", command=score)
main_button.pack()

score_label = tk.Label(root, text=f"Score: {stats['p_score']}")
score_label.pack()

stronger_clicks = tk.Button(
    root,
    text=f"Stronger clicks : 100 points : {stats['value']}",
    command=strgerclicks
)
stronger_clicks.pack()

root.mainloop()
