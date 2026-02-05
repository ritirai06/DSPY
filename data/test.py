# DSPy library import kar rahe hain
import dspy

# Test dataset - final evaluation ke liye
# Is data ko kabhi optimizer ya tuning mein use nahi karna
# Ye sirf final results trust karne ke liye hai
testset = [
    # Completely unseen examples
    dspy.Example(
        term="Blockchain",
        definition="Blockchain is a distributed ledger technology that maintains a secure and decentralized record of transactions across multiple computers."
    ).with_inputs("term"),
    
    dspy.Example(
        term="Quantum Computing",
        definition="Quantum computing is a type of computation that harnesses quantum mechanical phenomena to process information in fundamentally different ways than classical computers."
    ).with_inputs("term"),
    
    # Negative examples - should be rejected
    dspy.Example(
        term="Banana",
        definition="SHOULD_BE_REJECTED"
    ).with_inputs("term"),
]
