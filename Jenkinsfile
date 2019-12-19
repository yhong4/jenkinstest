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
            tools {nodejs "okmath-nodejs"}
            steps {
                sh """
                    npm install
                    npm install -g serverless
                    sls config credentials -p aws --key ${AWS_ACCESS_KEY_ID} --secret ${AWS_SECRET_ACCESS_KEY}
                    sls deploy --stage dev
                """
            }
        }
    } 

     environment {
	 		AWS_ACCESS_KEY_ID = "AKIAWDNCMCBINHHPGHNA"
			AWS_SECRET_ACCESS_KEY = "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"
	 }
}
