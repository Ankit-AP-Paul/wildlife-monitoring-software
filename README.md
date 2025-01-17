# Wildlife Monitoring using live audio

## Backend

Backend deployed at <https://wildlife-monitoring-software.onrender.com>

Test endpoints using Swagger at <https://wildlife-monitoring-software.onrender.com/docs>

## System Design

![architecture](https://github.com/Ankit-AP-Paul/wildlife-monitoring-software/assets/83993904/5dcfa878-dfe4-4675-8159-9f7348393301)

## Database Schema

![db schema](https://github.com/user-attachments/assets/4e909bac-90d6-4db7-b267-1f9123f6dc74)

## API Reference

User Signup

```
  POST /signup
```

User Login

```
  POST /signin
```

Add Region

```
POST /region
```

All regions

```
GET /all_region
```

Get region by id

```
GET /region/{id}
```

Add Sensor

```
POST /sensor
```

Get all sensors

```
GET /all_sensor
```

Get sensor by id

```
GET /sensor/{id}
```

Create alert

```
POST /alert
```

Get all alerts

```
GET /all_alerts
```

Get alert by sensor id

```
GET /alert/{id}
```
