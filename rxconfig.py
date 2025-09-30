import reflex as rx

config = rx.Config(
    app_name="fear_and_greed",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)