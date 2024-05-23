# PostBuddy

This project is a mini version of Postman, allowing you to execute HTTP requests, manage environment variables, and save/load workspaces.

## Project Structure

```
postbuddy/
├── app.py
├── static/
│   └── styles.css
├── templates/
│   ├── base.html
│   ├── index.html
│   └── variables.html
├── utils/
│   ├── request_handler.py
│   ├── workspace_manager.py
│   └── __init__.py
├── data/
│   └── sample_workspace.json
└── README.md
```

## How to Run

1. Clone the repository.
2. Run the `app.py` file:

```bash
python app.py
```

## Features

- Add, edit, and select environments.
- Add environment variables.
- Save and load workspaces.
- Execute HTTP requests with different types of authentication.
- Extract variables from responses for use in subsequent requests.

## Dependencies

- `flask`
- `requests`
- `bootstrap`