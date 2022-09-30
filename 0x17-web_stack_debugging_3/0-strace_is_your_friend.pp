#Fix Apache returning a 500 error
exec {'PHPSetting':
  command => 'sed -i "s/.phpp/g" /var/www/html/wp-settings.php',
  provider => shell
}
