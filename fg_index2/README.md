# Fear & Greed Index Dashboard ⚡️⚡️

A simple, elegant web dashboard built with **Reflex** that displays the latest **Crypto Fear and Greed Index** from the CoinMarketCap's API in real time. Created for educational purposes only 😉

![Screenshot](/fg_index2/assets/fgindex2.png)

## Features

- Real-time fetching of the latest Fear & Greed Index
- Dynamic **progress bar** (0–100) with intelligent color coding:
  - **Red** (< 25) → Extreme Fear  
  - **Orange** (25–50) → Fear/Neutral  
  - **Green** (> 50) → Greed/Extreme Greed
- Color-matched classification text and border
- Clean, centered layout optimized for mobile and desktop
- Full dark/light mode support with subtle translucent backgrounds
- Loading spinner and comprehensive error handling
- Built entirely in Python using Reflex (zero JavaScript)

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
