import sublime, sublime_plugin, subprocess

# You need tidy installed and in your path. http://tidy.sourceforge.net/
class TidyXmlCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    command = 'tidy -xml -i -utf8 -w -q'

    # help from http://www.sublimetext.com/forum/viewtopic.php?f=2&p=12451
    p = subprocess.Popen(command, bufsize=-1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    result, err = p.communicate(self.view.substr(self.view.sel()[0]).encode('utf-8'))

    if err:
        sublime.error_message(err.decode('utf-8'))
    else:
        self.view.replace(edit, self.view.sel()[0], result.decode('utf-8'))