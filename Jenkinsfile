def dockerImage = ''
void test() {
    sh 'touch try.txt'
    sh 'ls -la'
    sh 'cd / && ls -d */'
    sh 'touch itsMe.txt'
    sh 'echo "Hi its meeeee!" >> itsMe.txt'
    sh 'touch itsMe.txt'
}
repo = [
    imageNmae: 'its.a.test:123/idontknow.work/python:1'
]
pipeline {
    agent any

    stages {
        stage('Build Docker') {
            steps {
                script {
                    dockerImage = docker.build("${repo.imagename}")
                }
            }
        }

        stage('Test Dockerimage') {
            agent {
                docker {
                    //image "${dockerImage.id}"
                    image "${repo.imagename}"
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
