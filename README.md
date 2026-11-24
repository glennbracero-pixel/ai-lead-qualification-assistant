\# AI Lead Qualification \& Follow-Up Assistant



An AI-powered lead qualification and follow-up automation prototype built with Python, Google Forms, Google Sheets, Ollama, and the Gmail API.



\## Project Overview



This project automates the initial stages of customer lead management.



It collects customer inquiries through Google Forms, validates submissions, analyzes customer needs using a locally running AI model, calculates transparent lead scores, stores qualified leads in Google Sheets, and generates personalized Gmail follow-up drafts.



\*\*Emails are never sent automatically. Human review and approval are required before sending.\*\*



\## Key Features



\- \*\*Lead Capture:\*\* Collects customer information through Google Forms.

\- \*\*Input Validation:\*\* Uses Pydantic to validate lead information and email addresses.

\- \*\*AI Analysis:\*\* Uses Ollama with the Qwen model to interpret customer needs and urgency.

\- \*\*Lead Scoring:\*\* Calculates scores using transparent Python business rules.

\- \*\*Lead Classification:\*\* Categorizes leads as Hot, Warm, or Cold.

\- \*\*Google Sheets CRM:\*\* Stores qualified leads and checks for duplicate email addresses.

\- \*\*AI Email Generation:\*\* Creates personalized follow-up email content.

\- \*\*Gmail Integration:\*\* Saves generated emails as Gmail drafts.

\- \*\*Human Approval:\*\* Does not automatically send emails.

\- \*\*Error Handling:\*\* Includes logging and retry handling for temporary Google Sheets errors.

\- \*\*Automated Testing:\*\* Uses pytest to test important application components.



\## Technology Stack



| Technology | Purpose |

|---|---|

| Python | Main programming language |

| Pydantic | Data validation |

| Ollama | Local AI model runtime |

| Qwen 3.5 4B | AI-powered lead analysis and email generation |

| Google Forms | Lead collection |

| Google Sheets | CRM and response tracking |

| Gmail API | Email draft creation |

| gspread | Google Sheets integration |

| pytest | Automated testing |

| Git | Version control |



\## Lead Scoring System



The application calculates lead scores using three factors:



| Factor | Category | Points |

|---|---|---:|

| Budget | High | 30 |

| Budget | Medium | 20 |

| Budget | Low | 10 |

| Budget | Unknown | 0 |

| Urgency | Urgent | 30 |

| Urgency | Soon | 20 |

| Urgency | Later | 10 |

| Business Need | Clear | 40 |

| Business Need | Unclear | 10 |



\### Lead Categories



| Score | Classification |

|---|---|

| 80–100 | Hot |

| 50–79 | Warm |

| 0–49 | Cold |



These are transparent heuristic business rules, not a scientifically validated predictive model.



The AI interprets the customer's message. Python independently calculates the numerical score.



\## Workflow



1\. Customer submits a Google Form.

2\. Python retrieves pending submissions.

3\. Pydantic validates customer information.

4\. Ollama analyzes the customer's message.

5\. Python calculates the lead score.

6\. The qualified lead is saved to Google Sheets.

7\. The AI generates a personalized follow-up email.

8\. Gmail saves the email as a draft.

9\. A human reviews the draft and decides whether to send it.



\## Project Structure



```text

AI-Lead-Qualification-Assistant/

│

├── src/

│   ├── ai\_analyzer.py

│   ├── email\_generator.py

│   ├── follow\_up\_manager.py

│   ├── form\_reader.py

│   ├── gmail\_client.py

│   ├── gmail\_drafts.py

│   ├── google\_sheets.py

│   ├── lead.py

│   ├── logger\_config.py

│   ├── qualification.py

│   └── scoring.py

│

├── tests/

│   ├── test\_email\_generator.py

│   ├── test\_gmail\_drafts.py

│   ├── test\_google\_sheets.py

│   ├── test\_lead.py

│   ├── test\_qualification.py

│   └── test\_scoring.py

│

├── logs/

├── data/

├── main.py

├── .gitignore

└── README.md

```



\## Requirements



\- Windows 10 or Windows 11

\- Python 3.13

\- Git

\- Ollama

\- Qwen 3.5 4B model

\- Google account

\- Google Sheets API access

\- Gmail API access



\## Running the Project



1\. Clone the repository.

2\. Create and activate a Python virtual environment.

3\. Install the required Python packages.

4\. Install Ollama and download the Qwen model.

5\. Configure Google service account credentials and Gmail OAuth authorization.

6\. Configure your Google Spreadsheet IDs and worksheet names.

7\. Run the application:



```powershell

python main.py

```



The application runs locally and requires the relevant Google and Ollama services to be available.



\## Running Automated Tests



Run the complete test suite:



```powershell

python -m pytest tests -v

```



\### Current Test Results



\*\*18 automated tests passed.\*\*



Tests cover:



\- Lead validation

\- Lead scoring

\- Lead qualification

\- Google Sheets operations

\- Duplicate detection

\- Retry handling

\- Email generation

\- Gmail draft creation



External services are mocked in relevant automated tests to avoid creating real Gmail drafts or modifying live Google Sheets data.



\## Security and Privacy



\- Google service account credentials must never be committed to GitHub.

\- Gmail OAuth client files and authorization tokens must remain private.

\- Local configuration and credentials are excluded through `.gitignore`.

\- Customer information should be handled responsibly.

\- Generated emails require human review before sending.

\- The Gmail integration uses an OAuth permission scope that supports draft management and sending, but this application only implements draft creation.



\## Limitations



This is a local portfolio prototype, not a production-ready hosted service.



\- The application must be running to process new submissions.

\- Ollama must be running locally.

\- Google API access and permissions must be configured.

\- Lead scoring uses predefined heuristic rules.

\- Duplicate detection currently uses email addresses.

\- The application does not provide continuous cloud-based processing or guaranteed 24/7 availability.

\- Gmail drafts are created for human review, not automatically sent.



\## Project Purpose



This project demonstrates practical skills in Python automation, local AI integration, API connections, data validation, business logic, error handling, and automated testing.



It was developed as a hands-on learning and portfolio project focused on building useful AI-assisted business workflows.

