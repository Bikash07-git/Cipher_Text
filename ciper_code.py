import customtkinter as ctk

# Set theme and color mode
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Caesar Cipher Functions
def encrypt_text():
    text = input_text.get("0.0", "end").strip().lower()
    shift = shift_entry.get()

    if not shift.isdigit():
        output_text.configure(state="normal")
        output_text.delete("0.0", "end")
        output_text.insert("0.0", "❌ Please enter a valid number for shift.")
        output_text.configure(state="disabled")
        return

    shift = int(shift)
    alphabets = [chr(i) for i in range(97, 123)]
    cipher = ""

    for char in text:
        if char in alphabets:
            idx = (alphabets.index(char) + shift) % 26
            cipher += alphabets[idx]
        else:
            cipher += char

    output_text.configure(state="normal")
    output_text.delete("0.0", "end")
    output_text.insert("0.0", cipher)
    output_text.configure(state="disabled")

def decrypt_text():
    text = input_text.get("0.0", "end").strip().lower()
    shift = shift_entry.get()

    if not shift.isdigit():
        output_text.configure(state="normal")
        output_text.delete("0.0", "end")
        output_text.insert("0.0", "❌ Please enter a valid number for shift.")
        output_text.configure(state="disabled")
        return

    shift = int(shift)
    alphabets = [chr(i) for i in range(97, 123)]
    plain = ""

    for char in text:
        if char in alphabets:
            idx = (alphabets.index(char) - shift) % 26
            plain += alphabets[idx]
        else:
            plain += char

    output_text.configure(state="normal")
    output_text.delete("0.0", "end")
    output_text.insert("0.0", plain)
    output_text.configure(state="disabled")

# App layout
app = ctk.CTk()
app.title("🔐 CipherText - Caesar Cipher")
app.geometry("500x500")

title = ctk.CTkLabel(app, text="CipherText - Caesar Cipher", font=("Arial", 20, "bold"))
title.pack(pady=10)

input_label = ctk.CTkLabel(app, text="🔤 Enter your message:")
input_label.pack(pady=5)

input_text = ctk.CTkTextbox(app, height=80)
input_text.pack(padx=20, pady=5)

shift_label = ctk.CTkLabel(app, text="🔑 Enter shift key (number):")
shift_label.pack(pady=5)

shift_entry = ctk.CTkEntry(app)
shift_entry.pack(pady=5)

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

encrypt_btn = ctk.CTkButton(button_frame, text="Encrypt", command=encrypt_text)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = ctk.CTkButton(button_frame, text="Decrypt", command=decrypt_text)
decrypt_btn.grid(row=0, column=1, padx=10)

output_label = ctk.CTkLabel(app, text="📄 Output:")
output_label.pack(pady=5)

output_text = ctk.CTkTextbox(app, height=80, state="disabled")
output_text.pack(padx=20, pady=5)

app.mainloop()
