# DSPy library ko import kar rahe hain - ye main framework hai
import dspy
# Environment variables load karne ke liye
import os
from dotenv import load_dotenv

# Program module se get_program function import kar rahe hain
from dspy_program.program import get_program
# Optimizer module se optimize_program function import kar rahe hain
from dspy_program.optimizer import optimize_program
# Training data import kar rahe hain
from data.train import trainset
# Evaluation metric import kar rahe hain
from metrics.evaluation import definition_match

# .env file se environment variables load kar rahe hain (API key ke liye)
load_dotenv()

# DSPy ko configure kar rahe hain - Ollama local model set kar rahe hain
# Ollama free hai aur local machine pe chalti hai
dspy.configure(
    lm=dspy.LM(model="ollama/llama3.2")  # Ollama ka llama3.2 model use kar rahe hain (completely free)
)

# Program ko initialize kar rahe hain
program=get_program()

# Testing WITHOUT optimization first to see boundaries working
print("\n" + "="*60)
print("TESTING SYSTEM BOUNDARIES")
print("="*60)

# Test 1: Valid technical term
print("\n" + "="*60)
print("TEST 1: Valid Technical Term - 'Artificial Intelligence'")
print("="*60)
result1=program(term='Artificial Intelligence')
print(f"Is Valid: {result1.is_valid if hasattr(result1, 'is_valid') else 'N/A'}")
if hasattr(result1, 'validation_reason'):
    print(f"Validation Reason: {result1.validation_reason}")
print(f"Definition: {result1.definition}")

# Test 2: Random nonsense term (should be rejected)
print("\n" + "="*60)
print("TEST 2: Random Term - 'Grape' (Not a technical term)")
print("="*60)
result2=program(term='Grape')
print(f"Is Valid: {result2.is_valid if hasattr(result2, 'is_valid') else 'N/A'}")
if hasattr(result2, 'validation_reason'):
    print(f"Validation Reason: {result2.validation_reason}")
print(f"Definition: {result2.definition}")

# Test 3: Another valid term
print("\n" + "="*60)
print("TEST 3: Valid Technical Term - 'Machine Learning'")
print("="*60)
result3=program(term='Machine Learning')
print(f"Is Valid: {result3.is_valid if hasattr(result3, 'is_valid') else 'N/A'}")
if hasattr(result3, 'validation_reason'):
    print(f"Validation Reason: {result3.validation_reason}")
print(f"Definition: {result3.definition}")

print("\n" + "="*60)
print("System boundaries working! ✅")
print("="*60)
# Define the optimizer
from dspy.teleprompt import BootstrapFewShot

optimizer = BootstrapFewShot(metric=definition_match)

# First compile the program with optimizer
optimized_program = optimizer.compile(
    program,  # The program to optimize
    trainset=trainset
)

# Now use the optimized program
result = optimized_program(term='Artificial Intelligence')
print(f"Result: {result}")

# Result print kar rahe hain
print("\n" + "="*50)
print("TERM: Artificial Intelligence")
print("="*50)

# Agar Chain of Thought use ho raha hai, to reasoning bhi show hogi
if hasattr(optimized_program, 'rationale'):
    print(f"\nReasoning: {optimized_program.rationale}")
    
print(f"\nDefinition: {optimized_program.definition}")
print("="*50)
optimized_program=optimized_program(term='Deep Learning')  
optimized_program=optimized_program(term='grapes') # Ye term training data mein nahi hai, isliye model ko generalize karna padega
# Result ki definition print kar rahe hain
print(optimized_program.definition)
