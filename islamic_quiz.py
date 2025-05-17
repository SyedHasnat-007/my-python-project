import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Using Pillow for image support
import os
import random
import time  # Import time module

questions = {
        "Quran": [
            {"question": "How many chapters (Surahs) are there in the Quran?", 
             "options": ["A) 100", "B) 114", "C) 124", "D) 110"],
             "answer": "B"},
            {"question": "Which Surah is called the Heart of the Quran?", 
             "options": ["A) Surah Yaseen", "B) Surah Al-Baqara", "C) Surah Al-Fatiha", "D) Surah Al-Ikhlas"],
             "answer": "A"},
            {"question": "In which language was the Quran revealed?", 
             "options": ["A) Persian", "B) Arabic", "C) Hebrew", "D) Urdu"],
             "answer": "B"},
            {"question": "What is the longest Surah in the Quran?", 
             "options": ["A) Surah Al-Baqara", "B) Surah Al-Imran", "C) Surah An-Nisa", "D) Surah Al-Maidah"],
             "answer": "A"},
            {"question": "Which Surah was revealed completely at once?", 
             "options": ["A) Surah Al-Fatiha", "B) Surah Al-Kawthar", "C) Surah Yusuf", "D) Surah Al-Ikhlas"],
             "answer": "A"},
            {"question": "How many verses are in the Quran?", 
             "options": ["A) 6666", "B) 6236", "C) 6048", "D) 6152"],
             "answer": "B"},
            {"question": "What is the last Surah of the Quran?", 
             "options": ["A) Surah Al-Kahf", "B) Surah Al-Mulk", "C) Surah An-Nas", "D) Surah Al-Ikhlas"],
             "answer": "C"},
            {"question": "Which Surah is known as the 'Mother of the Book'?", 
             "options": ["A) Surah Yaseen", "B) Surah Al-Fatiha", "C) Surah Al-Ikhlas", "D) Surah Al-Kahf"],
             "answer": "B"},
            {"question": "Which Surah was the first to be revealed?", 
             "options": ["A) Surah Al-Fatiha", "B) Surah Al-Baqara", "C) Surah Al-Alaq", "D) Surah Al-Ikhlas"],
             "answer": "C"},
            {"question": "Which Surah has the greatest Ayah (Ayat-ul-Kursi)?", 
             "options": ["A) Surah Yaseen", "B) Surah Al-Baqara", "C) Surah Al-Fatiha", "D) Surah Al-Kahf"],
             "answer": "B"}
        ],
        "Islamic History": [
    {"question": "In which year was the Battle of Badr fought?", 
     "options": ["A) 1 AH", "B) 2 AH", "C) 3 AH", "D) 5 AH"],
     "answer": "B"},
    {"question": "Who was the first Caliph of Islam?", 
     "options": ["A) Umar ibn Al-Khattab", "B) Ali ibn Abi Talib", "C) Abu Bakr As-Siddiq", "D) Uthman ibn Affan"],
     "answer": "C"},
    {"question": "Which city was the first capital of the Islamic Caliphate?", 
     "options": ["A) Makkah", "B) Madinah", "C) Damascus", "D) Baghdad"],
     "answer": "B"},
    {"question": "Who was known as 'The Sword of Allah'?", 
     "options": ["A) Khalid ibn Al-Walid", "B) Abu Ubaidah ibn Jarrah", "C) Salahuddin Ayyubi", "D) Umar ibn Al-Khattab"],
     "answer": "A"},
    {"question": "Which treaty was signed between the Muslims and Quraysh of Makkah?", 
     "options": ["A) Treaty of Hudaibiya", "B) Treaty of Aqabah", "C) Treaty of Medina", "D) Treaty of Taif"],
     "answer": "A"},
    {"question": "Which battle is also known as the 'Battle of the Trench'?", 
     "options": ["A) Battle of Uhud", "B) Battle of Hunayn", "C) Battle of Khandaq", "D) Battle of Tabuk"],
     "answer": "C"},
    {"question": "During which Caliph's rule was the Quran compiled into a book format?", 
     "options": ["A) Abu Bakr As-Siddiq", "B) Umar ibn Al-Khattab", "C) Uthman ibn Affan", "D) Ali ibn Abi Talib"],
     "answer": "C"},
    {"question": "Who was the first martyr in Islam?", 
     "options": ["A) Bilal ibn Rabah", "B) Khadijah bint Khuwaylid", "C) Hamza ibn Abdul-Muttalib", "D) Sumayyah bint Khayyat"],
     "answer": "D"},
    {"question": "What was the name of the Christian king who gave refuge to the early Muslims in Abyssinia?", 
     "options": ["A) Heraclius", "B) Negus", "C) Kisra", "D) Pharaoh"],
     "answer": "B"},
    {"question": "Which battle resulted in the conquest of Makkah?", 
     "options": ["A) Battle of Badr", "B) Battle of Uhud", "C) Battle of Hunayn", "D) Conquest of Makkah"],
     "answer": "D"}
],
"Prophets in Islam": [
    {"question": "Who was the first Prophet of Islam?", 
     "options": ["A) Prophet Ibrahim", "B) Prophet Nuh", "C) Prophet Adam", "D) Prophet Musa"],
     "answer": "C"},
    {"question": "Which Prophet was swallowed by a whale?", 
     "options": ["A) Prophet Musa", "B) Prophet Yunus", "C) Prophet Isa", "D) Prophet Yusuf"],
     "answer": "B"},
    {"question": "Which Prophet built the Kaaba along with his son?", 
     "options": ["A) Prophet Nuh", "B) Prophet Ibrahim", "C) Prophet Musa", "D) Prophet Dawud"],
     "answer": "B"},
    {"question": "Which Prophet could speak to animals and control the wind?", 
     "options": ["A) Prophet Sulaiman", "B) Prophet Dawud", "C) Prophet Musa", "D) Prophet Nuh"],
     "answer": "A"},
    {"question": "Which Prophet parted the sea with Allah’s help?", 
     "options": ["A) Prophet Yusuf", "B) Prophet Musa", "C) Prophet Isa", "D) Prophet Lut"],
     "answer": "B"},
    {"question": "Who was the father of Prophet Yusuf?", 
     "options": ["A) Prophet Ishaq", "B) Prophet Yaqub", "C) Prophet Ibrahim", "D) Prophet Musa"],
     "answer": "B"},
    {"question": "Which Prophet was known for his patience?", 
     "options": ["A) Prophet Ayyub", "B) Prophet Yahya", "C) Prophet Idris", "D) Prophet Zakariya"],
     "answer": "A"},
    {"question": "Which Prophet was given the Torah?", 
     "options": ["A) Prophet Isa", "B) Prophet Musa", "C) Prophet Nuh", "D) Prophet Muhammad"],
     "answer": "B"},
    {"question": "Which Prophet was born without a father?", 
     "options": ["A) Prophet Adam", "B) Prophet Musa", "C) Prophet Isa", "D) Prophet Idris"],
     "answer": "C"},
    {"question": "Which Prophet is known as 'Kalimullah' (The one who spoke to Allah)?", 
     "options": ["A) Prophet Musa", "B) Prophet Isa", "C) Prophet Ibrahim", "D) Prophet Muhammad"],
     "answer": "A"}
],
"Islamic Practices": [
    {"question": "How many daily prayers are obligatory in Islam?", 
     "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
     "answer": "C"},
    {"question": "Which pillar of Islam involves fasting?", 
     "options": ["A) Zakat", "B) Salah", "C) Sawm", "D) Hajj"],
     "answer": "C"},
    {"question": "What is the percentage of Zakat that a Muslim must pay?", 
     "options": ["A) 1%", "B) 2.5%", "C) 5%", "D) 10%"],
     "answer": "B"},
    {"question": "Which month is considered the holiest in Islam?", 
     "options": ["A) Muharram", "B) Dhul-Hijjah", "C) Rajab", "D) Ramadan"],
     "answer": "D"},
    {"question": "What is the name of the Islamic pilgrimage to Makkah?", 
     "options": ["A) Salah", "B) Zakat", "C) Hajj", "D) Umrah"],
     "answer": "C"},
    {"question": "Which prayer is performed before dawn?", 
     "options": ["A) Dhuhr", "B) Asr", "C) Fajr", "D) Isha"],
     "answer": "C"},
    {"question": "How many Rak'ahs are in Isha prayer (including Sunnah)?", 
     "options": ["A) 10", "B) 12", "C) 13", "D) 17"],
     "answer": "D"},
    {"question": "What is the special night in Ramadan that is better than a thousand months?", 
     "options": ["A) Laylat-ul-Qadr", "B) Shab-e-Barat", "C) Eid-ul-Fitr", "D) Jumu’ah"],
     "answer": "A"},
    {"question": "Which direction do Muslims face when praying?", 
     "options": ["A) Towards Madinah", "B) Towards Jerusalem", "C) Towards the Kaaba", "D) Towards the Sun"],
     "answer": "C"},
    {"question": "Which Eid is celebrated after Hajj?", 
     "options": ["A) Eid-ul-Fitr", "B) Eid-ul-Adha", "C) Shab-e-Miraj", "D) Laylat-ul-Qadr"],
     "answer": "B"}
],

        "Hadith": [
            {"question": "Who is the most famous compiler of Hadith?", 
             "options": ["A) Imam Bukhari", "B) Imam Abu Hanifa", "C) Imam Malik", "D) Imam Ghazali"],
             "answer": "A"},
            {"question": "Which Hadith collection is considered the most authentic after the Quran?", 
             "options": ["A) Sunan Abu Dawood", "B) Sahih Muslim", "C) Sahih Bukhari", "D) Sunan Ibn Majah"],
             "answer": "C"},
            {"question": "What is the meaning of 'Hadith'?", 
             "options": ["A) Poetry", "B) Story", "C) Saying of Prophet (PBUH)", "D) Law"],
             "answer": "C"},
            {"question": "Which companion of the Prophet (PBUH) narrated the most Hadiths?", 
             "options": ["A) Abu Huraira (RA)", "B) Umar ibn Al-Khattab (RA)", "C) Ali ibn Abi Talib (RA)", "D) Aisha (RA)"],
             "answer": "A"},
            {"question": "Which book of Hadith contains the Muwatta collection?", 
             "options": ["A) Sunan Ibn Majah", "B) Sahih Bukhari", "C) Muwatta Imam Malik", "D) Sahih Muslim"],
             "answer": "C"},
            {"question": "How many Hadith are there in Sahih Bukhari?", 
             "options": ["A) 7563", "B) 7000", "C) 6800", "D) 8000"],
             "answer": "A"},
            {"question": "What does 'Sahih' mean in Hadith terminology?", 
             "options": ["A) Weak", "B) Authentic", "C) Fabricated", "D) Narrated"],
             "answer": "B"},
            {"question": "What is the name of the Hadith narrator who compiled Sunan Abu Dawood?", 
             "options": ["A) Imam Abu Dawood", "B) Imam Tirmidhi", "C) Imam Bukhari", "D) Imam Muslim"],
             "answer": "A"},
            {"question": "What does 'Daif' mean in Hadith classification?", 
             "options": ["A) Strong", "B) Authentic", "C) Weak", "D) Unknown"],
             "answer": "C"},
            {"question": "What does 'Mutawatir' mean in Hadith classification?", 
             "options": ["A) Repeated by a single narrator", "B) A fabricated Hadith", "C) Mass-transmitted Hadith", "D) A rare Hadith"],
             "answer": "C"}
        ]
    }
  # Shuffle questions within each category
for category in questions:
    random.shuffle(questions[category])

class IslamicQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Islamic Quiz")
        self.root.geometry("600x500")
        self.root.configure(bg="#f4f4f4")
        
        self.selected_category = None
        self.current_question_index = 0
        self.score = 0
        self.questions_list = []
        self.start_time = None  # Initialize start time
        
        # Create a style
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 20), padding=20)
        self.style.configure("TLabel", font=("Arial", 22), background="#f4f4f4")
        self.style.configure("TFrame", background="#f4f4f4")
        
        # Load category images safely using Pillow
        self.image_files = {
            "Quran": "quran.png",
            "Hadith": "hadith.png",
            "Islamic Practices": "practices.png",
            "Islamic History": "history.png",
            "Prophets in Islam": "prophets.png"
        }
        
        self.images = {}
        for category, file in self.image_files.items():
            path = os.path.join(os.getcwd(), file)
            if os.path.exists(path):
                self.images[category] = ImageTk.PhotoImage(Image.open(path).resize((200, 200)))
        
        # Welcome screen with background
        self.label = ttk.Label(root, text="Welcome to the Islamic Quiz!\nChoose a category:", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)
        
        self.frame = ttk.Frame(root)
        self.frame.pack()
        
        # Category buttons with images
        row, col = 0, 0
        for category in questions.keys():
            img = self.images.get(category, None)
            btn = ttk.Button(self.frame, text=category, image=img, compound="top", command=lambda c=category: self.start_quiz(c))
            btn.grid(row=row, column=col, padx=10, pady=10)
            col += 1
            if col > 2:
                col = 0
                row += 1
    
    def start_quiz(self, category):
        self.selected_category = category
        self.questions_list = questions[category]
        self.current_question_index = 0
        self.score = 0
        self.start_time = time.time()  # Record start time
        
        # Clear screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.display_question()
    
    def display_question(self):
        if self.current_question_index < len(self.questions_list):
            question_data = self.questions_list[self.current_question_index]
            
            self.question_label = ttk.Label(self.root, text=question_data["question"], font=("Arial", 22, "bold"), wraplength=500)
            self.question_label.pack(pady=20)

            self.buttons = []
            for i, option in enumerate(question_data["options"]):
                btn = ttk.Button(self.root, text=option, command=lambda i=i: self.check_answer(i))
                btn.pack(pady=5)
                self.buttons.append(btn)
            
            # Add progress bar
            progress = ttk.Label(self.root, text=f"Question {self.current_question_index + 1} of {len(self.questions_list)}")
            progress.pack(pady=10)
        else:
            self.display_result_card()
    
    def check_answer(self, selected_index):
        question_data = self.questions_list[self.current_question_index]
        correct_answer = question_data["answer"]
        
        if question_data["options"][selected_index].startswith(correct_answer):
            self.score += 1
        
        self.current_question_index += 1

        
        # Clear previous question UI
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.display_question()
    
    def display_result_card(self):
        end_time = time.time()  # Record end time
        time_taken = end_time - self.start_time  # Calculate time taken
        minutes, seconds = divmod(time_taken, 60)
        
        rating = ""
        score_percentage = (self.score / len(self.questions_list)) * 100
        if score_percentage >= 90:
            rating = "Excellent"
        elif score_percentage >= 75:
            rating = "Very Good"
        elif score_percentage >= 50:
            rating = "Good"
        else:
            rating = "Needs Improvement"
        
        # Clear screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create result card frame
        result_frame = ttk.Frame(self.root, padding=20)
        result_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Add result labels
        score_label = ttk.Label(result_frame, text=f"Your score: {self.score}/{len(self.questions_list)}", font=("Arial", 18))
        score_label.pack(pady=10)
        
        rating_label = ttk.Label(result_frame, text=f"Rating: {rating}", font=("Arial", 18))
        rating_label.pack(pady=10)
        
        time_label = ttk.Label(result_frame, text=f"Time taken: {int(minutes)} minutes and {int(seconds)} seconds", font=("Arial", 18))
        time_label.pack(pady=10)
        
        # Add a button to close the quiz
        close_button = ttk.Button(result_frame, text="Close", command=self.root.quit)
        close_button.pack(pady=10)
        
        # Add a button to play again
        play_again_button = ttk.Button(result_frame, text="Play Again", command=self.restart_quiz)
        play_again_button.pack(pady=10)
    
    def restart_quiz(self):
        # Clear screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Reset to welcome screen
        self.__init__(self.root)

# Run the quiz
root = tk.Tk()
app = IslamicQuizApp(root)
root.mainloop()
