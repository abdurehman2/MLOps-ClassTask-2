// pipeline {
//     agent any
    
//     environment {
//         DOCKERHUB_CREDENTIALS = credentials('dockerhub')
//         DOCKER_IMAGE = "abdurehman20/flask-app"  
//     }
    
//     stages {
//         stage('Clone Repository') {
//             steps {
//                 git branch: 'main', url: 'https://github.com/abdurehman2/MLOps-ClassTask-2.git'
//             }
//         }
        
//         stage('Build Docker Image') {
//             steps {
//                 script {
//                     docker.build("${DOCKER_IMAGE}:latest")
//                 }
//             }
//         }

//         stage('Push Docker Image to Docker Hub') {
//             steps {
//                 script {
//                     docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
//                         docker.image("${DOCKER_IMAGE}:latest").push()
//                     }
//                 }
//             }
//         }

//         stage('Cleanup') {
//             steps {
//                 script {
//                     sh 'docker rmi ${DOCKER_IMAGE}:latest'
//                 }
//             }
//         }
//     }
    
//     post {
//         success {
//             echo 'Docker image successfully pushed to Docker Hub!'
//         }
//         failure {
//             echo 'Pipeline failed!'
//         }
//     }
// }
