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
                sh 'python3 -m pytest -s --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'allure generate allure-results --clean -o allure-report'
            }
        }
    }

    post {
        success {
            emailext(
                subject: "Build Success - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    <html>
                    <body>
                        <h2 style="color:green;">Build Successful!</h2>
                        <table>
                            <tr><td><b>Job:</b></td><td>${env.JOB_NAME}</td></tr>
                            <tr><td><b>Build Number:</b></td><td>#${env.BUILD_NUMBER}</td></tr>
                            <tr><td><b>Status:</b></td><td>SUCCESS</td></tr>
                            <tr><td><b>Build URL:</b></td><td><a href="${env.BUILD_URL}">${env.BUILD_URL}</a></td></tr>
                        </table>
                        <br>
                        <p>Please find the Allure Test Report attached.</p>
                    </body>
                    </html>
                """,
                mimeType: 'text/html',
                to: "qakumarlead@gmail.com",
                attachmentsPattern: 'allure-report/**/*'
            )
        }

        failure {
            emailext(
                subject: "Build Failed - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    <html>
                    <body>
                        <h2 style="color:red;">Build Failed!</h2>
                        <table>
                            <tr><td><b>Job:</b></td><td>${env.JOB_NAME}</td></tr>
                            <tr><td><b>Build Number:</b></td><td>#${env.BUILD_NUMBER}</td></tr>
                            <tr><td><b>Status:</b></td><td>FAILED</td></tr>
                            <tr><td><b>Build URL:</b></td><td><a href="${env.BUILD_URL}">${env.BUILD_URL}</a></td></tr>
                        </table>
                        <br>
                        <p>Please find the Allure Test Report attached.</p>
                    </body>
                    </html>
                """,
                mimeType: 'text/html',
                to: "qakumarlead@gmail.com",
                attachmentsPattern: 'allure-report/**/*'
            )
        }
    }
}