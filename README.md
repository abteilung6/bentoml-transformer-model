Create and run this script to download the model.

```
python download_model.py
```

Manage models in local Mode Store

```
$ bentoml models list
Tag                             Module                Size      Creation Time
summarization:5fkhmzeye6gr2as4  bentoml.transformers  1.14 GiB  2023-12-11 14:19:28
```

Run a BentoML Service with model using `service.py`

```
$ bentoml serve service:svc
```

Make a sample request for input `Change my mind`

```
$ python3 make_request.py
[RESPONSE]  Change your mind. Change your name. Change my mind . Change your life. Change a mind. change your mind, change your life . Change it up. Change the mind. Give you a chance to change your story. Change you mind. Share your story with CNN iReport .
```

Package it into the standard distribution format in BentoML using `bentofile.yaml`.

```
$ bentoml build
Successfully built Bento(tag="summarization:v4da7feyfwbu2as4").
```

Containerize bentoml build

```
$ bentoml containerize summarization:latest
```

The Docker image’s tag is the same as the Bento tag by default.

```
$ docker images
```

Push to Bento cloud

```
$ bentoml push summarization:latest
```
