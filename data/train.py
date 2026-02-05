# DSPy library import kar rahe hain
import dspy
# Training dataset - ye examples model ko sikhane ke liye use honge
trainset=[
    # Pehla training example - API ki definition
    dspy.Example(
        term="API",  # Term jo define karna hai
        definition="An API, or Application Programming Interface, is a set of rules and protocols that allows different software applications to communicate with each other. It defines how requests and responses should be formatted, and what actions can be performed, enabling developers to integrate and utilize functionalities from other services or platforms without needing to understand their internal workings."  # API ki definition
    ).with_inputs("term"),  # Input field specify kar rahe hain - "term" input hai
    
    # Doosra training example - Neural Network ki definition
    dspy.Example(
        term="Neural Network",  # Term jo define karna hai
        definition="A neural network is a computational model inspired by the structure and function of the human brain. It consists of layers of interconnected nodes, or neurons, that process and transmit information. Neuralnetworks are widely used in artificial intelligence and machine learning for tasks such as image recognition, natural language processing, and predictive modeling."  # Neural Network ki definition
    ).with_inputs("term")  # Input field specify kar rahe hain
]