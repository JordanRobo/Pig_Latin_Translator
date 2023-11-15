import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font
import time

# Variables to define vowels and punctuation
vowels = ('a', 'e', 'i', 'o', 'u')
punct = (',', '.', '!', '?', ':', ';')

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Pig Latin Translator")

    # Define fonts for various components
    title_font = Font(family="Helvetica", size=20, weight="bold")
    paragraph_font = Font(family="Helvetica", size=12)
    button_font = Font(family="Helvetica", size=12, weight="bold")

    # Function for text conversion
    def convert_text():
        filename = filedialog.askopenfilename(
            title="Open Text File",
            filetypes=[("Text Files", "*.txt")]
        )
        if not filename:  # Check if a file was selected
            return

        # Read the content of the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Process each line
        processed_lines = []
        for line in lines:
            words = line.split()
            processed_words = [process_word(word) for word in words]
            processed_line = ' '.join(processed_words)
            processed_lines.append(processed_line)

        converted_text = '\n'.join(processed_lines)

        time.sleep(2) # Wait for two seconds before proceeding

        # Ask where to save the converted file
        save_filename = filedialog.asksaveasfilename(
            title="Save Converted File",
            filetypes=[("Text Files", "*.txt")],
            defaultextension=".txt"
        )
        if save_filename:
            with open(save_filename, 'w') as file:
                file.write(converted_text)

    # Function to process each word into Pig Latin
    def process_word(word):
        # Handling punctuation and capitalization
        original_punctuation = ''
        if word[-1] in punct:
            original_punctuation = word[-1]
            word = word[:-1]
        is_capitalized = word[0].isupper()
        word = word.lower()

        # Finding the first vowel and processing the word
        first_vowel_index = next((i for i, char in enumerate(word) if char in vowels), None)
        if first_vowel_index is None:
            processed_word = word  # No vowel found
        elif first_vowel_index == 0:
            processed_word = word + 'way'
        else:
            processed_word = word[first_vowel_index:] + word[:first_vowel_index] + 'ay'

        # Reapplying capitalization
        if is_capitalized:
            processed_word = processed_word.capitalize()

        return processed_word + original_punctuation

    # GUI layout configuration
    root.grid_columnconfigure(0, weight=1)
    for i in range(6):  # Configuring rows
        root.grid_rowconfigure(i, weight=1)

    # GUI components
    title = tk.Label(root, text="Welcome to the Pig Latin Translator", font=title_font, bg="#3B6869", fg="#ffffff")
    title.grid(row=1, column=0, sticky="NSEW")
    
    description_text = tk.Label(root, text="Using this program you are able to seamlessly convert a .txt document into Pig Latin.", wraplength=450, font=paragraph_font, bg="#3B6869", fg="#ffffff")
    description_text.grid(row=2, column=0, sticky="NSEW")

    instruction_text = tk.Label(root, text="To convert a document simply press the button below, select your document to be translated and save it to your PC.", wraplength=450, font=paragraph_font, bg="#3B6869", fg="#ffffff")
    instruction_text.grid(row=3, column=0, sticky="NSEW")

    convert_button = tk.Button(root, text="Select File", command=convert_text, font=button_font)
    convert_button.grid(row=5, column=0, sticky="NSEW")
    convert_button.bind("<Enter>", lambda e: convert_button.config(bg='#e5f0f0', fg="#070d0d"))
    convert_button.bind("<Leave>", lambda e: convert_button.config(bg="#FFFFFF", fg="#3B6869"))

    # Setting main window size and background color
    root.geometry("600x350")
    root.configure(bg="#3B6869")

    # Starting the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
