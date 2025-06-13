Audio file converter


| Service | URL                 | Docs URL                 |
| ------- | ------------------- | ------------------------ |
| ReactJS | http://0.0.0.0:5173 |                          |
| FastAPI | http://0.0.0.0:8000 | http://0.0.0.0:8000/docs |
| DRF     | http://0.0.0.0:8000 |                          |


```bash
# Start: ReactJS + FastAPI + API
docker compose -f reactjs_fastapi_compose.yml up
```

```
$ docker compose -f reactjs_fastapi_compose.yml up [+] Running 3/0
 ✔ Container wui-afc__api-1               Created                                                                  0.0s
 ✔ Container wui-afc__backend_fastapi-1   Created                                                                  0.0s
 ✔ Container wui-afc__frontend_reactjs-1  Created                                                                  0.0s
Attaching to afc__api-1, afc__backend_fastapi-1, afc__frontend_reactjs-1
afc__api-1 exited with code 0
afc__backend_fastapi-1   | INFO:     Started server process [1]
afc__backend_fastapi-1   | INFO:     Waiting for application startup.
afc__backend_fastapi-1   | INFO:     Application startup complete.
afc__backend_fastapi-1   | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
afc__frontend_reactjs-1  |
afc__frontend_reactjs-1  | > freactjs@0.1.0 dev
afc__frontend_reactjs-1  | > vite
afc__frontend_reactjs-1  |
afc__frontend_reactjs-1  |
afc__frontend_reactjs-1  |   VITE v6.3.5  ready in 387 ms
afc__frontend_reactjs-1  |
afc__frontend_reactjs-1  |   ➜  Local:   http://localhost:5173/
afc__frontend_reactjs-1  |   ➜  Network: http://192.168.48.2:5173/
^CGracefully stopping... (press Ctrl+C again to force)
[+] Stopping 3/2
 ✔ Container wui-afc__frontend_reactjs-1  Stopped                                                                 10.2s
 ✔ Container wui-afc__backend_fastapi-1   Stopped                                                                  0.3s
 ✔ Container wui-afc__api-1               Stopped                                                                  0.0s
canceled
```

```bash
# Delete
docker compose -f reactjs_fastapi_compose.yml rm -f -s -v
```

```
$ docker compose -f reactjs_fastapi_compose.yml rm -fsv
[+] Stopping 3/0
 ✔ Container wui-afc__frontend_reactjs-1  Stopped                                                                  0.0s
 ✔ Container wui-afc__backend_fastapi-1   Stopped                                                                  0.0s
 ✔ Container wui-afc__api-1               Stopped                                                                  0.0s
Going to remove wui-afc__frontend_reactjs-1, wui-afc__backend_fastapi-1, wui-afc__api-1
[+] Removing 3/0
 ✔ Container wui-afc__api-1               Removed                                                                  0.0s
 ✔ Container wui-afc__frontend_reactjs-1  Removed                                                                  0.0s
 ✔ Container wui-afc__backend_fastapi-1   Removed                                                                  0.0s
```


```bash
# Start: ReactJS + FastAPI + API
$ docker compose -f reactjs_drf_compose.yml up
[+] Running 3/0
 ✔ Container wui-afc__api-1               Created                                                                  0.0s
 ✔ Container wui-afc__backend_drf-1       Created                                                                  0.0s
 ✔ Container wui-afc__frontend_reactjs-1  Created                                                                  0.0s
Attaching to afc__api-1, afc__backend_drf-1, afc__frontend_reactjs-1
afc__api-1 exited with code 0
afc__backend_drf-1       | [2025-06-13 17:44:33 +0000] [1] [INFO] Starting gunicorn 23.0.0
afc__backend_drf-1       | [2025-06-13 17:44:33 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
afc__backend_drf-1       | [2025-06-13 17:44:33 +0000] [1] [INFO] Using worker: sync
afc__backend_drf-1       | [2025-06-13 17:44:33 +0000] [7] [INFO] Booting worker with pid: 7
afc__frontend_reactjs-1  |
afc__frontend_reactjs-1  | > freactjs@0.1.0 dev
afc__frontend_reactjs-1  | > vite
afc__frontend_reactjs-1  |
afc__frontend_reactjs-1  |
afc__frontend_reactjs-1  |   VITE v6.3.5  ready in 389 ms
afc__frontend_reactjs-1  |
afc__frontend_reactjs-1  |   ➜  Local:   http://localhost:5173/
afc__frontend_reactjs-1  |   ➜  Network: http://192.168.48.2:5173/
^CGracefully stopping... (press Ctrl+C again to force)
[+] Stopping 3/2
 ✔ Container wui-afc__frontend_reactjs-1  Stopped                                                                 10.4s
 ✔ Container wui-afc__backend_drf-1       Stopped                                                                  0.4s
 ✔ Container wui-afc__api-1               Stopped                                                                  0.0s
canceled
```

```bash
# Delete
$ docker compose -f reactjs_drf_compose.yml rm -f -s -v
[+] Stopping 3/0
 ✔ Container wui-afc__frontend_reactjs-1  Stopped                                                                  0.0s
 ✔ Container wui-afc__backend_drf-1       Stopped                                                                  0.0s
 ✔ Container wui-afc__api-1               Stopped                                                                  0.0s
Going to remove wui-afc__backend_drf-1, wui-afc__frontend_reactjs-1, wui-afc__api-1
[+] Removing 3/3
 ✔ Container wui-afc__api-1               Removed                                                                  0.0s
 ✔ Container wui-afc__frontend_reactjs-1  Removed                                                                  0.1s
 ✔ Container wui-afc__backend_drf-1       Removed                                                                  0.1s
```
