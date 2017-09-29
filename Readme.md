Crypto Sublime Text 2 and 3 Package
=============================

### Encrypt/ Decrypt a document or selection(s) using OpenSSL

This Package depends on `openssl`

![Preview](https://github.com/mediaupstream/SublimeText-Crypto/raw/master/screenshots/Crypto2.gif)

Install
-------
**Recommended:** Installation via the [Package Control](http://wbond.net/sublime_packages/package_control) (Search for `Crypto`)
  
To install manually clone this project into your `Sublime Text 2|3\Packages` folder:

### OSX
**SublimeText 2**:   
```bash
git clone git://github.com/mediaupstream/SublimeText-Crypto.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/Crypto
```

**SublimeText 3**:    
```bash
git clone git://github.com/mediaupstream/SublimeText-Crypto.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Crypto
```

### Windows

**SublimeText 2**:   
```bash
git clone git://github.com/mediaupstream/SublimeText-Crypto.git "%APPDATA%\Sublime Text 2\Packages\Crypto"
```
**SublimeText 3**:   
```bash
git clone git://github.com/mediaupstream/SublimeText-Crypto.git "%APPDATA%\Sublime Text 3\Packages\Crypto"
```


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
  - Obfuscate the password input - default 'false'

**Note**:

By default password input will *not* be obfuscated. If you want your password input to be obfuscated you can change the setting `obfuscate_password` to `true` in your `Preferences > Package Settings > Crypto > Settings - User`.

If you choose to enable `obfuscate_password` please be aware that there is a bug with the implementation that doesn't allow you to copy/paste your password.

The commands work on a selection, multiple selections or if nothing is selected the whole document. Once you trigger the command you will be prompted to enter a password.


Todo
----
* ~~Test on Linux and Windows~~
* ~~Obscure Password with Asterisks~~
* Encrypt on save / Decrypt on open


Author & Contributors
----------------------
[Derek Anderson](http://twitter.com/derekanderson)  
[Isaac Muse](https://github.com/facelessuser)  
[Elliot Marsden](https://github.com/eddiejessup)  
[@circulosmeos](https://github.com/circulosmeos)


License
-------
MIT License
