Crypto Sublime Text 2 and 3 Package
=============================

### Encrypt/ Decrypt a document or selection(s) using OpenSSL

This Package depends on `openssl`

![Preview](https://github.com/mediaupstream/SublimeText-Crypto/raw/master/screenshots/Crypto2.gif)

Install
-------
Installation via the [Package Control](http://wbond.net/sublime_packages/package_control) (Search for `Crypto`)
  
To install manually clone this project into your `Sublime Text 2\Packages` folder:

*OSX*

    git clone git://github.com/mediaupstream/SublimeText-Crypto.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Crypto

*Windows*

    git clone git://github.com/mediaupstream/SublimeText-Crypto.git "%APPDATA%\Sublime Text 2\Packages\Crypto"



Usage
-----
After installation you will have:  

* Right-click menu item `Crypto` and `Tools > Crypto` with two options:  
  - `Encrypt`
  - `Decrypt`
* Default keyboard shortcuts:  
  - `⌘+K,e` on OSX or `ctrl+K,e` on Linux/Windows (Encrypt)
  - `⌘+K,d` on OSX or `ctrl+K,d` on Linux/Windows (Decrypt)
* Package Settings: `Preferences > Package Settings > Crypto`  
  - Set the path to your `openssl` executable - default: `openssl`
  - Set the Encryption Cipher - default: `-aes128`


The commands work on a selection, multiple selections or if nothing is selected the whole document. Once you trigger the command you will be prompted to enter a password.


Todo
----
* ~~Test on Linux and Windows~~
* Add other functionality:
  - encryption on save
  - encrypt/decrypt multiple files, or all open files
  - encrypt/decrypt using a keyfile
  - etc...


Author & Contributors
----------------------
[Derek Anderson](http://twitter.com/derekanderson)  
[Isaac Muse](https://github.com/facelessuser)


License
-------
MIT License
