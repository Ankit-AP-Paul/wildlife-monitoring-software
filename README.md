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
Test endpoints at <http://localhost:8000/docs>

## Run desktop app

```
cd frontend
flutter pub get
flutter run -d windows
```

## System Design

![architecture](https://github.com/Ankit-AP-Paul/wildlife-monitoring-software/assets/83993904/5dcfa878-dfe4-4675-8159-9f7348393301)

## Database Schema

![db schema](https://github.com/user-attachments/assets/4e909bac-90d6-4db7-b267-1f9123f6dc74)

## API Reference

```http
  POST /auth/signup
```

```http
  POST /auth/login
```

```http
  GET /audio
```

```http
  POST /audio
```

```http
  DELETE /audio
```
