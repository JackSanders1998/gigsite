# GigSite

GigSite contains frontend and backend directories.

## Installation

Use npm to install dependencies in both client and server.

```bash
cd frontend
npm install
cd ../backend
npm install
```


## Usage

<!-- Run client & server on the same CLI tab from dashboard directory:

```
npm start
```
<i>Note: this script simply calls: </i>
```
"scripts": {
    "start": "(cd server && npm start) & (cd client && npm start)"
}
```
-->
Run client & server on different CLI tabs:

```
$ cd backend && python manage.py runserver
```

```
$ cd frontend && npm run dev
```

<!--
## Deployment

### Install the Heroku CLI

Download and install the <a href="https://devcenter.heroku.com/articles/heroku-command-line" class="hk-link">Heroku CLI</a>

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

```
$ heroku login
```

### Clone the repository

Use Git to clone amp-dashboard-server's source code to your local machine.

```
$ heroku git:clone -a amp-dashboard-server
$ cd amp-dashboard-server
```

### Deploy your changes

Make some changes to the code you just cloned and deploy them to Heroku using Git.

```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
-->
## Contributing

Create as many branches as necessary to complete your project.

For pushes to master or merge pull requests, please contact <jack@ampmusic.co>.

## Copyright
Copyright (C) ampmusic.co LLC - All Rights Reserved
Unauthorized copying of this repository, via any medium is strictly prohibited
Proprietary and confidential
Written by ampmusic.co, September 2021
