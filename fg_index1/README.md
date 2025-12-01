# Fear & Greed Index Dashboard ⚡️⚡️

A simple, elegant web dashboard built with **Reflex** that displays the latest **Crypto Fear and Greed Index** from the CoinMarketCap's API in real time. Created for educational purposes only 😉

![Screenshot](/fg_index1/assets/fgindex1.png)

## Features

- Fetches the most recent Fear & Greed Index value and classification
- Responsive dark/light mode support with dynamic styling
- Clean, modern UI with loading spinner and error handling
- Automatic data fetch on page load
- Fully written in Python using Reflex (no JavaScript required)

## Prerequisites

- Python 3.8 or higher
- A free or paid **CoinMarketCap Pro API key**[](https://coinmarketcap.com/api/)

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/fear-and-greed-reflex.git
cd fear-and-greed-reflex
````

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
3. **Install dependencies**

```bash
pip install reflex requests python-dotenv
```
4. **Set up your API key**
   Create a `.env` file in the project root\
   ‼️ but never commit it to version control:
```bash
COINMARKETCAP_API_KEY=your_api_key
```
## Running Locally
```
reflex run
```
The app will start at `http://localhost:3000` (frontend) and `http://localhost:8000` (backend)`

## API Reference
**[Documentation for API](https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide)**\
The dashboard uses CoinMarketCap's Fear and Greed Historical endpoint:
```
GET https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical?limit=1
```
