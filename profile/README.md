<a href="https://labs.watchthelight.org"><img src="https://labs.watchthelight.org/og.png" alt="watchthelight labs" width="100%"></a>

[![site](https://img.shields.io/badge/labs.watchthelight.org-6a9a6e?style=flat-square&labelColor=0d0e12&logo=githubpages&logoColor=c8ccd0)](https://labs.watchthelight.org) [![repos](https://img.shields.io/badge/repos-22-2a2d33?style=flat-square&labelColor=0d0e12)](https://github.com/orgs/watchthelight-labs/repositories) [![macOS](https://img.shields.io/badge/macOS_Tahoe-26.7.2-2a2d33?style=flat-square&labelColor=0d0e12&logo=apple&logoColor=c8ccd0)](https://labs.watchthelight.org) [![discord](https://img.shields.io/badge/discord-watchthelight-2a2d33?style=flat-square&labelColor=0d0e12&logo=discord&logoColor=c8ccd0)](https://discord.com/users/697169405422862417)

I'm getting a Lenovo Legion 5 15IAX10 to run macOS every day through OpenCore. Its Arrow Lake CPU, RTX 5070 Laptop GPU, Intel Xe iGPU and MediaTek MT7925 Wi-Fi 7 card have no macOS drivers, so these repos are the drivers and tools I wrote for them. The boot logs behind each one are public too.

Each repo has its own pages on **[labs.watchthelight.org](https://labs.watchthelight.org)**, with its docs, releases and issues. Boot logs from the Legion and from people who run these drivers are in [research](https://labs.watchthelight.org/research/), and the AI setup behind the code is in [agents](https://labs.watchthelight.org/agents/).

### Graphics

| | | |
|---|---|---|
| [**WTLNvidiaGfx**](https://labs.watchthelight.org/WTLNvidiaGfx/) | Fork of NullMoth's NVIDIA Metal driver for macOS, kept for one RTX 5070 Laptop (10DE:2D18) in a Legion 5 15IAX10 on Tahoe: 115 W TGP... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLNvidiaGfx?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLNvidiaGfx/releases/) |
| [**WTLIntelGfx**](https://labs.watchthelight.org/WTLIntelGfx/) | Intel Xe graphics acceleration for macOS and Hackintosh: Metal and Vulkan on Iris Xe, Intel Arc and Core Ultra (Meteor Lake, Arrow Lake)... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLIntelGfx?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLIntelGfx/releases/) |
| [**WTLHybridGfx**](https://labs.watchthelight.org/WTLHybridGfx/) | Hybrid graphics for macOS on the Lenovo Legion 5 15IAX10: NVIDIA Optimus-style dGPU power control, render offload and the panel mux... |  |

### Wi-Fi & Bluetooth

| | | |
|---|---|---|
| [**WTLMtkWireless**](https://labs.watchthelight.org/WTLMtkWireless/) | MediaTek MT7925 (Filogic 360, Wi-Fi 7, AMD RZ717) Wi-Fi driver for macOS Hackintosh: OpenCore, Sequoia 15 and Tahoe 26, WPA2, 190 Mb/s... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLMtkWireless?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLMtkWireless/releases/) |
| [**WTLWifiMenu**](https://labs.watchthelight.org/WTLWifiMenu/) | macOS's own Wi-Fi menu for the MediaTek MT7925 / AMD RZ717 on Hackintosh: an IO80211 controller and Skywalk data path on top of... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLWifiMenu?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLWifiMenu/releases/) |
| [**WTLMtkBluetooth**](https://labs.watchthelight.org/WTLMtkBluetooth/) | MediaTek MT7925 / AMD RZ717 Bluetooth on macOS Hackintosh: loads the card's firmware (USB 0489:E111 and 20 other MT7925 ids) so... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLMtkBluetooth?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLMtkBluetooth/releases/) |
| [**WTLLegionBtFix**](https://labs.watchthelight.org/WTLLegionBtFix/) | Lilu plugin for macOS Tahoe 26.7.1 (25G241) and 26.7.2 (25G332): two in-memory patches to bluetoothd for the MediaTek MT7925 Bluetooth... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLLegionBtFix?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLLegionBtFix/releases/) |

### Platform & power

| | | |
|---|---|---|
| [**WTLLegionCpuPower**](https://labs.watchthelight.org/WTLLegionCpuPower/) | Lilu plugin: real clocks and power for Intel Arrow Lake (Core Ultra 200HX) on macOS Tahoe: hidden 30 W MCHBAR limit and HWP unit fix | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLLegionCpuPower?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLLegionCpuPower/releases/) |
| [**WTLLegionCbmrFix**](https://labs.watchthelight.org/WTLLegionCbmrFix/) | OpenCore UEFI driver that fixes vm_page_validate_no_references kernel panics on Lenovo laptops (Legion 5 15IAX10) by unloading the... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLLegionCbmrFix?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLLegionCbmrFix/releases/) |

### Input & audio

| | | |
|---|---|---|
| [**WTLI2CArrowLake**](https://labs.watchthelight.org/WTLI2CArrowLake/) | Codeless kext that lets VoodooI2C drive the Intel Arrow Lake-HX / 800-series PCH I2C controllers (8086:7F4C-7F4F, 7F7A, 7F7B) with the... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLI2CArrowLake?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLI2CArrowLake/releases/) |
| [**WTLLegionITEKbdFix**](https://labs.watchthelight.org/WTLLegionITEKbdFix/) | Codeless kext for Lenovo Legion laptops with the ITE 8258 USB keyboard controller (048D:C195): claims the lighting (LampArray) interface... | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLLegionITEKbdFix?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLLegionITEKbdFix/releases/) |
| [**WTLAudio**](https://labs.watchthelight.org/WTLAudio/) | Audio on macOS Tahoe for the Realtek ALC257 behind Intel's Arrow Lake-HX HDA controller (8086:7F50): a patch and build script for... |  |
| [**WTLNumpadKeys**](https://labs.watchthelight.org/WTLNumpadKeys/) | macOS event tap that turns numpad 1/5/2/3 into the arrow keys, for keyboards whose arrows died (LaunchAgent) | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLNumpadKeys?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLNumpadKeys/releases/) |

### Boot & EFI

| | | |
|---|---|---|
| [**WTLLegionOpenCore**](https://labs.watchthelight.org/WTLLegionOpenCore/) | OpenCore 1.0.8 EFI, ACPI tables and config for macOS Tahoe 26.7.2 and Sequoia on the Lenovo Legion 5 15IAX10 (Core Ultra 9 275HX Arrow... |  |

### Testing tools

| | | |
|---|---|---|
| [**WTLGpuGuard**](https://labs.watchthelight.org/WTLGpuGuard/) | Boot-time safety net for testing GPU driver builds on macOS: stage, reboot, confirm on screen or roll back automatically | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLGpuGuard?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLGpuGuard/releases/) |
| [**WTLWifiGuard**](https://labs.watchthelight.org/WTLWifiGuard/) | Boot-time safety net for testing Wi-Fi kext builds on an OpenCore Hackintosh: stage on the EFI, reboot, pass or roll back | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLWifiGuard?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLWifiGuard/releases/) |
| [**WTLBootDump**](https://labs.watchthelight.org/WTLBootDump/) | LaunchDaemon that snapshots the kernel log and IORegistry at fixed times after boot, for boots that never reach the desktop | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLBootDump?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLBootDump/releases/) |
| [**WTLStagedReboot**](https://labs.watchthelight.org/WTLStagedReboot/) | Lets an AI coding agent restart the Mac it runs on for a staged boot attempt and tells the next session what happened | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLStagedReboot?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLStagedReboot/releases/) |
| [**WTLHackintoshTest**](https://labs.watchthelight.org/WTLHackintoshTest/) | Feature test for macOS on PC hardware: 119 probes over graphics, display, audio, input, network, power, with evidence | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLHackintoshTest?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLHackintoshTest/releases/) |
| [**WTLKcAbi**](https://labs.watchthelight.org/WTLKcAbi/) | Read-only Python tools for macOS x86_64 kernel collections: symbols, link checks, ABI dumps for kext development | [![release](https://img.shields.io/github/v/release/watchthelight-labs/WTLKcAbi?style=flat-square&labelColor=0d0e12&color=4d7a51&label=)](https://labs.watchthelight.org/WTLKcAbi/releases/) |

### Research & agents

| | | |
|---|---|---|
| [**research**](https://labs.watchthelight.org/research/) | Logs from our Hackintosh projects and from people who use them (redacted, sorted by user and machine), plus a daily record of what... |  |
| [**agents**](https://labs.watchthelight.org/agents/) | How I work with AI agents: Claude Code skills and hooks, my memory MCP server, device and USB workflows, upstream scouting, caveman and... |  |

<sub>Generated from the live repo list every 6 hours by tools/profile.py.</sub>
