from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>👩‍💻 About Me</h1>
    <p>Hello! I’m a passionate <strong>DevOps Enthusiast</strong> with a strong interest in automation, cloud, and CI/CD tools.</p>
    <p>I enjoy solving real-world problems using technologies like Docker, Kubernetes, Ansible, and more.</p>
    <p>I believe in continuous learning, collaboration, and building efficient, scalable systems.</p>
    <p>Explore the pages: <a href="/skills">Skills</a> | <a href="/projects">Projects</a> | <a href="/contact">Contact</a></p>
    '''

@app.route('/skills')
def skills():
    return '''
    <h1>🛠️ DevOps Skills</h1>
    <ul>
        <li>Linux Fundamentals</li>
        <li>Git & GitHub</li>
        <li>Docker & Docker Compose</li>
        <li>Kubernetes (Minikube, kubectl)</li>
        <li>Ansible</li>
        <li>CI/CD (Jenkins, GitHub Actions)</li>
        <li>AWS (EC2, S3, IAM)</li>
        <li>Python & Bash Scripting</li>
        <li>Monitoring Tools (Prometheus, Grafana)</li>
    </ul>
    <a href="/">Back to Home</a>
    '''

@app.route('/projects')
def projects():
    return '''
    <h1>📁 Projects</h1>
    <ol>
        <li><strong>Ansible Cluster Setup:</strong> Automated setup of a master-node Ansible cluster using Docker & Shell scripts.</li>
        <li><strong>Dockerized Web Scraper:</strong> Built and containerized a Python-based web scraper to collect live website data.</li>
        <li><strong>File Management using Python:</strong> Created a utility to organize files by type, extension, and date with logging.</li>
    </ol>
    <a href="/">Back to Home</a>
    '''

@app.route('/contact')
def contact():
    return '''
    <h1>📬 Contact Me</h1>
    <p><strong>Email:</strong> vaibhavi.sugandhi03@gmail.com</p>
    <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/vaibhavisugandhi" target="_blank">linkedin.com/in/vaibhavisugandhi</a></p>
    <p><strong>GitHub:</strong> <a href="http://github.com/VaibhaviSugandhi1733" target="_blank">github.com/VaibhaviSugandhi1733</a></p>
    <a href="/">Back to Home</a>
    '''

#  This runs the server
if __name__ == "__main__":
    app.run(host='0.0.0.0')
