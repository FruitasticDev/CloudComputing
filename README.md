# Fruitastic-Backend

- [Fruitastic-Backend](#Fruitastic-backend)
  - [Fruitastic](#Fruitastic)
  - [Documentation](#documentation)
  - [Backend and Cloud Architecture](#backend-and-cloud-architecture)
  - [Tech Stack](#tech-stack)
  - [Dependencies](#dependencies)
  - [Code Configuration](#code-configuration)
  - [Service Account Configuration](#Service-Account-Configuration)
  - [Local Development](#local-development)
  - [Configuration for Cloud Function](#configuration-for-cloud-function)
  - [Deployment To Google Cloud Platform](#deployment-to-google-cloud-platform)
  - [Public API](#public-api-this-project-use)

# Fruitastic

Fruitastic-Backend is a backend component of Fruitastic, an application that tracks fruit freshness and helps users assess the quality of the fruit they consume.


## Backend and Cloud Architecture

![FruitasticDev Cloud Architecture]![End User fix](https://github.com/user-attachments/assets/6b392282-a4b6-4d9d-a49a-32c1434ff2e7)


## Tech Stack

- Express.js
- Firebase
- Google Cloud Platform (GCP) services:
  - Cloud Functions
  - App Engine
  - Cloud Storage/Buckets

## Dependencies

- body-parser
- cors
- dotenv
- express
- firebase
- firebase-admin
- moment
- multer
- @google-cloud/storage
- nodemon
- Flask
- keras
- numpy
- pillow
- tensorflow-cpu
- gunicorn
- Werkzeug


## Code Configuration

To run this project, you will need to add the following environment variables to your `.env` file:

### Express Server Configuration
```
- `PORT=YOUR-PORT`
- `HOST=YOUR-HOST`
- `HOST_URL=http://YOUR-HOST:YOUR-PORT`
```
### Firebase Database Configuration

To obtain the required configuration, create a Firebase project and retrieve the following details:
```
API_KEY
AUTH_DOMAIN
PROJECT_ID
STORAGE_BUCKET
MESSAGING_SENDERID
APP_ID
```

## Documentation
Documentation API url: [https://docs.google.com/document/u/0/d/1dEyJzISDItxLhURuvhBKuBnJBaLflC3K/edit?usp=sharing&rtpof=true&sd=true&pli=1&authuser=0]

## Local Development
Follow these steps to run the Fruittastic-Backend locally:

Clone the project, navigate to the project directory, and install dependencies

```bash
git clone https://github.com/FruitasticDev/CloudComputing.git
cd FruitastiDev
cd CloudComputing
npm install
```
Start the server

```bash
  npm run start
```

## Configuration for Cloud Function
To configure the Fruitastic-Backend for deployment to Google Cloud Functions, follow these steps

Install the Firebase CLI:
```bash
npm install -g firebase-tools
```

Navigate to the project directory and initialize Firebase
```bash
cd fruitastic/firebasefunction
firebase init
```
Change to the Functions directory, install dependencies, and go back to the project directory
```bash
cd Functions
npm install
cd ../
```

Deploy your code to cloud function
```bash
firebase deploy --only functions
```

## Deployment To Google Cloud Platform

Clone the project, navigate to the project directory, and install dependencies

```bash
git clone https://github.com/FruitasticDev/CloudComputing.git
cd Fruitastic
cd CloudComputing
npm install
```

Deploy to App Engine

```bash
gcloud app deploy
```
