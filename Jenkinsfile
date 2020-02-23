pipeline {
    parameters {
        string(name: 'param1', defaultValue: '', description: 'Greeting message')
        string(name: 'param2', defaultValue: '', description: '2nd parameter')
        choice(name: 'PLATFORM_FILTER', choices: ['all', 'linux', 'windows', 'mac'], description: 'Run on specific platform')
    }
    
    agent {
        label 'linux'
    }

    stages {

        stage("Get dependencies and publish build info"){
            steps {
                sh "mkdir -p build"
                dir ('build') {
                    //def b = client.run(command: "install ..")
                    //server.publishBuildInfo b
                    sh "conan install .."
                }
            }

        }

        stage("Build/Test project"){
            steps {
                dir ('build') {
                    sh "cmake ../ && cmake --build ."
                }
            }
        }

    }
}