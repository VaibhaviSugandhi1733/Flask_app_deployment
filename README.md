

\# End-to-End Flask App Deployment with Jenkins Freestyle Job



This project showcases an end-to-end CI/CD pipeline that builds a custom Docker image for a Python Flask app and deploys it using Jenkins Freestyle Job.



\## 🚀 Overview



\- Goal: Automatically build and run a Flask app inside a Docker container using Jenkins Freestyle Job.

\- Tech Stack: Python, Flask, Docker, Jenkins, GitHub

\- Repository: \[GitHub Repo](https://github.com/VaibhaviSugandhi1733/Flask\_app\_deployment.git)



---



\## 📦 Technologies Used



\- Python 3.x

\- Flask

\- Docker

\- Jenkins (Freestyle Job)

\- Git \& GitHub

\- HTML (basic inline frontend)



---



\## 📁 Project Structure



```



Flask\\\_app\\\_deployment/

├── app.py                 # Main Flask application

├── Dockerfile             # Dockerfile to containerize the app

├── requirements.txt       # Flask and other dependencies

└── README.md              # Project description



````



---



\## 🐳 Dockerfile



Example Dockerfile:

```dockerfile

FROM python:3.10-slim



WORKDIR /app



COPY . .



RUN pip install -r requirements.txt



EXPOSE 5000



CMD \["python", "app.py"]

````



---



\## 🔧 Jenkins Freestyle Job Configuration



1\. Create a new Freestyle project in Jenkins.



2\. Source Code Management:



&nbsp;  \* Select Git

&nbsp;  \* Enter Repository URL: `https://github.com/VaibhaviSugandhi1733/Flask\_app\_deployment.git`



3\. Build Triggers (optional):



&nbsp;  \* Poll SCM or GitHub webhook



4\. Build Environment:



&nbsp;  \* Ensure Docker is installed and Jenkins has permission to run Docker.



5\. Build Steps → Execute Shell:



&nbsp;  ```bash

&nbsp;  #!/bin/bash



&nbsp;  echo "Building Docker image..."

&nbsp;  docker build -t flask-jenkins-app .



&nbsp;  echo "Removing old container if exists..."

&nbsp;  docker rm -f flask-app || true



&nbsp;  echo "Running container..."

&nbsp;  docker run -d -p 5000:5000 --name flask-app flask-jenkins-app

&nbsp;  ```





---



\## 🌐 Application Route



Once the Jenkins job runs successfully, access the Flask app at:



```

http://<your-server-ip>:5000/

```



Example:



```

http://localhost:5000/

```



---





---



\## 📬 Contact



\*\*Vaibhavi Sugandhi\*\*

📧 Email: \[vaibhavi@example.com](mailto:vaibhavi@example.com)

🔗 LinkedIn: \[linkedin.com/in/vaibhavisugandhi](https://linkedin.com/in/vaibhavisugandhi)

💻 GitHub: \[github.com/VaibhaviSugandhi1733](https://github.com/VaibhaviSugandhi1733)



---



\## 📝 License



This project is licensed under the MIT License.



```





