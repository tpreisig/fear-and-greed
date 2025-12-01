import os
from dotenv import load_dotenv
import requests
import reflex as rx
from typing import Dict, Any

# Load environment variables from .env file
load_dotenv()

class State(rx.State):
    data: Dict[str, Any] = {}
    loading: bool = True
    error: str = ""

    def fetch_data(self):
        api_key = os.getenv("COINMARKETCAP_API_KEY")
        if not api_key:
            self.error = "API key not found. Ensure COINMARKETCAP_API_KEY is set in the .env file."
            self.loading = False
            return

        url = "https://pro-api.coinmarketcap.com/v3/fear-and-greed/historical?limit=1"
        headers = {"X-CMC_PRO_API_KEY": api_key}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            result = response.json()
            
            if "data" in result and result["data"]:
                self.data = result["data"][0]  # Latest data point
            else:
                self.error = "Unexpected API response format."
            
        except requests.RequestException as e:
            self.error = f"API request failed: {str(e)}"
        
        self.loading = False

# Main page component
def index_page() -> rx.Component:
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.heading("Fear & Greed Index", size="4", margin_left="25px"),
        rx.cond(
            State.loading,
            rx.spinner(size="3"),
            rx.cond(
                State.error,
                rx.text(State.error, color="red"),
                rx.vstack(
                    rx.text(f"Value: {State.data.get('value', 'N/A')}/100"),
                    rx.text(f"⏱️ Timestamp {State.data.get('timestamp', 'N/A')}"),
                    rx.text(f"Classification {State.data.get('value_classification', 'N/A')}", color=rx.color_mode_cond(dark="aqua", light="deeppink"), font_weight="bold"),
                    spacing="3",
                    padding="1em",
                    border="1px solid slateblue",
                    border_radius="8px",
                    background=rx.color_mode_cond(light="rgba(0,0,200,0.1)", dark="rgba(255,200,255,0.2)"),
                    box_shadow=f"0px 2px 5px {rx.color_mode_cond(light="rgba(0,0,0,0.2)", dark="rgba(255,255,255,0.4)")}",
                )
            )
        ),
        padding="2em",
        spacing="1",
        margin_left="auto",
        width="60%",
        min_width="300px"
        
    )

# App configuration
app = rx.App()
app.add_page(index_page, route="/", on_load=State.fetch_data)