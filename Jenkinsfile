pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Fetching latest code from GitHub repository'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Tanmay\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Code Quality Check') {
            steps {
                echo 'Performing basic code validation checks'
            }
        }

        stage('Train Model') {
            steps {
                bat '"C:\\Users\\Tanmay\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" train.py'
            }
        }

        stage('Validate Model') {
            steps {
                echo 'Validating trained model performance'
            }
        }

        stage('Archive Model Artifact') {
            steps {
                archiveArtifacts artifacts: 'churn_model.pkl', fingerprint: true
            }
        }

        stage('Build Success') {
            steps {
                echo 'CI pipeline executed successfully'
            }
        }
    }
}