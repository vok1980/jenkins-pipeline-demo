#!/usr/bin/env groovy

stage("Welcome!") {
	println("Hello world!")
}

def do_work_func(message) {
	node() {
		stage("Some work") {
			ws("my_workspace") {
				println "Running on node ${env.NODE_NAME}"
				println(message)

				sh 'ls -la'

				sh '''
					pwd
				'''
			}
		}
	}
}

node() {
	parallel 'do 1': {
		do_work_func(1111111111111111)
	},
	'do 2': {
		do_work_func(2222222222222222)
	}
}

stage("Bye!") {
	println("BB2A")
	println("!!!!")
}
