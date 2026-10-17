# watchthelight labs

> **Heads up:** a good portion of the code in these repos is AI generated. I do understand how it works,
> and I'm happy to explain any of it. If something looks wrong or you have a question, open an issue
> or ping me on Discord (`watchthelight`).

macOS drivers and fixes for hardware Apple never shipped drivers for, written while getting a Lenovo Legion 5 15IAX10 (Core Ultra 9 275HX, RTX 5070 Laptop, MediaTek MT7925) to run macOS as a daily driver through OpenCore.

| Repo | What | State |
|---|---|---|
| [LegionCbmrFix](https://github.com/watchthelight-labs/LegionCbmrFix) | UEFI driver: fixes `vm_page_validate_no_references` panics caused by Lenovo's firmware loading Microsoft's cbmr_driver.efi | 1.0.0 |
| [MtkWlan](https://github.com/watchthelight-labs/MtkWlan) | kext for the MediaTek MT7925 Wi-Fi card (`14C3:7925`) | 0.9.0: scan, join, WPA2-PSK (host-tested), `mtkwifi` tool, 190/175 Mb/s |
| [MtkBt](https://github.com/watchthelight-labs/MtkBt) | firmware loader for the MT7925's Bluetooth (USB `0489:E111`) | 0.2.0, daily use |
| [LegionBtFix](https://github.com/watchthelight-labs/LegionBtFix) | Lilu plugin: bluetoothd patches for the MT7925 on macOS 26.7.1 (crash loop on LE connect, silent AirPods) | 0.2.0; AirPods need the logging workaround |
| [Legion-5-15IAX10-OpenCore](https://github.com/watchthelight-labs/Legion-5-15IAX10-OpenCore) | EFI, ACPI tables, config.plist (placeholder identity) and the kext list for this laptop | published 2026-10-17 |
| [NvGfx](https://github.com/watchthelight-labs/NvGfx) | fork of NullMoth's NVIDIA Metal driver for the RTX 5070 Laptop: Terminal overdraw fix, 165 Hz present path, 115 W TGP mode, shader cache fix (PolyForm Noncommercial) | public, daily use |
| [VoodooHDA-Legion](https://github.com/watchthelight-labs/VoodooHDA-Legion) | audio on Tahoe: patch and build script for VoodooHDA LE, ALC257 behind the Arrow Lake-HX `8086:7F50` controller | speakers work, mic detected |
| [LegionI2CArrowLake](https://github.com/watchthelight-labs/LegionI2CArrowLake) | codeless kext: VoodooI2C personality for the Arrow Lake-HX I2C controllers (`8086:7F4C-7F4F`), touchpad | 1.1.0, daily use |
| [LegionITEKbdFix](https://github.com/watchthelight-labs/LegionITEKbdFix) | codeless kext: keeps the HID driver off the ITE 8258 keyboard's lighting interface so it types | 1.0.0, daily use |

Each repo has a `docs/HOW-IT-WORKS.md` that explains the approach, and a Status table with what was actually tested. If it isn't in the table, assume it's untested.

New to OpenCore? Start with the [Dortania guide](https://dortania.github.io/OpenCore-Install-Guide/); these repos assume you already boot macOS.
