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
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Test') {
            steps {
                // Commands to run tests
                sh 'echo "Running tests"'
            }
        }
        stage('Deploy') {
            steps {
                // Commands to deploy to Kubernetes
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
