import sublime, sublime_plugin, subprocess

# You need tidyjson installed and in your path. http://www.raboof.com/Projects/TidyJson/
class TidyJsonCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    command = 'tidyjson'

    # help from http://www.sublimetext.com/forum/viewtopic.php?f=2&p=12451
    p = subprocess.Popen(command, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    result, err = p.communicate(self.view.substr(self.view.sel()[0]).encode('utf-8'))

    if err:
        sublime.error_message(err.decode('utf-8'))
    else:
        self.view.replace(edit, self.view.sel()[0], result.decode('utf-8'))