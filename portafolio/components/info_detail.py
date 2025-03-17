import reflex as rx
from portafolio.components.icon_badge import icon_badge
from portafolio.components.icon_button import icon_button
from portafolio.data import Info
from portafolio.styles.styles import IMAGE_HEIGHT, EmSize, Size


def info_detail(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title),
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size=Size.SMALL.value,
                    color_scheme="gray"
                ),
                rx.cond(
                    bool(info.technologies),  # ✅ Validar si hay tecnologías
                    rx.flex(
                        *[
                            rx.badge(
                                rx.box(class_name=tech["icon"]),  # ✅ Acceder como diccionario
                                tech["name"],  # ✅ Acceder como diccionario
                                color_scheme="gray"
                            )
                            for tech in [t.__dict__ for t in info.technologies]  # ✅ Convertir `Technology` en diccionario
                        ],
                        wrap="wrap",
                        spacing=Size.SMALL.value
                    )
                ),
                rx.hstack(
                    rx.cond(
                        bool(info.url),
                        icon_button(
                            "link",
                            info.url
                        )
                    ),
                    rx.cond(
                        bool(info.github),
                        icon_button(
                            "github",
                            info.github
                        )
                    )
                ),
                spacing=Size.SMALL.value,
                width="100%"
            ),
            spacing=Size.DEFAULT.value,
            width="100%"
        ),
        rx.cond(
            bool(info.image),
            rx.image(
                src=info.image,
                height=IMAGE_HEIGHT,
                width="auto",
                border_radius=EmSize.DEFAULT.value,
                object_fit="cover"
            )
        ),
        rx.vstack(
            rx.cond(
                bool(info.date),
                rx.badge(info.date)
            ),
            rx.cond(
                bool(info.certificate),
                icon_button(
                    "shield-check",
                    info.certificate,
                    solid=True
                )
            ),
            spacing=Size.SMALL.value,
            align="end"
        ),
        flex_direction=["column-reverse", "row"],
        spacing=Size.DEFAULT.value,
        width="100%"
    )
