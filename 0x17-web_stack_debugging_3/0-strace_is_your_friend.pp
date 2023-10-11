# correct server configration to use the correct files
exec { 'extension':
command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
provider => shell
}
