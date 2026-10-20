# watchthelight labs

> **Heads up:** a good portion of the code in these repos is AI generated. I do understand how it works,
> and I'm happy to explain any of it. If something looks wrong or you have a question, open an issue
> or ping me on Discord (`watchthelight`).

macOS drivers and fixes for hardware Apple never shipped drivers for, written while getting a Lenovo Legion 5 15IAX10 (Core Ultra 9 275HX, RTX 5070 Laptop, MediaTek MT7925) to run macOS as a daily driver through OpenCore.

| Repo | What | State |
|---|---|---|
| [NvGfx](https://github.com/watchthelight-labs/NvGfx) | fork of NullMoth's NVIDIA Metal driver for the RTX 5070 Laptop: 165 Hz present path, 115 W TGP mode, shader cache fix, `nvgfx-smi`, reproducible kext builds (PolyForm Noncommercial) | 2.4.3-nvgfx.1 (NullMoth 2.4.3 base, boot hold fix), daily use |
| [LegionCpuPower](https://github.com/watchthelight-labs/LegionCpuPower) | Lilu plugin: real clocks and power limits for Arrow Lake-HX on Tahoe (MCHBAR limit from MSR 0x610, per-core HWP), fan control and the LegionFan menu app | 0.3.3, daily use |
| [mt7925-hackintosh-wifi](https://github.com/watchthelight-labs/mt7925-hackintosh-wifi) | Wi-Fi driver for the MediaTek MT7925 / Filogic 360 / AMD RZ717 (`14C3:7925`, `14C3:0717`), the only one for this chip; 190 Mb/s; the bundle zip on its releases page holds the whole Wi-Fi set | 0.11.3, daily use |
| [mt7925-hackintosh-wifi-native](https://github.com/watchthelight-labs/mt7925-hackintosh-wifi-native) | macOS's own Wi-Fi menu on top of the driver (IO80211 and Skywalk): menu bar, System Settings, saved networks, auto-join, no client app, unlike the SimpleMtkWlan route | 0.4.11, daily use on Tahoe 26.7.1 |
| [mt7925-hackintosh-bluetooth](https://github.com/watchthelight-labs/mt7925-hackintosh-bluetooth) | firmware loader for the same card's Bluetooth (USB `0489:E111` and 20 other MT7925 ids, RZ717 confirmed) | 0.2.2, daily use |
| [LegionBtFix](https://github.com/watchthelight-labs/LegionBtFix) | Lilu plugin: bluetoothd patches for the MT7925 on macOS 26.7.1 (crash loop on LE connect, silent AirPods) | 0.2.0, daily use |
| [LegionCbmrFix](https://github.com/watchthelight-labs/LegionCbmrFix) | UEFI driver: fixes `vm_page_validate_no_references` panics caused by Lenovo's firmware loading Microsoft's cbmr_driver.efi | 1.0.0 |
| [Legion-5-15IAX10-OpenCore](https://github.com/watchthelight-labs/Legion-5-15IAX10-OpenCore) | EFI, ACPI tables, config.plist (placeholder identity) and the kext list for this laptop | published 2026-10-17 |
| [VoodooHDA-Legion](https://github.com/watchthelight-labs/VoodooHDA-Legion) | audio on Tahoe: patch and build script for VoodooHDA LE, ALC257 behind the Arrow Lake-HX `8086:7F50` controller | speakers work, mic detected |
| [LegionI2CArrowLake](https://github.com/watchthelight-labs/LegionI2CArrowLake) | codeless kext: VoodooI2C personality for the Arrow Lake-HX I2C controllers (`8086:7F4C-7F4F`), touchpad | 1.1.0, daily use |
| [LegionITEKbdFix](https://github.com/watchthelight-labs/LegionITEKbdFix) | codeless kext: keeps the HID driver off the ITE 8258 keyboard's lighting interface so it types | 1.0.0, daily use |
| [gpu-guard](https://github.com/watchthelight-labs/gpu-guard) | boot-time safety net for GPU driver builds: stage, reboot, confirm on screen within a window or the last good driver goes back and the Mac restarts | 0.1.1, in use for every driver boot |
| [wifi-guard](https://github.com/watchthelight-labs/wifi-guard) | the same for Wi-Fi kexts staged on the EFI partition: pass when the network comes up, roll back when it does not | 0.1.0, in use |
| [bootdump](https://github.com/watchthelight-labs/bootdump) | LaunchDaemon that snapshots the kernel log and the IORegistry at 20, 60, 180 and 300 s after boot, readable later from another OS | 0.1.0, in use |
| [legion-reboot](https://github.com/watchthelight-labs/legion-reboot) | lets an AI coding agent restart the Mac it runs on for a staged boot attempt, and tells the next session what happened | 0.1.1, in use |
| [hackintosh-feature-test](https://github.com/watchthelight-labs/hackintosh-feature-test) | 119 probes over graphics, display, video, audio, input, network, Bluetooth, services and power, with evidence files and a diff between passes | 0.1.0 |
| [kcabi](https://github.com/watchthelight-labs/kcabi) | read-only Python tools for the x86_64 kernel collections: which symbols a kext may link against, ABI dumps, link checks | 0.1.0 |
| [numpad-arrows](https://github.com/watchthelight-labs/numpad-arrows) | event tap that turns numpad 1, 5, 2 and 3 into the arrow keys, for a keyboard whose arrows died | 0.1.0, daily use |

Each repo has a `docs/HOW-IT-WORKS.md` that explains the approach, and a Status table with what was actually tested. If it isn't in the table, assume it's untested.

New to OpenCore? Start with the [Dortania guide](https://dortania.github.io/OpenCore-Install-Guide/); these repos assume you already boot macOS.
