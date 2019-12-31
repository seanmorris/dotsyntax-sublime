![avatar](https://avatars3.githubusercontent.com/u/640101?s=80&v=4)

# dotsyntax

*Highlight dotfiles your way.*

![seanmorris-dotsyntax](https://img.shields.io/badge/seanmorris-dotsyntax-900?style=for-the-badge) ![Size badge](https://img.shields.io/github/languages/code-size/seanmorris/dotsyntax-sumblime?style=for-the-badge)

I'm tired of having to deal with a lack of syntax highlighting when creating a custom dotfile. Even worse, I cannot stand having to configure each and every editor on each and every machine before I can get back to just writing code.

This plugin changes all that. Simply place a `.syntax` file in the root of any project and sublime will automatically use it to highlight the files in that project the rules you define.

Theres a version in the works for Eclipse,

A syntaxfile is simple a `key:value` map, where the keys are filenames or extensions to act on, and the values are the file types that you want to use. For example, the syntaxfile below will cause`.syntax` to be highlighted as if it were a `.yml` file, and the .env file to be renderd like bash.

## Usage:

Create a `.syntax` file in the root of your project and add  keys and values in the form `filename:type` to get started. Leading/Trailing whitespace will be trimmed for the value. Upon saving, sublime will immediately begin to use whatever syntax highlighter it would normally use for the given file extension.

The script just ascends the directory tree lookign for a .syntax file.

If it finds one, it applies one simple rule: if the filename or extension is an exact match for the value on the left side of the colon, sublime will pretend it has the extension from the right side of the colon.

```yaml
.env: .sh
.syntax: .yml
```

Please note, this does not cause these files to become `yml` or `bash` files, it only configures the syntax highglighter to ease eye strain, however it will enable filetype specific behavior, such as the comment/ hotkey. Try it out!
