# 🗳️ Election Assistant — AI-Powered Civic Guide

> An interactive, AI-powered assistant that helps users understand the election process, timelines, and steps in a simple and easy-to-follow way.

🔴 **[Live Demo → vijayvardhanm75-web.github.io/election-assistant](https://vijayvardhanm75-web.github.io/election-assistant)**

---

## 📌 Problem Statement

Many citizens — especially first-time voters — find elections confusing. They don't know:
- How to register to vote
- What happens on polling day
- How votes are counted
- What the Model Code of Conduct means

Static information pages are hard to navigate. People need a **guided, conversational experience**.

---

## 💡 Solution

A fully interactive, browser-based Election Assistant powered by **Claude AI** that:
- Answers any election-related question in plain language
- Guides users through the 5 stages of the election process
- Provides personalized, context-aware responses
- Works instantly — no installation, no login required

---

## ✨ Key Features

- **AI Chat Interface** — Powered by Claude (claude-sonnet), remembers conversation context
- **Interactive Election Timeline** — Click any stage to get a detailed explanation
- **Topic Cards** — Quick access to Voter Registration, Polling Day, Vote Counting, and MCC
- **Quick Fact Chips** — EVM & VVPAT, Eligibility Check, Election Commission roles
- **Smart Suggestions** — Pre-built questions to guide first-time users
- **Fully Responsive** — Works on desktop and mobile browsers

---

## 🗺️ Election Process Covered

| Stage | Description |
|-------|-------------|
| 1️⃣ Announcement | Election Commission announces schedule, MCC begins |
| 2️⃣ Nominations | Candidates file papers, scrutiny & withdrawal period |
| 3️⃣ Campaigning | Party campaigns, 48-hr silent period before polling |
| 4️⃣ Polling Day | Voters cast votes via EVM, VVPAT slip confirms vote |
| 5️⃣ Counting & Results | Votes tallied, winner declared by Returning Officer |

---

## 🛠️ Tech Stack

- **Frontend** — HTML5, CSS3, Vanilla JavaScript
- **AI** — Anthropic Claude API (`claude-sonnet-4-20250514`)
- **Fonts** — Fraunces (display) + DM Sans (body) via Google Fonts
- **Hosting** — GitHub Pages

---

## 📂 Repository Structure

```
election-assistant/
├── index.html      # Complete app — UI + AI chat logic
└── README.md       # Project documentation
```

---

## 🚀 How to Run

**Option 1 — Live Demo (recommended):**
Just open the live link above. No setup needed.

**Option 2 — Run locally:**
1. Clone this repo
2. Open `index.html` in any browser
3. That's it — works instantly

---

## 🎯 How It Works

1. User opens the app and sees an interactive election timeline
2. They can click any topic card or timeline stage to ask a question
3. The AI assistant (Claude) responds with clear, step-by-step guidance
4. Users can also type any custom question in the chat
5. The assistant remembers the conversation and provides follow-up answers

---

## 🧠 AI Design

The assistant is prompted to:
- Use Indian election context (ECI, EVM, VVPAT, Form 6, Lok Sabha, etc.)
- Give concise, friendly answers under 200 words
- Use numbered steps for processes
- End each reply with a follow-up question to encourage learning
- Never discuss specific candidates or parties

---

## 📈 Impact

- Helps **first-time voters** understand their rights and process
- Makes civic education **accessible and interactive**
- Reduces confusion around **EVMs, voter registration, and MCC**
- Encourages **voter participation** through better awareness

---

## 🔮 Future Scope

- State-wise election information and schedules
- Real-time election date tracking via Election Commission API
- Multilingual support (Hindi, Tamil, Telugu, Kannada, etc.)
- Polling booth locator using Google Maps
- Push notifications for important election dates

---

*Built for Challenge 2 — Interactive Election Process Assistant*
