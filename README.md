# SQL_NLP

SQL_NLP is a project that leverages Natural Language Processing (NLP) to interact with SQL databases using plain English queries. This tool translates user-friendly language into SQL commands, making database management accessible to non-technical users.

## Requirements

- Python 3.8+
- Access to the database
- Gemini API Keys

## Setup

1. **Clone the repository:**
     ```bash
     git clone https://github.com/risshi-dev/NL_SQL_GENERATOR.git
     cd SQL_NLP
     ```

2. **Install dependencies:**
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure your database:**
     - Update the database connection string in `.env` or you can input it in command line as asked.

4. **Configure you Gemini Keys:**
     - Generate API keys using Google Studio, and export it in your system.

## How It Works

1. **Pre-Processing:** As you enter your database credentials, all tables schemas are fetched, and stored in vector database(ChromaDb).
2. **Input:** We first pass your query to our RAG pipeline to fetch table schemas which matches your query, and then create a prompt with table schema context and your input.
3. **Execution:** The generated SQL query is executed against the connected database.
4. **Output:** Results are displayed in a readable format.

