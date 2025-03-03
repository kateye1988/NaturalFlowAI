import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.corpus import wordnet
import random

# Check for enchant
try:
    from enchant.checker import SpellChecker
except ImportError:
    print("Error: PyEnchant is not installed. Please install it using 'pip install pyenchant'.")
    exit(1)

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/wordnet')
except LookupError:
    print("Downloading required NLTK data...")
    try:
        nltk.download('punkt')
        nltk.download('wordnet')
    except Exception as e:
        print(f"Error downloading NLTK data: {e}")
        exit(1)

class WritingStyler:
    def __init__(self):
        try:
            self.checker = SpellChecker("en_US")
        except enchant.errors.DictNotFoundError:
            print("Error: English (US) dictionary not found for PyEnchant.")
            exit(1)
        
    def get_synonyms(self, word):
        synonyms = set()
        for syn in wordnet.synsets(word.lower()):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().replace('_', ' '))
        if word[0].isupper():
            return [s.capitalize() for s in synonyms]
        return list(synonyms)

    def check_spelling(self, text):
        self.checker.set_text(text)
        corrections = {}
        for err in self.checker:
            suggestions = err.suggest()
            if suggestions:
                corrections[err.word] = suggestions[0]
        return corrections

    def enhance_sentence(self, sentence):
        words = word_tokenize(sentence)
        enhanced_words = []
        
        for word in words:
            if len(word) <= 3 or not word.isalnum():
                enhanced_words.append(word)
                continue
            synonyms = self.get_synonyms(word)
            if synonyms and random.random() < 0.25:
                enhanced_words.append(random.choice(synonyms))
            else:
                enhanced_words.append(word)
        
        detokenizer = TreebankWordDetokenizer()
        return detokenizer.detokenize(enhanced_words)

    def process_text(self, text):
        print("\n=== Original Text ===")
        print(text)
        
        spelling_corrections = self.check_spelling(text)
        if spelling_corrections:
            print("\n=== Spelling Suggestions ===")
            for wrong, correct in spelling_corrections.items():
                print(f"'{wrong}' could be corrected to '{correct}'")
        
        sentences = sent_tokenize(text)
        enhanced_text = []
        
        print("\n=== Style Enhanced Version ===")
        for sentence in sentences:
            enhanced = self.enhance_sentence(sentence)
            enhanced_text.append(enhanced)
            print(enhanced)
        
        print("\n=== Writing Style Tips ===")
        self.provide_tips(text)
        
        return '\n'.join(enhanced_text)

    def provide_tips(self, text):
        words = word_tokenize(text.lower())
        sentences = sent_tokenize(text)
        
        word_count = {}
        for word in words:
            if word.isalnum():
                word_count[word] = word_count.get(word, 0) + 1
        
        repeated_words = [w for w, c in word_count.items() if c > 3]
        if repeated_words:
            print("- Try to avoid repeating these words too often:", ', '.join(repeated_words))
        
        if sentences:
            avg_length = sum(len(word_tokenize(s)) for s in sentences) / len(sentences)
            if avg_length > 20:
                print("- Consider using shorter sentences for better readability")
            elif avg_length < 10:
                print("- Try combining some sentences for better flow")
        else:
            print("- No sentences detected in the text.")
        
        print("- Use transition words (e.g., 'however', 'therefore') to connect ideas")
        print("- Vary your sentence beginnings for more engaging writing")

def main():
    styler = WritingStyler()
    
    print("Welcome to the English Writing Style Helper!")
    print("Enter your text (press Enter twice to finish):\n")
    
    lines = []
    while True:
        line = input(">> ")
        if line:
            lines.append(line)
        elif lines:
            break
    
    text = ' '.join(lines)
    enhanced_text = styler.process_text(text)

if __name__ == "__main__":
    main()
    pip install pyenchant
    
