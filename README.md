# SloGen 🚀 - AI-Powered Marketing Slogan Generator

**SloGen** is a modern, locally-hosted AI web application that generates creative, professional, and catchy marketing slogans. Unlike generic text generators, SloGen is fine-tuned specifically for marketing copy, balancing creativity with strict keyword adherence.

## 🌟 Features

* **Smart AI Engine:** Powered by **Qwen2.5-1.5B-Instruct**, a state-of-the-art Small Language Model (SLM).
* **Triple Generation:** Generates **3 unique slogan options** at once so you can choose the best fit.
* **Fine-Tuned Performance:** Custom-trained using **LoRA (Low-Rank Adaptation)** on a dataset of 300+ high-quality slogans.
* **GPU Accelerated:** Optimized for NVIDIA GPUs (RTX 4070 tested) using mixed-precision (fp16) for blazing-fast generation.
* **Modern UI:** Features Glassmorphism design, floating animations, and a history sidebar.
* **Zero-Reload Experience:** Built with AJAX/Fetch API for instant results without refreshing the page.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3 (Animations, Glassmorphism), JavaScript (Fetch API)
* **Backend:** Python, Flask
* **AI/ML Frameworks:** PyTorch, Hugging Face Transformers, PEFT (Parameter-Efficient Fine-Tuning)
* **Model:** Qwen/Qwen2.5-1.5B-Instruct (Base) + Custom LoRA Adapters

---
## Live Demo
you can reach live demo at https://chancelor-slogen-demo.hf.space/

## 📦 Installation & Local Setup

If you want to run this project on your own machine, follow these steps.

### Prerequisites
* **OS:** Windows 10/11 or Linux
* **Python:** Version 3.10 or higher
* **GPU:** NVIDIA GPU with 6GB+ VRAM recommended (Runs slower on CPU)

### Quick Start (Copy & Paste)
Run these commands in your terminal (PowerShell or CMD) to set up everything at once:

```bash
### 1. Clone the repository and enter the folder
git clone [https://github.com/LordChancelor/SloGen-Slogan-Generator.git](https://github.com/LordChancelor/SloGen-Slogan-Generator.git)
cd SloGen

### 2. Create and Activate Virtual Environment (Windows)
python -m venv venv
.\venv\Scripts\activate

### 3. Install Dependencies
# First, install PyTorch with CUDA 12.1 support (Required for NVIDIA GPUs)
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)

### Then, install the AI, Web, and Optimization libraries
pip install transformers flask peft accelerate datasets bitsandbytes




