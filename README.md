# Chatter

A FastAPI backend integrated with Firebase.

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Firebase credentials file: `backend/firebase-admin-key.json`

### Installation

1. **Clone the repository**  
   ```sh
   git clone https://github.com/DustinYates/chatter.git
   cd chatter
   ```

2. **Install dependencies**  
   ```sh
   python3 -m pip install fastapi firebase-admin uvicorn
   ```

3. **Add your Firebase credentials**  
   Place your Firebase Admin SDK private key JSON file at:  
   ```
   backend/firebase-admin-key.json
   ```

### Running the Backend

Start the FastAPI server using Uvicorn:
```sh
python3 -m uvicorn backend.app.main:app --reload
```
- The server will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Testing

Open your browser and visit:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)  
You should see:  
```json
{"message": "Firebase is working!"}
```

### Notes

- If you get `command not found: uvicorn`, use:
  ```sh
  python3 -m uvicorn backend.app.main:app --reload
  ```
- Make sure your Firebase credentials JSON file is in the correct location.

---

## Project Structure

```
chatter/
├── backend/
│   ├── app/
│   │   └── main.py
│   └── firebase-admin-key.json
├── README.md
└── ...
```

---

## License

MIT License
