import reflex as rx
from portafolio.components.heading import heading
from portafolio.styles.styles import EmSize, Size


def tech_stack(technologies: list[dict]) -> rx.Component:
    return rx.vstack(
        heading("Tecnologías"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology["icon"],  # 🔥 Cambio aquí
                        font_size="24px"
                    ),
                    rx.text(technology["name"]),  # 🔥 Cambio aquí
                    size="2"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
