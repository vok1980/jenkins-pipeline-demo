#!/usr/bin/env groovy

stage("Welcome!") {
	println("Hello world!")
}

node() {
	stage("Some work") {
		ws("my_workspace") {
			sh 'ls -la'

			sh '''
				pwd
			'''
		}
	}
}

stage("Bye!") {
	println("BB2A")
	println("!!!!")
}
