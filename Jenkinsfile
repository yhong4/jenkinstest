pipeline {
    agent any


    stages {
        stage ('Install_Requirements') {
            steps {
                withPythonEnv('/usr/bin/python3.7') {
                    sh """
                        echo ${SHELL}
                        [ -d venv ] && rm -rf venv
                        pip install virtualenv
                        #virtualenv --python=python3.7 venv
                        virtualenv venv
                        #. venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    """
                }
            }
        }
        stage ('Deploy') {
            steps {
                withPythonEnv('/usr/bin/python3.7') {
                    sh """
                        sls deploy
                    """
                }
            }
        }
    } 
}
