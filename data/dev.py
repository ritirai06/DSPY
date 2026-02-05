# DSPy library import kar rahe hain
import dspy

# Development/Validation dataset - ye tuning decisions ke liye use hoga
# Optimizer is data ko nahi dekhta - sirf hum inspection ke liye use karte hain
devset = [
    # Validation examples - different from training
    dspy.Example(
        term="Deep Learning",
        definition="Deep learning is a subset of machine learning that uses neural networks with multiple layers to model complex patterns in data."
    ).with_inputs("term"),
    
    dspy.Example(
        term="Cloud Computing",
        definition="Cloud computing is the delivery of computing services including servers, storage, databases, networking, software, and analytics over the Internet."
    ).with_inputs("term"),
]
