import tkinter as tk
from tkinter import messagebox

class NotesApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("My Notes")
        self.window.geometry("500x400")
        
        #Title
        tk.Label(
            self.window, 
            text = "My Notes App",
            font = ("Arial", 16, "bold")
        ).pack(pady=10)
        
        #Title entry
        tk.Label(self.window, text="Note Title: ").pack()
        self.title_entry = tk.Entry(self.window, width=40)
        self.title_entry.pack(pady=5)
        
        #Note content
        tk.Label(self.window, text="Note Content: ").pack
        self.note_text = tk.Text(self.window, height=10, width=50)
        self.note_text.pack(pady=10)
        
        #Button
        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=10)
        
        tk.Button(
            btn_frame,
            text = "Save Note",
            command=self.save_note,
            bg="green",
            fg="white"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Clear",
            command=self.clear_form,
            bg="orange"
        ).pack(side=tk.LEFT, padx=5)
        
    def save_note(self):
        title = self.title_entry.get().strip()
        content = self.note_text.get("1.0", tk.END).strip()
        
        if not title:
            messagebox.showerror("Error", "Please enter a title")
            return
        
        if not content:
            messagebox.showerror("Error", "Please enter note content")
            return
        
        #Save to file
        with open(f"{title}.txt", "w") as file:
            file.write(content)
            
        messagebox.showinfo("Success", f"Note '{title}' saved!")
        self.clear_form()
        
    def clear_form(self):
        self.title.delete(0, tk.END)
        self.note_text.delete("1.0", tk.END)
        
    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    app = NotesApp()
    
    app.run()