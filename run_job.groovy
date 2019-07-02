
def job_echo(text) {
	build job: 'echo',
		wait: true,
		propagate: true,
		parameters: [
			string(name: 'TEXT', value: "${text}"),
		]
}


return this
