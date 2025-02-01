pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/kabilesh667/ci-cd-web-app.git'
        DOCKER_IMAGE = 'kabilesh667/ci-cd-web-app:latest'
        SONAR_HOST = 'http://192.168.31.240:9000'
        SONAR_TOKEN = 'sqa_2e2279482ee22241b073345f0b1a18966b3d7532'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${GITHUB_REPO}"
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    sh """
                    /opt/sonar-scanner/bin/sonar-scanner -Dsonar.projectKey=ci-cd-web-app \
                    -Dsonar.host.url=${SONAR_HOST} \
                    -Dsonar.login=${SONAR_TOKEN}
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh """
                    docker login -u kabilesh667 -p SK@123#!sk
                    docker push ${DOCKER_IMAGE}
                    docker logout
                    """
                }
            }
        }

        stage('Deploy Application') {
            steps {
                script {
                    sh """
                    docker pull ${DOCKER_IMAGE}
                    docker stop ci-cd-web-app || true
                    docker rm ci-cd-web-app || true
                    docker run -d -p 8081:8080 --name My-Web-App ${DOCKER_IMAGE}
                    """
                }
            }
        }
    }
}
