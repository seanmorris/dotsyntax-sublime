import sublime_plugin
import sublime
import os.path
import fnmatch
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
			if not file:
				continue
			print('dotsyntax checking ' + file)
			mapped_ext  = self.map_file_extension(file)
			syntax_file = self.lookup_syntax_def_file(mapped_ext)
			_view.settings().set('syntax', syntax_file)

	def lookup_syntax_def_file(self, extension):

		if(len(self.mappings) == 0):

			self.load_settings()

		if extension in self.mappings:

			return self.mappings[extension]
	
	def map_file_extension(self, file):
		
		filename = os.path.basename(file)
		dir  = os.path.dirname(file)

		dot_syntax_files = self.find_dotsyntax_files(dir)

		for dot_syntax_file in dot_syntax_files:

			dot_syntax_dir = os.path.dirname(dot_syntax_file)
			rel_path       = os.path.relpath(file, dot_syntax_dir)
			# rel_path       = os.path.dirname(rel_path)
			
			with open(dot_syntax_file, "r") as handle:

				defs = [i.strip().rpartition(':') for i in handle if i.strip()]
				match = next((i for i in defs if self.filename_match(rel_path,i)), None)

				if not match:
					match = next((i for i in defs if self.filename_match(filename,i)), None)

				if not match:
					continue

				*_, extension = match

				extension = extension.strip()

				print("\t.syntax " + dot_syntax_file)
				print("\t syntax " + extension + "\n")

				return extension.strip()

	def filename_match(self, file, check):

		*_ ,ext  = os.path.splitext(file)
		check    = check[0].strip()

		if check in {ext,file} or fnmatch.fnmatch(file, check):

			print("\tmatched " + check + "\n\t   file " + file)

			return check


	def find_dotsyntax_files(self, dir):

		files = []

		while dir != '/':

			syntaxFile = dir + '/.syntax'

			if os.path.exists(syntaxFile):

				files.append(syntaxFile)

			dir = os.path.abspath(os.path.join(dir, os.pardir))

		return files

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
