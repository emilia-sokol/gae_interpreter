# GAE Interpreter
Interpreter module for Internet of Things Ecosystem


## 🚀 Getting Started


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

#### 2. JPY (POSSIBLY THIS WILL NOT BE USED)

```cmd
 > cd lib/jpy/
 > export JDK_HOME=<your-jdk-dir>
 > export JAVA_HOME=$JDK_HOME
 > python get-pip.py

 # optional step:
 > sudo apt-get install python-dev
 > python setup.py build maven bdist_wheel
```

then in python type
```python
import sys
sys.path.append('build/lib-os-platform-python-version')
```
or copy jpy folder to site-packages directory

if you have JAVA_HOME in .bashrc:
 echo $JAVA_HOME
if empty line:
 . ~/.bashrc


#### 2. Run
- use Python 2.7 interpreter
- add GAE SDK path 


to run from terminal:
```cmd
> python /your/path/to/google-cloud-sdk/bin/dev_appserver.py --host 127.0.0.1
```


#### 3. Dev tools
format html, js or css code:
```cmd
> npm run prettier
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




