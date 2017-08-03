<img align="right" src="https://raw.github.com/cliffano/jenkins-apiai-demo/master/avatar.jpg" alt="Avatar"/>

Jenkins api.ai Demo
-------------------

Demo project for [Jenkins CI](http://jenkins-ci.org) and [api.ai](http://api.ai) integration using AWS API Gateway and Lambda as the webhooks.

Architecture
------------

[![Architecture Diagram](https://raw.github.com/cliffano/jenkins-apiai-demo/master/architecture.jpg)](https://raw.github.com/cliffano/jenkins-apiai-demo/master/architecture.jpg)

| Component      | Description                                                                                |
|----------------|--------------------------------------------------------------------------------------------|
| apiai-agent    | Exported api.ai agent configuration                                                        |
| apiai-webhooks | AWS API Gateway and Lambda serving as api.ai webhooks which proxies requests to Jenkins CI |
| jenkins-data   | Jenkins jobs configuration files                                                           |

Installation
------------

Requirements:

* Install [Chalice](https://github.com/awslabs/chalice), used for managing api.ai webhooks
* Install [Nestor](https://github.com/cliffano/nestor), used for creating Jenkins jobs

Download Jenkins api.ai Demo code:

    git clone https://github.com/cliffano/jenkins-apiai-demo

Configuration
-------------

Configure `jenkins_host`, `jenkins_username`, and `jenkins_password` in `apiai-webhooks/.chalice/config.json` .

Configure `webhook/url` in `apiai-agent/agent.json` .

Set `JENKINS_URL` environment variable in the form of `<protocol>://<username>:<password>@<host>:<port>` .

Usage
-----

Create Jenkins jobs:

    make create-jenkins-jobs

Deploy api.ai webhooks:

    make deploy-apiai-webhooks

Login to api.ai and import the content of `apiai-agent` .


Colophon
--------

Presentations:

* TODO

Related Projects:

* [swaggy-jenkins](http://github.com/cliffano/swaggy-jenkins) - A set of Jenkins API clients in multiple languages generated from Swagger / Open API specification
