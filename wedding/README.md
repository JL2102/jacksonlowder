# Wedding Party Mystery Investigation 🔍

A detective-themed, multi-page interactive experience to ask your friends to be part of your wedding party. Styled as a classified "Case File" investigation where the visitor is the final suspect.

## 🌐 Access

Share the link: **jacksonlowder.com/TheMystery**

This redirects to `/wedding/` behind the scenes. The page is not linked from the main site — it's only accessible via direct URL.

## 🕵️ How It Works

The experience is a 6-page investigation:

1. **Case File Opening** — Visitor enters their name to "access the case file"
2. **The Suspects** — Displays suspect cards for the visitor's wedding party group (bridesmaids or groomsmen)
3. **Psychological Profile** — A personalized free-text question unique to each person (bride/groom skip this page)
4. **Background Check: "Relationship Lore"** — Multiple choice question about the couple's origin story
5. **Bride/Groom File: "Deep Lore"** — Multiple choice question (different options for bride-side vs. groom-side)
6. **The Final Suspect** — "Who took the bouquet?" → Correct answer ("You") triggers the **CASE CLOSED** reveal

The reveal text is staggered line-by-line and assigns the visitor their role (Bridesmaid, Groomsman, Maid of Honor, or Best Man).

## ✨ Features

- **Detective/Mystery Theme** — Dark background, manila folder card, Courier New monospace typography, "CLASSIFIED" stamps
- **Audio Narration** — Speech synthesis reads each page's narration aloud (with support for custom audio files)
- **Personalized Questions** — Each person has a unique psych question on Page 3 with hints after wrong answers
- **Side-Specific Content** — Visitors only see suspect cards and questions for their own group (bridesmaids or groomsmen)
- **Special Roles** — Automatically assigns "Best Man" (curtis) and "Maid of Honor" (erin) on the reveal
- **Responsive Design** — Adapts to mobile and small screens
- **Skip Safety Net** — After 3 wrong attempts on the psych question, a skip button appears

## 📝 Adding People

Edit `people.json`. The file has two arrays: `bridesmaids` and `groomsmen`.

```json
{
  "bridesmaids": [
    {
      "name": "erin",
      "role": "bridesmaid",
      "description": "Suspect profile shown on Page 2",
      "psych_question": "A personal question only Erin would know?",
      "psych_answer": "the answer",
      "psych_hint": "A hint shown after the first wrong attempt"
    }
  ],
  "groomsmen": [
    {
      "name": "curtis",
      "role": "groomsman",
      "description": "Suspect profile shown on Page 2",
      "psych_question": "A personal question only Curtis would know?",
      "psych_answer": "the answer",
      "psych_hint": "A hint shown after the first wrong attempt"
    }
  ]
}
```

### Fields:
- **name** — First name, lowercase (matched case-insensitively)
- **role** — `"bridesmaid"`, `"groomsman"`, `"bride"`, or `"groom"` (bride/groom skip the psych question page)
- **description** — Suspect profile text displayed on the Page 2 suspect card
- **psych_question** — Personal question shown on Page 3
- **psych_answer** — Correct answer (case-insensitive)
- **psych_hint** — Hint revealed after the first wrong attempt (set to `null` for bride/groom)

## 🔊 Audio

By default, narration uses the browser's **Speech Synthesis** API. To use your own voice recordings:

1. Create an `audio/` folder inside `wedding/`
2. Add files named `page1.mp3` through `page6.mp3` and `reveal.mp3`
3. Set `useAudioFiles = true` in the `<script>` section of `index.html`

## 🎨 Customization

### Reveal Messages:
Edit the `lines` array inside the `buildReveal()` function in `index.html` to change the staggered reveal text.

### Special Roles:
Best Man and Maid of Honor are assigned by name in `buildReveal()`. Update the names there to match your people:
```javascript
if (currentPerson.name === 'curtis') roleText = 'BEST MAN';
if (currentPerson.name === 'erin') roleText = 'MAID OF HONOR';
```

### Multiple Choice Questions:
Pages 4, 5, and 6 have hardcoded multiple choice options in `buildPage4()`, `buildPage5()`, and `buildPage6()` inside `index.html`.

## 🛠️ Testing

Serve the `wedding/` directory locally (e.g. `quick_server.bat` or `start_server.py`) since it fetches `people.json` via HTTP. Then:

1. Enter a name from `people.json`
2. Walk through all 6 pages
3. Verify the reveal shows the correct role

## 📱 Sharing

Send the link **jacksonlowder.com/TheMystery** to each person. They'll enter their name and work through the investigation to discover their role.
