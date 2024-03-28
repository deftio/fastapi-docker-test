# FastAPI - Docker static Quicktest

This is a basic test app for docker & FastAPI
when logged in to the server run docker (or similar)


```sh
docker build -t web_fastapi .
docker run -d --name web_fastapi -p 80:80 web_fastapi_image
```

or run the scripts with restart included

```
./runweb.sh
```

stop and prune the image

```
./stopweb.sh
```


