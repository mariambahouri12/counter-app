pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        IMAGE     = "laykoun123/counter-app"
        DOCKERHUB = credentials('dockerhub-creds')
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Build et tests unitaires') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt -r requirements-dev.txt
                    pytest -v
                '''
            }
        }

        stage('Build image Docker') {
            steps {
                sh 'docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .'
            }
        }

        stage('Push Docker Hub') {
            steps {
                sh 'echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USR --password-stdin'
                sh 'docker push $IMAGE:$BUILD_NUMBER'
                sh 'docker push $IMAGE:latest'
            }
        }
    }

    post {
        always { sh 'docker logout || true' }
    }
}
