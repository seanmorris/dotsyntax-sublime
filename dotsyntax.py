import sublime_plugin
import sublime
import os.path
import fnmatch
import yaml
import io
import re

class DotSyntaxCommand(sublime_plugin.EventListener):

	mappings = {}
	
	def on_load_async(self, view):

		self.set_syntax(view)

	def on_post_save_async(self, view):

		self.set_syntax(view)

	def set_syntax(self, view):

		file  = os.path.basename(view.file_name());

		views = [view];

		if file == '.syntax':
			views = view.window().views()

		for _view in views:
			file        = _view.file_name();
			print('dotsyntax refreshing ' + file)
			mapped_ext  = self.map_file_extension(file)
			syntax_file = self.lookup_syntax_file(mapped_ext)
			_view.settings().set('syntax', syntax_file)

	def lookup_syntax_file(self, extension):

		if(len(self.mappings) == 0):

			self.load_settings()

		if extension in self.mappings:

			return self.mappings[extension]
	
	def map_file_extension(self, file):
		
		dir  = os.path.dirname(file)

		dot_syntax_file = self.find_dotsyntax_file(dir)

		if dot_syntax_file:
			
			with open(dot_syntax_file, "r") as handle:

				defs = [i.strip().rpartition(':') for i in handle]
				match = next((i for i in defs if self.filename_match(file,i)), None)

				if not match:
					return None

				*_, extension = match

				return extension.strip()

	def filename_match(self, file, check):

		filename = os.path.basename(file)
		*_ ,ext  = os.path.splitext(file)
		check    = check[0].strip()

		if check in {ext,filename}:

			return True

		return fnmatch.fnmatch(filename, check);

	def find_dotsyntax_file(self, dir):

		while dir != '/':

			syntaxFile = dir + '/.syntax'

			if os.path.exists(syntaxFile):

				return syntaxFile

			dir = os.path.abspath(os.path.join(dir, os.pardir))

	def load_settings(self):

		syntaxDefFiles = sublime.find_resources('*.sublime-syntax')

		extmode=0

		for syntaxDefFile in syntaxDefFiles:

			try:

				settings = sublime.load_resource(syntaxDefFile)

				for line in io.StringIO(settings):

					if extmode == 1:

						match = re.match('\s{2}-(.+?)\s+?\#?', line)

						if match is not None:	

							extension = '.' + match.group(1).strip()
							self.mappings[extension] = syntaxDefFile

						else:

							extmode = 0
							break;

					match = re.match('^file_extensions\:', line)
					
					if match is not None:
					
						extmode=1
						continue;

			except:

				continue
