# Changing login user for holberton without errors


exec {'/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }

