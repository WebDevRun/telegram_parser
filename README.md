# Parser telegram

## Description 

This script parse telegram football channel and find match and watch one while that time will more then 60 minutes.
After than script send message about match.

## Install

Create **.env**  and **<phone>.session** files in project folder.
In .env file write:

```
API_ID=
API_HASH=
PHONE=
PARSED_CHAT_ID=
MESSAGE_CLIENT=
```

For build image:

```
docker compose build
```

For run program:

```
docker compose run
```