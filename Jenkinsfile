def dockerImage = ''
pipeline {
    agent any

    stages {
        stage('Build Docker') {
            steps {
                script {
                    dockerImage = docker.build('its.a.test:123/python:1')
                }
            }
        }

        stage('Test Dockerimage') {
            agent {
                docker {
                    image "${dockerImage.id}"
                    reuseNode true
                }
            }
            steps{
                script{
                    sh 'python3 hello.py'
                    sh 'ls -la'
                    sh 'cd / && ls -d */'
                }
            }
        }
    }
}
