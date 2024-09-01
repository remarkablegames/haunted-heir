<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/haunted-heir/master/game/gui/window_icon.png" alt="Ren'Py Template">
</p>

# Haunted Heir

![release](https://img.shields.io/github/v/release/remarkablegames/haunted-heir)
[![build](https://github.com/remarkablegames/haunted-heir/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/haunted-heir/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/haunted-heir/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/haunted-heir/actions/workflows/lint.yml)

👻 Haunted Heir

Play the game on:

- [remarkablegames](https://remarkablegames.org/haunted-heir)

## Ideation

- [Excalidraw](https://excalidraw.com/#json=FDEvc4r71jpkUDXUXfyKL,8NkgqD3_dHVBEEv-6jlqbQ)
- [Game Design Document](https://docs.google.com/document/d/1f7EV2XIVscNHl7_zC7w7ZSFk6rEn6_HovDL0cl7gp2s/edit)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/haunted-heir.git
cd haunted-heir
```

Replace the assets:

- [ ] `web-presplash.jpg`
- [ ] `game/gui/main_menu.png`
- [ ] `game/gui/window_icon.png`

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to display the developer menu.

Clean the cache:

```sh
find game -name "*.rpyc" -delete
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
