# UNICO XAI Bot

This repo implements the UNICO Python library with the X api to generate a completion from an UNICO agent
and post it to X UNICO official account.

## Get Started

1. **Install [pipenv](https://pipenv.pypa.io/en/latest/installation.html)**:
   Pipenv is used to handle the virtual environment and the necessary packages.

2. **Install necessary packages from `Pipfile`**

   ```bash
   pipenv install
   ```

3. **Rename `.env.example` to `.env`** then replace the content with your keys

    ```bash
   cp .env.example .env
   ```

4. **Replace `YOUR_AGENT_ID` with your agent**

5. **Point to production (Optional):** The script by default points to staging because our agent is in a staging account.
We recommend to use this environment only for develop purposes, and when all the changes are implemented, point to production

   ```python
   unico_client = UnicoApiClient(api_key=os.environ['UNICO_API_KEY']) # Remove base_url
   ```

6. **Execute the script**

   ```bash
   pipenv run python main.py
   ```
