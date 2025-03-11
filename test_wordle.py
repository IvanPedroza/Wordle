from wordle import format_guess

G = '\x1b[0;30;42m'  # Green
Y = '\x1b[0;30;43m'  # Yellow
N = '\x1b[0m'        # Normal

def test_format_guess_correct():
    guess = "APPLE"
    word = "APPLE"
    formatted_guess, is_correct = format_guess(guess, word)
    assert formatted_guess == f"{G}A{G}P{G}P{G}L{G}E{N}"
    assert is_correct

def test_format_guess_partial():
    guess = "APRON"
    word = "APPLE"
    formatted_guess, is_correct = format_guess(guess, word)
    # "A" and "P" correct position, R,O,N incorrect
    assert formatted_guess == f"{G}A{G}P{N}R{N}O{N}N{N}"
    assert not is_correct

def test_format_guess_mixed():
    guess = "PLEAD"
    word = "APPLE"
    formatted_guess, is_correct = format_guess(guess, word)
    # "P", "L", "E", "A" exist but wrong spot, "D" incorrect
    assert formatted_guess == f"{Y}P{Y}L{Y}E{Y}A{N}D{N}"
    assert not is_correct

def test_format_guess_incorrect():
    guess = "WRONG"
    word = "APPLE"
    formatted_guess, is_correct = format_guess(guess, word)
    # All letters incorrect; thus, letters uncolored
    assert formatted_guess == f"{N}W{N}R{N}O{N}N{N}G{N}"
    assert not is_correct
