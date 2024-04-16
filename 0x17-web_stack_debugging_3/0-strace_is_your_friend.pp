# A puppet manuscript to replace a line in a file on a server

$file_path = "/var/www/html/wp-settings.php"

# Go into file, and replace the line containing "phpp" with "php"

exec { "replace_line":
    command => "sed -i 's/phpp/php/g' ${file_path}",
    path    => ['/bin','/usr/bin']
}