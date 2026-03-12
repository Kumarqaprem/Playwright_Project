pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Install Playwright Browsers') {
            steps {
                sh 'python3 -m playwright install'
            }
        }
        stage('Run Automation Tests') {
            steps {
                sh 'python3 -m pytest -s --html=report.html --self-contained-html'
            }
        }
    }

    post {
        success {
            emailext(
                subject: "Build Success - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    Build Status: SUCCESS
                    Job: ${env.JOB_NAME}
                    Build Number: ${env.BUILD_NUMBER}
                    Build URL: ${env.BUILD_URL}
                    
                    Automation execution completed successfully!
                """,
                to: "qakumarlead@gmail.com"
            )
        }
        failure {
            emailext(
                subject: "Build Failed - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    Build Status: FAILED
                    Job: ${env.JOB_NAME}
                    Build Number: ${env.BUILD_NUMBER}
                    Build URL: ${env.BUILD_URL}
                    
                    Automation execution failed. Please check Jenkins logs.
                """,
                to: "qakumarlead@gmail.com"
            )
        }
    }
}