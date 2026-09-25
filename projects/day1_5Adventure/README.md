# The Lost Lantern

## What the project does

`adventure.py` is a small text-based command-line adventure game. You name
your adventurer, walk through a forest, solve a bridge challenge, open (or
work around) a cave door, and choose how to deal with a dragon guarding the
lost lantern.

The code is intentionally written from top to bottom as a Days 1-5 review.
It does not use functions, classes, imports, modules, files, packages, or
external libraries.

## How to run it

1. Open a terminal in this folder.
2. Run:

   ```text
   python adventure.py
   ```

3. Follow the prompts. Enter a number when the game asks for miles or steps.

## Days 1-5 concepts used

### Day 1

- `print()` displays the story and results.
- Variables store the name, health, gold, distance, and game state.
- Comments explain a few learning-focused sections.
- `int`, `float`, `str`, and `bool` values appear throughout the game.
- F-strings format the player's changing information.
- `input()` collects the player's choices.

### Day 2

- Arithmetic operators change health and gold.
- Comparison operators check choices, steps, and health.
- Logical operators combine game conditions.
- `int()`, `float()`, and `str()` convert input or game values.

### Day 3

- `if`, `elif`, and `else` control the story.
- Boolean values track the torch, clue, door, and escape.
- Nested conditions handle the bridge and cave choices.
- A blank name or blank door code demonstrates a falsy string.

### Day 4

- A `for` loop walks through the forest.
- A `while` loop controls the limited cave decision rounds.
- `range()` creates the step and choice-round sequences.
- `break` ends the game loop after escape or defeat.
- `continue` skips to the next round after a bad or unavailable choice.
- The cave has a nested `for` loop inside the `while` loop, as well as nested
  decision logic.

### Day 5

- String indexing reads the first letter of the player's name.
- String slicing creates a short name preview.
- `upper()` and `lower()` normalize or display text.
- `strip()` removes extra spaces from input.
- `split()` breaks the clue into words.
- `replace()` changes the clue and formats the final summary.
- `join()` combines words and summary values.
- F-strings provide readable string formatting.

## Learning checklist

- [ ] Trace the variables from the top of `adventure.py` to the ending.
- [ ] Identify each `if`, `elif`, and `else` branch.
- [ ] Follow the forest `for` loop one step at a time.
- [ ] Explain why `continue` is used for an invalid cave choice.
- [ ] Explain why `break` stops the cave choices after escaping.
- [ ] Find the indexing and slicing examples.
- [ ] Find every string method: `upper`, `lower`, `strip`, `split`,
      `replace`, and `join`.
- [ ] Try different passwords, door letters, and cave actions.
- [ ] Change the starting health or gold and predict the result.
