import flet as ft
from deep_translator import GoogleTranslator

colors = {
    "primary": ft.colors.GREY_800,
    "primary_light": ft.colors.GREY_900,
    "primary_dark": ft.colors.GREY_900,
    "card_bg": ft.colors.GREY_800,
    "text": ft.colors.WHITE,
    "border": ft.colors.BLACK,
    "hint_text": ft.colors.GREY
}

languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh",
    "Japanese": "ja",
    "Russian": "ru",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Italian": "it",
    "Dutch": "nl",
    "Turkish": "tr",
    "Korean": "ko",
    "Vietnamese": "vi",
    "Polish": "pl",
    "Danish": "da",
    "Swedish": "sv",
    "Norwegian": "no",
    "Finnish": "fi",
    "Hungarian": "hu",
    "Czech": "cs",
    "Greek": "el",
    "Hebrew": "he",
    "Thai": "th",
    "Indonesian": "id",
    "Malay": "ms",
    "Filipino": "tl",
    "Romanian": "ro",
    "Bulgarian": "bg",
    "Ukrainian": "uk",
    "Serbian": "sr",
    "Croatian": "hr",
    "Slovak": "sk",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Estonian": "et",
    "Catalan": "ca",
    "Basque": "eu",
    "Galician": "gl",
    "Swahili": "sw",
    "Yoruba": "yo",
    "Amharic": "am",
    "Haitian Creole": "ht",
    "Persian": "fa",
    "Hindi": "hi",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Sinhala": "si",
    "Nepali": "ne",
    "Mongolian": "mn",
    "Khmer": "km",
    "Lao": "lo",
    "Burmese": "my",
    "Tibetan": "bo",
    "Armenian": "hy",
    "Georgian": "ka",
    "Azerbaijani": "az",
    "Kazakh": "kk",
    "Uzbek": "uz",
    "Turkmen": "tk",
    "Kyrgyz": "ky",
    "Pashto": "ps",
    "Dari": "dr",
    "Somali": "so",
    "Maltese": "mt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Serbo-Croatian": "sh",
    "Latin": "la",
}


def main(page: ft.Page):
    page.window_width = 390
    page.window_height = 844

    page.bgcolor = colors["primary_light"]

    def translate_text(e):
        output_text.value = "Translating..."
        page.update()

        text_to_translate = input_text.value

        source_lang_code = source_lang.value
        target_lang_code = target_lang.value

        translator = GoogleTranslator(source=source_lang_code, target=target_lang_code)
        translated = translator.translate(text_to_translate)

        output_text.value = translated
        page.update()

    def swap_languages(e):
        source_lang.value, target_lang.value = target_lang.value, source_lang.value
        input_text.value, output_text.value = output_text.value, input_text.value
        source_lang.update()
        target_lang.update()


        translate_text(None)

    input_text = ft.TextField(
        label="Enter text to translate",
        multiline=True,
        on_change=translate_text,
    )

    output_text = ft.TextField(
        label="Translation",
        hint_text="Translation will appear here...",
        multiline=True,
        expand=True,
        max_lines=10,
        disabled=True,  # Make the text field disabled
        color=colors["text"],
        border_color=colors["border"]
    )

    source_lang = ft.Dropdown(
        label="Translate from",
        options=[ft.dropdown.Option(key=code, text=lang) for lang, code in languages.items()],
        value="en"  # Default to English
    )

    target_lang = ft.Dropdown(
        label="Translate to",
        options=[ft.dropdown.Option(key=code, text=lang) for lang, code in languages.items()],
        value="es"  # Default to Spanish
    )

    loading_indicator = ft.ProgressRing(width=50, height=50)

    swap_button = ft.IconButton(
        icon=ft.icons.COMPARE_ARROWS_ROUNDED,  # Icon with two arrows facing in different directions
        icon_size=40,
        on_click=swap_languages,
        tooltip="Swap languages",
        rotate=90,
        icon_color=ft.colors.GREY
    )

    page.add(
        ft.Row(
            controls=[ft.Text("IQ TRANSLATE", weight=ft.FontWeight.BOLD, size=20)],
            alignment=ft.MainAxisAlignment.CENTER,

        ),

        ft.Column(
            controls=[
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(controls=[
                            source_lang,
                            input_text
                        ]),
                        padding=10,
                        height=300  # Ensure the height is set for the card
                    ),
                    elevation=5,
                    color=colors["card_bg"],
                    width=page.window_width * 0.9,  # Set width relative to screen size
                ),
                swap_button,  # Swap languages button
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(controls=[
                            target_lang,
                            output_text
                        ]),
                        padding=10,
                        height=300  # Ensure the height is set for the card
                    ),
                    elevation=5,
                    color=colors["card_bg"],
                    width=page.window_width * 0.9,  # Set width relative to screen size
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            expand=True,  # Allow the column to expand and center content on the page
        ),
    )

    # Adjust the layout on window resize (for responsive design)
    def on_resize(e):
        page.update()

    page.on_resize = on_resize

# Run the app
ft.app(target=main)