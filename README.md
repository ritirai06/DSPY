# DSPy Project - Term Definition Generator

## 📖 Project Overview
This is a DSPy-based AI project that generates definitions for any given term. The project uses the DSPy framework to optimize Language Models automatically.

## 🎯 What's Happening?

### Flow of Execution:
```
User Input (term)
    ↓
Signature (Defines Input/Output contract)
    ↓
Program (Predict module - Calls the LLM)
    ↓
Optimizer (Learns from training examples to improve the program)
    ↓
Optimized Program (Generates better prompts)
    ↓
Final Output (Definition of the term)
```

## 🔧 Project Structure

```
dspy-project/
│
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .env                   # API keys (git ignore)
│
├── main.py                # Entry point - program starts here
│
├── dspy_program/
│   ├── __init__.py
│   ├── signature.py       # Defines Input/Output structure
│   ├── program.py         # Sets up DSPy Predict module
│   └── optimizer.py       # Optimizes program using training data
│
├── data/
│   ├── train.py           # Training examples (API, Neural Network definitions)
│   ├── dev.py             # Validation data (future use)
│   └── test.py            # Test data (future use)
│
└── metrics/
    └── evaluation.py      # Quality check metric - validates predictions
```

## 🚀 How It Works?

### 1. **Signature (signature.py)**
- Defines the structure of input and output
- `term` → Input field (the term to define)
- `definition` → Output field (generated definition)

### 2. **Program (program.py)**
- Uses DSPy's `Predict` module
- Generates predictions from LLM according to the signature

### 3. **Training Data (data/train.py)**
- Provides example definitions (API, Neural Network)
- Helps the model learn from examples

### 4. **Optimizer (optimizer.py)**
- Uses the `BootstrapFewShot` technique
- Improves the program based on training examples
- Automatically generates better prompts

### 5. **Evaluation Metric (metrics/evaluation.py)**
- Compares generated definition with expected definition
- Tells the optimizer how accurate the prediction is

### 6. **Main Program (main.py)**
- Integrates all components together
- Configures the LLM (Ollama - free local model)
- Optimizes the program
- Generates definition for input term

## 💻 Installation & Setup

### Prerequisites
```bash
# Python 3.8 or higher
python3 --version

# Install Ollama (free local LLM)
curl -fsSL https://ollama.com/install.sh | sh

# Download Llama model
ollama pull llama3.2
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## ▶️ How to Run the Program

```bash
cd dspy-project
python3 main.py
```

### Output Example:
```
Artificial intelligence is the development of computer systems 
able to perform tasks that typically require human intelligence, 
such as visual perception, speech recognition, decision-making, 
and language translation.
```

## 🔑 Features

✅ **Completely Free** - Uses Ollama local model (no API costs)  
✅ **Automatic Optimization** - Automatically improves from training examples  
✅ **Type-safe** - Input/Output signatures clearly defined  
✅ **Modular Design** - Each component organized in separate files  
✅ **Well Documented** - Detailed comments in every file  

## 🛠️ Technologies Used

- **DSPy** - Language Model programming framework
- **Ollama** - Local LLM inference (Llama 3.2 model)
- **Python-dotenv** - Environment variables management

## 📝 Current Model
- **Model**: Ollama Llama 3.2
- **Type**: Local (runs on your machine)
- **Cost**: Free
- **Performance**: Good for definition generation

## 🎓 Learning Points

1. **DSPy Framework** - Using LLMs programmatically
2. **Signature System** - Input/Output contracts
3. **Optimization** - Automatic prompt improvement
4. **Few-shot Learning** - Learning from examples
5. **Local LLMs** - Free alternatives to paid APIs

## 🔄 How DSPy Optimization Works

1. Provide training examples
2. DSPy automatically generates prompts
3. Tests on examples
4. Selects best performing prompts
5. Optimized program ready!

## 📊 Project Status
✅ Project structure created  
✅ All modules implemented  
✅ Free LLM integrated (Ollama)  
✅ Working end-to-end  
✅ Fully documented with comments  

## 🤝 Contributing
Feel free to contribute with issues and improvements on GitHub!

---
**Made with DSPy & Ollama 🚀**

Prompts are learned artifacts

Why DSPy Exists

Traditional prompt engineering has serious problems:

Prompts are brittle

Small wording changes break behavior

Improvements are manual and non-reproducible

No clear evaluation or optimization loop

DSPy was created to solve this by treating prompts like trainable parameters, similar to weights in machine learning.

What DSPy Does

DSPy:

Tries multiple prompt variants internally

Uses training examples as supervision

Evaluates each prompt using a metric

Automatically selects the best performing prompt

You never directly control prompt wording.

What DSPy Is NOT

DSPy is NOT:

A chatbot framework

A UI or frontend tool

An agent framework

A LangChain replacement

A tool for “better writing”

DSPy is a backend LLM systems engineering framework.

Project Goal (Example)

In this project:

User provides a term

System returns a clear and correct definition

No prompt is written manually

Project Structure
dspy-project/
│
├── README.md
├── requirements.txt
├── main.py
│
├── dspy_program/
│   ├── signature.py
│   ├── program.py
│   └── optimizer.py
│
├── data/
│   └── train.py
│
└── metrics/
    └── evaluation.py


This structure is simple, clean, and production-friendly.

Requirements

Python 3.9+

OpenAI or Anthropic API key

Internet connection

Install dependencies
pip install dspy-ai

Step 1: Define the Signature (Input / Output)
# dspy_program/signature.py
import dspy

class DefineTerm(dspy.Signature):
    term: str
    definition: str


Signature rules:

Only input and output fields

No instructions

No prompt language

Signature defines the contract, not behavior.

Step 2: Create the Program
# dspy_program/program.py
import dspy
from .signature import DefineTerm

def get_program():
    return dspy.Predict(DefineTerm)


Use:

Predict for simple tasks

ChainOfThought for reasoning tasks

Step 3: Provide Training Data
# data/train.py
import dspy

trainset = [
    dspy.Example(
        term="API",
        definition="An API is an interface that allows software systems to communicate."
    ).with_inputs("term"),

    dspy.Example(
        term="Database",
        definition="A database stores and manages structured data."
    ).with_inputs("term")
]


DSPy learns from input–output examples, not from prompts.

Step 4: Define the Evaluation Metric
# metrics/evaluation.py
def definition_match(example, prediction):
    return example.definition.lower() in prediction.definition.lower()


The metric decides:

Which output is good

Which prompt performs best

Weak metrics produce weak systems.

Step 5: Optimize the Program
# dspy_program/optimizer.py
import dspy
from metrics.evaluation import definition_match

def optimize_program(program, trainset):
    optimizer = dspy.BootstrapFewShot(metric=definition_match)
    return optimizer.compile(program, trainset=trainset)


This is where DSPy:

Tries multiple prompts

Evaluates them

Selects the best one automatically

Step 6: Run the System
# main.py
import dspy
from dspy_program.program import get_program
from dspy_program.optimizer import optimize_program
from data.train import trainset

dspy.configure(
    lm=dspy.OpenAI(model="gpt-4o-mini")
)

program = get_program()
optimized_program = optimize_program(program, trainset)

result = optimized_program(term="Artificial Intelligence")
print(result.definition)

Complete DSPy Flow (One Line)
Signature → Program → Data → Metric → Optimizer → Learned Prompt


Prompts are outputs, not inputs.

What You SHOULD Do in DSPy

Define clear input and output fields

Provide real, representative examples

Design strong evaluation metrics

Think in terms of optimization, not wording

What You Should NOT Do in DSPy

Do not write prompts

Do not tweak wording manually

Do not put instructions inside signatures

Do not expect good results without data

Do not use DSPy for simple chatbots

Key Mental Model

Anything you would normally put into a prompt,
in DSPy you put into data or metrics.

Final Summary

DSPy is not prompt engineering.
DSPy is LLM systems engineering.

If you care about:

Accuracy

Reproducibility

Scalability

DSPy is the right tool.# DSPY
