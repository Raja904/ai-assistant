# AI Assistant with Internet and Google Suite Integration

This project is an AI Assistant built with LangChain and LangGraph, offering powerful capabilities to interact with the internet and your Google Suite (Gmail, Calendar). It leverages various tools to enable web search, URL navigation, email management, and calendar event handling, all powered by an intelligent agent.

## Features

* **Web Search Functionality:** Utilizes the Google Serper API for accurate and up-to-date internet searches.
* **URL Navigation:** Employs Browserless for seamless navigation and extraction of content from web pages.
* **Gmail Integration:** Perform actions like reading emails, drafting new emails, and sending emails directly from the assistant.
* **Google Calendar Integration:** Create and delete calendar events effortlessly.
* **Extensible Toolset:** The architecture allows for easy expansion by adding more tools in the `tools.py` file. For instance, you could integrate a Google Drive tool from LangChain's extensive list of [integrations and tools](https://python.langchain.com/v0.2/docs/integrations/tools/).
* **Intelligent Agent:** Built with LangGraph's React Agent, which follows a "Reasoning + Act" paradigm to intelligently decide which tools to use based on user queries.
* **Chat History with Checkpointing:** Leverages LangGraph's checkpointing feature (specifically `InMemory`) to maintain chat history for the current session. The history is cleared upon refreshing the page. (Note: Due to prompt template incompatibilities, `RunnableChatMemory` was not used with the `create_react_agent` implementation).
* **Simple Web Interface:** A user-friendly web application created with Streamlit allows for easy interaction with the AI assistant.

## How it Works

The core of this project is the `agent.py` file, where the intelligent agent is defined. This agent has access to a suite of tools that provide internet functionality (Web Search, URL Navigation) and Google Suite capabilities (Gmail, Calendar). The agent, implemented using LangGraph's React framework, analyzes user queries, reasons about the necessary steps, and then executes the appropriate tools to fulfill the request.

## Technologies Used

* **Python 3.12.1**
* **LangChain / LangGraph:** For agent orchestration and tool management.
* **Streamlit:** For the web user interface.
* **Google Serper API:** For web search.
* **Browserless:** For URL navigation.
* **Google Cloud APIs:** Gmail API, Calendar API.
* **Google OAuth 2.0:** For secure authentication with Google services.
* **pytz:** For timezone-aware date/time handling.

## Setup and Installation

Follow these steps to get your AI Assistant up and running locally:

### 1. Clone the Repository

```bash
!git clone https://github.com/Raja904/ai-assistant.git
```
```
cd ai-assistant
```
### 2. Create and Activate a Virtual Environment
```
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
### 3. Install Dependencies
Install all required Python packages:

```
pip install -r requirements.txt
```
### 4. Google Cloud Console Setup (OAuth 2.0)
This project requires authentication with Google APIs (Gmail and Calendar).

- Go to the Google Cloud Console.

- Create a new project or select an existing one.

- Navigate to APIs & Services > OAuth consent screen.

- Configure your OAuth consent screen (choose "External" user type if you're not an organizational user) and add necessary scopes:

https://console.cloud.google.com/apis/

- Navigate to APIs & Services > Credentials.

- Click + CREATE CREDENTIALS and choose OAuth client ID.

- Select Desktop app as the application type. Give it a name (e.g., AI Assistant Desktop).

- Click CREATE. This will generate your client ID and client secret.

- Click DOWNLOAD JSON to get your credentials.json file.

- Place this credentials.json file directly in the root directory of your project (same level as app.py).

- Enable APIs - In the Google Cloud Console, navigate to APIs & Services > Library 





### 5. Obtain token.json (First-Time Authentication)
The token.json file stores your user's authentication tokens. It will be generated automatically the first time you run the Streamlit app.

When you run the app for the first time, your web browser will automatically open, prompting you to log in with your Google account and grant the necessary permissions. After successful authentication, token.json will be saved in your project's root directory.

### 6. Environment Variables Setup
Create a file named .env in the root directory of your project (same level as app.py) and populate it with your API keys:

```
MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY"
SERPER_API_KEY="YOUR_SERPER_API_KEY"
BROWSERLESS_API_KEY="YOUR_BROWSERLESS_API_KEY"
```
MISTRAL_API_KEY: Obtain this from the Mistral AI website. You can also use other LLMs (e.g., OpenAI, Google Gemini) by changing the import statement and model instantiation in agent.py accordingly.

SERPER_API_KEY: Obtain this from Serper API.

BROWSERLESS_API_KEY: Obtain this from Browserless.io.

### 7. Run the Streamlit Application
```
streamlit run app.py
```
This will open the AI Assistant web interface in your default browser.

### 8. Initial Authentication (if token.json doesn't exist)
The first time you run streamlit run app.py (and if token.json is not present), the application will open a browser tab for Google authentication. Follow the prompts to log in and grant permissions. Upon success, the token.json file will be created in your project's root, and the app will continue loading.

## Extending Functionality
The tools.py file is where all the custom tools for your agent are defined. You can easily add more functionalities by creating new tools here.

Refer to LangChain's integrations and tools documentation for inspiration, such as integrating with Google Drive, Notion, or other services.

### Agent Architecture (React Graph)
The agent in this project is built using LangGraph's React (Reasoning + Act) agent implementation. This architecture allows the agent to:

- Reason: Analyze the user's input and its current state.

- Act: Choose and execute the appropriate tool based on its reasoning.

- Observe: Get the results from the tool's execution.

- Repeat: Continue this cycle until the user's request is fulfilled.



![Screenshot 2025-06-25 121418](https://github.com/user-attachments/assets/c32fdc53-c027-49c4-96b1-ab2c4bce9ab9)

This approach leads to more robust and capable agents that can handle complex multi-step tasks.


Feel free to open issues or submit pull requests if you have suggestions or find bugs!
