pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Downloading your codebase from github"
                deleteDir()
                checkout scm
            }
        }

        stage('Python Setup') {
            steps {
                echo "setting up python environment"

                bat 'python --version'
                bat 'python -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'installing dependencies'

                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'

                bat '.venv\\Scripts\\python.exe -m pip install -r requirements-test.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'validating python application'

                bat '.venv\\Scripts\\python.exe -m compileall -q app.py backend.py'

                bat '.venv\\Scripts\\python.exe -m pip check'

                bat '.venv\\Scripts\\python.exe -c "from backend import app"'
            }
        }

        stage('Testing') {
            steps {
                echo 'Executing Automated Test Cases'

                bat '''
                 
                .venv\\Scripts\\python.exe -m pytest tests/ -v --junitxml=reports/test-results.xml --cov=backend --cov-report=html:reports/coverage 
                 '''
            }

            post {
                always {
                    junit (
                        testResults: "reports/test-results.xml",
                        allowEmptyResults: true
                    )

                    archiveArtificats(
                        artificats: 'reports/**/*',
                        allowEmptyArchive: true
                    )
                }
            }
        }
    }

    post {
        success {
            echo 'Build successful. All tests passed'
        }

        failure {
            echo 'Build Failed. Please check the console output'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}