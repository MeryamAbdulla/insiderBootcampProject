pipline {
    agent any
    environment {
        DEVELOPER_BRANCH = 'develop'
        BRANCH = "${BRANCH_NAME}"
        ANSIBLE_FORCE_COLOR = 'true'
    }

    stages {
        stage('Get Branch Name') {
            steps {
                script {
                    branch = env.BRANCH
                }
            }
        }

        stage('Set Pending Status') {
            steps {
                script {
                    sh 'echo "Pending"'
                }
            }
        }

        stage('Automation Process') {
            steps {
                script {
                    dir('/User/maryamabdullayeva/.jenkins/workspace/InsiderFinalProject') {
                        echo 'Automation Process running...'
                            sh 'pip3 install -r requirements.txt'
                            sh 'pwd'
                    }
                }
            }
        }

        post {
            always {
                echo 'Automation Process finished...'
            }
        }
    }
}