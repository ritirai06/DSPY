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

# .env file se environment variables load kar rahe hain (API key ke liye)
load_dotenv()

# DSPy ko configure kar rahe hain - Ollama local model set kar rahe hain
# Ollama free hai aur local machine pe chalti hai
dspy.configure(
    lm=dspy.LM(model="ollama/llama3.2")  # Ollama ka llama3.2 model use kar rahe hain (completely free)
)

# Program ko initialize kar rahe hain
program=get_program()
# Optimized program ko training data ke saath optimize kar rahe hain
optimized_program=optimize_program(program, trainset)

# Optimized program ko call kar rahe hain 'Artificial Intelligence' term ke liye
result=optimized_program(term='Artificial Intelligence')

# Result print kar rahe hain
print("\n" + "="*50)
print("TERM: Artificial Intelligence")
print("="*50)

# Agar Chain of Thought use ho raha hai, to reasoning bhi show hogi
if hasattr(result, 'rationale'):
    print(f"\nReasoning: {result.rationale}")
    
print(f"\nDefinition: {result.definition}")
print("="*50)
result=optimized_program(term='Deep Learning')  
result=optimized_program(term='grapes') # Ye term training data mein nahi hai, isliye model ko generalize karna padega
# Result ki definition print kar rahe hain
print(result.definition)