def dockerImage = ''
void test() {
    sh 'touch try.txt'
    sh 'ls -la'
    sh 'cd / && ls -d */'
    sh 'touch itsMe.txt'
    sh 'echo "Hi its meeeee!" >> itsMe.txt'
    sh 'touch itsMe.txt'
}
pipeline {
    agent any

    stages {
        stage('Build Docker') {
            steps {
                script {
                    dockerImage = docker.build('its.a.test:123/iDontKnow.Work/python:1')
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
                    test()
                    sh 'python3 ./folder/bye.py'
                }
            }
        }
    }
}
