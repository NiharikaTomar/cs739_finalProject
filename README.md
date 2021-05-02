## Setup

### Requirements:

1. Python Version: 3.8
2. Pip Version: pip 21.0
3. Docker version 20.10.5
4. CouchDB Version: 3.1.1

### Python Environment Setup:

We will use python virtual environment. For setting that up, open a bash terminal and run the following commands:

```
# Make a directory where you can keep your virtual environments (if you don’t already have one)
$ mkdir ~/envs
```

 ```
# Make a virtual environment called ’cs739p4’
$ virtualenv --python=python3.8 ~/envs/cs739p4
```

```
# activate the virtual environment
$ source ~/envs/cs739p4/bin/activate
```

```
(cs739p4) $ pip install -r requirements.txt
```

```
(cs739p4) $ python shortener.py
```

When you don’t need the virtual environment, just ‘deactivate’ it

```
(cs739p1) $ deactivate
```

### CouchDB Setup:

Installation: 
- [Official Documentation](https://docs.couchdb.org/en/stable/install/docker.html)

Cluster setup:
- [Medium post](https://medium.com/@singinjon/cluster-couchdb-2-and-docker-on-localhost-f0490649d960)
- [Official Documentation](https://docs.couchdb.org/en/stable/setup/cluster.html)

Replication setup:
- After cluster setup, just add address of other two nodes for enabling replication.

Database initialization:
- Create database 'key_value_store'
- Creating database for one instance will automatically reflect in all instances
