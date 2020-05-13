# gae Interpreter
Interpreter module for Internet of Things Ecosystem


## Getting Started


#### 0. Setup

- Create your account on [google cloud site](https://cloud.google.com) 
- Create GAE project
- Install GAE SDK using [instructions](https://cloud.google.com/sdk/docs/quickstarts) 

- Initialize SDK
```cmd
> gcloud init 
```
- login to you google cloud account
- pick the project you created

#### 1. Install
```cmd
> pip install -r requirements.txt
```

[[!!] Important](https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27) :
- open appengine_config.py
- make sure that a path in vendor.add("/path/to/my/third/party/libs") is correct

#### 2. Run
- use Python 2.7 interpreter
- add GAE SDK path 


to run from terminal:
```cmd
> python /your/path/to/google-cloud-sdk/bin/dev_appserver.py --host 127.0.0.1
```

## How to use Rest API
##### this will be updated soon

- address: http://127.0.0.1:8080/api/engine
- method: POST
- body: 
```json {
  "algorithm_signature" : "upper_case_posts",
  "algorithm_language": "python",
  "data":
  [
    {"name": "test1","message": "test message"},
    {"name": "test2","message": "test message"},
    {"name": "test3","message": "test message"},
    {"name":"test4","message": "test message"},
    {"name": "test5","message": "test message"}
  ]
}
```
- example data, JSON format


