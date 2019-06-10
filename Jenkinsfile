#!/usr/bin/env groovy

stage("Welcome!") {
	println("Hello world!")
}

def do_work_func(lable) {
	node(lable) {
		stage("Some work") {
			ws("my_workspace") {
				println "Running on node ${env.NODE_NAME}"

				sh 'ls -la'

				sh '''
					pwd
				'''
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
