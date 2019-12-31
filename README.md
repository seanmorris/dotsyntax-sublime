# dotsyntax-sublime

*Highlight your dotfiles your way.*

I'm tired of having to deal with a lack of syntax highlighting when creating a custom dotfile. Even worse, I cannot stand having to configure each and every editor to use the correct standard.

This plugin changes all that. Simply place a `.syntax` file in the root of any project and sublime will automatically use it to highlight the files in that project the rules you define.

A syntaxfile is simple a `key:value` map, where the keys are filenames or extensions to act on, and the values are the file types that you want to use. For example, the syntaxfile below will cause`.syntax` to be highlighted as if it were a `.yml` file, and the .env file to be renderd like bash.

Please note, this does not cause these files to become `yml` or `bash` files, it only configures the syntax highglighter to ease eye strain.

```yaml
.syntax: .yaml
.env:    .bash
```