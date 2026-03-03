# Bridesmaid & Groomsmen Proposal Page

A personalized, interactive way to ask your friends to be part of your wedding party! 💍✨

## 🌐 Access

The page will be accessible at: **jacksonlowder.com/wedding**

This page is not linked from the main site navigation - it's a standalone page accessible only via direct URL that you can share with your potential bridesmaids and groomsmen.

## 💐 How It Works

1. **Name Entry**: Visitor enters their name
2. **Personal Question**: They get asked a personalized question that only they would know
3. **Reveal**: Upon correct answer, they see a beautiful reveal asking them to be a bridesmaid or groomsman!

## ✨ Features

- **Personalized Experience**: Each person gets their own custom question
- **Security Through Trivia**: Only the intended person can see their proposal
- **Animated Reveal**: Beautiful animations and transitions
- **Responsive Design**: Works perfectly on all devices
- **Elegant Design**: Purple gradient background with clean white card
- **Different Messages**: Automatically shows bridesmaid or groomsman message based on the person

## 📝 Adding People

Edit `people.json` to add or modify people. The file has two arrays: `bridesmaids` and `groomsmen`.

```json
{
  "bridesmaids": [
    {
      "name": "erin",
      "question": "What year did we meet?",
      "answer": "2018",
      "emoji": "💐"
    }
  ],
  "groomsmen": [
    {
      "name": "curtis",
      "question": "What's my favorite sport?",
      "answer": "basketball",
      "emoji": "🤵"
    }
  ]
}
```

### Fields:
- **name**: Full name in lowercase (the system will match case-insensitively)
- **question**: A personal question only they would know
- **answer**: The correct answer (case-insensitive)
- **emoji**: Emoji to display on reveal (💐 for bridesmaids, 🤵 for groomsmen)

## 🎨 Customization

### Change Background Colors:
Edit line 16 in `index.html`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Customize Messages:
Edit the reveal messages in the `submitAnswer()` function (lines 278-284):
```javascript
if (currentPerson.type === 'bridesmaid') {
    document.getElementById('revealTitle').textContent = 'Will you be my Bridesmaid?';
    document.getElementById('revealMessage').textContent = "Your custom message here!";
}
```

### Change Emojis:
Modify the emoji field for each person, or update the default emojis in the reveal section.

## 🛠️ Testing

Open `index.html` in a web browser:
1. Enter a name you've added to the people object
2. Answer their question correctly
3. See the reveal!

### Example Test Cases:
- Name: "jane doe" → Question about meeting year → Answer: "2015"
- Name: "john doe" → Question about favorite sport → Answer: "basketball"

## 📱 Sharing

Simply send the link **jacksonlowder.com/wedding** to each person via text, email, or however you prefer!

They'll enter their name and answer their personal question to see your special proposal. 💕
