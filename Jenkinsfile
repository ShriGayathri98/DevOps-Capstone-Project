pipeline {
    agent any
    environment {
        // Define environment variables
        DOCKER_IMAGE = "shrigayathri98/my-flask-app:latest"
    }
    stages {
        stage('Build') {
            steps {
                // Commands to build your Docker image
                bat 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Test') {
            steps {
                // Commands to run tests
                bat 'echo "Running tests"'
            }
        }
        stage('Deploy') {
            steps {
                // Commands to deploy to Kubernetes
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
}
