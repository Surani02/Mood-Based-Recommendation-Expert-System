# Mood-Based Recommendation Expert System  

## Overview  
The **Mood-Based Recommendation Expert System** is a Python-based application that provides personalized activity suggestions to support mental well-being. By analyzing the user's mood and preferences, the system uses rule-based logic to recommend activities that align with the user's emotional state and desired activity type. It offers a structured and thoughtful way to promote mental health by providing users with helpful suggestions during moments of emotional uncertainty.  

## Key Features  
- **Mood-Based Input:** Accepts user input about their current emotional state (e.g., happy, sad, stressed, anxious, etc.).  
- **Activity Preferences:** Allows users to specify their preferred activity type (e.g., physical, quiet, social).  
- **Personalized Recommendations:** Suggests the best activity for the user's mood and preference, with alternative suggestions available upon request.  
- **Rule-Based Reasoning:** Leverages the Experta framework to process user inputs and apply predefined rules to generate recommendations.  
- **Interactive User Interface:** Built using Tkinter, the system offers a user-friendly interface for inputting mood and preferences, viewing recommendations, and exploring alternatives.  
- **Explainability:** Each recommendation includes a brief explanation of why it is suitable, enhancing user trust in the system.  

## How It Works  
1. **Input Stage:**  
   - Users enter their current mood and optionally specify an activity preference.  
2. **Processing Stage:**  
   - The system uses a knowledge base of predefined rules to match the mood and preference with suitable activities.  
   - It evaluates confidence levels to determine the best solution.  
3. **Output Stage:**  
   - The best activity suggestion is displayed first.  
   - Users can view alternative suggestions, which are ranked by relevance.  

## Technologies Used  
- **Python 3.9:** Core programming language.  
- **Experta Framework:** For rule-based reasoning and decision-making.  
- **Tkinter:** For creating a graphical user interface.  

## Benefits  
- Enhances mental well-being by providing tailored activity suggestions.  
- Mimics human reasoning to offer recommendations that feel intuitive and supportive.  
- Handles incomplete user inputs by offering general suggestions when preferences are not specified.  

## Installation and Usage  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/Surani02/Mood-Based-Recommendation-Expert-System.git  
   ```  
2. Navigate to the project directory:  
   ```bash  
   cd Mood-Based-Recommendation-Expert-System 
   ```  
3. Install dependencies:  
   ```bash  
   pip install experta
   pip install tk
   ```  
4. Run the application:  
   ```bash  
   python main.py  
   ```  

## Contributing  
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.  

## License  
This project is licensed under the MIT License.  
