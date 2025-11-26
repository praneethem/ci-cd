pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "No build step needed for Python CLI app"
            }
        }

        stage('Test') {
            steps {
                sh 'echo 4 | python3 src/todo.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t praneethem/todo-cli:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'echo 4 | docker run --rm praneethem/todo-cli:latest'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: "docker-creds", usernameVariable: "USER", passwordVariable: "PASS")]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push praneethem/todo-cli:latest'
                }
            }
        }
    }
}

