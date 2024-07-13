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

## System Design

![architecture](https://github.com/Ankit-AP-Paul/wildlife-monitoring-software/assets/83993904/5dcfa878-dfe4-4675-8159-9f7348393301)

## Database Schema

![db schema](https://github.com/user-attachments/assets/4e909bac-90d6-4db7-b267-1f9123f6dc74)

## API Reference

```
  POST /auth/signup
```

```
  POST /auth/login
```

```
  GET /audio
```

```
  POST /audio
```

```
  DELETE /audio
```

```
  GET /sensor
```

```
  POST /sensor
```

```
  GET /region
```

```
  GET /alert
```

```
  POST /alert
```
