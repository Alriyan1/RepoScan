# RepoScan - Medical Report Analysis System

A sophisticated AI-powered medical report analysis system that leverages multiple specialized medical agents to provide comprehensive health assessments. The system uses a multidisciplinary approach combining insights from cardiologists, psychologists, and pulmonologists to deliver holistic patient evaluations.

## 🏥 Features

- **Multi-Agent Analysis**: Three specialized medical AI agents working in parallel
  - **Cardiologist Agent**: Analyzes cardiac workup, ECG, blood tests, and echocardiogram results
  - **Psychologist Agent**: Assesses mental health aspects and psychological factors
  - **Pulmonologist Agent**: Evaluates respiratory health and pulmonary concerns
- **Multidisciplinary Team**: Combines all agent insights for comprehensive diagnosis
- **Parallel Processing**: Uses ThreadPoolExecutor for efficient concurrent analysis
- **Streamlit Web Interface**: User-friendly web application for report upload and analysis
- **Groq LLM Integration**: Powered by Llama 3.3 70B model for accurate medical analysis

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Groq API key
- Required Python packages (see Installation section)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd reposcan
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit langchain-core langchain-groq
   ```

3. **Set up your Groq API key**
   - Get your API key from [Groq Console](https://console.groq.com/)
   - Update the API key in `utils/agent.py` (line 20)

### Usage

#### Web Application (Recommended)

1. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to the provided URL

3. **Upload a medical report** (supports .txt and .pdf files)

4. **View the analysis** from all three medical specialists

#### Command Line Interface

1. **Prepare your medical report** as a text file

2. **Run the analysis**
   ```bash
   python main.py
   ```

3. **Check results** in the `results/final_diagnosis.txt` file

## 📁 Project Structure

```
reposcan/
├── app.py                 # Streamlit web application
├── main.py               # Command-line interface
├── utils/
│   └── agent.py         # AI agent implementations
├── results/              # Output directory for analysis results
├── Medical_Report.txt    # Sample medical report
├── Medical_Report_1.txt  # Additional sample reports
├── Medical_Report_2.txt
└── README.md            # This file
```

## 🧠 Architecture

### Agent System

The system implements a sophisticated multi-agent architecture:

1. **Base Agent Class**: Abstract base class with common functionality
2. **Specialized Agents**: 
   - `Cardiologist`: Focuses on cardiac health assessment
   - `Psychologist`: Evaluates mental health and psychological factors
   - `Pulmonologist`: Analyzes respiratory health
3. **Multidisciplinary Team**: Orchestrates and synthesizes all agent outputs

### Processing Flow

1. **Report Upload**: Medical report is uploaded via Streamlit or loaded from file
2. **Parallel Analysis**: All three agents analyze the report simultaneously
3. **Response Collection**: Individual agent responses are collected
4. **Synthesis**: Multidisciplinary team combines all insights
5. **Final Diagnosis**: Comprehensive analysis with 3 possible health issues and reasoning

## 🔧 Configuration

### Model Settings

- **Model**: Llama 3.3 70B Versatile
- **Temperature**: 0.0 (deterministic responses)
- **Provider**: Groq (high-performance inference)

### API Configuration

Update the API key in `utils/agent.py`:

```python
self.model = ChatGroq(
    api_key = "your_groq_api_key_here",
    model = "llama-3.3-70b-versatile",
    temperature=0.0
)
```

## 📊 Sample Output

The system generates comprehensive analysis including:

- **Individual Specialist Reports**: Detailed assessments from each medical domain
- **Final Diagnosis**: Consolidated list of 3 possible health issues with reasoning
- **Recommendations**: Next steps and management strategies

## 🛡️ Security & Privacy

- **Local Processing**: All analysis is performed locally through API calls
- **No Data Storage**: Medical reports are not permanently stored
- **Secure API**: Uses secure Groq API for AI model access

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## ⚠️ Disclaimer

This system is designed for educational and research purposes. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

## 🆘 Support

For issues, questions, or contributions:

1. Check existing issues in the repository
2. Create a new issue with detailed description
3. Contact the development team

## 🔮 Future Enhancements

- [ ] Support for more medical specialties
- [ ] Integration with medical databases
- [ ] Enhanced report visualization
- [ ] Multi-language support
- [ ] Batch processing capabilities
- [ ] Export to medical report formats

---

**Built with ❤️ for medical research and education**
