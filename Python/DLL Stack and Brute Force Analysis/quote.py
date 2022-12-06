from random import randint


# Get a random Leonardo da Vinci quote
def get_quote():
    quote_list = [
        "Learning never exhausts the mind.",
        "Simplicity is the ultimate sophistication.",
        "Time stays long enough for anyone who will use it.",
        "Poor is the pupil who does not surpass his master.",
        "The noblest pleasure is the joy of understanding.",
        "All our knowledge has its origins in our perceptions.",
        "Life well spent is long.",
        "The truth of things is the chief nutriment of superior intellects.",
        "Common sense is that which judges the things given to it by other senses.",
        "Knowledge of the past and of the places of the earth is the ornament and food of the mind of man.",
        "As a well-spent day brings happy sleep, so a life well spent brings happy death.",
        "Men of lofty genius when they are doing the least work are most active."
    ]

    # Return a random quote from the list
    return quote_list[randint(0, len(quote_list) - 1)]
