# Soda Theme

Dark and light custom UI themes for Sublime Text 2.

## Design

![Soda Light Theme](http://buymeasoda.github.com/soda-theme/images/screenshots/soda-2-light-theme.png?v=1)

![Soda Dark Theme](http://buymeasoda.github.com/soda-theme/images/screenshots/soda-dark-theme.png?v=7)

## Installation

### Using Sublime Package Control

If you are using Will Bond's excellent [Sublime Package Control](http://wbond.net/sublime_packages/package_control), you can easily install Soda Theme via the `Package Control: Install Package` menu item. The Soda Theme package is listed as `Theme - Soda` in the packages list.

### Using Git

Alternatively, if you are a git user, you can install the theme and keep up to date by cloning the repo directly into your `Packages` directory in the Sublime Text 2 application settings area.

Go to your Sublime Text 2 `Packages` directory and clone the theme repository using the command below:

    git clone https://github.com/buymeasoda/soda-theme/ "Theme - Soda"

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `Theme - Soda`
* Copy the folder to your Sublime Text 2 `Packages` directory

## Activating the theme

To configure Sublime Text 2 to use the theme:

* Open your User Settings Preferences file `Sublime Text 2 -> Preferences -> Settings - User`
* Add (or update) your theme entry to be `"theme": "Soda Light.sublime-theme"` or `"theme": "Soda Dark.sublime-theme"`

### Example User Settings

    {
        "theme": "Soda Light.sublime-theme"
    }

## Configurable Features

### Alternate Tab Styles

Soda Theme ships with two alternate UI tab styles.

By default, a square tab style is used. If you'd prefer to use the original curved tab style, add the following custom setting to your `Settings - User` file:

    "soda_classic_tabs": true

![Soda Tab Styles](http://buymeasoda.github.com/soda-theme/images/features/multiple-tab-styles.png)

## Bonus Options

### Syntax Highlighting Colour Schemes

The Soda Light screenshot uses a modified version of Espresso Tutti Colori and the Soda Dark screenshot uses a modified version of Monokai.

If you'd like to use the syntax highlighting schemes shown in the screenshots: 

* Download [colour-schemes.zip](http://buymeasoda.github.com/soda-theme/extras/colour-schemes.zip)
* Unzip and place the extracted `tmtheme` files in the Sublime Text 2 `Packages/User` folder
* Enable the colour scheme via `Preferences -> Color Scheme -> User`

### Code Font

The code font shown in the screenshot is [Meslo](https://github.com/andreberg/Meslo-Font), which is a modified version of Menlo.

## Release Notes

Soda theme is designed to work with the latest [development build](http://www.sublimetext.com/dev) of Sublime Text 2. ST2 dev builds move quickly and changes can occur with the theme API between releases, so there may be occasions where the theme doesn't quite work with a brand new dev release.

## Development

While developing the theme, I have documented some [theme challenges and ideas](https://github.com/buymeasoda/soda-theme/wiki/Theme-challenges-and-ideas) encountered along the way.

## License

Soda Theme is licensed under the [Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). You are free to share and remix the theme, however please abide by the license terms when doing so. 

The following details apply to the Creative Commons license "author specified" components:

* Attribution example: Based on Soda Theme by Ian Hill (http://buymeasoda.com/)

* Naming guidelines: If you create and distribute a derivative theme, please give your theme a unique and original name that does not directly include "Soda Theme" (or a close variant) in the main project title, repo name or Package Control name.

The theme contains some icons from the excellent [Pictos](http://pictos.drewwilson.com/) series by Drew Wilson which I have a license for. Any use of these icons, other than for the purpose of the theme itself, would need to comply with Drew's [icon licensing agreement](http://stockart.drewwilson.com/license/).