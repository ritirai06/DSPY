# DSPy library import kar rahe hain
import dspy
# Evaluation metric import kar rahe hain jo program ki quality check karega
from metrics.evaluation import definition_match 

# Program ko optimize karne ka function
def optimize_program(program, trainset):
    # BootstrapFewShot optimizer initialize kar rahe hain
    # Ye few-shot examples use karke program ko better banata hai
    optimizer = dspy.BootstrapFewShot(metric=definition_match)
    # Program ko training data ke saath compile kar rahe hain
    # Isse optimized program milega jo better results dega
    return optimizer.compile(program, trainset=trainset)