# bouiboui/kumiko fork

- Removed browser/HTML reading
- Added PDF file input
  ```sh
  ./kumiko -i "comics/MyComic/file.pdf" --pdf
  ```
- Added optional panels JPG output for all input types
  ```sh
  ./kumiko -i "comics/MyComic/file.jpg" -s
  ``` 

# Introduction

![Kumiko mascot by Cthulhulumaid](artwork/kumiko-big.png "Kumiko mascot by Cthulhulumaid")

> Kumiko mascot
>
by [Hurluberlue](https://www.twitch.tv/hurluberlue "twitch link"), [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/ "Creative Commons License")

*Kumiko, the Comics Cutter* is a set of tools to compute useful information about comic book pages, panels, and more.
Its main strength is to find out the **locations of panels** within a comic's page (image file).
*Kumiko* can also compile information about panels for all pages in a comic book, and present it as one piece of data (
JSON-formatted object).

*Kumiko* makes use of the great (freely licensed) [opencv](https://opencv.org/) library, which provides image processing
algorithms of all sorts.
Mainly, the contour detection algorithm is used to detect panels within an image.

# Demo

*TL;WR* Too Long; Won't Read the whole doc?

A **live demo** is now [available here](https://kumiko.njean.me/demo), where you can try *Kumiko* out and cut your own
comic pages into panels.

# Philosophy

*Kumiko* aims at being a functional library to extract information from comic pages / books.
The goal is to provide a set of tools that is usable beforehand, to extract all needed information.

External programs can later use the generated information for different purposes: panel-by-panel viewing, actual
splitting of an image down into panels, etc.

# Requirements

`apt-get install python3-opencv` will install the only necessary library needed: *opencv*.

This should do the trick for Debian distros and derivatives (Ubuntu, Linux Mint...).
If you successfully use *Kumiko* on any other platform, please let us know!

*Kumiko* now uses python3.

# Usage & Testing

See the [usage doc](doc/Usage.md) for details on how to use the *Kumiko* tools.

Also check the [testing doc](doc/Testing.md) if you want to test modified versions of the code.

# Numbering

The numbering is left-to-right, or right-to-left if requested.

Here is an example of how *Kumiko* is going to number panels by default (numbers and red lines not in the original
picture).

![Pepper&Carrot](doc/img/numbering.png "Pepper&Carrot")

> [Pepper & Carott](https://www.peppercarrot.com/)
>
by [David Revoy](https://www.davidrevoy.com), [episode 2](https://www.peppercarrot.com/en/article237/episode-2-rainbow-potions), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

# Limitations

For now, *Kumiko* only deals with clear (white-ish) and dark (black-ish) backgrounds.
Panels within a comic page will be any "object" that has non-white & non-black boundaries (not necessarily vertical or
horizontal lines).

If you have ideas on how to programmatically guess the background color of a page, please let us know!

# Short- and longer-term awesome features (roadmap)

## Kumiko library

* detect panels on a growing range of comic page layouts
    * detect non-framed panels (without clear boundaries/borders)
    * separate intertwined panels

* be able to detect panel contours on pages with non-white, non-black background
    * implies being able to determine the background color: histogram, probing of some kind? (worst case: manually?)

## Back-office (validation / edition tool)

Let's face it: we probably can't ensure that *Kumiko* can perfectly find out the panels in *any* image.
There is a huge diversity of panel boundaries, layouts and whatnot.

This is why we should have some kind of back-office / editing tool that lets a human editor:

* validate pages
* add, delete, move or resize incorrect panels
* report bugs
* ...

Such a tool should edit the JSON file representing a comic book information, for later use by other programs that'll
rely on it.
