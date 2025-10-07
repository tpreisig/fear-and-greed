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
                self.data = result["data"][0]
                print(self.data)
            else:
                self.error = "Unexpected API response format."
            
        except requests.RequestException as e:
            self.error = f"API request failed: {str(e)}"
        
        self.loading = False

    @rx.var
    def color(self) -> str:
        value = self.data.get("value", 0)
        if value < 25:
            return "red"
        elif value <= 50:
            return "orange"
        return "green"

def index_page() -> rx.Component:
    return rx.vstack(
        rx.color_mode.button(position="top-right", margin="-4px"),
        rx.heading("Current Fear & Greed Index", size="3"),
        rx.cond(
            State.loading,
            rx.spinner(size="3"),
            rx.cond(
                State.error,
                rx.text(State.error, color="red"),
                rx.vstack(
                    rx.text(f"Value: {State.data.get('value', 'N/A')}/100"),
                    rx.progress(value=State.data.get("value", 0), max=100, color_scheme=State.color),
                    rx.text(f" ➡️ Classification: {State.data.get('value_classification', 'N/A')}", color=State.color),
                    rx.text(f"Timestamp ⏱️: {State.data.get('timestamp', 'N/A')}"),
                    spacing="2",
                    padding="1em",
                    border=f"1px solid {State.color}",
                    background=rx.color_mode_cond(dark="rgba(255,255,255,0.1)", light="rgba(255,200,200,0.1)"),
                    border_radius="8px",
                    width="100%"
                )
            )
        ),
        width="100%",
        padding="2em",
        spacing="2",
        max_width="600px",
        margin="auto"
    )

# App configuration
app = rx.App()
app.add_page(index_page, route="/", on_load=State.fetch_data)