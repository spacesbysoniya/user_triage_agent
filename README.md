# Weather & Time Agent (`weather_time_agent`)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Google Cloud ADK](https://img.shields.io/badge/Platform-Google_Cloud_ADK_2.0-green.svg)](https://cloud.google.com/)

A lightweight, enterprise-grade Generative AI agent built using **Google Cloud's Agent Development Kit (ADK) 2.0**. This agent utilizes the advanced **Gemini 3.8 Flash** model to answer user inquiries regarding current time and weather conditions. 

It features native lifecycle callbacks to extract user telemetry, track session-level metadata, and output structured, search-ready JSON payloads directly to standard output for Google Cloud logging.

---

## 📌 Key Features

*   🤖 **Powered by Gemini 3.8 Flash:** Our most intelligent workhorse model, optimized for software engineering, agentic tasks, and critical multi-step reasoning.
*   🛠️ **Custom Tool Integration:** Integrated Python function execution for real-time weather retrieval.
*   📊 **Lifecycle Hooks:** Uses ADK 2.0 callbacks (`before_agent_callback`) to extract session attributes like `user_id` and browser language.
*   🪵 **Structured Logging:** Outputs clean, parser-friendly `jsonPayload` format to `stdout` for robust monitoring (compatible with Cloud Logging).

---

## 📂 Project Structure

```text
├── main.py          # Core agent implementation and entry point
├── requirements.txt # Python dependency file
└── README.md        # Project documentation

```

---

## ⚙️ Setup & Installation

### Prerequisites
*   Python **3.10** or higher.
*   A Google Cloud Project with the **Vertex AI API** enabled.
*   Authenticated Google Cloud credentials in your environment (e.g., `gcloud auth application-default login`).

### 1. Clone & Navigate
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2. Create Virtual Environment
Create and activate a virtual environment to manage dependencies securely:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

### 3. Install Dependencies
Save the following packages into a `requirements.txt` file and install them:
```text
google-adk-agents>=2.0.0
# Add other SDK dependencies as required
```
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the agent script locally:
```bash
python main.py
```

### Supported Queries
*   *"What is the weather like in New York?"*
*   *"Can you tell me the current weather report?"*

---

## 🔍 Code Deep-Dive

### Custom Tools
The agent uses standard Python type hints and docstrings to register tools. The `gemini-2.5-flash` model parses these docstrings to decide when to call the tool:

```python
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.
    
    Args:
        city (str): The name of the city.
    """
    # Returns structured weather data for supported locations...
```

### Lifecycle Observability Callback
At the start of every model invocation, the `before_agent_callback` hook intercepts the execution context to gather user telemetry and emit structured audit logs:

```python
def before_agent_callback(callback_context: Any) -> Optional[Any]:
    # Extracts agent name and session-level user metrics
    user_id = callback_context.session.user_id
    
    # Generates a search-ready JSON payload for Cloud Logging
    log_entry = {
        "event": "agent_invocation",
        "user_id": user_id,
        "agent_name": agent_name,
        "message": f"Agent invoked by User ID: {user_id}",
    }
    print(json.dumps(log_entry), file=sys.stdout)
```

---

## 📜 License

This project is licensed under the Apache License, Version 2.0. 

```text
Copyright 2026 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

---