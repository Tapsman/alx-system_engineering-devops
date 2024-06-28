# Creates a manifest that uses puppet to kill a process killmenow
exec {'pkill killmenow':
	path => '/usr/bin:/usr/sbin:/bin'
}

