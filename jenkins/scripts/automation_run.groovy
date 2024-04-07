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
                        sh 'python3 -m venv venv'
                        sh '. venv/bin/activate'
                        sh 'pip install -r requirements.txt'
                        sh 'export PYTHONPATH=$PYTHONPATH:/User/maryamabdullayeva/.jenkins/workspace/InsiderFinalProject/base'
                        sh 'python3 tests/test_pom_violation.py'
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