# Utilising LLMs to perform stock predictions

## 1. Collecting Data

For all large language models, the data is the foundation of the systems, providing 

### 1.1 Data Sources

- yfinance, an opensource tool that uses Yahoo's publicly available APIs, intended for research. It provides access to a wide variety of stocks, etfs, and other securities (crypto). The docs can be seen here: https://yfinance-python.org/. 

### 1.2 Usage

#### 1.2.1 Setting up environment

Step 1. To use the system, first create a virtual environment,

    conda create --name <env_name> python=3.9 --file requirements.txt 

Step 2. Then activate your conda environment with,

    conda activate <env_name>

#### 1.2.1 Running System

Step 1. First alter the stocks you would like to download in main.py

    data_handler.download_ticker_grouped_json(<Ticker>, <filename>, start="YYYY-MM-DD", end="YYYY-MM-DD")

Step 2. Then execute the code with

    main.py

Step 3. View the recently downloaded and formatted files in 'datasets/historicals/json' or in 'datasets/historicals/csv'.