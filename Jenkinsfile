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
                sh '/usr/local/bin/allure generate allure-results --clean -o allure-report'
            }
        }
    }

    post {
        success {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'allure-report',
                reportFiles: 'index.html',
                reportName: 'Allure Report'
            ])
            emailext(
                subject: "Build Success - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    <html>
                    <body>
                        <h2 style="color:green;">Build Successful!</h2>
                        <table border="1" cellpadding="8">
                            <tr><td><b>Job</b></td><td>${env.JOB_NAME}</td></tr>
                            <tr><td><b>Build Number</b></td><td>#${env.BUILD_NUMBER}</td></tr>
                            <tr><td><b>Status</b></td><td style="color:green;"><b>SUCCESS</b></td></tr>
                            <tr><td><b>Build URL</b></td><td><a href="${env.BUILD_URL}">${env.BUILD_URL}</a></td></tr>
                        </table>
                        <br>
                        <h3>View Allure Report:</h3>
                        <p><a href="${env.BUILD_URL}Allure_20Report/">
                        Click Here to View Full Allure Report</a></p>
                    </body>
                    </html>
                """,
                mimeType: 'text/html',
                to: "qakumarlead@gmail.com"
            )
        }

        failure {
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'allure-report',
                reportFiles: 'index.html',
                reportName: 'Allure Report'
            ])
            emailext(
                subject: "Build Failed - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    <html>
                    <body>
                        <h2 style="color:red;">Build Failed!</h2>
                        <table border="1" cellpadding="8">
                            <tr><td><b>Job</b></td><td>${env.JOB_NAME}</td></tr>
                            <tr><td><b>Build Number</b></td><td>#${env.BUILD_NUMBER}</td></tr>
                            <tr><td><b>Status</b></td><td style="color:red;"><b>FAILED</b></td></tr>
                            <tr><td><b>Build URL</b></td><td><a href="${env.BUILD_URL}">${env.BUILD_URL}</a></td></tr>
                        </table>
                        <br>
                        <h3>View Allure Report:</h3>
                        <p><a href="${env.BUILD_URL}Allure_20Report/">
                        Click Here to View Full Allure Report</a></p>
                    </body>
                    </html>
                """,
                mimeType: 'text/html',
                to: "qakumarlead@gmail.com"
            )
        }
    }
}