# Handles 500 Apache error by renaming a file
exec { 'renamefile':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => '/bin/',
}
