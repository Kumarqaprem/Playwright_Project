pipeline {
    agent any

    stages {
        stage('Run Automation Tests') {
            steps {
                sh 'echo Running automation tests'
                sh 'pytest'
            }
        }
    }

    post {
        success {
            emailext(
                subject: "Build Success",
                body: "Automation execution completed successfully",
                to: "qakumarlead@gmail.com"
            )
        }
        failure {
            emailext(
                subject: "Build Failed",
                body: "Automation execution failed. Please check Jenkins logs.",
                to: "qakumarlead@gmail.com"
            )
        }
    }
}