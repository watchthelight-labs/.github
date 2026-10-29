# Support

Where to ask what:

- **A bug in one of our drivers or tools:** open an issue in that repo and fill in the form. One problem per issue.
- **It works (or doesn't) on your machine:** open an issue in that repo with the hardware report form. Reports from hardware I don't own are how the tested lists grow.
- **Questions and setup help:** [GitHub Discussions](https://github.com/orgs/watchthelight-labs/discussions). Use it for "how do I", "which kext do I need", or "is my card supported".
- **NullMoth's NVIDIA driver itself:** NvGfx is a fork. If the problem also happens with NullMoth's own release, report it at [nullmoth/nvidia-macos-driver](https://github.com/nullmoth/nvidia-macos-driver/issues).
- **General OpenCore setup:** the [Dortania guide](https://dortania.github.io/OpenCore-Install-Guide/) covers most of it.
- **Security problems:** see [SECURITY.md](SECURITY.md). Please don't post them in public.

Wherever you ask, always say:

1. The machine (laptop model, or board for a desktop).
2. The macOS build, from `sw_vers` (for example 26.7.2 (25G332)).
3. The kext and its version, from `kmutil showloaded --list-only | grep -i <kext name>`.

Each repo's README names the `ioreg` and `log show` commands for its driver. Paste their output as text, not screenshots, and remove serial numbers and MAC addresses first.

Each repo also has its own pages on [labs.watchthelight.org](https://labs.watchthelight.org), with docs, releases and known issues. It's worth a look before asking.

I answer when I can. This is a spare-time project, so it may take a few days.
