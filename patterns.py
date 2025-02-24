import regex as re

# Patterns for ESL-specific challenges, tone, and cultural considerations
# Each pattern is a tuple: (regex pattern, description, suggested feedback)

# 1. Hypercorrections
HYPERCORRECTION_PATTERNS = [
    (r"\bshall\b", 
     "Overuse of 'shall' (formal, unnatural in casual contexts)", 
     "Try 'will' instead of 'shall' for a more natural tone."),
    (r"\bwhom\b", 
     "Overuse of 'whom' (often hypercorrected by learners)", 
     "Use 'who' unless it's the object of a preposition or verb—e.g., 'Who are you?'"),
    (r"\b(?:doesn’t|don’t|isn’t|aren’t|won’t)\s+not\b", 
     "Double negatives from hypercorrection (e.g., 'doesn’t not')", 
     "Remove the second 'not'—e.g., 'It doesn’t work,' not 'It doesn’t not work.'"),
]

# 2. Tone and Emotional Subcategories
TONE_PATTERNS = [
    # Hesitation
    (r"\b(maybe|perhaps|possibly|probably)\b", 
     "Hesitant qualifiers", 
     "Replace with confident phrasing like 'I believe' or 'It is' to sound more assertive."),
    (r"\b(no|yes|right|okay)\?$", 
     "Tag questions indicating hesitation", 
     "Avoid tag questions like 'no?' in formal writing for a stronger tone."),
    # Enthusiasm
    (r"!{1,}", 
     "Exclamation marks indicating enthusiasm", 
     "Great for informal contexts, but reduce in formal writing for a neutral tone."),
    (r"\b(great|awesome|fantastic|amazing)\b", 
     "Positive adjectives showing enthusiasm", 
     "Your enthusiasm shines through—keep it for casual settings or soften for formality."),
    # Frustration
    (r"\b(never|always|ugh|argh)\b", 
     "Words suggesting frustration", 
     "This suggests frustration—try a calmer phrase like 'sometimes' or 'I’m unsure.'"),
    # Confidence
    (r"\b(definitely|certainly|absolutely)\b", 
     "Confident adverbs", 
     "Your confidence is clear—well done! Ensure it fits the context.")
]

# 3. Cultural Considerations
CULTURAL_PATTERNS = [
    # Idioms
    (r"\bbreak a leg\b", 
     "Idiom meaning 'good luck'", 
     "'Break a leg' is informal and means 'good luck.' It may confuse non-native readers."),
    (r"\bkick the bucket\b", 
     "Idiom meaning 'to die'", 
     "'Kick the bucket' is a casual way to say 'die.' Use a literal phrase in formal contexts."),
    # Collocations
    (r"\bmake a mistake\b", 
     "Common collocation", 
     "Correct usage of 'make a mistake'—good job! Alternatives like 'do a mistake' are incorrect."),
    (r"\b(?:do|take)\s+a\s+mistake\b", 
     "Incorrect collocation", 
     "Use 'make a mistake,' not 'do a mistake' or 'take a mistake.'"),
    # Puns/Wordplay (fuzzy matching for learner errors)
    (r"\b(?:rain|rein|reign)\s+(?:cats|dogs)\b", 
     "Idiom 'raining cats and dogs' with possible misspellings", 
     "'Raining cats and dogs' means heavy rain. Check spelling ('rain,' not 'rein' or 'reign')."),
]

# 4. Common ESL Mistakes
ESL_MISTAKE_PATTERNS = [
    (r"\bthe\s+(?:good|bad|nice)\b", 
     "Overuse of 'the' before adjectives without nouns", 
     "Omit 'the' before adjectives unless followed by a noun—e.g., 'good,' not 'the good.'"),
    (r"\b(?:in|on|at)\s+last\b", 
     "Preposition confusion with 'last'", 
     "Use 'at last,' not 'in last' or 'on last,' to mean 'finally.'"),
    (r"\b(?:informations|furnitures|advices)\b", 
     "Pluralized uncountable nouns", 
     "Use singular forms: 'information,' 'furniture,' 'advice.' These nouns don’t take an 's.'")
]

# Function to apply patterns and generate feedback
def analyze_text(text, pattern_list):
    feedback = []
    for pattern, description, suggestion in pattern_list:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        if matches:
            feedback.append({
                "matches": matches,
                "description": description,
                "suggestion": suggestion
            })
    return feedback

# Example usage
if __name__ == "__main__":
    sample_text = "I shall make a mistake, maybe the good idea, no? Break a leg!"
    all_patterns = HYPERCORRECTION_PATTERNS + TONE_PATTERNS + CULTURAL_PATTERNS + ESL_MISTAKE_PATTERNS
    
    results = analyze_text(sample_text, all_patterns)
    for result in results:
        print(f"Found: {result['matches']} - {result['description']}")
        print(f"Suggestion: {result['suggestion']}\n")
