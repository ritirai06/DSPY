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

**Written By**: Riti Rai

