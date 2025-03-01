# SmartBucks App Backend

This is the backend for the SmartBucks app, an AI-powered application designed to provide insights and recommendations on how to budget effectively. The backend is built using Flask and utilizes MySQL and PostgreSQL databases.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **MySQL**: An open-source relational database management system.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **XAI**: Explainable AI techniques to ensure transparency in AI decision-making.
- **Gemini**: Advanced AI models for financial insights.
- **OpenAI**: State-of-the-art AI models for natural language processing.
- **DeepSeek**: AI algorithms for deep learning and data analysis.

## Features

- **Budget Recommendations**: Provides personalized budgeting advice based on user data.
- **Financial Insights**: Offers insights into spending habits and financial health.
- **Explainable AI**: Ensures that AI recommendations are transparent and understandable.
- **Multi-Database Support**: Utilizes both MySQL and PostgreSQL for data storage and management.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/smartbucks-backend.git
   cd smartbucks-backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the databases (MySQL and PostgreSQL) and configure the connection settings in the `config.py` file.

5. Run the Flask application:
   ```bash
   flask run
   ```

## Usage

Once the backend is running, it will be accessible at `http://127.0.0.1:5000/`. You can use this endpoint to interact with the SmartBucks app and receive budgeting recommendations and financial insights.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
