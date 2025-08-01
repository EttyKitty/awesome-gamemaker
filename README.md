<p align="center">
    <a href="https://gamemaker.io/"><img src="https://github.com/bytecauldron/awesome-gamemaker/raw/main/images/banner.png" /></a>
</p>

# Awesome GameMaker [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Made with GameMaker](https://img.shields.io/badge/Made%20with-GameMaker-000000.svg?style=flat&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAAZlBMVEX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2BrG8stAAAAIXRSTlMABg0OFBkfcn1%2Bf4CBgoOFhoeIiouWmNDa5ebp8PX2%2B%2F6o6Vq%2BAAAAY0lEQVR42k2OWQ6AIAwFn%2BIOioobrnD%2FS4o0EeanmQxNAdErRFTWtsFq6%2BiiZozz0CSnTjYBwo0RkF8DWDLf51Ni9K%2FYdq0Fy3KAfzk97M7goK1F%2F4rGH9Kk1OlboQtEDIrmC%2BU3CVxTr%2FRMAAAAAElFTkSuQmCC)](https://www.yoyogames.com/gamemaker) [![Links](https://github.com/bytecauldron/awesome-gamemaker/actions/workflows/links.yml/badge.svg)](https://github.com/bytecauldron/awesome-gamemaker/actions/workflows/links.yml)

> A curated list of awesome libraries, snippets, guides, and projects for GameMaker. 😎

[GameMaker](https://gamemaker.io/) is a user-friendly, cross-platform game engine by YoYo Games that allows both beginner and advanced game developers to create 2D and 3D games for desktop, HTML5, and console platforms.

What kind of games can you make in GameMaker? [Check out this list.](https://steamdb.info/tech/Engine/GameMaker/)

## Contents
- [Getting Started](#getting-started)
- [Utilities](#utilities)
- [Debugging](#debugging)
- [Input Handling](#input-handling)
- [User Interface](#user-interface)
- [Localization](#localization)
- [Physics](#physics)
- [Sprites](#sprites)
- [Audio](#audio)
- [Levels](#levels)
- [Particles](#particles)
- [Lighting](#lighting)
- [Shaders](#shaders)
- [3D](#3d)
- [Sprite Stacking](#sprite-stacking)
- [Networking](#networking)
- [Integrations](#integrations)
- [Camera](#camera)
- [Sequences](#sequences)
- [State Machines](#state-machines)
- [Pathing](#pathing)
- [Useful Extras](#useful-extras)
- [Blogs](#blogs)
- [YouTube](#youtube)
- [Community](#community)
- [Special Thanks](#special-thanks)

## Getting Started

- [GameMaker Manual](https://manual.gamemaker.io/)
- [GameMaker Release Notes](https://gms.yoyogames.com/ReleaseNotes.html)
- [GameMaker Marketplace](https://marketplace.gamemaker.io/)
- [Beginner GameMaker Tutorials](https://www.youtube.com/watch?v=nBCDzE9MDbk&list=PLPRT_JORnIur4v19PHXCtJ5P05vaokFdP) - Tutorials from Shaun Spalding. A comprehensive introduction to basic features of the IDE. Highly recommended to check out the full playlist if you're a complete beginner. ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)
- [Advanced GameMaker Tutorials](https://www.youtube.com/watch?v=n8-MuIuOQFE&list=PL_hT--4HOvrfuDcYrTufdpgwoALAczPR2) - Tutorials from DragoniteSpam that dive into more advanced topics related to the GML language. They also have comprehensive 3D and shader introduction videos. ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)

### Recommendations

- If you already have programming experience, learn the GameMaker Language (GML) instead of the Visual (Drag and Drop) feature.
- For pixel art, [Aseprite](https://www.aseprite.org/) is a popular alternative to the native sprite editor. 💸
  - [Aseprite's source code](https://github.com/aseprite/aseprite) can be compiled for free.
- Don't be afraid to use other developer libraries. A lot of them are free for a reason. Just be mindful of the license.
- Updates to the IDE and runtime can break your game (like syntax changes to GML). If you are working in a group, make sure you are running on the same version of GMS and only update when given a fair warning. You can reinstall previous versions of your IDE at the GMS download page.
- Unless your game requires complex physics interactions, it's generally advised to avoid GameMaker's built-in physics system.
- Schedule routine backups for projects. If you are dealing with larger media files in your repo, try [Git LFS](https://git-lfs.github.com/).

## Icons
- 💸 - a paid resource.
- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png) - a YouTube video.
- 🧰 - an online tool to do something.
- 🗒️ - a written guide.
- 🟢 - had repository activity in the past 3 months.
- 🟡 - had repository activity in the past 6 months.
- 🔴 - had no repository activity in more than 6 months.

## Utilities

| Name | Description | Status |
|------|-------------|--------|
| [Stitch](https://www.npmjs.com/package/@bscotch/stitch) | Pipeline Development Kit. Includes cross-project imports, batch-creating/updating sprites and sounds, texture page management, and more. Tested on Windows only. | 🟢 Active |
| [Coroutines](https://github.com/JujuAdams/Coroutines) | Asynchronous functions for GameMaker. | 🟢 Active |
| [GML-OOP](https://github.com/Mtax-Development/GML-OOP) | A constructor library for operating the primary functionalities of GameMaker. | 🟢 Active |
| [Canvas](https://github.com/tabularelf/Canvas) | Another great solution for surface management. | 🟢 Active |
| [Extension Collection](https://samuel-venable.itch.io/gamemaker-extension-collection) | A suite of various extensions. | 🟢 Active |
| [GMLive](https://yellowafterlife.itch.io/gamemaker-live) 💸 | Livecoding / interactive programming. | 🟢 Active |
| [GMEdit](https://github.com/YellowAfterlife/GMEdit) | Code editor to use in conjunction with GameMaker. | 🟢 Active |
| [Catspeak](https://github.com/katsaii/catspeak-lang) | Cross-platform programming language for modding support. | 🟢 Active |
| [GMBenchmark](https://github.com/DragoniteSpam/GMBenchmark) | A tool to benchmark GML code. | 🟢 Active |
| [GMD3D11](https://github.com/blueburncz/GMD3D11) | A DLL for interfacing with Windows Direct3D. | 🟡 Semi-Active |
| [Exception](https://github.com/KeeVeeGames/Exception.gml) | A base class for custom exceptions. | 🟡 Semi-Active |
| [BSONGML](https://github.com/LAGameStudio/BSONGML) | Save and load GML structured data in binary files. | 🟡 Semi-Active |
| [gm-core](https://github.com/gm-core) | Foundational utility suite and great starting point. Includes quality-of-life tools and networking. | 🔴 Inactive |
| [FAST](https://github.com/Hyomoto/FAST) | Flexible Assistant Toolkit with input and resolution handling. | 🔴 Inactive |
| [DDDEditor](https://github.com/DragoniteSpam/DDDEditorGMS2) | General purpose game editor. | 🔴 Inactive |
| [handytools](https://github.com/JujuAdams/handytools/) | A collection of Juju's libraries. | 🔴 Inactive |
| [GameMaker Scaffolding](https://github.com/babaganosch/GameMakerScaffolding) | Template for tile-based games. | 🔴 Inactive |
| [Iota](https://github.com/JujuAdams/iota) | Lightweight timestep library. | 🔴 Inactive |
| [Stopwatch](https://github.com/Lojemiru/Stopwatch) | GameMaker alarm replacement. | 🔴 Inactive |
| [wTimer](https://mors-games.itch.io/wtimer) | Robust alternative for alarms. | 🔴 Inactive |
| [FrogAlarm](https://github.com/colmeye/FrogAlarms) | Easy alarm system alternative. | 🔴 Inactive |
| [fuwafuwa](https://github.com/kemonologic/fuwafuwa) | Easy-to-use timer system. | 🔴 Inactive |
| [Timer](https://github.com/nommiin/Timers) | JS-like timer functions for GML. | 🔴 Inactive |
| [Broadcast](https://github.com/JulianDicken/Broadcast) | Event handling library. | 🔴 Inactive |
| [Polarca](https://github.com/VitorEstevam/polarca) | Interpolation functions. | 🔴 Inactive |
| [Twerp](https://pixelatedpope.itch.io/twerp) | Easing function like lerp(). | 🔴 Inactive |
| [GML-Classes](https://github.com/Nikko-the-cat/GML-Classes) | Adds OOP functionality to GameMaker. | 🔴 Inactive |
| [Map](https://github.com/GameMakerDiscord/Map.gml) | Hash table implementations. | 🔴 Inactive |
| [Matrices](https://github.com/JujuAdams/matrices) | Matrix handling scripts. | 🔴 Inactive |
| [gm-stream](https://github.com/daikon-games/gm-stream) | Data structure manipulation. | 🔴 Inactive |
| [Promises](https://github.com/YAL-GameMaker/Promise.gml) | JavaScript-like Promises for GML. | 🔴 Inactive |
| [Destructors](https://github.com/DatZach/Destructors) | Use ds_* types inside structs. | 🔴 Inactive |
| [SNAP](https://github.com/JujuAdams/SNAP) | Easy data format saving/loading. | 🔴 Inactive |
| [Dynamo](https://github.com/JujuAdams/Dynamo) | Dynamic data loader. | 🔴 Inactive |
| [LWO](https://github.com/tabularelf/lwo) | Lightweight objects using structs. | 🔴 Inactive |
| [Gumshoe](https://github.com/JujuAdams/Gumshoe) | Simple deep file search. | 🔴 Inactive |
| [Lock And Key](https://github.com/AlubJ/Lock-And-Key) | String and file encryption. | 🔴 Inactive |
| [Mathematical Scripts](https://github.com/adam-rumpf/game-maker-scripts) | Math helper scripts. | 🔴 Inactive |
| [Seedpod](https://github.com/daikon-games/gm-seedpod) | Utility scripts to enhance GML dev. | 🔴 Inactive |
| [Trixscript](https://trixelized.itch.io/trixscript) | General utility script pack. | 🔴 Inactive |
| [CoreExtension](https://github.com/blueburncz/CoreExtension) | CC0 programming libraries. (archived) | 🔴 Inactive |
| [Voxeledphoton's FreeGMScripts](https://github.com/vphoton/FreeGMScripts) | Misc GML helper functions. | 🔴 Inactive |
| [ForEach](https://github.com/KeeVeeGames/foreach.gml) | `foreach` for many GML structures. | 🔴 Inactive |
| [DeepCopy](https://github.com/KeeVeeGames/DeepCopy.gml) | Deep clone complex structs/arrays. | 🔴 Inactive |
| [Motion Scripts](https://avis.itch.io/motion-scripts) | Custom motion helper methods. | 🔴 Inactive |
| [Cottonwool](https://github.com/JujuAdams/Cottonwool) | Safe surface handling. | 🔴 Inactive |
| [zlib functions](https://yellowafterlife.itch.io/gamemaker-zlib) | Compression/decompression in GML. | 🔴 Inactive |
| [Window Taskbar](https://yellowafterlife.itch.io/gamemaker-window-taskbar) | Flash window/taskbar in Windows. | 🔴 Inactive |
| [GMSDLL](https://github.com/YAL-GameMaker/GMSDLL) | Template for GameMaker DLLs. | 🔴 Inactive |
| [GMLodash](https://github.com/DatZach/GMLodash) | Functional programming helpers. | 🔴 Inactive |
| [Autoframer](https://github.com/mstop4/auto-framer) | View resizing across resolutions. | 🔴 Inactive |
| [gameframe](https://github.com/YAL-GameMaker/gameframe) | Custom window frame on Windows. | 🔴 Inactive |
| [GML+](https://xgasoft.itch.io/gmlp) 💸 | Comprehensive utility script pack. | 🔴 Inactive |
| [YYP Maker](https://sahaun.itch.io/yyp-maker) | Automates `.yyp` file creation. | 🔴 Inactive |
| [Rubber](https://github.com/GameMakerDiscord/Rubber) | CLI compilation tool for GameMaker. | 🔴 Inactive |
| [gml-highscorer](https://github.com/Grisgram/gml-highscorer) | Highscore & trophy system. | 🔴 Inactive |
| [SSave](https://github.com/stoozey/SSave) | Simple file saving system. | 🔴 Inactive |
| [GMTimeLine](https://github.com/TimVN/GMTimeLine) | Code-based timeline replacement. | 🔴 Inactive |
| [Agenda](https://github.com/benal20/Agenda.gml) | Callback scheduling and delay. | 🔴 Inactive |
| [GMSnip](https://manta-ray.itch.io/gmsnip) | Unlimited snippets in IDE. | 🔴 Inactive |
| [Airkiver](https://github.com/AlubJ/Airkiver) | Game file archiving tool. | 🔴 Inactive |
| [OKColor](https://github.com/KeeVeeGames/OKColor.gml) | Color manager using OKLab/OKLCH. | 🔴 Inactive |
| [ArrayList](https://github.com/KeeVeeGames/ArrayList.gml) | Advanced list class for GML. | 🔴 Inactive |
| [GM Sysinfo](https://github.com/SpikeHD/gm-sysinfo) | System info cross-platform extension. | 🔴 Inactive |
| [GML-Multiprocessing](https://github.com/tinkerer-red/GML-Multiprocessing) | Proof of concept for multiprocessing. | 🔴 Inactive |

## Debugging

| Name | Description | Status |
|------|-------------|--------|
| [Duck](https://github.com/imlazyeye/duck) | A fast GML analyzer to enforce code styling and detect errors. | 🟢 Active |
| [Gobo](https://github.com/Pizzaandy/Gobo/) | An opinionated code formatter for GML. | 🟢 Active |
| [Snitch](https://github.com/JujuAdams/Snitch) | Crash and logging system. | 🟡 Semi-Active |
| [rt-shell](https://github.com/daikon-games/rt-shell) | Easy to use in-game shell. Create your own commands, command meta data, command suggestions, history, etc. | 🔴 Inactive |
| [Olympus](https://github.com/bscotch/olympus#readme) | Testing Framework. | 🔴 Inactive |
| [Crispy](https://github.com/bfrymire/crispy) | Unit testing in GameMaker. | 🔴 Inactive |
| [DeerLog](https://mulfok.itch.io/gamemaker-deerlog) | Small log writer. | 🔴 Inactive |
| [gms2-test](https://github.com/pmarincak/gms2-test) | Unit testing framework. | 🔴 Inactive |
| [Meta](https://github.com/nommiin/meta) | Runtime asset inspector. | 🔴 Inactive |
| [FPS Speedometer](https://dragonite.itch.io/fps-speedometer-for-gamemaker) | Pretty framerate display. | 🔴 Inactive |
| [Inspectron](https://github.com/shdwcat/Inspectron) | A fluent API for easily creating GameMaker debug views. | 🔴 Inactive |


## Input Handling

| Name | Description | Status |
|---|---|---|
| [Input](https://github.com/offalynne/input) | No nonsense gamepad/keyboard library. | 🟢 Active |
| [Native Cursors](https://yellowafterlife.itch.io/gamemaker-native-cursors) 💸 | System-level custom cursors. | 🟢 Active |
| [InputCandy](https://github.com/LAGameStudio/InputCandy) | Similar to Input as it acts as a wrapper for SDL, with actions and signalling, but also provides testing, on-screen diagnostics, and some other UI components related to peripherals, as well as pre-built end-user configuration menus that can be easily restyled. | 🟡 Semi-Active |
| [Input(JujuAdams fork)](https://github.com/JujuAdams/input) | No nonsense gamepad/keyboard library. | 🔴 Inactive |
| [XeroInput](https://www.reddit.com/r/gamemaker/comments/icoh6m/xeroinput_gms23_input_handler/) | Another library to handle multiple inputs for a single action. | 🔴 Inactive |
| [Good Vibes](https://github.com/mrdaneeyul/good-vibes) | Device vibration. | 🔴 Inactive |
| [Mouse Queue](https://github.com/YAL-GameMaker/window_mouse_queue) | Tracks the Windows mouse pointer with high precision. | 🔴 Inactive |

## User Interface

- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[Menu Tutorial](https://www.youtube.com/watch?v=1ITZOrI2qkA&list=PLSFMekK0JFgx2vmcCnttxxhrNVTjUB8R1) - FriendlyCosmonaut.
- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[Smart Clickable GUI](https://www.youtube.com/watch?v=RbBgE3cUShc) - Pixelated Pope.

| Name | Description | Status |
|---|---|---|
| [Scribble](https://github.com/JujuAdams/scribble) | Efficient multi-effects text renderer. | 🟢 Active |
| [YUI](https://github.com/shdwcat/YUI) | A UI system with live reloading, template system, data binding, and a drag and drop feature. | 🟢 Active |
| [Emu UI](https://github.com/DragoniteSpam/Emu) | Common UI elements (text input, checkboxes, radio buttons, dialog boxes, etc). | 🟢 Active |
| [gooey](https://manta-ray.itch.io/gooey) | Sprite-based UI Library for GameMaker LTS. | 🟢 Active |
| [Chatterbox](https://github.com/JujuAdams/chatterbox) | Narrative scripting tool. | 🟡 Semi-Active |
| [Scripture](https://pixelatedpope.itch.io/scripture) | Another easy to use, highly compatible text renderer. | 🔴 Inactive |
| [Textboxy](https://github.com/glitchroy/textboxy) | Simple textboxes. | 🔴 Inactive |
| [Crochet](https://github.com/FaultyFunctions/Crochet) | An interactive dialogue editor for writers and programmers. | 🔴 Inactive |
| [NotificationSystem](https://github.com/babaganosch/NotificationSystem) | Notifications in GameMaker. | 🔴 Inactive |
| [Guido](https://github.com/JujuAdams/Guido) | Simple immediate mode GUI framework. | 🔴 Inactive |
| [GMUI-Framework](https://github.com/AlertStudios/GMUI-Framework) | A pure GML solution to structure and control your menus, drawing parallels to .NET UI. | 🔴 Inactive |
| [GMS2-UI-Library](https://github.com/nabilatsoulcade/GMS2-UI-Library) | A Library Full of useful scripts for implementing your UI designs in GameMaker. | 🔴 Inactive |
| [Easy And Fast Menu](https://pkgames.itch.io/easy-and-fast-menus-for-gms-23) | Simple implementation to have a menu up and running in seconds. Seems like a great fit if you're not looking for a bigger solution like GMUI. | 🔴 Inactive |
| [Pause Menu](https://jasontomlee.itch.io/pause-menu-gamemaker-1-2) | Another smaller implementation but has a cool animation between menu options. | 🔴 Inactive |
| [Magpie](https://dragonite.itch.io/magpie) | Generic Inventory System. | 🔴 Inactive |
| [ImGuiGML](https://rousr.itch.io/imguigml) | DLL/GML wrapper of Dear ImGui. | 🔴 Inactive |
| [GUI Framework](https://niris.itch.io/gui-framework) | GUI implementation from Niris Games. | 🔴 Inactive |
| [zitk](https://github.com/TandyRum1024/zitk) | Another interesting, Dear ImGui-inspired GUI toolkit. In development, but worth keeping an eye on. | 🔴 Inactive |
| [SimpleUI](https://github.com/evolutionleo/SimpleUI) | Minimalistic UI framework. | 🔴 Inactive |

## Localization

| Name | Description | Status |
|---|---|---|
| [lexicon](https://github.com/tabularelf/lexicon) | Another localization solution focused on simplifying implementation. | 🟢 Active |
| [polyglot](https://github.com/daikon-games/polyglot) | Localization library. | 🔴 Inactive |
| [gm-i18n](https://github.com/CreativeHandOficial/gm-i18n) | Internationalization of texts simply and quickly, using JSON files. | 🔴 Inactive |
| [GMLocalize](https://github.com/DragoniteSpam/GMLocalize2) | Not a full localization solution. Extracts text strings for localization from a GameMaker Studio 2 project and saves it to a JSON file. | 🔴 Inactive |
| [Small Pentapop Localization Tool](https://github.com/AntonBergaker/small_pp_localization_tool) | Similar export tool to GMLocalize but exports to a csv. | 🔴 Inactive |
| [gms2-mofile](https://github.com/pmarincak/gms2-mofile) | Mofile reader used for localization. | 🔴 Inactive |

## Physics

| Name | Description | Status |
|---|---|---|
| [Verlet Integration Library](https://jamjamteam.itch.io/verlet-integration-gamemake-studio-2) | Verlet integration by Sarek Lambert. | 🟡 Semi-Active |
| [Loj Hadron Collider](https://github.com/Lojemiru/Loj-Hadron-Collider) | A robust, pixel-perfect collision engine. | 🔴 Inactive |
| [On Slopes and Grids](https://forum.yoyogames.com/index.php?threads/on-slopes-and-grids-subpixel-perfect-topdown-movement-and-collision-line-without-objects.4073/) | A tutorial to implement 45° slopes. | 🔴 Inactive |
| [GMS2 Platforming System](https://benal.itch.io/basic-modern-platforming-system) | GameMaker implementation by Ben Allen and an expansion on Shaun Spalding's original 1.4 platformer tutorial. | 🔴 Inactive |
| [Inverse Kinematics Extension](https://github.com/tonystr/Inverse-Kinematics-Extension-for-Gamemaker) | A library for working with inverse kinematics. | 🔴 Inactive |
| [GMVerlet-Integration](https://github.com/tabularelf/GMVerlet-Integration) | Verlet integration example used for visuals. | 🔴 Inactive |
| [Top-Down Movement & Collision](https://pixelatedpope.itch.io/tdmc/devlog/156556/converting-tdmc-to-use-tiles) | Robust object-based collision system from Pixelated Pope. | 🔴 Inactive |

## Sprites

| Name | Description | Status |
|---|---|---|
| [Collage](https://github.com/tabularelf/Collage) | Texture page builder and image manager. Mimics GameMaker's texture page packing while offering higher flexibility. | 🟢 Active |
| [AESnips](https://github.com/angelwire/AESnips) | A sprite playback system. | 🔴 Inactive |
| [phgen](https://github.com/squircledev/phgen) | Placeholder asset generation. | 🔴 Inactive |
| [Disarm](https://github.com/NuxiiGit/disarm) | A spriter skeletal animation at runtime. | 🔴 Inactive |
| [Spritely](https://github.com/bscotch/stitch/tree/develop/packages/spritely) | Image correction and cleanup for 2D video game sprites. | 🔴 Inactive |
| [PixelUpscaler](https://github.com/JujuAdams/Pixel-Art-Upscaling) | Pixel art upscaling shader for awkward resolutions for GameMaker. | 🔴 Inactive |
| [ASESync](https://sahaun.itch.io/asesync) | Automatically syncs aesprite files in GameMaker. | 🔴 Inactive |
| [conveyorbelt](https://github.com/imissmyfriends/conveyorbelt) | Similar to ASESync. Export Aesprite files to GameMaker sprites. | 🔴 Inactive |

## Audio

| Name | Description | Status |
|---|---|---|
| [GMEXT-FMOD](https://github.com/YoYoGames/GMEXT-FMOD) | Official support for FMOD in GameMaker. | 🟢 Active |
| [Vinyl](https://github.com/JujuAdams/Vinyl) | Live updating audio system. | 🟢 Active |
| [FML](https://github.com/Nikkilae/fml) | GameMaker bindings for the FMOD Studio API. | 🟡 Semi-Active |
| [Echo/Delay Effect](https://madwolf-studios.itch.io/audio-echodelay-effect-for-gamemaker-studio-2) 💸 | Optimized delay effect. | 🔴 Inactive |
| [wavload](https://github.com/nkrapivin/wavload) | Demonstrates how to externally load .wav files. | 🔴 Inactive |
| [audioExt](https://github.com/tabularelf/audioExt) | Sound External Loader/Unloader Manager. | 🔴 Inactive |
| [ExternalAudio](https://github.com/NuxiiGit/ExternalAudio) | Load external .wav files at runtime. | 🔴 Inactive |
| [Phonix](https://github.com/Andre-404/Phonix/) | Compact audio system. Great for dynamic music! | 🔴 Inactive |
| [LineAudio](https://github.com/WangleLine/LineAudio) | Audio helper functions. | 🔴 Inactive |
| [Bard](https://github.com/gl326/bard-audio) | An engine for desiging and implementing good audio in GameMaker. Updated to make use of the more recent GameMaker audio effects. | 🔴 Inactive |

## Levels

| Name | Description | Status |
|---|---|---|
| [LDtkParser](https://github.com/evolutionleo/LDtkParser) | Advanced LDtk Importer. | 🟢 Active |
| [GMRoomLoader](https://github.com/glebtsereteli/GMRoomLoader) | Streamlined room loading at runtime. Great for reusable room prefabs and procedural generation. | 🟢 Active |
| [LDtk to GMS](https://shynif.itch.io/ldtk-to-gms) | LDtk Importer. | 🔴 Inactive |
| [Room Data Inspector](https://github.com/heygleeson/GM-RoomInspector) | Collects room data and stores it into a JSON for later use. | 🔴 Inactive |
| [Random Dungeon Generator](https://github.com/BlaXun/Random-Dungeon-Generator-GMS-2.3) | Combines user-defined chambers to create a dungeon. | 🔴 Inactive |
| [Random Level Generator](https://github.com/GameMakerDiscord/random-level-gen-gms2) | A random level generation example (similar to Nuclear Throne) using GameMaker. | 🔴 Inactive |
| [Wave Function Collapse](https://quadolorgames.itch.io/wfc-gml-demo) | Generates a random tile map but not production ready in its current state. | 🔴 Inactive |
| [Destructible Terrain](https://github.com/niksudan/gms2-destructible-terrain) | An example of collidable, destructible terrain in GameMaker Studio using surfaces and grids. | 🔴 Inactive |
| [Cellular Automata Caves](https://alessiogamedev.itch.io/gms-cellular-automata-algorithm) | Generates huge caves in a few hundred milliseconds. | 🔴 Inactive |

## Particles

| Name | Description | Status |
|---|---|---|
| [Particle Editor](https://gamemakercasts.itch.io/particle-editor) | Create particles with an easy UI and export into GML code. | 🟢 Active |
| [Particles Wrapper](https://github.com/GamemakerCasts/particles) | A simplistic particle system wrapper that is designed to make creating particles fun and easy. | 🔴 Inactive |
| [Advanced Particles](https://limekys.itch.io/advanced-particle-system) | A particle implementation that comes with it's own delta timing methods. | 🔴 Inactive |
| [Pulse](https://github.com/Delfos1/Pulse) | A library to create more complex particle emitters, systems and particles. | 🔴 Inactive |
| [Burrn](https://github.com/FoxyOfJungle/Burrn) | Built-in particle system that uses the particle asset built into the IDE. | 🔴 Inactive |

## Lighting

- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[Lighting Systems](https://www.youtube.com/playlist?list=PLYVea5brHS8YHECGPoEp4_gWU-k6nWzUy) - Very fast dynamic 2D lighting implementation from GrizzliusMaximus using shadow casting.

| Name | Description | Status |
|---|---|---|
| [Crystal](https://foxyofjungle.itch.io/crystal-2d-lighting-engine) 💸 | Complete and efficient 2D lighting solution. | 🟢 Active |
| [Bulb](https://github.com/JujuAdams/Bulb) | 2D lighting and shadows. | 🔴 Inactive |
| [Lighting System 2D](https://github.com/borup3/Lighting-System-2D) | Requires GameMaker 2.2+ according to the repo. | 🔴 Inactive |
| [GameMaker Lighting Engine](https://github.com/bilouw/Gamemaker-Lighting-Engine) | Tile-based Lighting Engine that projects shadows. | 🔴 Inactive |

## Shaders

- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[Shader Tutorials](https://www.youtube.com/watch?v=ch4BYqkL1w8&list=PL0kTSdIvQNCNE-BDKOlYu628AalMmXy_P) - Gaming Reverends.
- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[Shader Tutorials](https://www.youtube.com/watch?v=a4S7LXx6-sQ&list=PL_hT--4HOvrdkihto8Xu7hhp1-5Gj8zsa) - DragoniteSpam.
- 🗒️[GMShaders.com](https://gmshaders.com/) - Shader tutorials from Xor. Originally hosted at "xorshaders.com".
- 🧰[Shadertoy to GameMaker](https://iarri.github.io/Shadertoy2GM/) - Convert shadertoy.com GLSL shaders to run in GameMaker.

| Name | Description | Status |
|---|---|---|
| [Post-Processing FX](https://foxyofjungle.itch.io/post-processing-fx) 💸 | 50+ high-quality, customizable effects. | 🟢 Active |
| [TransFX](https://short-bread.itch.io/transfx) | Transition Library. | 🔴 Inactive |
| [BJRTFX](https://zikbakguru.itch.io/bjrtfx) | Zik's CRT Utility Shader. | 🔴 Inactive |
| [bktGlitch](https://odditica.itch.io/bktglitch) | Glitch shader. | 🔴 Inactive |
| [H O R R I - F I](https://gizmo199.itch.io/horri-fi) | VHS Shader. | 🔴 Inactive |
| [Depth Sorted Sillouettes](https://pixelatedpope.itch.io/depth-sorted-silhouette-example) | Example project to demonstrate shader-based depth sorting sillouettes. Tested on PC, Mac, HTML5, and Android. | 🔴 Inactive |
| [1PassBlur](https://github.com/XorDev/1PassBlur/wiki) | Blur Shader with adjustable radius. | 🔴 Inactive |
| [Bokeh Blur](https://github.com/XorDev/Bokeh/wiki) | Extension of the 1PassBlur which provides a different look. Similar to a real lens blur. Although it's much slower than 1Pass or Dual-Kawase. | 🔴 Inactive |
| [Dual-Kawase](https://github.com/XorDev/Dual-Kawase/wiki) | Blur Shader that limits radius but is very efficient. | 🔴 Inactive |
| [Xor's Halftone](https://xordev.itch.io/halftone) | A wonderful, versitile halftone shader. Lots of tweakable settings. | 🔴 Inactive |
| [Voronoi](https://github.com/XorDev/GMS-Voronoi-Pixels) | Sampled pixels on a Voronoi diagram. | 🔴 Inactive |
| [Fire-Fun](https://github.com/XorDev/Fire-Fun/wiki) | Some fun magic fireballs. | 🔴 Inactive |
| [Jump Flooding](https://terohannula.itch.io/jump-flooding-algorithm) | Jump Flooding Algorithm for GameMaker made with shaders. | 🔴 Inactive |
| [Outline Shader](https://github.com/Grisgram/gml-outline-shader-drawer) | Outline shader. | 🔴 Inactive |
| [Chameleon](https://github.com/Lojemiru/Chameleon) | Palette Swapper. | 🔴 Inactive |
| [Xpanda](https://github.com/GameMakerDiscord/Xpanda) | Include code from external files in your shaders. | 🔴 Inactive |

## 3D

- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[3D GameMaker Playlist](https://www.youtube.com/watch?v=ojfN--tdSNM&list=PL_hT--4HOvrcML9uqHe4fwBVTm650Vy3V) - DragoniteSpam.
- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[3D Collisions Playlist](https://www.youtube.com/watch?v=o7kjtTEMpeU&list=PL_hT--4HOvrf_VYo26LNl3zN5uwfuC3CC) - DragoniteSpam.
- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[3D Optimization Playlist](https://www.youtube.com/watch?v=knfAZbJJKNY&list=PL_hT--4HOvrf_CJSA7fVU1tkjGVv5Sq2t) - DragoniteSpam.

| Name | Description | Status |
|---|---|---|
| [BBMOD](https://github.com/blueburn-cz/BBMOD) | 3D Rendering Solution. Comes with several modules to import obj, 3D camera setup, integration with ColMesh, and more. | 🟢 Active |
| [ColMesh](https://forum.yoyogames.com/index.php?threads/colmesh-3d-collisions-made-easy.82765/) | 3D Collision Library from TheSnidr. | 🟢 Active |
| [DmrVBM](https://github.com/Dreamer13sq/DmrVBM-blender-to-gms2) | Import/Export tools to load vertex buffer data out of Blender and into GMS. | 🟢 Active |
| [Penguin](https://dragonite.itch.io/penguin) | 3D model conversion tool. | 🟢 Active |
| [3D-2D](https://github.com/YoYoGames/3D-2D) | Official tool to turn 3D models into 2D sprites. | 🔴 Inactive |
| [BSP 4 GMS](https://cdlegasse.itch.io/ozarq-bsp-4-gms) | Import BSP files into GameMaker. Currently just a demo but worth keeping an eye on. | 🔴 Inactive |
| [dotobj](https://github.com/JujuAdams/dotobj) | Lightweight .obj/.mtl 3D model loader written in native GML. | 🔴 Inactive |
| [Bronze Box](https://github.com/cicadian/Bronze-Box) | Example of how to build 3D world models from a 2D grid. | 🔴 Inactive |
| [Camera3D](https://gizmo199.itch.io/camera3d) | Simple 3D camera setup. | 🔴 Inactive |
| [Blender to GameMaker](https://github.com/blender-to-gmstudio) | A collection of scripts to export and import Blender models to and from GameMaker. | 🔴 Inactive |
| [Three Mice In a Trench Coat](https://github.com/XorDev/ThreeMiceInaTrenchcoat) | Source for a GameMaker 3D game. | 🔴 Inactive |
| [sPart](https://marketplace.yoyogames.com/assets/7299/spart-3d-particle-system) | 3D Particle System from TheSnidr. | 🔴 Inactive |
| [Terrain Editor](https://dragonite.itch.io/terrain) | Terrain editor. Exports to gm models, obj, or vertex buffers. | 🔴 Inactive |
| [Snowy Snow](https://dragonite.itch.io/snowy-snow) | 3D Snow Shader. | 🔴 Inactive |
| [3D Fragment Point Lights](https://danieldavis.itch.io/ddg-point-light-shader-system) 💸 | 3D point lights using shaders. | 🔴 Inactive |


## Sprite Stacking

- 🗒️[Beginners Guide to Sprite Stacking](https://medium.com/@avsnoopy/beginners-guide-to-sprite-stacking-in-gamemaker-studio-2-and-magica-voxel-part-1-f7a1394569c0) - A primer on sprite stacking from Avis. Check out part 2 from dev_dwarf as well.
- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[Sprite Stacking Tutorials](https://www.youtube.com/watch?v=VIDN-nG3EOU&list=PL3Kbpztq9qwT9MbW_k4yyJU__or1r8P2j) - Gizmo199.

| Name | Description | Status |
|---|---|---|
| [Fauxton3D](https://gizmo199.itch.io/fauxton3d) | Sprite stacking engine. | 🔴 Inactive |

## Networking

- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[Multiplayer Networking Tutorial](https://www.youtube.com/watch?v=NbsXRuNijlo&list=PLxaJReoxlrY_S4MrCYjzFCSrNX1TUX626) - Wizirdi.

| Name | Description | Status |
|---|---|---|
| [MultiClient](https://github.com/tabularelf/MultiClient) | Non-dll, multiple client launcher for network development. | 🟢 Active |
| [Warp](https://github.com/evolutionleo/Warp) | A feature-rich framework for multiplayer games, written in GameMaker and Node.js. | 🟡 Semi-Active |
| [EZ Networking](https://jasontomlee.itch.io/easy-gms-networking-platformer-build) | Host/client implementation with a chat feature. | 🔴 Inactive |
| [Patchwire-GM](https://github.com/gm-core/patchwire-gm) | The network library from gm-core if you want to use this implementation without the entire gm-core suite. | 🔴 Inactive |
| [GMHandshake](https://gist.github.com/nkrapivin/c73f5a962466a4ecb63187a009a300d8) | A Gist demonstrating a network handshake. | 🔴 Inactive |
| [HTTP GML](https://github.com/Sidorakh/http.gml) | Recieve GET requests and upload files in GML. | 🔴 Inactive |
| [GMNest](https://github.com/TimVN/GMNest) | Socket.IO extension for HTML5 games. | 🔴 Inactive |
| [Good GameMaker Rollback](https://springrollgames.itch.io/ggmr) | Rollback netcode library. | 🔴 Inactive |
| [GM Networking](https://github.com/gmclan-org/gm_networking) | Very simple network code demonstration. | 🔴 Inactive |
| [Boomers Networking](https://github.com/gmclan-org/gm_boomers_networking) | Network library which mimics pre-GM:Studio favorite networking extension 39dll using GM native functions. | 🔴 Inactive |
| [Rocket Networking Engine](https://marketplace.gamemaker.io/assets/11424/rocket-networking-engine) | Easy low-code multiplayer engine. | 🔴 Inactive |

## Integrations

| Name | Description | Status |
|---|---|---|
| [GMHook](https://github.com/Kruger0/GMHook) | We really like Discord integration. | 🟢 Active |
| [GMS2_RPC](https://github.com/Mtax-Development/GMS2_RPC) | Another Discord integration. | 🟡 Semi-Active |
| [DHook](https://github.com/tabularelf/DHook) | Discord integration. | 🔴 Inactive |
| [NekoPresence](https://marketplace.yoyogames.com/assets/9526/nekopresence) | Oops, all Discord integration. | 🔴 Inactive |
| [Steamworks.gml](https://github.com/YAL-GameMaker/steamworks.gml) | Various expansions to Steamworks SDK support in GameMaker: Studio. | 🔴 Inactive |
| [Parworks](https://github.com/nkrapivin/Parworks) | Additional functionality for the YYG Steamworks extension. | 🔴 Inactive |
| [GOG.gml](https://github.com/GameMakerDiscord/GOG.gml) | A native extension for GOG.com SDK support. | 🔴 Inactive |
| [GMTwitch](https://github.com/GameMakerDiscord/GMTwitch) | Twitch integration. | 🔴 Inactive |

## Camera

- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[GameMaker Cameras: As Simple as Possible](https://www.youtube.com/watch?v=_g1LQ6aIJFk) - Pixelated Pope's guide on GameMaker's camera system.
- 🗒️[Camera System Guide](https://maddestudiosgames.com/gms2-meet-the-camera-system/) - Getting started with cameras in GameMaker.

| Name | Description | Status |
|---|---|---|
| [Pixel Perfect Smooth Camera](https://github.com/YAL-GameMaker/pixel-perfect-smooth-camera) | An example of pixel-perfect yet smooth camera. | 🔴 Inactive |
| [Dynamic Splitscreen](https://maddestudios.itch.io/gms2-project-dynamic-splitscreen) | Local multiplayer split screen implementation that merges the camera when players are close. | 🔴 Inactive |
| [STANNcam](https://github.com/jack27121/STANNcam) | Camera and resolution manager. | 🔴 Inactive |
| [Camera All-In-One](https://jasontomlee.itch.io/allinone-camera) | Editor, screenshake, view-resizing, follow modes, screen effects, etc. | 🔴 Inactive |

## Sequences

- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[Sequences Tutorial](https://www.youtube.com/watch?v=WO6gzhrx5b8) - Shaun Spalding.
- ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)[Making Splash Screen Sequences](https://www.youtube.com/watch?v=hTh5UpFxx1E) - Mash Arcade.

| Name | Description | Status |
|---|---|---|
| [DuplicateSequence](https://github.com/KeeVeeGames/DuplicateSequence.gml) | Make a deep copy of sequence assets/structs for editing at runtime. | 🔴 Inactive |

## State Machines

| Name | Description | Status |
|---|---|---|
| [SnowState](https://github.com/sohomsahaun/SnowState) | Robust finite state machine. | 🟢 Active |
| [FastSM](https://github.com/JulianDicken/FastSM) | Lightweight alternative to SnowState. | 🔴 Inactive |
| [wFSM](https://mors-games.itch.io/wfsm) | Another Easy-to-use Finite State Machine library. | 🔴 Inactive |
| [True State](https://pixelatedpope.itch.io/truestate) | Feature-rich finite state machine to handle complex objects. | 🔴 Inactive |
| [Pinocchio](https://github.com/JujuAdams/Pinocchio) | State-based animation system. | 🔴 Inactive |
| [BehaviorTree](https://github.com/Gizmo199/BehaviorTree) | A simple behavior tree system. | 🔴 Inactive |
| [FSM AI](https://github.com/gmclan-org/FSM-AI-module) | Finite state machine for NPC AI. | 🔴 Inactive |

## Pathing

| Name | Description | Status |
|---|---|---|
| [Aquila](https://dragonite.itch.io/aquila) | A* Pathfinding implementation. | 🔴 Inactive |
| [A-Star-Pathing](https://github.com/helloalbertdang/A-Star-Pathing) | Another A* pathfinding implementation. | 🔴 Inactive |
| [Grid-based Pathfinding Scripts](https://proton-squid.itch.io/pathfinding) | Flexible pathfinding system with 3 different algorithms. | 🔴 Inactive |
| [Pathfinding in graph](https://github.com/gmclan-org/dijkstra-graph) | Shortest pathfinding system in (weighted) graph, using Dijkstra algorithm. | 🔴 Inactive |

## Useful Extras

- [Animated Flag](https://github.com/Grisgram/gml-animated-flag) - Vertex-animated flag.
- [Video Player Extension](https://forum.yoyogames.com/index.php?threads/video-player-for-windows-macos-and-ubuntu.77882/) - Play videos. However, the latest version of GMS has video support.
- [GMESCAPI](https://marketplace.yoyogames.com/assets/9529/gmescapi) - Webcam capture.
- [Danmaku Project](https://github.com/OmegaX1000/DanmakuProject) - Bullet hell engine.
- [OrbinautFramework](https://github.com/TrianglyRU/OrbinautFramework) - Accurate framework to make classic Sonic games.
- [Mouse Trail Effect](https://all-x.itch.io/gms2-mouse-trail-effect) - Shows how to trace a line with primitives to create a colorful trail.
- [Starfield Generator](https://github.com/PixelProphecy/gml_starfield_generator) - A script to generate starfields in GameMaker's GML language.
- [CleanShapes](https://github.com/JujuAdams/Clean-Shapes) - Antialiased primitives library for GameMaker.
- [GMLScripts.com](https://www.gmlscripts.com/script/index) - Dozens of helper scripts, organized similarly to the official documentation.
- [GM48 Resources](https://gm48.net/resources) - Free resources from the community to become better at GameMaker Studio, game development and game jams.
- [GameMaker Kitchen](https://www.gamemakerkitchen.com/) - Another great resource for open source libraries, assets, and snippets.
- [obj_podcast](https://objpodcast.com/) - Gamedev-centered podcast featuring members of the GameMaker community.
- [Dracula Theme](https://github.com/dracula/gamemaker-studio) - A dark theme for the IDE.
- [Gruvbox Theme](https://github.com/heygleeson/Gruvbox-GMTheme) - A retro groove theme for the IDE.
- [2.3 Syntax in Detail](https://yal.cc/gamemaker-2-3-syntax-in-details/) - A full guide of the syntax features/changes in GML from Yal.
- [GameMaker Garbage Collection](https://gist.github.com/DatZach/96a30d6ae4225f8ec152719e57aed26b) - How garbage collection works in GML.
- [GitHub Yacc to GML Fix](https://www.reddit.com/r/gamemaker/comments/n5m35l/a_simple_fix_for_github_incorrectly_detecting/) - Tell GitHub your repo is all GML, not Yacc.
- [GameMaker Repo Badges](https://github.com/matthiaszarzecki/MadeWithGameMakerStudioBadges) - Fancy badges to add to your README files.
- [GameMaker Discord Community GitHub](https://github.com/GameMakerDiscord) - Have you made a gamemaker tool you want to share? Consider submitting it to the official Discord's GitHub.
- [Source Control with Git & GameMaker](https://www.youtube.com/watch?v=UZG-P68xWio&list=PLSFMekK0JFgzmyDxVxj5Cctafu5UX_vUC) - FriendlyCosmonaut. ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)
- [Game Resolution & Aspect Ratio Management](https://www.youtube.com/watch?v=_g1LQ6aIJFk&list=PLXkVsacazW2qvdnKNzgBLkUwlgi3FU-VO) - Pixelated Pope. ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)
- [Setting up a Virtual Machine for GameMaker](https://www.youtube.com/watch?v=cK5k1_zN4eM) - MicahTheManiac. ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)
- [Making Attacks Feel Good](https://www.youtube.com/watch?v=RWkMsD2WUz8) - Blobfish. ![YouTube](https://github.com/bytecauldron/awesome-gamemaker/raw/main/icons/youtube.png)
- [vim-GML](https://github.com/JafarDakhan/vim-gml) - High quality Vim syntax highlighting for GameMaker.
- [Rousr Release](https://gitlab.com/rousr-release/) - Unmaintained projects from the Rousr team (in case anyone asks where OutsideTheBox/Dissonance went).
- [Tome](https://github.com/chesrowe/Tome/) - Automatically generate documentation sites from GameMaker projects.
- [Piano example](https://github.com/gmclan-org/piano_example) - Example of playing intrument notes by changing pitch, using only one audio file.
- [Compatibility scripts](https://github.com/gmclan-org/compatibility-scripts) - Scripts that are used by GM when importing GM:S 1.4 projects, taken directly from runtime files.
- [Pause example](https://github.com/gmclan-org/pause_no_surface) - Simple example of a pause screen without using surfaces.
- [Build Automation, CI/CD](https://gist.github.com/shichen85/887d237cdc4338fa3f4e4749a14990db) - Tutorial on using GitHub Actions as a CI/CD pipeline to automate building games.

## Blogs

- [RefresherTowel](https://refreshertowelgames.wordpress.com/category/tutorial/) - Contains several posts on level generation.
- [Tony Str](https://tonystr.net/) - Some great articles on working with JSON, regular expressions *(regex)*, and drawing circles in GML.
- [Katsaii](https://www.katsaii.com/content/blog/posts.html) - Some articles on more advanced GML topics.
- [Meseta on Game Dev](https://meseta.dev/) - Seasoned GameMaker dev's thoughts on GameMaker concepts and libraries.
- [Thoughts On GameMaker](https://github.com/JujuAdams/ThoughtsOnGameMaker) - Not a traditional blog but has great info on different GML techniques.

## YouTube

- [Jordan Guillou](https://www.youtube.com/channel/UCBmOLRTaPrfOxnTqpCLrwdQ) - Hobbyist indie dev with a few GameMaker-related tutorials.
- [DragoniteSpam](https://www.youtube.com/c/DragoniteSpam) - Covers highly technical elements of GameMaker with a focus on 3D.
- [Shaun Spalding](https://www.youtube.com/c/ShaunSpalding) - Previous community manager at YoYo Games. Has a wide variety of beginner-friendly GameMaker tutorials and helpful updates on new GameMaker features.
- [FriendlyCosmonaut](https://www.youtube.com/c/FriendlyCosmonaut) - Great playlist on building a farming RPG in GameMaker with several other tutorials.
- [Pixelated Pope](https://www.youtube.com/c/PixelatedPope) - Guides on GameMaker resolution management, cameras, GUI, and more.
- [Xor](https://www.youtube.com/c/XorDev) - Tons of shader demonstrations with a focus on 3D.
- [GamingEngineer](https://www.youtube.com/c/GamingEngineer) - A GameMaker developer that has been in the community for many years. They have a wide variety videos showcasing what GameMaker is capable of, with a focus on 3D.
- [TheSnidr](https://www.youtube.com/c/TheSnidr) - A lot of awesome 3D showcases and tutorials for GameMaker.
- [Peyton Burnham](https://www.youtube.com/channel/UCfh2Q3TsvlxM1S2GvXQ4eeQ) - GameMaker tutorials for top-down shooters and RPGs.
- [Gaming Reverends](https://www.youtube.com/channel/UC7fkptPD1FHQyDc9Fnm9S_A) - If you want to learn foundational material regarding GameMaker shaders, the "Shaders for Hobby-Programmers" playlist is definitely worth checking out.
- [Let's Learn This Together](https://www.youtube.com/c/LetsLearnThisTogether) - Small indie dev company with a focus on providing GameMaker guides.
- [Matharoo](https://www.youtube.com/c/GameMakerStationMatharoo) - Tons of free GameMaker tutorials and news about GameMaker.
- [GravityShift Games](https://www.youtube.com/c/SlasherXGAMES/) - A couple of genre-specific GameMaker tutorials, integrating databases into GameMaker, and more.
- [Slyddar](https://www.youtube.com/c/Slyddar/) - A channel dedicated to both DnD and GML tutorials.
- [SamSpadeGameDev](https://www.youtube.com/@SamSpadeGameDev) - In-depth coding tutorials for the hobbyist game maker.
- [gentoo's iceberg Playlist](https://www.youtube.com/playlist?list=PLks6h7R6jAUGrofUAQB178r6K8h43Ml5-) - Series based on iceberg to display advanced programming ideas in GameMaker.

## Community

[![GameMaker Forums](https://img.shields.io/badge/Forums-6AA916?style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAAZlBMVEX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2BrG8stAAAAIXRSTlMABg0OFBkfcn1%2Bf4CBgoOFhoeIiouWmNDa5ebp8PX2%2B%2F6o6Vq%2BAAAAY0lEQVR42k2OWQ6AIAwFn%2BIOioobrnD%2FS4o0EeanmQxNAdErRFTWtsFq6%2BiiZozz0CSnTjYBwo0RkF8DWDLf51Ni9K%2FYdq0Fy3KAfzk97M7goK1F%2F4rGH9Kk1OlboQtEDIrmC%2BU3CVxTr%2FRMAAAAAElFTkSuQmCC&&logoColor=white)](https://forum.yoyogames.com/index.php)
[![Reddit](https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white)](https://www.reddit.com/r/gamemaker/)
[![Discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/gamemaker)

## Special Thanks

JujuAdams, FaultyFunctions, Gleb Tsereteli, Shaun Spalding, DragoniteSpam, Nick Ver Voort, Pixelated Pope, Tony Strømsnæs, HeartBeast, Xor, Gaming Reverends, Matharoo, YellowAfterlife, Gizmo199, Avis, Josh Wilson, Lojemiru

## Footnotes

- This is based on a list from [GameMaker Libraries](https://github.com/FaultyFunctions/GameMakerLibraries) and from Gleb Tsereteli with additional links/details.
- A majority of linked resources will only work with `GameMaker 2.3+` due to GML syntax changes. However, if you are working in GameMaker 1.4, most library creators would appreciate it if someone makes a backport of their project. 🙂
- If you need more general game development resources, check out [Awesome Gamedev](https://github.com/Calinou/awesome-gamedev) or [MagicTools](https://github.com/ellisonleao/magictools#readme).

*GameMaker® is the property of YoYo Games™. This list is not affiliated with YoYo Games.*

## Contributing

Have something awesome to share? Check out the [Contributing Guidelines](https://github.com/bytecauldron/awesome-gamemaker/blob/main/CONTRIBUTING.md).

## GameMaker Keybindings

![Keybindings](https://github.com/bytecauldron/awesome-gamemaker/raw/main/images/keybindings.png)
