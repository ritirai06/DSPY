# DSPy library import kar rahe hain
import dspy

# SYSTEM BOUNDARY: Check if term is valid/answerable
# Ye signature pehle decide karta hai ki term ka answer de sakte hain ya nahi
class ValidateTerm(dspy.Signature):
    """Determine if a term is a valid technical/academic/scientific term that requires a formal definition.
    
    Valid terms: Computer Science, AI, Machine Learning, Neural Network, Algorithm, etc.
    Invalid terms: Common objects (grape, apple), names, random words, non-technical terms.
    """
    
    term = dspy.InputField(desc="The term to validate")
    is_valid = dspy.OutputField(desc="'yes' ONLY if technical/academic/scientific term, 'no' if common word/object/random")
    reason = dspy.OutputField(desc="Brief reason for validation decision")

# DefineTerm class bana rahe hain jo dspy.Signature ko extend karti hai
# Ye class input aur output ka structure define karti hai
# IMPORTANT: Ye sirf valid terms ke liye call hoga
class DefineTerm(dspy.Signature):
    """Given a VALID technical/academic term, provide its definition."""
    
    term = dspy.InputField()  # Input field - jo term define karni hai
    definition = dspy.OutputField()  # Output field - term ki definition