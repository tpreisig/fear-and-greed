import reflex as rx

config = rx.Config(
    app_name="fg_index2",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)