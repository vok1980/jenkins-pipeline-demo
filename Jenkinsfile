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
						sh 'ctest --output-on-failure -T test || echo "Some tests failed"'
					}
					else {
						bat 'dir'
						bat 'cmake -S .. -B .'
						bat 'cmake --build . --config Release'
						bat 'ctest --output-on-failure -T test -C Release || echo "Some tests failed"'
					}

					xunit (
						thresholds: [
							failed(unstableThreshold: '0', unstableNewThreshold: '0', failureThreshold: '100', failureNewThreshold: '100')
						],
						tools: [ CTest(pattern: "Testing/**/Test.xml") ]
					)
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
