# text-to-sql
Text-to-SQL Agent: Agentic AI Application
A natural language interface for querying SQL databases and creating visualizations using AI agents powered by LangChain and OpenAI.

🚀 Live Demo on Streamlit Cloud 🚀

What This Project Does
This application enables users to interact with an e-commerce SQL database using natural language queries. It leverages two specialized AI agents:

SQL Agent: Converts natural language questions into SQL queries and retrieves data
Python Agent: Generates interactive Plotly visualizations based on query results
The system maintains conversation context, allowing for follow-up questions and iterative data exploration without repeating information.

Architecture
┌───────────────────────────────────────────────────────────────────-──┐
│                         Streamlit Web UI                             │
│                      (streamlit_app.py)                              │
└────────────┬────────────────────────────────────────┬────────────────┘
             │                                        │
             │ User Query                             │ Display Results
             ▼                                        │
┌─────────────────────────────────────────────────────┴────────────────┐
│                      Query Router                                    │
│                                                                      │
│  Checks for keywords: "plot", "graph", "chart", "diagram"            │
└────────────┬──────────────────────────────────┬──────────────────────┘
             │                                  │
    Visualization                        Text Query
    Keywords Found                       Only
             │                                  │
             ▼                                  ▼
┌─────────────────────────┐        ┌─────────────────────────┐
│    SQL Agent            │        │    SQL Agent            │
│  (src/llm_agent.py)     │        │  (src/llm_agent.py)     │
│                         │        │                         │
│  • OpenAI GPT-4         │        │  • OpenAI GPT-4         │
│  • LangChain            │        │  • LangChain            │
│  • SQLDatabaseToolkit   │        │  • SQLDatabaseToolkit   │
└──────────┬──────────────┘        └───────────┬─────────────┘
           │                                   │
           │ SQL Query                         │ SQL Query
           ▼                                   │
┌─────────────────────────┐                    │
│   SQLite Database       │◄───────────────────┘
│   (ecommerce)           │
│                         │
│  Tables:                │
│  • users                │
│  • orders               │
│  • order_items          │
│  • products             │
│  • inventory_items      │
│  • distribution_centers │
│  • events               │
└──────────┬──────────────┘
           │
           │ Query Results
           ▼
┌─────────────────────────┐
│   Python Agent          │
│  (src/llm_agent.py)     │
│                         │
│  • OpenAI GPT-4         │
│  • PythonREPLTool       │
│  • Plotly Library       │
└──────────┬──────────────┘
           │
           │ Python Code
           │ (Plotly)
           ▼
┌─────────────────────────┐
│  Visualization Engine   │
│  (src/helper.py)        │
│                         │
│  • Code extraction      │
│  • Safe execution       │
│  • Chart rendering      │
└─────────────────────────┘
           │
           │ Interactive Chart
           ▼
      [Display to User]

┌─────────────────────────┐
│  Conversation Memory    │
│  (SQLChatMessageHistory)│
│                         │
│  • session_history.db   │
│  • Context preservation │
└─────────────────────────┘

Project Structure
text-to-sql-agent/
├── streamlit_app.py     # Main Streamlit application (entry point)
├── setup_database.py    # Database initialization script
├── .python-version      # Python 3.10 specification for version managers
├── .env.example         # Environment variables template
├── .env                 # Your local secrets (not in git)
├── .gitignore           # Git ignore file
├── requirements.txt     # Python dependencies
├── ecommerce            # SQLite database file (created by setup script)
├── session_history.db   # Conversation history storage
├── src/                 # Supporting modules
│   ├── __init__.py      # Package initialization
│   ├── config.py        # Configuration loader (.env + Streamlit secrets)
│   ├── helper.py        # Display utilities
│   └── llm_agent.py     # AI agent initialization (SQL + Python)
├── data/                # CSV files for database
│   ├── users.csv        # 100,000 user records
│   ├── orders.csv       # 125,530 order records
│   ├── order_items.csv  # 181,891 order item records
│   ├── products.csv     # 29,120 product records
│   ├── inventory_items.csv # 246,386 inventory records
│   ├── distribution_centers.csv # 10 distribution center records
│   └── events.csv       # 1,012,244 event records
└── README.md

Note: This structure follows Streamlit best practices with streamlit_app.py at the root for automatic detection during deployment.

Testing Locally
Prerequisites
Python 3.10 (recommended for compatibility)
OpenAI API key
Git
Setup Instructions
Clone the repository

git clone <repository-url>
cd text-to-sql-agent
Create virtual environment with Python 3.10

# If you have Python 3.10 installed
python3.10 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Verify Python version
python --version  # Should show Python 3.10.x
⚠️ Important: Always use a virtual environment to avoid conflicts with system Python packages.

Install dependencies in virtual environment

# Ensure venv is activated (you should see (venv) in your prompt)
pip install --upgrade pip
pip install -r requirements.txt
💡 Pro Tip: All Python commands should be run inside the activated virtual environment.

Configure secrets (Local)

Copy the example environment file and add your OpenAI API key:

cp .env.example .env
Edit .env and add your actual API key:

OPENAI_API_KEY=sk-your-actual-api-key-here
LLM_MODEL_NAME=gpt-4.1-2025-04-14
DATABASE=ecommerce
⚠️ Important: The .env file is already in .gitignore and will not be committed to version control.

Set up the database (REQUIRED)

⚠️ Important: The database file is not included in the repository due to its large size (144MB). You must create it locally:

# Ensure venv is activated (you should see (venv) in your prompt)
python setup_database.py
This will create the ecommerce database file with 7 tables populated from the CSV files in the data/ directory:

users: 100,000 records
orders: 125,530 records
order_items: 181,891 records
products: 29,120 records
inventory_items: 246,386 records
distribution_centers: 10 records
events: 1,012,244 records
Note: The ecommerce database file is in .gitignore to avoid GitHub's 100MB file limit.

Run the application in virtual environment

# Ensure venv is activated (you should see (venv) in your prompt)
streamlit run streamlit_app.py
Access the application

Open your browser to http://localhost:8501

Testing Tips
Test with simple queries first: "Show me the top 10 users by orders"
Try visualization queries: "Plot the distribution of orders by month"
Test conversation context: Ask follow-up questions
Verify error handling: Try ambiguous or invalid queries

Deploying to Streamlit Community Cloud
Prerequisites
GitHub account
Streamlit Community Cloud account (free at share.streamlit.io)
OpenAI API key
Deployment Steps
Push to GitHub

git add .
git commit -m "Prepare for Streamlit deployment"
git push origin main
Deploy on Streamlit Cloud

a. Go to share.streamlit.io

b. Click "New app"

c. Connect your GitHub repository

d. Configure deployment:

Repository: Your repo URL
Branch: main
Main file path: streamlit_app.py (auto-detected)
Python version: 3.9+
Configure Secrets

In Streamlit Cloud app settings:

a. Click "Advanced settings" → "Secrets"

b. Add secrets in TOML format:

OPENAI_API_KEY = "sk-your-actual-api-key-here"
LLM_MODEL_NAME = "gpt-4.1-2025-04-14"
DATABASE = "ecommerce"
Deploy & Database Considerations

For Demo/Testing (Current Setup):

App automatically creates SQLite database from CSV files on first launch
Shows "Setting up database for first time..." spinner
⚠️ Limitation: Streamlit Cloud has ephemeral storage - database recreated on app restarts
For Production (Recommended):

Streamlit Cloud doesn't provide persistent database hosting. For production, consider:

Option 1: Cloud Database Services

PostgreSQL: AWS RDS, Google Cloud SQL, Supabase
MySQL: PlanetScale, Railway, DigitalOcean
Serverless: Neon, Xata, Turso (SQLite-compatible)
Option 2: Update Connection String

# In src/config.py, replace SQLite with cloud database
DATABASE_URL = get_config("DATABASE_URL", "postgresql://user:pass@host:5432/dbname")
# Then update src/llm_agent.py:
db = SQLDatabase.from_uri(DATABASE_URL)
Option 3: Data Persistence Services

Use external APIs for data storage
Connect to existing company databases
Cloud data warehouses (BigQuery, Snowflake)
Current setup works for demos - use external DB for production!

Secrets Management Guide
How Configuration Works
The application uses a unified configuration system via src/config.py that automatically handles both local and cloud deployments:

Priority Order:

Environment variables from .env file (preferred for local development)
Streamlit secrets (for Streamlit Cloud deployment)
Default values
Note: You may see a "No secrets files found" message in local development - this is normal and can be ignored when using .env files.

Local Development: .env File
Create your .env file:

cp .env.example .env
Add your credentials:

OPENAI_API_KEY=sk-your-actual-api-key-here
LLM_MODEL_NAME=gpt-4.1-2025-04-14
DATABASE=ecommerce
Run the app:

streamlit run streamlit_app.py
The .env file is automatically loaded by src/config.py and is excluded from git by .gitignore.

Streamlit Cloud Deployment: Secrets Manager
Deploy your app on share.streamlit.io

Add secrets in app settings → Advanced settings → Secrets:

OPENAI_API_KEY = "sk-your-production-key"
LLM_MODEL_NAME = "gpt-4.1-2025-04-14"
DATABASE = "ecommerce"
Deploy - No code changes needed! The same src/config.py automatically uses Streamlit secrets in cloud.

Usage Examples
Text Queries
"Show me the top 10 customers by total order value"
"What is the average order value by month?"
"How many returns do we have this quarter?"
Visualization Queries
"Plot the distribution of orders by state"
"Create a chart showing monthly revenue trends"
"Graph the top 10 products by sales"
Follow-up Queries
User: "Show me total sales by category"
Agent: [Returns data]
User: "Now plot that as a bar chart"  # Uses context from previous query
Troubleshooting
Common Issues
1. "No OpenAI API key found"

Verify .env file exists and contains OPENAI_API_KEY
Check API key format starts with sk-
Ensure you ran cp .env.example .env and added your real key
2. "Database connection error"

Ensure SQLite database exists and is accessible
Check DATABASE value in .env file matches your database name
3. "Module not found" errors

Run pip install -r requirements.txt
Verify virtual environment is activated
4. Visualization not rendering

Check that query includes visualization keywords
Verify Plotly is installed
Look for Python code syntax errors in logs
5. Agent not responding

Check OpenAI API quota/billing
Verify model name is correct
Review Streamlit terminal logs for errors
6. Python version conflicts

Use Python 3.10 (recommended): python3.10 -m venv venv
Always activate virtual environment before running
Check version: python --version should show 3.10.x
If issues persist, delete venv/ and recreate it
7. "Wrong Python packages installed"

Ensure virtual environment is activated (you should see (venv) in terminal)
Reinstall in venv: pip install -r requirements.txt
Never install packages globally with sudo pip install
Dependencies
The project uses 12 core dependencies (all others are transitive):

streamlit - Web interface framework
Unidecode - Text normalization for queries
langchain==0.2.10 - LLM agent framework
langchain-community==0.2.5 - SQL agents and chat models
langchain-experimental==0.0.61 - Python REPL tool
langchain-openai==0.1.17 - OpenAI chat models (compatible version)
langchainhub==0.1.20 - LangChain prompt templates
SQLAlchemy - Database ORM for SQL operations
openai==1.30.5 - OpenAI API client (compatible version)
python-dotenv - Environment variable management
plotly - Interactive visualizations
pandas - Data manipulation (required for database setup)