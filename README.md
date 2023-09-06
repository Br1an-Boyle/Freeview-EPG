> **Warning**
This branch is still in active development - please use with caution and report any errors as you encounter them.

![logo](https://user-images.githubusercontent.com/9065463/232618260-d9017259-1786-4d85-807f-63752143d403.png)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/dp247/Freeview-EPG/actions.yml?color=%232ca9bc&label=EPG%20Generation&style=flat-square) ![GitHub issues](https://img.shields.io/github/issues-raw/dp247/Freeview-EPG?color=%232ca9bc&style=flat-square)

<a href='https://ko-fi.com/K3K4EYJL5' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

Freeview-EPG is a project designed to provide a reliable source of XMLTV data for UK free-to-air TV channels and _national_ radio stations. The channel list was designed to match [this](https://github.com/ExperiencersInternational/tvsetup) project as closely as possible, and is a cutdown fork from the [iptv/epg](https://github.com/iptv-org/epg) project. 

![image](https://user-images.githubusercontent.com/9065463/235314658-369f0825-692c-4626-8938-d3f60de3d167.png)


The project works by using various APIs to parse channel and programme data and then build the resulting dataset into an XMLTV file. The file provides a 48h EPG and is automatically updated every 8 hours. Metadata is bound by both what the API provides and what can be represented in the XMLTV format (see [here](https://github.com/XMLTV/xmltv/blob/master/xmltv.dtd)), but the aim is to at least provide:

- Programme title
- Programme description
- Start and end times
- Some kind of image for the programme (this will probably be a screengrab, which doesn't fit poster-based EPGs like Plex's, but is better than nothing)

## Disclaimers
- I'm open to adding any *free-to-air* channels to this EPG, whether that's for an IPTV channel or a Freeview channel, but I won't be adding PPV or subscription-based channels here.
- The software and data are provided as-is. While I intend for it to be as reliable as possible, the data is sourced from respective APIs and is out of my control.


## Usage
The version in the application works a little differently and does not automatically build its own EPG. However, it does allow for customisation of how many days data should be pulled back, as well as where the EPG file should be saved.

This branch needs a config.ini file to work properly - the app will create one in the project directory when it's first run. The options are as follows:
- epg_dir = The folder that the EPG file should be saved in
- epg_filename = The filename (minus the extension) that the EPG file should be called
- days = A number between 1 and 7 of how many days (after today) data should be pulled back - e.g. 1 would pull back today and tomorrow.

## To-do
- Changes from main branch

## Contributing
### Guidelines
- Please check [the FAQ](https://github.com/dp247/Freeview-EPG/wiki/FAQ) to make sure your question hasn't already been answered.
- Please report issues [here](https://github.com/dp247/Freeview-EPG/issues/new?assignees=&labels=bug&template=issue-report.md&title=%5BIssue%5D), including as much detail as possible about the problem.
- You can request channels [here](https://github.com/dp247/Freeview-EPG/issues/new?assignees=&labels=channel&template=channel-request.md&title=%5BChannel+request%5D). Please bear in mind that a request is not a guarantee.
- If you'd like to suggest a change or feature, feel free to either open a blank fork and PR back in. Big changes should be discussed in a [blank issue](https://github.com/dp247/Freeview-EPG/issues/new) first.


## License
[GNU General Public License v3.0](https://github.com/dp247/Freeview-EPG/blob/master/LICENSE)
```text
TLDR from TLDRLegal:
You may copy, distribute and modify the software as long as you track changes/dates in source files. Any modifications to or software including (via compiler) GPL-licensed code must also be made available under the GPL along with build & install instructions.
```

## Related projects
- [YouTube to M3U8](https://github.com/dp247/YouTubeToM3U8) - converts and maintains YouTube live streams in a single M3U8 playlist
- [iptv-cutter](https://github.com/dp247/iptv-cutter) - deduplicator and generator of M3Us for popular IPTV services
- [Freeview M3U](https://github.com/ExperiencersInternational/tvsetup) - companion playlist for this project
