#  AI Stock Market Agent with CrewAI

An **AI-powered Stock Market Agent** that searches the internet for **trending companies** and recommends potential investments.
Built with the **CrewAI framework**, the agent combines **Serper API, Gemini AI, and push notifications** to deliver real-time financial insights.

---

##  Features

* 🌐 **Web Search** – Uses **Serper API** to fetch the latest stock news & trends
* 🧠 **AI Orchestration** – Built with **CrewAI** for structured agent workflows
* 🤖 **LLM Backend** – Powered by **Gemini AI** for analysis & reasoning
* 📲 **Push Notifications** – Sends stock picks directly to your phone
* 📝 **Automated Reports** – Generates and stores reports of selected companies

---

##  Tech Stack

* [CrewAI](https://github.com/joaomdmoura/crewAI) – Framework for building AI agents
* [Serper API](https://serper.dev/) – Google search API
* [Gemini AI](https://deepmind.google/technologies/gemini/) – LLM provider
* Pushover Notification Service – Sends stock alerts to mobile
* Python

---

##  Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ai-stock-agent.git
cd ai-stock-agent
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
   Create a `.env` file in the project root:

```ini
SERPER_API_KEY=your_serper_api_key
GEMINI_API_KEY=your_gemini_api_key
PUSHOVER_NOTIFICATION_KEY=your_push_service_key
```

---

##  Usage

Run the agent:

```bash
python main.py
```

* The agent will search for trending companies
* Analyze them using **Gemini AI**
* Send a **push notification** with stock picks
* Generate a **detailed report** saved locally

---

##  Example Output

* **Push Notification**:

  > "📈 Top Pick: Reliance Industries – Strong momentum in renewable energy sector."

---

##  Roadmap

* [ ] Add support for multiple LLM providers
* [ ] Enable scheduled stock checks
* [ ] Build a simple web dashboard
* [ ] Integrate with brokerage APIs for auto-trading

---

##  Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.

---


