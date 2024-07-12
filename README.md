# Wildlife Monitoring using live audio

## Run fastAPI

```
cd backend
pip install --upgrade pip
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvircorn main:app --reload
```

FastAPI will start running on <http://localhost:8000>

## Run desktop app

```
cd frontend
flutter pub get
flutter run -d windows
```

## System Design

![architecture](https://github.com/Ankit-AP-Paul/wildlife-monitoring-software/assets/83993904/5dcfa878-dfe4-4675-8159-9f7348393301)
