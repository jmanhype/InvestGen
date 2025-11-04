# InvestGen - AI-Driven Financial Advisor System

An advanced AI-powered platform that provides personalized financial advice, market analysis, and visual data representations. Built with Langflow for creating sophisticated financial analysis workflows.

## 🌟 Features

- **Semantic Routing**: Intelligently routes user queries to appropriate financial analysis workflows
- **Financial Data Fetching**: Real-time data from Financial Modeling Prep API
- **Automated Analysis**: Calculate key financial ratios and metrics
- **Data Visualization**: Generate interactive charts using Plotly
- **Database Storage**: Store analysis results and chat history in PostgreSQL
- **Custom Components**: Extensible Langflow components for financial operations

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL database
- [Langflow](https://github.com/logspace-ai/langflow) installed
- API keys:
  - OpenAI API key (for semantic routing)
  - Financial Modeling Prep API key (for market data)
  - Cohere API key (optional, for alternative semantic routing)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/InvestGen.git
   cd InvestGen
   ```

2. **Set up a PostgreSQL database**

   Create a PostgreSQL database with the following configuration (or customize as needed):
   ```bash
   # Using Docker (recommended)
   docker run --name investgen-db \
     -e POSTGRES_USER=langchain \
     -e POSTGRES_PASSWORD=langchain \
     -e POSTGRES_DB=langchain \
     -p 6024:5432 \
     -d postgres:15
   ```

3. **Configure environment variables**

   Copy the example environment file and add your API keys:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your actual credentials:
   ```env
   OPENAI_API_KEY=sk-proj-your-actual-key-here
   FMP_API_KEY=your-fmp-api-key-here
   DB_PASSWORD=your-secure-password
   ```

4. **Install Python dependencies**
   ```bash
   pip install langflow semantic-router plotly pandas sqlalchemy psycopg2-binary requests
   ```

5. **Import the workflow into Langflow**

   - Start Langflow: `langflow run`
   - Open Langflow UI (typically at http://localhost:7860)
   - Import the `InvestGen (1).json` workflow file
   - Configure component credentials using environment variables (not hardcoded!)

## 🔒 Security Best Practices

**⚠️ NEVER commit API keys or passwords to version control!**

This repository includes several security measures:

1. **`.env.example`**: Template for environment variables (safe to commit)
2. **`.env`**: Your actual credentials (automatically ignored by git)
3. **`.gitignore`**: Prevents accidental commits of sensitive files
4. **Empty credential fields**: All API keys in the workflow JSON should be empty - configure them in Langflow UI using environment variables

### How to Get API Keys

- **OpenAI**: https://platform.openai.com/api-keys
- **Financial Modeling Prep**: https://financialmodelingprep.com/developer/docs/
- **Cohere** (optional): https://dashboard.cohere.ai/api-keys

## 📊 Workflow Components

### Custom Components Included

1. **Semantic Router**: Routes queries to appropriate financial analysis workflows
2. **Fetch Financial Data**: Retrieves balance sheets, income statements, and cash flow data
3. **Analyze Financial Data**: Calculates financial ratios (current ratio, etc.)
4. **Visualize Financial Data**: Generates line and candlestick charts
5. **Store Analysis Results**: Saves results to PostgreSQL
6. **Store Message**: Maintains chat history in database

## 🗄️ Database Schema

The system creates tables dynamically based on your workflow configuration. Typical tables include:

- `analysis_results`: Financial analysis outputs
- `chat_messages`: Conversation history
- Custom tables defined in your workflow

## 🔧 Configuration

### Database Configuration File

If your workflow uses a JSON configuration file for database settings, create `db_config.json`:

```json
{
  "user": "langchain",
  "password": "your_password",
  "host": "localhost",
  "port": 6024,
  "database": "langchain"
}
```

**Important**: `db_config.json` is in `.gitignore` - never commit this file!

### Connection String Format

```
postgresql+psycopg2://user:password@host:port/database
```

Example:
```
postgresql+psycopg2://langchain:langchain@localhost:6024/langchain
```

## 📝 Usage Examples

1. **Start Langflow**:
   ```bash
   langflow run
   ```

2. **Load the workflow**: Import `InvestGen (1).json` in the UI

3. **Configure API keys**: In each component, reference environment variables instead of hardcoding

4. **Run analysis**:
   - Input a stock ticker (e.g., "TSLA", "AAPL")
   - Select analysis type (balance sheet, income statement, etc.)
   - View results and visualizations

## 🛠️ Development

### Adding New Components

1. Create a new custom component in Langflow
2. Follow the existing component patterns
3. Use environment variables for sensitive data
4. Test thoroughly before committing

### Testing

```bash
# Test database connection
python -c "from sqlalchemy import create_engine; import os; engine = create_engine(os.getenv('DATABASE_URL')); print('Connected!' if engine.connect() else 'Failed')"

# Test API keys (be careful not to expose keys in output)
python -c "import os; print('OpenAI key configured' if os.getenv('OPENAI_API_KEY') else 'Missing OpenAI key')"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Security reminder**: Always check your commits don't contain API keys or passwords!

## ⚠️ Troubleshooting

### Common Issues

1. **Database connection errors**
   - Verify PostgreSQL is running
   - Check credentials in `.env`
   - Ensure port 6024 (or your configured port) is not blocked

2. **API rate limiting**
   - Financial Modeling Prep has rate limits on free tier
   - Implement retry logic (already included in fetch component)

3. **Missing dependencies**
   ```bash
   pip install -r requirements.txt  # If available
   # Or install manually
   pip install langflow semantic-router plotly pandas sqlalchemy psycopg2-binary requests
   ```

## 📄 License

This project is open source. Please add an appropriate license file for your needs.

## 🙏 Acknowledgments

- Built with [Langflow](https://github.com/logspace-ai/langflow)
- Data provided by [Financial Modeling Prep](https://financialmodelingprep.com/)
- AI routing powered by [Semantic Router](https://github.com/aurelio-labs/semantic-router)

## 📧 Support

For issues and questions:
- Open an issue on GitHub
- Check the Langflow documentation
- Review the component code in the workflow JSON

---

**Remember**: Keep your API keys secret! Use environment variables, not hardcoded values.
