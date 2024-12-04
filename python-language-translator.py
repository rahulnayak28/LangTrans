from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

# Initialize the main window
root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.title("Language Translator")
root.config(bg='ghost white')

# Heading
Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='white smoke').pack()
Label(root, text="Deep Translator", font='arial 20 bold', bg='white smoke', width='20').pack(side='bottom')

# Input and Output Text Widgets
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=200, y=60)
Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)

Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=60)
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

# Language Selection
translator_instance = GoogleTranslator()  # Create an instance of GoogleTranslator
LANGUAGES = translator_instance.get_supported_languages()  # Get all supported languages
language_mapping = {lang.capitalize(): lang for lang in LANGUAGES}  # Create mapping for user-friendly names

src_lang = ttk.Combobox(root, values=list(language_mapping.keys()), width=22)
src_lang.place(x=20, y=60)
src_lang.set('English')  # Default input language

dest_lang = ttk.Combobox(root, values=list(language_mapping.keys()), width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('French')  # Default output language

# Define Translate Function
def Translate():
    try:
        src_language_code = language_mapping.get(src_lang.get())
        dest_language_code = language_mapping.get(dest_lang.get())
        
        if not src_language_code or not dest_language_code:
            raise ValueError("Please select valid input and output languages.")
        
        text_to_translate = Input_text.get(1.0, END).strip()
        if not text_to_translate:
            raise ValueError("Input text is empty.")
        
        translated_text = GoogleTranslator(source=src_language_code, target=dest_language_code).translate(text_to_translate)
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated_text)
    except Exception as e:
        Output_text.delete(1.0, END)
        Output_text.insert(END, f"Error: {str(e)}")

# Translate Button
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='royal blue1', activebackground='sky blue')
trans_btn.place(x=490, y=180)

# Run the application
root.mainloop()
