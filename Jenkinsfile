#!/usr/bin/env groovy

stage("Welcome!") {
	println("Hello world!")
}

def do_work_func(lable) {
	node(lable) {
		stage("Some work") {
			ws("my_workspace") {
				println "Running on node ${env.NODE_NAME}"

				checkout scm

				dir('build') {
					deleteDir()
					writeFile file:'dummy', text:''

					if (isUnix()) {
						sh 'ls -la'

						sh '''
							pwd
						'''

						sh 'cmake -DCMAKE_BUILD_TYPE=Release ..'
						sh 'cmake --build .'
						sh 'ctest --output-on-failure'
					}
					else {
						bat 'dir'
						bat 'cmake -S .. -B .'
						bat 'cmake --build . --config Release'
						bat 'ctest --output-on-failure -C Release'
					}
				}
			}
		}
	}
}

node() {
	parallel 'do linux': {
		do_work_func('linux')
	},
	'do windows': {
		do_work_func('windows')
	}
}

stage("Bye!") {
	println("BB2A")
	println("!!!!")
}
