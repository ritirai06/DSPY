# DSPy library import kar rahe hain
import dspy
# Signatures import kar rahe hain
from .signature import ValidateTerm, DefineTerm

# CONTROLLED SYSTEM: Multi-step program with boundaries
class ControlledDefinition(dspy.Module):
    """A controlled system that validates before defining."""
    
    def __init__(self):
        super().__init__()
        # Step 1: Validate karo ki term valid hai ya nahi
        self.validate = dspy.ChainOfThought(ValidateTerm)
        # Step 2: Agar valid hai, to define karo
        self.define = dspy.ChainOfThought(DefineTerm)
    
    def forward(self, term):
        # Pehle validation check karo
        validation = self.validate(term=term)
        
        # Agar term valid nahi hai, to refuse karo
        if validation.is_valid.lower().strip() not in ['yes', 'true', '1']:
            return dspy.Prediction(
                definition=f"I cannot provide a definition for '{term}'. Reason: {validation.reason}",
                is_valid=False,
                validation_reason=validation.reason
            )
        
        # Agar valid hai, to definition generate karo
        result = self.define(term=term)
        return dspy.Prediction(
            definition=result.definition,
            is_valid=True,
            validation_reason=validation.reason
        )

# Program create karne ka function
def get_program():
    # Controlled system return kar rahe hain with validation
    return ControlledDefinition()