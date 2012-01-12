import sublime
import traceback
import os
import sys
import time

import sftp.debug
import sftp.times
import sftp.paths
# Fixes a reloading issue
if 'sftp.commands' in sys.modules:
    reload(sys.modules['sftp.commands'])
import sftp.commands
from sftp.commands import (SftpShowPanelCommand, SftpCreateServerCommand,
    SftpBrowseServerCommand, SftpLastServerCommand, SftpEditServerCommand,
    SftpDeleteServerCommand, SftpBrowseCommand, SftpUploadFileCommand,
    SftpMonitorFileCommand, SftpUploadOpenFilesCommand,
    SftpDiffRemoteFileCommand, SftpRenameLocalAndRemotePathsCommand,
    SftpDeleteRemotePathCommand, SftpDownloadFileCommand,
    SftpUploadFolderCommand, SftpSyncUpCommand, SftpSyncDownCommand,
    SftpSyncBothCommand, SftpDownloadFolderCommand, SftpVcsChangedFilesCommand,
    SftpCancelUploadCommand, SftpEditConfigCommand, SftpCreateConfigCommand,
    SftpCreateSubConfigCommand)
from sftp.listeners import (SftpCloseListener, SftpLoadListener,
    SftpFocusListener, SftpAutoUploadListener, SftpAutoConnectListener)


settings = sublime.load_settings('SFTP.sublime-settings')
sftp.debug.set_debug(settings.get('debug', False))


# Override default uncaught exception handler
def uncaught_except(type, value, tb):
    message = ''.join(traceback.format_exception(type, value, tb))

    if message.find('/sftp/') != -1 or message.find('\\sftp\\') != -1:
        def append_log():
            log_file_path = os.path.join(sublime.packages_path(), 'User',
                'SFTP.errors.log')
            send_log_path = log_file_path
            timestamp = sftp.times.timestamp_to_string(time.time(),
                    '%Y-%m-%d %H:%M:%S\n')
            with open(log_file_path, 'a') as f:
                f.write(timestamp)
                f.write(message)
            if sftp.debug.get_debug() and sftp.debug.get_debug_log_file():
                send_log_path = sftp.debug.get_debug_log_file()
                sftp.debug.debug_print(message)
            sublime.error_message(('%s: An unexpected error occurred, ' +
                'please send the file %s to support@wbond.net') % ('SFTP',
                send_log_path))
            sublime.active_window().run_command('open_file',
                {'file': sftp.paths.fix_windows_path(send_log_path)})
        sublime.set_timeout(append_log, 10)

    sys.__excepthook__(type, value, tb)
if sys.excepthook.__name__ != 'uncaught_except':
    sys.excepthook = uncaught_except


def unload_handler():
    # Kill all connections
    sftp.commands.SftpThread.cleanup()

    # Unload all of the modules
    sftp_mods = []
    for mod in sys.modules:
        if mod[0:5] == 'sftp.' or mod == 'sftp':
            sftp_mods.append(mod)
    for sftp_mod in sftp_mods:
        del sys.modules[sftp_mod]

    # Reset the exception handler
    sys.excepthook = sys.__excepthook__
