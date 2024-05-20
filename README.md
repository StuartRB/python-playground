curl for POST:

```
curl --location 'localhost:5001/post' \
--header 'Content-Type: application/json' \
--data-raw '{
    "message": "I like cheese",
    "email": "alan@cheese.com"
}'
```