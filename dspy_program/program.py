# DSPy library import kar rahe hain
import dspy
# Same package se DefineTerm signature import kar rahe hain
from .signature import DefineTerm

# Program create karne ka function
def get_program():
    # DSPy ka ChainOfThought module return kar rahe hain jo DefineTerm signature use karega
    # ChainOfThought module LLM ko step-by-step reasoning karne ke liye force karta hai
    # Pehle reasoning generate hogi, phir final answer
    return dspy.ChainOfThought(DefineTerm)