# Fix Apache returning a 500 error
exec {'PHPSetting':
  command  => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  provider => shell
}
