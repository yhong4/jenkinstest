pipeline {
    agent any
    stages {
        stage ('Install_Requirements') {
            steps {
                sh """
                    echo ${SHELL}
                    [ -d venv ] && rm -rf venv
                    pip install virtualenv
                    #virtualenv --python=python3.8 venv
                    virtualenv venv
                    #. venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt -r dev-requirements.txt
                    make clean
                """
            }
        }
    } 
}
