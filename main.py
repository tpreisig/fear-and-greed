import reflex as rx
import os
import datetime from datetime

# Backend
class State(rx.State):
    data: List[Dict[str, Any]] = []
    loading: bool = True
    error: str = ""

# Frontend
@rx.page("/", "Fear and Greed Index")
def index_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.color_mode.button(position="top-right"),
            rx.heading("Fear and Greed Index", size="7"),
            rx.cond(
                State.loading,
                rx.spinner(size="3"),
                rx.cond(
                    State.error,
                    rx.text(State.error, color="red"),
                    rx.hstack(
                        rx.heading("Result"),
                        spacing="4",
                        width="100%",
                        border="1px solid slateblue",
                        color="slateblue"
                    ),
                )
            ),
            margin_top="-30vh"  
        ),
        width="70%",
        border="1px solid blue",
        margin="5vh auto",
        min_height="60vh",
        border_radius="12px"
    )


# Page
app = rx.App()


