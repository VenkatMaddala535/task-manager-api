pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Workspace') {
            steps {
                sh '''
                echo "Current Workspace"
                pwd
                ls -la
                '''
            }
        }

        stage('Verify Tools') {
            steps {
                sh '''
                echo "Python Version"
                python3 --version

                echo "Git Version"
                git --version
                '''
            }
        }

        stage('Finish') {
            steps {
                echo "Pipeline Completed Successfully"
            }
        }

    }

}