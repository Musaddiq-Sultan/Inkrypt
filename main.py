from stegano import lsb
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptocode import encrypt, decrypt

def hide_text():
    file_path = filepath_text.get().strip()
    original_text = secret_message.get("1.0", "end-1c")
    password = password_entry.get()
    
    text = encrypt(original_text, password)
    
    if not file_path:
        messagebox.showerror("Error", "Please select an image.")
        return
    if not text:
        messagebox.showerror("Error", "Please enter a secret message.")
        return
    
    try:
        image = Image.open(file_path).convert("RGB")
        secret = lsb.hide(image, text)
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Images", "*.png")],
            title="Save Image As"
        )
        secret.save(save_path)
        secret_message.delete("1.0", "end-1c")
        messagebox.showinfo("Success", "Message hidden successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to hide message: {e}")

def reveal_text():
    file_path = filepath_text.get().strip()
    password = password_entry.get()
    
    if not file_path:
        messagebox.showerror("Error", "Please select an image.")
        return
    
    try:
        original_revealed_text = lsb.reveal(file_path)
        revealed_text = decrypt(original_revealed_text, password)
        if revealed_text:
            secret_message.delete("1.0", tk.END)
            secret_message.insert("1.0", revealed_text)
        else:
            messagebox.showwarning("No Message", "No hidden message found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to reveal message: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("PNG Images", "*.png"), ("JPG Images", "*.jpg"), ("JPEG Images", "*.jpeg"), ("All Files", "*.*")]
    )
    if file_path:
        filepath_text.delete(0, tk.END)
        filepath_text.insert(0, file_path)

# GUI Setup
root = tk.Tk()
root.title("Inkrypt")
root.resizable(0,0)

main_frame = tk.Frame(root)
main_frame.pack(padx=5, pady=5)

filepath_frame = tk.LabelFrame(main_frame, text="Open File")
filepath_frame.pack(fill="x", pady=(0, 5))
filepath_frame.columnconfigure(0, weight=1)

filepath_text = tk.Entry(filepath_frame)
filepath_text.grid(row=0, column=0, padx=(0, 5), ipady=5 ,sticky="ew")

browse_button = tk.Button(filepath_frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=1)

secret_message_frame = tk.LabelFrame(main_frame, text="Secret Message")
secret_message_frame.pack(fill="x", pady=(0, 5))

secret_message = tk.Text(secret_message_frame)
secret_message.pack()

password_frame = tk.LabelFrame(main_frame, text="Password")
password_frame.pack(fill="x", pady=(0, 5))

password_entry = tk.Entry(password_frame)
password_entry.pack(expand=True, fill="x")

buttons_frame = tk.Frame(main_frame)
buttons_frame.pack(pady=(0, 5))

hide_button = tk.Button(buttons_frame, text="Encrypt", command=hide_text)
hide_button.grid(row=0, column=0, padx=(0, 5))

reveal_button = tk.Button(buttons_frame, text="Decrypt", command=reveal_text)
reveal_button.grid(row=0, column=1)

root.mainloop()
