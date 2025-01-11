Access `/outer` and get:

```json
[
    {
        "id": 1,
        "inner": {
            "id": 1,
            "file": {
                "id": "da9433e4-be79-41eb-827f-326ba48451e4",
                "file": "/media_files/da9433e4-be79-41eb-827f-326ba48451e4.png",
                "owner": 1,
                "created_at": "2025-01-11T00:55:57.057002Z"
            }
        },
        "file": {
            "id": "75124cc1-072d-4e3a-add0-4e1806847ff5",
            "file": "http://127.0.0.1:8000/media_files/75124cc1-072d-4e3a-add0-4e1806847ff5.png",
            "owner": 1,
            "created_at": "2025-01-11T00:55:50.285385Z"
        }
    }
]
```

Notice the inner file, which is relative rather than absolute
