# DSPy library import kar rahe hain
import dspy

# DefineTerm class bana rahe hain jo dspy.Signature ko extend karti hai
# Ye class input aur output ka structure define karti hai
class DefineTerm(dspy.Signature):
    """Given a term, provide its definition."""
    
    term = dspy.InputField()  # Input field - jo term define karni hai
    definition = dspy.OutputField()  # Output field - term ki definition