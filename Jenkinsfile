pipeline {
    agent any
    def dockerImage = ''

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
                docker {$"dockerImage".id}
            }
            steps{
                script{
                    python3 hello.py                    
                }
            }
        }
    }
}
