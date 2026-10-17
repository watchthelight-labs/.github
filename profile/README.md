# watchthelight labs

> **Heads up:** a good portion of the code in these repos is AI generated. I do understand how it works,
> and I'm happy to explain any of it. If something looks wrong or you have a question, open an issue
> or ping me on Discord (`watchthelight`).

macOS drivers and fixes for hardware Apple never shipped drivers for, written while getting a Lenovo Legion 5 15IAX10 (Core Ultra 9 275HX, RTX 5070 Laptop, MediaTek MT7925) to run macOS as a daily driver through OpenCore.

| Repo | What | State |
|---|---|---|
| [LegionCbmrFix](https://github.com/watchthelight-labs/LegionCbmrFix) | UEFI driver: fixes `vm_page_validate_no_references` panics caused by Lenovo's firmware loading Microsoft's cbmr_driver.efi | 1.0.0 |
| [MtkWlan](https://github.com/watchthelight-labs/MtkWlan) | kext for the MediaTek MT7925 Wi-Fi card (`14C3:7925`) | 0.9.0: scan, join, WPA2-PSK (host-tested), `mtkwifi` tool, 190/175 Mb/s |
| MtkBt | firmware loader for the MT7925's Bluetooth (USB `0489:E111`) | coming |
| LegionBtFix | Lilu plugin: bluetoothd patches for the MT7925 on macOS 26.7.1 (crash loop on LE connect, silent AirPods) | coming, in testing |
| Legion-5-15IAX10-OpenCore | EFI, config.plist and install notes for this laptop | coming |

Each repo has a `docs/HOW-IT-WORKS.md` that explains the approach, and a Status table with what was actually tested. If it isn't in the table, assume it's untested.

New to OpenCore? Start with the [Dortania guide](https://dortania.github.io/OpenCore-Install-Guide/); these repos assume you already boot macOS.
