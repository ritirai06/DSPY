# DSPy Project - Term Definition Generator

## 📖 What is DSPy?

**DSPy (Declarative Self-Improving Python)** is a framework for building LLM systems without manually writing prompts.

Instead of prompt engineering, you:
- Define inputs and outputs
- Provide training examples
- Define a quality metric
- Let DSPy automatically generate and optimize prompts

### Prompts are Learned Artifacts

In DSPy, **prompts are not written** — they are learned automatically from your data and metrics.

---

## 🤔 Why DSPy Exists

Traditional prompt engineering has serious problems:

- ❌ **Prompts are brittle** - Small wording changes break behavior
- ❌ **Improvements are manual** and non-reproducible
- ❌ **No clear evaluation** or optimization loop

DSPy was created to solve this by **treating prompts like trainable parameters**, similar to weights in machine learning.

---

## ✨ What DSPy Does

DSPy:
- ✅ Tries multiple prompt variants internally
- ✅ Uses training examples as supervision
- ✅ Evaluates each prompt using a metric
- ✅ Automatically selects the best performing prompt

**You never directly control prompt wording.**

---

## 🚫 What DSPy Is NOT

DSPy is **NOT**:
- ❌ A chatbot framework
- ❌ A UI or frontend tool
- ❌ An agent framework
- ❌ A LangChain replacement
- ❌ A tool for "better writing"

**DSPy is a backend LLM systems engineering framework.**

---

## 🎯 Project Goal

In this project:
- User provides a **term**
- System returns a **clear and correct definition**
- **No prompt is written manually**

---

## 🔧 Project Structure

```
dspy-project/
│
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .env                   # API keys (git ignore)
├── main.py                # Entry point
│
├── dspy_program/
│   ├── __init__.py
│   ├── signature.py       # Input/Output definitions
│   ├── program.py         # DSPy modules (Predict)
│   └── optimizer.py       # Optimization logic
│
├── data/
│   ├── train.py           # Training examples
│   ├── dev.py             # Validation data
│   └── test.py            # Test data
│
└── metrics/
    └── evaluation.py      # Quality metrics
```

This structure is simple, clean, and production-friendly.

---

## 📋 Requirements

- Python 3.9+
- Ollama (free local LLM) or OpenAI API key
- Internet connection

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama (Free Option)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download Llama model
ollama pull llama3.2
```

---

## 🛠️ Step-by-Step Implementation

### Step 1: Define the Signature (Input / Output)

```python
# dspy_program/signature.py
import dspy

class DefineTerm(dspy.Signature):
    """Given a term, provide its definition."""
    
    term = dspy.InputField()
    definition = dspy.OutputField()
```

**Signature rules:**
- Only input and output fields
- No instructions
- No prompt language
- **Signature defines the contract, not behavior**

---

### Step 2: Create the Program

```python
# dspy_program/program.py
import dspy
from .signature import DefineTerm

def get_program():
    return dspy.Predict(DefineTerm)
```

**Use:**
- `Predict` for simple tasks
- `ChainOfThought` for reasoning tasks

---

### Step 3: Provide Training Data

```python
# data/train.py
import dspy

trainset = [
    dspy.Example(
        term="API",
        definition="An API is an interface that allows software systems to communicate."
    ).with_inputs("term"),

    dspy.Example(
        term="Neural Network",
        definition="A neural network is a computational model inspired by the human brain."
    ).with_inputs("term")
]
```

**DSPy learns from input–output examples, not from prompts.**

---

### Step 4: Define the Evaluation Metric

```python
# metrics/evaluation.py
def definition_match(example, prediction, trace=None):
    return example.definition.strip().lower() == prediction.definition.strip().lower()
```

**The metric decides:**
- Which output is good
- Which prompt performs best

⚠️ **Weak metrics produce weak systems.**

---

### Step 5: Optimize the Program

```python
# dspy_program/optimizer.py
import dspy
from metrics.evaluation import definition_match

def optimize_program(program, trainset):
    optimizer = dspy.BootstrapFewShot(metric=definition_match)
    return optimizer.compile(program, trainset=trainset)
```

**This is where DSPy:**
- Tries multiple prompts
- Evaluates them
- Selects the best one automatically

---

### Step 6: Run the System

```python
# main.py
import dspy
import os
from dotenv import load_dotenv
from dspy_program.program import get_program
from dspy_program.optimizer import optimize_program
from data.train import trainset

load_dotenv()

# Configure with free Ollama model
dspy.configure(
    lm=dspy.LM(model="ollama/llama3.2")
)

program = get_program()
optimized_program = optimize_program(program, trainset)

result = optimized_program(term="Artificial Intelligence")
print(result.definition)
```

---

## 🔄 Complete DSPy Flow (One Line)

```
Signature → Program → Data → Metric → Optimizer → Learned Prompt
```

**Prompts are outputs, not inputs.**

---

## ▶️ How to Run

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

---

## ✅ What You SHOULD Do in DSPy

- ✅ Define clear input and output fields
- ✅ Provide real, representative examples
- ✅ Design strong evaluation metrics
- ✅ Think in terms of optimization, not wording

---

## ❌ What You Should NOT Do in DSPy

- ❌ Do not write prompts
- ❌ Do not tweak wording manually
- ❌ Do not put instructions inside signatures
- ❌ Do not expect good results without data
- ❌ Do not use DSPy for simple chatbots

---

## 💡 Key Mental Model

> **Anything you would normally put into a prompt,  
> in DSPy you put into data or metrics.**

---

## 🎓 Final Summary

**DSPy is not prompt engineering.  
DSPy is LLM systems engineering.**

If you care about:
- ✅ **Accuracy**
- ✅ **Reproducibility**
- ✅ **Scalability**

**DSPy is the right tool.**

---

## 🔑 Features

✅ **Completely Free** - Uses Ollama local model (no API costs)  
✅ **Automatic Optimization** - Learns best prompts from examples  
✅ **Type-safe** - Input/Output signatures clearly defined  
✅ **Modular Design** - Clean, production-ready structure  
✅ **Well Documented** - Detailed comments in every file  

---

## 🛠️ Technologies Used

- **DSPy** - Language Model programming framework
- **Ollama** - Local LLM inference (Llama 3.2 model)
- **Python-dotenv** - Environment variables management

---

## 📊 Project Status

✅ Project structure created  
✅ All modules implemented  
✅ Free LLM integrated (Ollama)  
✅ Working end-to-end  
✅ Fully documented with comments  

---

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
# DSPY
