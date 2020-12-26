# Guide location: https://learn.adafruit.com/aio-quote-board-matrix-display/code-the-quote-board
import time
import random
import board
import terminalio
from adafruit_matrixportal.matrixportal import MatrixPortal
 
# --- Display setup ---
matrixportal = MatrixPortal(status_neopixel=board.NEOPIXEL, debug=True)
 
# Create a new label with the color and text selected
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(0, (matrixportal.graphics.display.height // 2) - 1),
    scrolling=True,
)
 
# Static 'Connecting' Text
matrixportal.add_text(
    text_font=terminalio.FONT,
    text_position=(2, (matrixportal.graphics.display.height // 2) - 1),
)

QUOTES_FEED = "christmas-messages.display-messages"
SCROLL_DELAY = 0.02
UPDATE_DELAY = 600 
 
quotes = []
colors = ["FF0000", "#2C6F3C" ]
matrixportal.set_text("Starting", 1)

last_update = time.monotonic()
matrixportal.set_text(" ", 1)

def get_quotes_from_feed():
    print("Updating data from Adafruit IO")
 
    matrixportal.set_text("Retrieving", 1)

    try:
        print(QUOTES_FEED)
        quotes_data = matrixportal.get_io_data(QUOTES_FEED)
        quotes.clear()

        for json_data in quotes_data:
            quotes.append(matrixportal.network.json_traverse(json_data, ["value"]))

        print(quotes)
    # pylint: disable=broad-except
    except Exception as error:
        print(error) 

def get_random_quote():
    last_quote = None
    quote_index = None

    if len(quotes) > 1 and last_quote is not None:
        while quote_index == last_quote:
            quote_index = random.randrange(0, len(quotes))
    else:
        quote_index = random.randrange(0, len(quotes))
    last_quote = quote_index
    return quotes[quote_index]

def get_random_color():
    last_color = None
    color_index = None

    if len(colors) > 1 and last_color is not None:
        while color_index == last_color:
            color_index = random.randrange(0, len(colors))
    else:
        color_index = random.randrange(0, len(colors))
    last_color = color_index
    return colors[color_index]

get_quotes_from_feed() 

while True:
    quote = get_random_quote()
    color = get_random_color()

    matrixportal.set_text(quote)
    matrixportal.set_text_color(color)
 
    # Scroll it
    matrixportal.scroll_text(SCROLL_DELAY)
 
    if time.monotonic() > last_update + UPDATE_DELAY:
        get_quotes_from_feed() 
        last_update = time.monotonic()