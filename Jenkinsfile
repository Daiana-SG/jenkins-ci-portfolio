pipeline {
  agent any

  options {
    timestamps()
    disableConcurrentBuilds()
  }

  parameters {
    booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Ejecutar tests')
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh 'ls -la'
      }
    }

    stage('Tests') {
      when { expression { return params.RUN_TESTS } }
      steps {
        sh '''
          set -eux
          python3 --version

          python3 -m venv .venv
          . .venv/bin/activate

          pip install --upgrade pip
          pip install pytest

          mkdir -p reports
          pytest -q --junitxml=reports/junit.xml
          ls -la reports
        '''
      }
      post {
        always {
          // Publicar resultados SOLO si existe el archivo
          script {
            if (fileExists('reports/junit.xml')) {
              junit 'reports/junit.xml'
            } else {
              echo "No se generó reports/junit.xml (tests no llegaron a correr o fallaron antes)."
            }
          }
        }
      }
    }
  }

  post {
    always {
      cleanWs()
    }
  }
}

