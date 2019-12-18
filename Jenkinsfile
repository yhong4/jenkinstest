pipeline {
    agent { docker { image 'python:3.8'}}
    stages {
        stage ('Install_Requirements') {
            steps {
                sh """
                    echo ${SHELL}
                    [ -d venv ] && rm -rf venv
                    #virtualenv --python=python3.8 venv
                    virtualenv venv
                    #. venv/bin/activate
                    export PATH=${VIRTUAL_ENV}/bin:${PATH}
                    pip install --upgrade pip
                    pip install -r requirements.txt -r dev-requirements.txt
                    make clean
                """
            }
        }
    } 
}
