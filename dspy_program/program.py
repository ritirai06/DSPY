# DSPy library import kar rahe hain
import dspy
# Same package se DefineTerm signature import kar rahe hain
from .signature import DefineTerm

# Program create karne ka function
def get_program():
    # DSPy ka Predict module return kar rahe hain jo DefineTerm signature use karega
    # Ye module LLM se prediction generate karega
    return dspy.Predict(DefineTerm)