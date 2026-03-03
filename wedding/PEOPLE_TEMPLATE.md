# Quick Reference: Adding People

Edit the `people.json` file to add or modify people.

## Template

```json
{
  "name": "full name lowercase",
  "question": "Your personalized question here?",
  "answer": "correct answer",
  "emoji": "💐"
}
```

## Example Bridesmaids

Add to the `bridesmaids` array in `people.json`:

```json
{
  "name": "emily johnson",
  "question": "What was the name of our favorite college hangout spot?",
  "answer": "joes cafe",
  "emoji": "💐"
},
{
  "name": "rachel green",
  "question": "What city did we take our first road trip to?",
  "answer": "chicago",
  "emoji": "💐"
}
```

## Example Groomsmen

Add to the `groomsmen` array in `people.json`:

```json
{
  "name": "michael scott",
  "question": "What was my nickname in high school?",
  "answer": "mikey",
  "emoji": "🤵"
},
{
  "name": "james bond",
  "question": "What video game did we play all night in college?",
  "answer": "halo",
  "emoji": "🤵"
}
```

## Tips for Good Questions

✅ **Good Questions:**
- Personal memories only they would know
- Simple, one-word or short answers
- Not too obscure (they should be able to answer it!)
- Examples: years, places, nicknames, shared experiences

❌ **Avoid:**
- Questions with complex answers
- Multiple possible correct answers
- Questions requiring exact spelling of long words
- Trivia that's too hard to remember

## Where to Edit

1. Open `wedding/people.json`
2. Add entries to either the `bridesmaids` or `groomsmen` array
3. Make sure to include a comma after each entry except the last one in each array
4. Save the file
5. Test with their name before sharing!

## JSON Structure

```json
{
  "bridesmaids": [
    { "name": "...", "question": "...", "answer": "...", "emoji": "💐" },
    { "name": "...", "question": "...", "answer": "...", "emoji": "💐" }
  ],
  "groomsmen": [
    { "name": "...", "question": "...", "answer": "...", "emoji": "🤵" },
    { "name": "...", "question": "...", "answer": "...", "emoji": "🤵" }
  ]
}
```
