
# 🚀 Flask Docker Deployment with Jenkins CI/CD (Freestyle Job)

This project demonstrates a complete CI/CD pipeline where a Python Flask application is containerized with Docker, pushed to Docker Hub, and deployed automatically using a Jenkins Freestyle Job.

---

## 📚 Project Overview

- **App**: Python Flask Web App  
- **CI/CD Tool**: Jenkins (Freestyle Job)  
- **Containerization**: Docker  
- **Image Hosting**: Docker Hub  
- **Source Code**: [GitHub Repository](https://github.com/VaibhaviSugandhi1733/Flask_app_deployment.git)

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- Docker
- Jenkins
- Git & GitHub

---

## 📁 Folder Structure

```

Flask\_app\_deployment/
├── app.py                 # Flask application script
├── Dockerfile             # Docker image build instructions
├── requirements.txt       # Project dependencies
└── README.md              # Documentation

````

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
````

---

## ⚙️ Jenkins Freestyle Job Setup

### 1. Create Freestyle Job

* Open Jenkins → New Item → Freestyle project → Name it (e.g., `flask-ci-docker`)
* Enable **Git** and add your repository URL:

  ```
  https://github.com/VaibhaviSugandhi1733/Flask_app_deployment.git
  ```

### 2. Build Step → Execute Shell

Paste the following in **Execute Shell**:

```bash
#!/bin/bash

echo "🔁 Pulling latest code..."
git pull origin main

echo "🐳 Building Docker image..."
docker build -t vaibhavisugandhi/flask-jenkins-app:latest .

echo "📤 Pushing image to Docker Hub..."
echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin
docker push vaibhavisugandhi/flask-jenkins-app:latest

echo "🧹 Removing old container if exists..."
docker rm -f flask-app || true

echo "🚀 Running new container..."
docker run -d -p 5000:5000 --name flask-app vaibhavisugandhi/flask-jenkins-app:latest
```

> 🔐 **Note**: Store Docker Hub credentials in Jenkins as environment variables:

* `DOCKERHUB_USERNAME`
* `DOCKERHUB_PASSWORD`

### 3. Save & Build the Project

---

## 🌐 Accessing the Flask App

After a successful build:

```
http://<your-server-ip>:5000/
```

Example:

```
http://localhost:5000/
```

---


## 🙋‍♀️ Author

**Vaibhavi Sugandhi**
📧 Email: [vaibhavi@example.com](mailto:vaibhavi.sugandhi03@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/vaibhavisugandhi)
💻 [GitHub](https://github.com/VaibhaviSugandhi1733)
🐳 [Docker Hub](https://hub.docker.com/u/vaibhavisugandhi1733)

---


---

### ✅ Summary of Updates:
- Added **Docker Hub push command**
- Used **env variables for Docker credentials**
- Beautified with icons and polished formatting
- Structured everything for **maximum clarity**



