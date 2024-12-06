import tkinter as tk
from tkinter import messagebox
from io import StringIO
import sys
from experta import *
from difflib import get_close_matches
from Mental_Health_ES_Knowledge_Base import MentalHealthExpertSystem, MOOD_SYNONYMS, PREFERENCE_SYNONYMS

# Unified font settings
APP_FONT = ("Helvetica", 12)

# Function to validate user input with close matching
def validate_input(user_input, valid_options, category):
    # Select the synonym mapping based on category
    synonym_map = MOOD_SYNONYMS if category == "mood" else PREFERENCE_SYNONYMS

    # Split input into words for keyword matching
    words = user_input.lower().split()
    for word in words:
        # Check if the word matches directly
        if word in valid_options:
            return word
        
        # Check if the word matches a synonym
        for key, synonyms in synonym_map.items():
            if word in synonyms:
                return key

        # Use close matches as a fallback
        close_matches = get_close_matches(word, valid_options)
        if close_matches:
            suggestion = close_matches[0]
            confirm = messagebox.askyesno("Confirm", f"Did you mean '{suggestion}' for your {category}?")
            if confirm:
                return suggestion
    
    # If no match is found, return None
    return None

# Function to display expert system suggestions
def display_suggestions(engine):
    # Redirect stdout to capture expert system output
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        engine.run()
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Here are some suggestions based on your mood and preference:\n\n", "header")
    
     # Add mood and preference info to the output
    mood = user_inputs.get('mood', 'Unknown')
    preference = user_inputs.get('preference', None)

    # Display mood, ensuring it always has a value to capitalize
    output_text.insert(tk.END, f"Your mood: {mood.capitalize()}\n", "details")
    if preference:
        output_text.insert(tk.END, f"Your preference: {preference.capitalize()}\n\n", "details")
    else:
        output_text.insert(tk.END, "Your preference: Not provided (general preferences will be suggested)\n\n", "details")
    
    # Add expert system output with explanations
    for line in output.strip().split("\n"):
        # Assuming the expert system provides suggestions with additional text on why or how they are confident
        output_text.insert(tk.END, f"{line}\n", "suggestion")

# Function to handle the mood submission
def on_mood_submit():
    mood = mood_var.get()
    valid_moods = list(MOOD_SYNONYMS.keys())
    validated_mood = validate_input(mood, valid_moods, "mood")

    if not validated_mood:
        messagebox.showerror("Invalid Input", "Please enter a valid mood.")
        return
    user_inputs['mood'] = validated_mood
    messagebox.showinfo("Mood Accepted", f"Your mood '{validated_mood}' has been accepted. Now, enter your preference (optional).")

# Function to handle the preference submission and trigger the expert system
def on_preference_submit():
    if 'mood' not in user_inputs or not user_inputs['mood']:
        messagebox.showwarning("Missing Mood", "Please enter and submit your mood first.")
        return
    
    preference = preference_var.get()
    valid_preferences = list(PREFERENCE_SYNONYMS.keys())
    validated_preference = validate_input(preference, valid_preferences, "preference")

    if not validated_preference:
        user_inputs['preference'] = None
        messagebox.showinfo("Preference Not Found", "No close match found. General suggestions will be provided.")
    else:
        user_inputs['preference'] = validated_preference

     # Initialize and run the expert system    
    engine = MentalHealthExpertSystem()
    engine.reset()
    engine.declare(Fact(mood=user_inputs['mood']))

    if user_inputs['preference']:
        engine.declare(Fact(preference=user_inputs['preference']))
    display_suggestions(engine)

# Function to reset inputs and clear the output
def reset_inputs():
    mood_var.set("")
    preference_var.set("")
    user_inputs.clear()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Suggestions will appear here...\n", "header")
    messagebox.showinfo("Reset", "All inputs have been reset.")

def show_frame(frame_to_show, frame_to_hide):
    frame_to_hide.pack_forget()
    frame_to_show.pack(fill="both", expand=True)

# Set up the Tkinter UI window
root = tk.Tk()
root.title("Mood-Based Recommendation Expert System")
root.configure(bg="#f9f9f9")

root.attributes('-zoomed', True)  # For Linux and some systems

# Store user inputs globally
user_inputs = {}

# Welcome page
welcome_frame = tk.Frame(root, bg="#f9f9f9")
tk.Label(welcome_frame, text="\n\n\n\n\n\n\n\nWelcome to the \nMood-Based Recommendation Expert System!", font=("Helvetica", 22, "bold"), bg="#f9f9f9", fg="#0056b3").pack(pady=20)
tk.Label(welcome_frame, text="Click below button to begin!", font=("Helvetica", 16, "bold"),bg="#f9f9f9").pack(pady=10)
tk.Button(welcome_frame,  text="Start", font=APP_FONT, command=lambda: show_frame(input_frame, welcome_frame), bg="#4CAF50", fg="white").pack(pady=20)

# Input page
input_frame = tk.Frame(root, bg="#f9f9f9")
tk.Label(input_frame, text="\nMood-Based Recommendation Expert System", font=("Helvetica", 16, "bold", "underline"), bg="#f9f9f9", fg="#0056b3").pack(pady=10)

# Create labels and entry widgets for mood
tk.Label(input_frame, text="How are you feeling today? (Happy, Stressed, Sad, Anxious, Bored, Fear, Love):", font=APP_FONT, bg="#f9f9f9").pack(pady=10)
mood_var = tk.StringVar()
mood_entry = tk.Entry(input_frame, textvariable=mood_var, font=APP_FONT, width=30)
mood_entry.pack(pady=5)

# Create a button to submit the mood
tk.Button(input_frame, text="Submit Mood", font=APP_FONT, command=on_mood_submit).pack(pady=10)

# Create labels and entry widgets for preference
tk.Label(input_frame, text="What type of activities would you prefer? (Physical, Quiet, Social):", font=APP_FONT, bg="#f9f9f9").pack(pady=10)
preference_var = tk.StringVar()
preference_entry = tk.Entry(input_frame, textvariable=preference_var, font=APP_FONT, width=30)
preference_entry.pack(pady=5)

# Create a button to submit the preference
tk.Button(input_frame, text="Submit Preference and Get Suggestions", font=APP_FONT, command=on_preference_submit).pack(pady=10)

# Create a text box with customized font and background
output_text = tk.Text(input_frame, height=16, width=50, wrap=tk.WORD, font=APP_FONT, bg="#ffffff", fg="#333333", pady="8")
output_text.pack(pady=20)
output_text.insert(tk.END, "Suggestions will appear here...\n", "header")

# Define custom tags for styling the text
output_text.tag_configure("header", font=("Helvetica", 12, "bold"), foreground="#333333")
output_text.tag_configure("details", font=("Helvetica", 12, "italic"), foreground="#333333", spacing1=5)
output_text.tag_configure("suggestion", font=("Helvetica", 12), foreground="#333333", spacing1=5)

# Create a reset button
tk.Button(input_frame, text="Reset", font=APP_FONT, command=reset_inputs).pack(pady=10)

# Initially show the welcome page
welcome_frame.pack(fill="both", expand=True)
input_frame.pack_forget()

# Run the Tkinter event loop
root.mainloop()
