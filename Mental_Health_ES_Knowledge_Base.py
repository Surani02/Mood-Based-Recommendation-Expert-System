from experta import *

# Synonym mapping for moods and preferences
MOOD_SYNONYMS = {
    "happy": ["joyful", "cheerful", "content", "excited", "pleased", "on cloud nine", "ecstatic", "elated", "thrilled"],
    "stressed": ["overwhelmed", "tense", "burned out", "pressured", "under the pump"],
    "sad": ["unhappy", "down", "worried", "depressed", "melancholy", "lonely", "blue", "heartbroken", "gloomy"],
    "anxious": ["nervous", "apprehensive", "jittery", "on edge", "panicked"],
    "bored": ["disinterested", "unengaged", "tired", "restless", "uninspired", "meh"],
    "fear": ["scared", "frightened", "afraid", "panicked", "terrified", "spooked"],
    "love": ["affectionate", "romantic", "passionate", "caring", "adoring", "smitten"]
}

PREFERENCE_SYNONYMS = {
    "physical": ["active", "energetic", "exercise", "movement", "sporty", "outdoorsy"],
    "quiet": ["calm", "peaceful", "relaxing", "still", "low-key", "laid-back"],
    "social": ["interactive", "group", "communicative", "friendly", "sociable", "outgoing", "chatty"]
}

# Define the KnowledgeEngine
class MentalHealthExpertSystem(KnowledgeEngine):
    def suggest_activities(self, activities):
        # Sort the activities by confidence (from high to low)
        sorted_activities = sorted(activities, key=lambda x: x['confidence'], reverse=True)
        
        # Extract the top suggestion
        best_suggestion = sorted_activities[0]
        alternative_suggestions = sorted_activities[1:]  # Get all except the best one
        
        # Print the best suggestion
        print(f"Solution:\n\n ✦ {best_suggestion['activity']}: {best_suggestion['reason']} \n(Confidence: {best_suggestion['confidence']}% — {best_suggestion['confidence_description']})")
        
        # Print all alternative solutions together
        print("\nAlternative Solutions:\n")
        for activity in alternative_suggestions:
            print(f"✦ {activity['activity']}: {activity['reason']} \n(Confidence: {activity['confidence']}% — {activity['confidence_description']})")

# Stressed
    @Rule(Fact(mood='stressed'), Fact(preference='physical'))
    def stressed_physical(self):
        activities = [
            {"activity": "Yoga or stretching exercises", "reason": "Helps relieve tension and improves focus", "confidence": 85, "confidence_description": "Highly recommended"},
            {"activity": "A brisk walk", "reason": "Increases endorphins and reduces cortisol levels", "confidence": 80, "confidence_description": "Quite effective"},
            {"activity": "Dancing", "reason": "Boosts mood through physical activity and music", "confidence": 75, "confidence_description": "Likely helpful"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='stressed'), Fact(preference='quiet'))
    def stressed_quiet(self):
        activities = [
            {"activity": "Guided meditation", "reason": "Calms the mind and reduces stress", "confidence": 90, "confidence_description": "Strongly recommended"},
            {"activity": "Reading a book", "reason": "Helps shift focus and induces relaxation", "confidence": 75, "confidence_description": "Effective in most cases"},
            {"activity": "A relaxing bath", "reason": "Soothes the body and mind", "confidence": 70, "confidence_description": "Recommended for stress relief"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='stressed'), Fact(preference='social'))
    def stressed_social(self):
        activities = [
            {"activity": "Talking to a friend", "reason": "Sharing feelings reduces emotional burden", "confidence": 85, "confidence_description": "Highly effective"},
            {"activity": "Spending time with loved ones", "reason": "Increases feelings of connection", "confidence": 80, "confidence_description": "Helpful for stress relief"},
            {"activity": "Joining a stress-relief workshop", "reason": "Learn new coping techniques", "confidence": 70, "confidence_description": "Beneficial for stress management"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='stressed'), NOT(Fact(preference=W())))
    def stressed_general(self):
        activities = [
            {"activity": "Practice mindfulness", "reason": "Improves focus and reduces anxiety", "confidence": 85, "confidence_description": "Highly effective"},
            {"activity": "Listen to calming music", "reason": "Lowers stress hormones", "confidence": 80, "confidence_description": "Helpful in reducing stress"},
            {"activity": "Take a nature walk", "reason": "Being in nature improves mood", "confidence": 75, "confidence_description": "Good for relaxation"}
        ]
        self.suggest_activities(activities)

    # Happy
    @Rule(Fact(mood='happy'), Fact(preference='physical'))
    def happy_physical(self):
        activities = [
            {"activity": "Exercise outdoors", "reason": "Boosts mood and keeps the energy flowing", "confidence": 90, "confidence_description": "Strongly recommended"},
            {"activity": "Dance", "reason": "Celebrates joy and improves mental well-being", "confidence": 85, "confidence_description": "Excellent for happiness"},
            {"activity": "Try a new sport", "reason": "Fun way to maintain happiness through novelty", "confidence": 80, "confidence_description": "Engaging and enjoyable"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='happy'), Fact(preference='quiet'))
    def happy_quiet(self):
        activities = [
            {"activity": "Reflect on your achievements", "reason": "Gratitude amplifies happiness", "confidence": 85, "confidence_description": "Highly beneficial"},
            {"activity": "Watch a feel-good movie", "reason": "Reinforces positive emotions", "confidence": 80, "confidence_description": "Excellent for uplifting mood"},
            {"activity": "Journaling", "reason": "Helps deepen happiness through self-reflection", "confidence": 75, "confidence_description": "Positive impact on happiness"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='happy'), Fact(preference='social'))
    def happy_social(self):
        activities = [
            {"activity": "Hang out with friends", "reason": "Celebrate happiness with loved ones", "confidence": 90, "confidence_description": "Highly recommended"},
            {"activity": "Host a gathering", "reason": "Strengthens social bonds and spreads positivity", "confidence": 85, "confidence_description": "Great for maintaining happiness"},
            {"activity": "Volunteer", "reason": "Helping others enhances your own happiness", "confidence": 80, "confidence_description": "Effective for joy"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='happy'), NOT(Fact(preference=W())))
    def happy_general(self):
        activities = [
            {"activity": "Reflect on your gratitude", "reason": "Reinforces happiness and satisfaction", "confidence": 90, "confidence_description": "Very helpful"},
            {"activity": "Share your joy with others", "reason": "Positivity multiplies when shared", "confidence": 85, "confidence_description": "Great for increasing happiness"},
            {"activity": "Enjoy a hobby", "reason": "Keeps the happiness flowing through creative outlets", "confidence": 80, "confidence_description": "Highly effective"}
        ]
        self.suggest_activities(activities)

    # Anxious
    @Rule(Fact(mood='anxious'), Fact(preference='physical'))
    def anxious_physical(self):
        activities = [
            {"activity": "Try some yoga", "reason": "Relieves anxiety and restores calmness", "confidence": 90, "confidence_description": "Strongly recommended"},
            {"activity": "Go for a jog", "reason": "Releases stress-relieving endorphins", "confidence": 85, "confidence_description": "Effective for reducing anxiety"},
            {"activity": "Do deep breathing exercises", "reason": "Helps in reducing immediate anxiety", "confidence": 80, "confidence_description": "Helpful in calming nerves"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='anxious'), Fact(preference='quiet'))
    def anxious_quiet(self):
        activities = [
            {"activity": "Practice meditation", "reason": "Eases the mind and brings peace", "confidence": 90, "confidence_description": "Highly effective for anxiety"},
            {"activity": "Listen to calming sounds", "reason": "Lowers heart rate and anxiety", "confidence": 85, "confidence_description": "Great for relaxation"},
            {"activity": "Read a book", "reason": "Shifts focus and relaxes the mind", "confidence": 75, "confidence_description": "Can help ease anxiety"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='anxious'), Fact(preference='social'))
    def anxious_social(self):
        activities = [
            {"activity": "Talk to someone you trust", "reason": "Sharing reduces the burden of anxiety", "confidence": 85, "confidence_description": "Highly effective"},
            {"activity": "Join a support group", "reason": "Encouraging connection helps manage anxiety", "confidence": 80, "confidence_description": "Helpful for anxiety relief"},
            {"activity": "Attend a social event", "reason": "Gradually increases comfort in social settings", "confidence": 75, "confidence_description": "Boosts confidence over time"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='anxious'), NOT(Fact(preference=W())))
    def anxious_general(self):
        activities = [
            {"activity": "Deep breathing exercises", "reason": "Calms the nervous system", "confidence": 90, "confidence_description": "Excellent for calming"},
            {"activity": "Practice grounding techniques", "reason": "Shifts focus away from anxious thoughts", "confidence": 80, "confidence_description": "Helps reduce anxiety"},
            {"activity": "Write about your anxiety", "reason": "Putting it on paper relieves tension", "confidence": 75, "confidence_description": "Great for processing anxiety"}
        ]
        self.suggest_activities(activities)

    # Sad
    @Rule(Fact(mood='sad'), Fact(preference='physical'))
    def sad_physical(self):
        activities = [
            {"activity": "Go for a walk", "reason": "Physical movement boosts mood and energy", "confidence": 85, "confidence_description": "Effective for improving mood"},
            {"activity": "Stretching exercises", "reason": "Helps release emotional tension", "confidence": 80, "confidence_description": "Great for stress relief"},
            {"activity": "Try a light workout", "reason": "Boosts serotonin levels and mood", "confidence": 75, "confidence_description": "Good for uplifting mood"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='sad'), Fact(preference='quiet'))
    def sad_quiet(self):
        activities = [
            {"activity": "Watch an uplifting movie", "reason": "Helps shift mood to a positive space", "confidence": 85, "confidence_description": "Great for improving mood"},
            {"activity": "Listen to positive affirmations", "reason": "Encourages healing through words", "confidence": 80, "confidence_description": "Positive impact"},
            {"activity": "Journaling", "reason": "Helps process and release sadness", "confidence": 75, "confidence_description": "Useful for emotional healing"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='sad'), Fact(preference='social'))
    def sad_social(self):
        activities = [
            {"activity": "Call a supportive friend", "reason": "Talking helps release pent-up sadness", "confidence": 85, "confidence_description": "Highly effective"},
            {"activity": "Spend time with loved ones", "reason": "Emotional support eases sadness", "confidence": 80, "confidence_description": "Helpful for emotional healing"},
            {"activity": "Attend a support group", "reason": "Knowing others understand can be comforting", "confidence": 75, "confidence_description": "Effective for emotional relief"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='sad'), NOT(Fact(preference=W())))
    def sad_general(self):
        activities = [
            {"activity": "Reflect on what made you sad", "reason": "Understanding the cause helps resolve it", "confidence": 85, "confidence_description": "Useful for processing sadness"},
            {"activity": "Engage in a creative hobby", "reason": "It can improve mood and provide a sense of accomplishment", "confidence": 80, "confidence_description": "Great for boosting mood"},
            {"activity": "Spend time in nature", "reason": "Nature has calming and healing effects", "confidence": 75, "confidence_description": "Good for emotional recovery"}
        ]
        self.suggest_activities(activities)

    # Bored
    @Rule(Fact(mood='bored'), Fact(preference='physical'))
    def bored_physical(self):
        activities = [
            {"activity": "Go for a run", "reason": "Energizes you and breaks the monotony", "confidence": 85, "confidence_description": "Highly effective for boredom"},
            {"activity": "Try a new sport", "reason": "New experiences can lift boredom", "confidence": 80, "confidence_description": "Excellent for stimulating interest"},
            {"activity": "Dance", "reason": "Great way to move and break the boredom cycle", "confidence": 75, "confidence_description": "Fun and engaging"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='bored'), Fact(preference='quiet'))
    def bored_quiet(self):
        activities = [
            {"activity": "Read a new book", "reason": "Engaging stories can distract from boredom", "confidence": 85, "confidence_description": "Highly recommended for mental stimulation"},
            {"activity": "Learn a new skill online", "reason": "Keeps your mind stimulated and curious", "confidence": 80, "confidence_description": "Great for learning something new"},
            {"activity": "Listen to a podcast", "reason": "Educates and entertains at the same time", "confidence": 75, "confidence_description": "Good for keeping engaged"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='bored'), Fact(preference='social'))
    def bored_social(self):
        activities = [
            {"activity": "Meet up with friends", "reason": "Socializing breaks the monotony", "confidence": 85, "confidence_description": "Highly effective for improving mood"},
            {"activity": "Join a community event", "reason": "Explore new activities with others", "confidence": 80, "confidence_description": "Great for social engagement"},
            {"activity": "Take a class or workshop", "reason": "Engage with people and learn something new", "confidence": 75, "confidence_description": "Good for both learning and connecting"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='bored'), NOT(Fact(preference=W())))
    def bored_general(self):
        activities = [
            {"activity": "Start a new hobby", "reason": "Keeps the mind engaged and entertained", "confidence": 85, "confidence_description": "Highly recommended"},
            {"activity": "Organize your space", "reason": "Cleaning can break the boredom and give a sense of accomplishment", "confidence": 80, "confidence_description": "Helpful for resetting your environment"},
            {"activity": "Try a new creative project", "reason": "Great way to keep yourself entertained", "confidence": 75, "confidence_description": "Effective for sparking creativity"}
        ]
        self.suggest_activities(activities)

    # Fear
    @Rule(Fact(mood='fear'), Fact(preference='physical'))
    def fear_physical(self):
        activities = [
            {"activity": "Practice progressive muscle relaxation", "reason": "Relaxes physical tension caused by fear", "confidence": 85, "confidence_description": "Highly effective for reducing anxiety"},
            {"activity": "Do deep breathing exercises", "reason": "Helps to reduce adrenaline and calm the body", "confidence": 80, "confidence_description": "Effective for calming your physical state"},
            {"activity": "Take a brisk walk", "reason": "Physical activity distracts and lowers fear responses", "confidence": 75, "confidence_description": "Good for relieving tension"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='fear'), Fact(preference='quiet'))
    def fear_quiet(self):
        activities = [
            {"activity": "Practice mindfulness meditation", "reason": "Focuses your thoughts and reduces fear intensity", "confidence": 90, "confidence_description": "Highly effective for calming your mind"},
            {"activity": "Listen to calming sounds", "reason": "Creates a peaceful environment to ease fear", "confidence": 85, "confidence_description": "Effective for creating a sense of calm"},
            {"activity": "Journal about your fears", "reason": "Helps to process and organize your thoughts", "confidence": 80, "confidence_description": "Useful for emotional clarity"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='fear'), Fact(preference='social'))
    def fear_social(self):
        activities = [
            {"activity": "Talk to a trusted person", "reason": "Sharing fears can make them seem less overwhelming", "confidence": 85, "confidence_description": "Highly effective for emotional support"},
            {"activity": "Join a support group", "reason": "Being with others who understand helps reduce fear", "confidence": 80, "confidence_description": "Effective for emotional relief"},
            {"activity": "Face your fear with someone", "reason": "Gradually facing fear with support can help desensitize it", "confidence": 75, "confidence_description": "Great for overcoming specific fears"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='fear'), NOT(Fact(preference=W())))
    def fear_general(self):
        activities = [
            {"activity": "Challenge your fearful thoughts", "reason": "Reframing thoughts helps reduce fear intensity", "confidence": 85, "confidence_description": "Highly effective for overcoming fear"},
            {"activity": "Visualize a calm and safe place", "reason": "Visualization helps create a mental escape from fear", "confidence": 80, "confidence_description": "Helpful for managing fear"},
            {"activity": "Take one small step towards confronting your fear", "reason": "Gradual exposure to fear helps build resilience", "confidence": 75, "confidence_description": "Effective for gradual fear reduction"}
        ]
        self.suggest_activities(activities)

    # Love
    @Rule(Fact(mood='love'), Fact(preference='physical'))
    def love_physical(self):
        activities = [
            {"activity": "Plan a romantic date", "reason": "Creates moments of connection and affection", "confidence": 90, "confidence_description": "Highly recommended for nurturing love"},
            {"activity": "Spend quality time with your partner", "reason": "Fosters emotional connection and intimacy", "confidence": 85, "confidence_description": "Great for strengthening relationships"},
            {"activity": "Dance together", "reason": "Physical connection through dancing brings joy and bonding", "confidence": 80, "confidence_description": "Fun and intimate activity"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='love'), Fact(preference='quiet'))
    def love_quiet(self):
        activities = [
            {"activity": "Write love letters", "reason": "Expressing love through words strengthens relationships", "confidence": 85, "confidence_description": "Highly effective for emotional connection"},
            {"activity": "Reflect on happy memories", "reason": "Reminding yourself of positive moments fosters love", "confidence": 80, "confidence_description": "Great for rekindling feelings of love"},
            {"activity": "Practice gratitude for your partner", "reason": "Gratitude deepens appreciation in a relationship", "confidence": 75, "confidence_description": "Helpful for strengthening love"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='love'), Fact(preference='social'))
    def love_social(self):
        activities = [
            {"activity": "Surprise your partner with something special", "reason": "Thoughtful gestures deepen emotional bonds", "confidence": 90, "confidence_description": "Highly effective for showing love"},
            {"activity": "Attend a romantic event together", "reason": "Shared experiences enhance love and connection", "confidence": 85, "confidence_description": "Great for bonding"},
            {"activity": "Volunteer together", "reason": "Helping others as a couple strengthens your relationship", "confidence": 80, "confidence_description": "Beneficial for deepening emotional ties"}
        ]
        self.suggest_activities(activities)

    @Rule(Fact(mood='love'), NOT(Fact(preference=W())))
    def love_general(self):
        activities = [
            {"activity": "Share something meaningful with your partner", "reason": "Emotional sharing deepens love", "confidence": 90, "confidence_description": "Highly effective for intimacy"},
            {"activity": "Plan future adventures together", "reason": "Creating shared dreams strengthens a relationship", "confidence": 85, "confidence_description": "Great for nurturing love"},
            {"activity": "Express affection through small gestures", "reason": "Consistent, small acts of love reinforce the bond", "confidence": 80, "confidence_description": "Effective for maintaining love"}
        ]
        self.suggest_activities(activities)