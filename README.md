# Outlook AI Assistant

An intelligent Outlook companion that leverages Microsoft Graph and Azure AI to enhance email productivity. This assistant automatically organizes emails, summarizes daily messages, and provides real-time notifications and analytics — all seamlessly integrated within your Outlook environment.

---

## Features

### AI Email Understanding & Categorization
- Uses **Azure AI Document Intelligence** to extract and interpret the content of incoming emails.
- Automatically routes emails into smart folders such as:
  - `Meetings`
  - `Tasks`
  - `Follow-Up`
  - `General Updates`

### AI Personal Assistant for Outlook
- **Daily Summary Chatbot**: Summarizes all emails received throughout the day.
- **Interactive Q&A**: Ask natural language questions about emails (e.g., "What meetings do I have this week?" or "Summarize emails from HR").
- **Email Prioritization**: Highlights urgent or important messages.

### Smart Notifications
- Real-time desktop and/or Teams-based alerts for high-priority or filtered emails.
- Configurable notification rules (e.g., VIP sender alerts, subject line keywords).

### Email Analytics Dashboard
- Visualize email activity:
  - Number of emails received/sent
  - Response times
  - Most contacted recipients
  - Topic clustering

---

## Getting Started

### Prerequisites

- Python 3.9+
- Microsoft 365 account with API access
- Azure subscription with:
  - Azure OpenAI
  - Azure AI Document Intelligence (formerly Form Recognizer)
- Microsoft Graph API permissions (`Mail.Read`, `Mail.ReadWrite`, `User.Read`, etc.)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/outlook-ai-assistant.git
cd outlook-ai-assistant
```

### 2. Create .env file
```
AZURE_OPENAI_KEY=your_azure_openai_key
AZURE_DOC_INTELLIGENCE_ENDPOINT=https://<your-resource>.cognitiveservices.azure.com/
AZURE_DOC_INTELLIGENCE_KEY=your_doc_intel_key
GRAPH_CLIENT_ID=your_client_id
GRAPH_CLIENT_SECRET=your_secret
GRAPH_TENANT_ID=your_tenant_id
```

###  3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Backend Server
```
uvicorn main:app --reload
```
---

## Tech Stack

| Component                     | Technology                                      |
|------------------------------|-------------------------------------------------|
| Email Integration            | Microsoft Graph API                             |
| Email Parsing & Classification | Azure AI Document Intelligence (Layout Model) |
| Backend API                  | FastAPI (Python)                                |
| Frontend/Assistant UI        | React                 |
| Authentication               | Azure AD / Microsoft Identity                   |
| Deployment                   | Azure App Service / Docker                      |
