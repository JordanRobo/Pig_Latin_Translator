import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font
import time

# Variable to define vowels
vowels = ('a', 'e', 'i', 'o', 'u')
punct = (',', '.', '!', '?', ':', ';')

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Pig Latin Generator")

    title_font = Font(family="Helvetica", size=20, weight="bold")
    paragraph_font = Font(family="Helvetica", size=12)
    button_font = Font(family="Helvetica", size=12, weight="bold")

    # Function for text conversion
    def convert_text():
        filename = filedialog.askopenfilename(
            title="Open Text File",
            filetypes=[("Text Files", "*.txt")]
        )
        if not filename:  # No file was selected
            return

        # If a file was selected Python will read the file contents
        with open(filename, 'r') as file:
            input_text = file.read()

        def process_word(word):
        # Check if the word ends with a punctuation mark
            if word[-1] in punct:
                # If it does, remove the punctuation and store it
                punctuation = word[-1]
                word = word[:-1]
            else:
                # If not, there's no punctuation to add later
                punctuation = ''

            # Process the word so that it follows the Pig Latin rules
            if word[0].lower() in vowels:
                processed_word = word + 'ay'
            else:
                processed_word = word[1:] + word[0] + 'ay'

            # Return the processed word with the punctuation added back (if any)
            return processed_word + punctuation
        

        words = input_text.split()
        p_latin = [process_word(word) for word in words]
        converted_text = ' '.join(p_latin)

        time.sleep(2) # Tells python to wait two seconds before saving the file
        # Ask where to save the converted file
        save_filename = filedialog.asksaveasfilename(
            title="Save Converted File",
            filetypes=[("Text Files", "*.txt")],
            defaultextension=".txt"
        )
        # Once it has read and converted the document it will write the new converted one
        if save_filename:
            with open(save_filename, 'w') as file:
                file.write(converted_text)

        
    # Configure the grid - set column weight
    root.grid_columnconfigure(0, weight=1)  # This makes the column expand

    # Configure the grid
    root.grid_columnconfigure(0, weight=1)
    for i in range(6):  # Creates 6 Rows
        root.grid_rowconfigure(i, weight=1)  # This makes the row expand

    # Application Heading
    title = tk.Label(root, text="Welcome to Pig Latin Text Converter", font=title_font, bg="#3B6869", fg="#ffffff")
    title.grid(row=1, column=0, sticky="NSEW")

    description_text = tk.Label(root, text="Using this program you are able to seamlessly convert a .txt document into Pig Latin.", wraplength=450, font=paragraph_font,bg="#3B6869", fg="#ffffff")
    description_text.grid(row=2, column=0, sticky="NSEW")

    instruction_text = tk.Label(root, text="To convert a document simply press the button below, select your document and save it to your PC.", wraplength=450, font=paragraph_font,bg="#3B6869", fg="#ffffff")
    instruction_text.grid(row=3, column=0, sticky="NSEW")

    # Convert button
    convert_button = tk.Button(root, text="Select File", command=convert_text, font=button_font)
    convert_button.grid(row=5, column=0, sticky="NSEW")
    convert_button.bind("<Enter>", lambda e: convert_button.config(bg='#e5f0f0', fg="#070d0d"))
    convert_button.bind("<Leave>", lambda e: convert_button.config(bg="#FFFFFF", fg="#3B6869"))

     # Set the main window size and background color
    root.geometry("600x350")
    root.configure(bg="#3B6869")

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()
