![avatar](https://avatars3.githubusercontent.com/u/640101?s=80&v=4)

# dotsyntax

*Highlight dotfiles your way.*

![seanmorris-dotsyntax](https://img.shields.io/badge/seanmorris-dotsyntax_0.0.0-900?style=for-the-badge) ![Size badge](https://img.shields.io/github/repo-size/seanmorris/dotsyntax-sublime?color=280&style=for-the-badge) ![seanmorris-dotsyntax](https://img.shields.io/badge/built_for_sublime-3511-d70?style=for-the-badge)


I'm tired of having to deal with a lack of syntax highlighting when creating a custom dotfile. Even worse, I cannot stand having to configure each and every editor on each and every machine before I can get back to just writing code.

This plugin changes all that. Simply place a `.syntax` file in the root of any project and sublime will automatically use it to highlight the files in that project the rules you define.

I'm amazed nothing like this exists already.

 For example, the syntaxfile below will cause`.syntax` to be highlighted as if it were a `.yml` file, and the .env file to be renderd like bash.

syntaxfiles may also appear in subdirectories, and will override those found in parent directories.


## syntaxfile:

A syntaxfile is a file named `.syntax` describing the syntax of the files in its directory. It makes up for sitations where file names/extensions won't work.

A syntaxfile is simple a `key:value` map. The keys are filename, extensions or patterns that specify files the plugin will act on. 

The values are the extensions file types that you want to use. These extensions must include the leading dot.

## Usage

Create a `.syntax` file in the root of your project and add  keys and values in the form `filename:type` to get started. Leading/Trailing whitespace will be trimmed for the value. Upon saving, sublime will immediately begin to use whatever syntax highlighter it would normally use for the aliased file extension.

```yaml
.env:    .sh
.syntax: .yml
```

You can also specify a relative path. If the relative path of the *file* from the perspective of the *syntaxfile* matches, the match will take precedence over non-patch matches.

```yaml
.env:           .sh
templates/.env: .mustache
.syntax: .yml
```
Globbing may also be applied according to python's `fnmatch` rules.

```yaml
conf/*.cfg: ini
```

dotsyntax will refrest each file on load/save, and refresh all files in the current window if a syntaxfile is saved.

Please note, this does not cause these files to become `yml` or `bash` files, it only configures the syntax highglighter to ease eye strain, however it will enable filetype specific behavior, such as the comment/ hotkey. Try it out!

## Installation

As far as I know, I havent been accepted to package control yet. That leaves us with the manual install path as our only option. Open sublime and go to `tools > browse packages` and you'll get a file explorer from your current OS and time period. Note the directory.

Once you've done that, head over to the [releases](https://github.com/seanmorris/dotsyntax-sublime/releases) page and grab the lastest one. Extract that file into the directory from before, under a folder named `dotsyntax`  (make sure your archive manager doesn't end up creating a subfolder with the same name).

When you've done the above correctly, you should now see this on your sublime console whenever you save/load a file:

```
dotsyntax refreshing /home/sean/dotsyntax/README.md
```

You can open the console with `ctrl ~` on linux or `cmd ~` on osx.

## License

### Copyright 2019 Sean Morris

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
