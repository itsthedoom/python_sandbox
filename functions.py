def which_prize(points):
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = 'a wafer"
    elif points >=181:
        prize = "a penguin"

    if prize:
        return "congrats! you have won" + prize + "!"
    else:
        return "Oh dear, no prize"

    
