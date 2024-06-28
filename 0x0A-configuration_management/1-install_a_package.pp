#!/usr/bin/pup
# Installs flask from pip3 and version is 2.1.0
package {'flask':
	ensure	 => '2.1.0'
	provider => 'pip'
} 


