<a href="https://labs.watchthelight.org"><img src="https://labs.watchthelight.org/og.png" alt="watchthelight labs: macOS drivers and tools for hardware Apple never shipped drivers for" width="100%"></a>

[![site](https://img.shields.io/badge/labs.watchthelight.org-6a9a6e?style=flat-square&labelColor=0d0e12&logo=githubpages&logoColor=c8ccd0)](https://labs.watchthelight.org) [![repos](https://img.shields.io/badge/repos-21-2a2d33?style=flat-square&labelColor=0d0e12)](https://github.com/orgs/watchthelight-labs/repositories) [![macOS](https://img.shields.io/badge/macOS_Tahoe-26.7.1-2a2d33?style=flat-square&labelColor=0d0e12&logo=apple&logoColor=c8ccd0)](https://labs.watchthelight.org) [![discord](https://img.shields.io/badge/discord-watchthelight-2a2d33?style=flat-square&labelColor=0d0e12&logo=discord&logoColor=c8ccd0)](https://discord.com/users/697169405422862417)

> **Heads up:** a good portion of the code in these repos is AI generated. I do understand how it works,
> and I'm happy to explain any of it. If something looks wrong or you have a question, open an issue
> or ping me on Discord (`watchthelight`).

Built while getting a Lenovo Legion 5 15IAX10 to run macOS as a daily driver through OpenCore: an Arrow Lake CPU, an RTX 5070 Laptop GPU, an Intel Xe iGPU and a MediaTek MT7925 Wi-Fi 7 card, none of which macOS supports. Everything is open source, logs included.

Every repo, with live badges and a starfield: **[labs.watchthelight.org](https://labs.watchthelight.org)**. Logs from every boot attempt and from people who use these: [research](https://github.com/watchthelight-labs/research). How the AI side works: [agents](https://github.com/watchthelight-labs/agents).

### Graphics

| | | |
|---|---|---|
| [**NvGfx**](https://github.com/watchthelight-labs/NvGfx) | Fork of NullMoth's NVIDIA Metal driver for macOS, kept for one RTX 5070 Laptop (10DE:2D18) in a Legion 5 15IAX10 on Tahoe: 115 W TGP... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/NvGfx?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/NvGfx/releases) |
| [**XeGfx**](https://github.com/watchthelight-labs/XeGfx) | Intel Xe graphics for macOS: Linux i915 through FreeBSD drm-kmod and LinuxKPI on XNU, staged and safe to test (work in progress,... |  |

### Wi-Fi & Bluetooth

| | | |
|---|---|---|
| [**mt7925-hackintosh-wifi**](https://github.com/watchthelight-labs/mt7925-hackintosh-wifi) | MediaTek MT7925 (Filogic 360, Wi-Fi 7, AMD RZ717) Wi-Fi driver for macOS Hackintosh: OpenCore, Sequoia 15 and Tahoe 26, WPA2, 190 Mb/s.... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/mt7925-hackintosh-wifi?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/mt7925-hackintosh-wifi/releases) |
| [**mt7925-hackintosh-wifi-native**](https://github.com/watchthelight-labs/mt7925-hackintosh-wifi-native) | macOS's own Wi-Fi menu for the MediaTek MT7925 / AMD RZ717 on Hackintosh: IO80211 controller and Skywalk data path over... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/mt7925-hackintosh-wifi-native?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/mt7925-hackintosh-wifi-native/releases) |
| [**mt7925-hackintosh-bluetooth**](https://github.com/watchthelight-labs/mt7925-hackintosh-bluetooth) | MediaTek MT7925 / AMD RZ717 Bluetooth on macOS Hackintosh: loads the card's firmware (USB 0489:E111 and 20 other MT7925 ids) so... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/mt7925-hackintosh-bluetooth?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/mt7925-hackintosh-bluetooth/releases) |
| [**LegionBtFix**](https://github.com/watchthelight-labs/LegionBtFix) | Lilu plugin for macOS Tahoe 26.7.1 (25G241): two in-memory patches to bluetoothd for the MediaTek MT7925 Bluetooth controller (LE Create... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/LegionBtFix?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/LegionBtFix/releases) |

### Platform & power

| | | |
|---|---|---|
| [**LegionCpuPower**](https://github.com/watchthelight-labs/LegionCpuPower) | Lilu plugin: real clocks and power for Intel Arrow Lake (Core Ultra 200HX) on macOS Tahoe: hidden 30 W MCHBAR limit and HWP unit fix | [![release](https://img.shields.io/github/v/release/watchthelight-labs/LegionCpuPower?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/LegionCpuPower/releases) |
| [**LegionCbmrFix**](https://github.com/watchthelight-labs/LegionCbmrFix) | OpenCore UEFI driver that fixes vm_page_validate_no_references kernel panics on Lenovo laptops (Legion 5 15IAX10) by unloading the... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/LegionCbmrFix?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/LegionCbmrFix/releases) |

### Input & audio

| | | |
|---|---|---|
| [**LegionI2CArrowLake**](https://github.com/watchthelight-labs/LegionI2CArrowLake) | Codeless kext that lets VoodooI2C drive the Intel Arrow Lake-HX / 800-series PCH I2C controllers (8086:7F4C-7F4F) with the right timing... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/LegionI2CArrowLake?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/LegionI2CArrowLake/releases) |
| [**LegionITEKbdFix**](https://github.com/watchthelight-labs/LegionITEKbdFix) | Codeless kext for Lenovo Legion laptops with the ITE 8258 USB keyboard controller (048D:C195): claims the lighting (LampArray) interface... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/LegionITEKbdFix?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/LegionITEKbdFix/releases) |
| [**VoodooHDA-Legion**](https://github.com/watchthelight-labs/VoodooHDA-Legion) | Audio on macOS Tahoe for the Realtek ALC257 behind Intel's Arrow Lake-HX HDA controller (8086:7F50): a patch and build script for... |  |
| [**numpad-arrows**](https://github.com/watchthelight-labs/numpad-arrows) | macOS event tap that turns numpad 1/5/2/3 into the arrow keys, for keyboards whose arrows died (LaunchAgent) | [![release](https://img.shields.io/github/v/release/watchthelight-labs/numpad-arrows?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/numpad-arrows/releases) |

### Boot & EFI

| | | |
|---|---|---|
| [**Legion-5-15IAX10-OpenCore**](https://github.com/watchthelight-labs/Legion-5-15IAX10-OpenCore) | OpenCore 1.0.8 EFI, ACPI tables and config for macOS Tahoe 26.7.1 and Sequoia on the Lenovo Legion 5 15IAX10 (Core Ultra 9 275HX Arrow... |  |

### Testing tools

| | | |
|---|---|---|
| [**gpu-guard**](https://github.com/watchthelight-labs/gpu-guard) | Boot-time safety net for testing GPU driver builds on macOS: stage, reboot, confirm on screen or roll back automatically | [![release](https://img.shields.io/github/v/release/watchthelight-labs/gpu-guard?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/gpu-guard/releases) |
| [**wifi-guard**](https://github.com/watchthelight-labs/wifi-guard) | Boot-time safety net for testing Wi-Fi kext builds on an OpenCore Hackintosh: stage on the EFI, reboot, pass or roll back | [![release](https://img.shields.io/github/v/release/watchthelight-labs/wifi-guard?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/wifi-guard/releases) |
| [**bootdump**](https://github.com/watchthelight-labs/bootdump) | LaunchDaemon that snapshots the kernel log and IORegistry at fixed times after boot, for boots that never reach the desktop | [![release](https://img.shields.io/github/v/release/watchthelight-labs/bootdump?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/bootdump/releases) |
| [**legion-reboot**](https://github.com/watchthelight-labs/legion-reboot) | Lets an AI coding agent restart the Mac it runs on for a staged boot attempt and tells the next session what happened | [![release](https://img.shields.io/github/v/release/watchthelight-labs/legion-reboot?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/legion-reboot/releases) |
| [**hackintosh-feature-test**](https://github.com/watchthelight-labs/hackintosh-feature-test) | Feature test for macOS on PC hardware: 119 probes over graphics, display, audio, input, network, power, with evidence | [![release](https://img.shields.io/github/v/release/watchthelight-labs/hackintosh-feature-test?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/hackintosh-feature-test/releases) |
| [**kcabi**](https://github.com/watchthelight-labs/kcabi) | Read-only Python tools for macOS x86_64 kernel collections: symbols, link checks, ABI dumps for kext development | [![release](https://img.shields.io/github/v/release/watchthelight-labs/kcabi?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://github.com/watchthelight-labs/kcabi/releases) |

### Research & agents

| | | |
|---|---|---|
| [**research**](https://github.com/watchthelight-labs/research) | Logs from our Hackintosh projects and from people who use them (redacted, sorted by user and machine), plus a daily record of what... |  |
| [**agents**](https://github.com/watchthelight-labs/agents) | How I work with AI agents: Claude Code skills and hooks, my memory MCP server, device and USB workflows, upstream scouting, caveman and... |  |

<sub>Generated from the live repo list every 6 hours by tools/profile.py.</sub>
