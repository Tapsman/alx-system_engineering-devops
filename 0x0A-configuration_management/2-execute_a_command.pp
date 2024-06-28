# Creates a manifest that uses puppet to kill a process killmenow
exec { 'killmenow':
	command	 =>  '/usr/bin/pkill killmenow',
	provider =>  'shell',
	returns  =>  [0, 1],
}

