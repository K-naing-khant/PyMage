adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb (past tense): ")
place = input("Enter a place: ")

story = f"It was a {adjective} day when the {noun} decided to {verb} all the way to {place}."
print(story)
print("\n--- Your Story ---")
print(story.strip())
print(f"Word Count: {len(story.split())}")

title = noun.upper() + "'S ADVENTURE"
print(f'\n{title}')