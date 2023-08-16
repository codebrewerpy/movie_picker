def dockerImage = ''
pipeline {
    agent any

    stages {
        stage('Build Docker') {
            steps {
                script {
                    dockerImage = docker.build('python:1')
                }
            }
        }

        stage('Test Dockerimage') {
            agent {
                docker "${dockerImage}.id"
                reuseNode true
            }
            steps{
                script{
                    sh 'python3 hello.py'                    
                }
            }
        }
    }
}
