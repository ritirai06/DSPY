# Evaluation metric function - ye check karta hai ki prediction sahi hai ya nahi
def definition_match(example, prediction, trace=None):
    # Example ki definition aur prediction ki definition ko compare kar rahe hain
    # strip() - extra spaces remove karta hai
    # lower() - sab kuch lowercase mein convert karta hai (case-insensitive comparison ke liye)
    # trace parameter optional hai - DSPy optimizer ke liye
    # Agar dono match karte hain to True return hoga, warna False
    return example.definition.strip().lower() == prediction.definition.strip().lower()