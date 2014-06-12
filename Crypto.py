'''
@name     Crypto
@package  sublime_plugin
@author   Derek Anderson
@requires OpenSSL

This Sublime Text 2 plugin adds AES encryption/decryption
features to the right click context menu.

Usage: Make a selection (or not), Choose AES Encrypt or AES Decrypt 
from the context menu and then enter a password

'''

import sublime, sublime_plugin, os, random, string
from subprocess import Popen, PIPE, STDOUT

# -- try this to fix "Broken pipe", maybe
# from signal import signal, SIGPIPE, SIG_DFL
# signal(SIGPIPE,SIG_DFL)

ST3 = int(sublime.version()) >= 3000

#
# Capture user input (password) and send to the CryptoCommand
#
class AesCryptCommand(sublime_plugin.WindowCommand):
  def run(self, enc):
    self.enc = enc
    message = "Create a Password:" if enc else "Enter Password:"
    self.window.show_input_panel(message, "", self.on_done, None, None)
    pass
  def on_done(self, password):
    try:
      if self.window.active_view():
        self.window.active_view().run_command("crypto", {"enc": self.enc, "password": password})
    except ValueError:
        pass


#
# ST3 needs a Text Command called to insert text
#
class CryptoMessageCommand(sublime_plugin.TextCommand):
  def run(self, edit, message):
    self.view.insert(edit, self.view.size(), message)


#
# Create a new output panel, insert the message and show it
#
def panel(window, message):
  p = window.get_output_panel('crypto_error')
  if ST3:
    p.run_command("crypto_message", {"message": message})
  else:
    p_edit = p.begin_edit()
    p.insert(p_edit, p.size(), message)
    p.end_edit(p_edit)
  p.show(p.size())
  window.run_command("show_panel", {"panel": "output.crypto_error"})


#
# Encrypt/Decrypt using OpenSSL -aes128 and -base64
# EG similar to running this CLI command:
#   echo "data" | openssl enc -e -aes128 -base64 -pass "pass:lolcats"
#
def crypto(view, enc_flag, password, data):
  s = sublime.load_settings("Crypto.sublime-settings")
  cipher = s.get('cipher')
  openssl_command = os.path.normpath( s.get('openssl_command') )

  # pass the password as an ENV variable, for better security
  envVar = ''.join( random.sample( string.ascii_uppercase, 23 ) )
  os.environ[ envVar ] = password
  _pass = "env:%s" % envVar

  try:
    openssl = Popen([openssl_command, "enc", enc_flag, cipher, "-base64", "-pass", _pass], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    result, error = openssl.communicate(data.encode("utf-8"))
    os.unsetenv( envVar ) # get rid of the temporary ENV var
  except IOError as e:
    error_message = "Error: %s" % e
    panel(view.window(), error_message)
    return False
  except OSError as e:
    error_message = """
 Please verify that you have installed OpenSSL.
 Attempting to execute: %s
 Error: %s
    """ % (openssl_command, e[1])
    panel(view.window(), error_message)
    return False

  # probably a wrong password was entered
  if error:
    _err = error.splitlines()[0]
    if ST3:
      _err = str(_err)
    if _err.find('unknown option') != -1:
      panel(view.window(), 'Error: ' + _err)
    elif _err.find("WARNING:") != -1:
      # skip WARNING's
      return result
    else:
      panel(view.window(), 'Error: Wrong password?')
    return False

  return result

#
# Get the selected text regions (or the whole document) and process it
#
class CryptoCommand(sublime_plugin.TextCommand):
  def run(self, edit, enc, password):
    # are we encrypting or decrypting?
    enc_flag = '-e' if enc else '-d'
    # save the document size
    view_size = self.view.size()
    # get selections
    regions = self.view.sel()
    num = len(regions)
    x = len(self.view.substr(regions[0]))
    # select the whole document if there is no user selection
    if num <= 1 and x == 0:
      regions.clear()
      regions.add( sublime.Region(0, view_size) )

    # get current document encoding or set sane defaults
    encoding = self.view.encoding()
    if encoding == 'Undefined':
      encoding = 'utf-8'
    elif encoding == 'Western (Windows 1252)':
      encoding = 'windows-1252'

    # encrypt / decrypt selections
    for region in regions:
      data = self.view.substr(region)
      results = crypto(self.view, enc_flag, password, data)
      if results:
        if enc:
          if ST3:
            results = str(results, encoding)
          else:
            results.encode( encoding )
        else:
          if ST3:
            results = str(results, encoding)
          else:
            results = results.decode( encoding )
        self.view.replace(edit, region, results)
