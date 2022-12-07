

sed  's/print/&(/' release_version.py
sed -i 's/print/&(/' release_version.py
sed  '/^print/{s/$/ )/}' release_version.py
sed  -i  '/^print/{s/$/ )/}' release_version.py
