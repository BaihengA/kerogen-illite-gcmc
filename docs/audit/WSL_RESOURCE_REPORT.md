# WSL Resource Report

generated_at: 2026-07-07T11:17:38.784727+00:00

```text
32
MemTotal:       16273420 kB
MemAvailable:   15530552 kB
SwapTotal:       4194304 kB
SwapFree:        4194304 kB
[    0.049633] Spectre V2 : Mitigation: Enhanced / Automatic IBRS
[    0.049634] Spectre V2 : Spectre v2 / PBRSB-eIBRS: Retire a single CALL on VMEXIT
[    0.049634] RETBleed: Mitigation: Enhanced IBRS
[    0.049635] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
[    0.049635] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl
[    0.049636] Register File Data Sampling: Mitigation: Clear Register File
[    0.049643] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
[    0.049644] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
[    0.049645] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
[    0.049645] x86/fpu: Supporting XSAVE feature 0x800: 'Control-flow User registers'
[    0.049645] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
[    0.049646] x86/fpu: xstate_offset[11]:  832, xstate_sizes[11]:   16
[    0.049646] x86/fpu: Enabled xstate features 0x807, context size is 848 bytes, using 'compacted' format.
[    0.053573] Freeing SMP alternatives memory: 44K
[    0.053573] pid_max: default: 32768 minimum: 301
[    0.053573] LSM: initializing lsm=capability,landlock,yama,safesetid,selinux,integrity
[    0.053573] landlock: Up and running.
[    0.053573] Yama: becoming mindful.
[    0.053573] SELinux:  Initializing.
[    0.053573] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.053573] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
[    0.053573] smpboot: CPU0: Intel(R) Core(TM) i9-14900KF (family: 0x6, model: 0xb7, stepping: 0x1)
[    0.053573] RCU Tasks: Setting shift to 5 and lim to 1 rcu_task_cb_adjust=1 rcu_task_cpu_ids=32.
[    0.053573] RCU Tasks Rude: Setting shift to 5 and lim to 1 rcu_task_cb_adjust=1 rcu_task_cpu_ids=32.
[    0.053573] RCU Tasks Trace: Setting shift to 5 and lim to 1 rcu_task_cb_adjust=1 rcu_task_cpu_ids=32.
[    0.053573] Performance Events: unsupported p6 CPU model 183 no PMU driver, software events only.
[    0.053573] signal: max sigframe size: 1776
[    0.053573] rcu: Hierarchical SRCU implementation.
[    0.053573] rcu: 	Max phase no-delay instances is 1000.
[    0.053573] NMI watchdog: Perf NMI watchdog permanently disabled
[    0.053573] smp: Bringing up secondary CPUs ...
[    0.053573] smpboot: x86: Booting SMP configuration:
[    0.053573] .... node  #0, CPUs:        #2  #4  #6  #8 #10 #12 #14 #16 #18 #20 #22 #24 #26 #28 #30  #1  #3  #5  #7  #9 #11 #13 #15 #17 #19 #21 #23 #25 #27 #29 #31
[    0.061830] smp: Brought up 1 node, 32 CPUs
[    0.061832] smpboot: Max logical packages: 1
[    0.061833] smpboot: Total of 32 processors activated (203980.80 BogoMIPS)
[    0.074783] node 0 deferred pages initialised in 8ms
[    0.075904] devtmpfs: initialized
[    0.075904] x86/mm: Memory block size: 128MB
[    0.075904] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.077606] futex hash table entries: 8192 (order: 7, 524288 bytes, linear)
[    0.077686] pinctrl core: initialized pinctrl subsystem
[    0.078699] NET: Registered PF_NETLINK/PF_ROUTE protocol family
[    0.079434] DMA: preallocated 2048 KiB GFP_KERNEL pool for atomic allocations
[    0.080107] DMA: preallocated 2048 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.080138] audit: initializing netlink subsys (disabled)
[    0.080161] audit: type=2000 audit(1783423056.028:1): state=initialized audit_enabled=0 res=1
[    0.080161] thermal_sys: Registered thermal governor 'step_wise'
[    0.080161] thermal_sys: Registered thermal governor 'user_space'
[    0.080161] cpuidle: using governor ladder
[    0.080161] cpuidle: using governor menu
[    0.080161] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
[    0.080161] dca service started, version 1.12.1
[    0.080161] PCI: Fatal: No config space access function found
[    0.080161] kprobes: kprobe jump-optimization is enabled. All kprobes are optimized if possible.
[    0.080161] HugeTLB: registered 1.00 GiB page size, pre-allocated 0 pages
[    0.080161] HugeTLB: 16380 KiB vmemmap can be freed for a 1.00 GiB page
[    0.080161] HugeTLB: registered 2.00 MiB page size, pre-allocated 0 pages
[    0.080161] HugeTLB: 28 KiB vmemmap can be freed for a 2.00 MiB page
[    0.081581] cryptd: max_cpu_qlen set to 1000
[    0.081660] ACPI: Added _OSI(Module Device)
[    0.081661] ACPI: Added _OSI(Processor Device)
[    0.081661] ACPI: Added _OSI(Processor Aggregator Device)
[    0.083601] ACPI: 1 ACPI AML tables successfully acquired and loaded
[    0.083916] ACPI: _OSC evaluation for CPUs failed, trying _PDC
[    0.084013] ACPI: Interpreter enabled
[    0.084015] ACPI: PM: (supports S0 S5)
[    0.084016] ACPI: Using IOAPIC for interrupt routing
[    0.084020] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
[    0.084021] PCI: Using E820 reservations for host bridge windows
[    0.084102] ACPI: Enabled 1 GPEs in block 00 to 0F
[    0.084831] iommu: Default domain type: Translated
[    0.084831] iommu: DMA domain TLB invalidation policy: lazy mode
[    0.084831] SCSI subsystem initialized
[    0.084831] libata version 3.00 loaded.
[    0.084831] pps_core: LinuxPPS API ver. 1 registered
[    0.084831] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.084831] PTP clock support registered
[    0.084831] EDAC MC: Ver: 3.0.0
[    0.097621] hv_vmbus: Vmbus version:5.3
[    0.097676] hv_vmbus: Unknown GUID: 6e382d18-3336-4f4b-acc4-2b7703d4df4a
[    0.097685] hv_vmbus: Unknown GUID: dde9cbc0-5060-4436-9448-ea1254a5d177
[    0.098032] NetLabel: Initializing
[    0.098033] NetLabel:  domain hash size = 128
[    0.098033] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
[    0.098040] NetLabel:  unlabeled traffic allowed by default
[    0.098040] PCI: Using ACPI for IRQ routing
[    0.098041] PCI: System does not support PCI
[    0.098056] vgaarb: loaded
[    0.098251] clocksource: Switched to clocksource tsc-early
[    0.098251] VFS: Disk quotas dquot_6.6.0
[    0.098251] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.098251] FS-Cache: Loaded
[    0.098251] pnp: PnP ACPI init
[    0.098251] pnp: PnP ACPI: found 1 devices
[    0.104875] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
[    0.104906] NET: Registered PF_INET protocol family
[    0.105331] IP idents hash table entries: 262144 (order: 9, 2097152 bytes, linear)
[    0.106518] tcp_listen_portaddr_hash hash table entries: 8192 (order: 5, 131072 bytes, linear)
[    0.106570] Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
[    0.106777] TCP established hash table entries: 131072 (order: 8, 1048576 bytes, linear)
[    0.107225] TCP bind hash table entries: 65536 (order: 9, 2097152 bytes, linear)
[    0.107297] TCP: Hash tables configured (established 131072 bind 65536)
[    0.107409] UDP hash table entries: 8192 (order: 6, 262144 bytes, linear)
[    0.107468] UDP-Lite hash table entries: 8192 (order: 6, 262144 bytes, linear)
[    0.107539] NET: Registered PF_UNIX/PF_LOCAL protocol family
[    0.107542] NET: Registered PF_XDP protocol family
[    0.107545] PCI: CLS 0 bytes, default 64
[    0.107559] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
[    0.107559] software IO TLB: mapped [mem 0x00000000f4000000-0x00000000f8000000] (64MB)
[    0.107618] Trying to unpack rootfs image as initramfs...
[    0.109238] Freeing initrd memory: 2772K
[    0.109769] RAPL PMU: API unit is 2^-32 Joules, 0 fixed counters, 10737418240 ms ovfl timer
[    0.109778] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x2df10e7656b, max_idle_ns: 440795364873 ns
[    0.110459] clocksource: Switched to clocksource tsc
[    0.111526] Initialise system trusted keyrings
[    0.111531] Key type blacklist registered
[    0.111639] workingset: timestamp_bits=36 max_order=22 bucket_order=0
[    0.111874] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.111881] fuse: init (API version 7.39)
[    0.111966] SGI XFS with ACLs, security attributes, realtime, verbose warnings, quota, no debug enabled
[    0.112197] 9p: Installing v9fs 9p2000 file system support
[    0.116488] Key type asymmetric registered
[    0.116490] Asymmetric key parser 'x509' registered
[    0.116505] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 245)
[    0.116600] io scheduler mq-deadline registered
[    0.116601] io scheduler kyber registered
[    0.118836] hv_vmbus: registering driver hv_pci
[    0.119029] hv_pci c4b741f5-5582-4c98-8f8b-2e082933c396: PCI VMBus probing: Using version 0x10004
[    0.119367] hv_pci c4b741f5-5582-4c98-8f8b-2e082933c396: PCI host bridge to bus 5582:00
[    0.119368] pci_bus 5582:00: root bus resource [mem 0x9ffe00000-0x9ffe02fff window]
[    0.119369] pci_bus 5582:00: No busn resource found for root bus, will use [bus 00-ff]
[    0.119637] pci 5582:00:00.0: [1af4:1043] type 00 class 0x010000
[    0.119879] pci 5582:00:00.0: reg 0x10: [mem 0x9ffe00000-0x9ffe00fff 64bit]
[    0.120018] pci 5582:00:00.0: reg 0x18: [mem 0x9ffe01000-0x9ffe01fff 64bit]
[    0.120157] pci 5582:00:00.0: reg 0x20: [mem 0x9ffe02000-0x9ffe02fff 64bit]
[    0.121125] pci_bus 5582:00: busn_res: [bus 00-ff] end is updated to 00
[    0.121128] pci 5582:00:00.0: BAR 0: assigned [mem 0x9ffe00000-0x9ffe00fff 64bit]
[    0.121239] pci 5582:00:00.0: BAR 2: assigned [mem 0x9ffe01000-0x9ffe01fff 64bit]
[    0.121349] pci 5582:00:00.0: BAR 4: assigned [mem 0x9ffe02000-0x9ffe02fff 64bit]
[    0.121669] hv_pci 74205353-7324-4df8-ad45-4c350951ceb8: PCI VMBus probing: Using version 0x10004
[    0.121897] hv_pci 74205353-7324-4df8-ad45-4c350951ceb8: PCI host bridge to bus 7324:00
[    0.121898] pci_bus 7324:00: No busn resource found for root bus, will use [bus 00-ff]
[    0.122022] pci 7324:00:00.0: [1414:008e] type 00 class 0x030200
[    0.123468] pci_bus 7324:00: busn_res: [bus 00-ff] end is updated to 00
[    0.123959] ioatdma: Intel(R) QuickData Technology Driver 5.00
[    0.124010] virtio-pci 5582:00:00.0: enabling device (0000 -> 0002)
[    0.125297] Serial: 8250/16550 driver, 8 ports, IRQ sharing enabled
[    0.144482] Linux agpgart interface v0.103
[    0.144499] AMD-Vi: AMD IOMMUv2 functionality not available on this system - This is not a bug.
[    0.144506] ACPI: bus type drm_connector registered
[    0.145284] printk: console [hvc0] enabled
[    0.148403] brd: module loaded
[    0.149922] loop: module loaded
[    0.150063] Loading iSCSI transport class v2.0-870.
[    0.150279] rdac: device handler registered
[    0.150426] Microchip SmartPQI Driver (v2.1.24-046)
[    0.150564] VMware PVSCSI driver - version 1.0.7.0-k
[    0.150690] hv_vmbus: registering driver hv_storvsc
[    0.151267] PPP generic driver version 2.4.2
[    0.151432] VMware vmxnet3 virtual NIC driver - version 1.7.0.0-k-NAPI
[    0.151602] scsi host0: storvsc_host_t
[    0.151653] hv_vmbus: registering driver hv_netvsc
[    0.151929] Fusion MPT base driver 3.04.20
[    0.152032] Copyright (c) 1999-2008 LSI Corporation
[    0.152159] Fusion MPT SPI Host driver 3.04.20
[    0.152272] Fusion MPT SAS Host driver 3.04.20
[    0.152403] Fusion MPT misc device (ioctl) driver 3.04.20
[    0.152573] mptctl: Registered with Fusion MPT base driver
[    0.152684] mptctl: /dev/mptctl @ (major,minor=10,220)
[    0.152850] i8042: PNP: No PS/2 controller found.
[    0.152971] hv_vmbus: registering driver hyperv_keyboard
[    0.153117] rtc_cmos 00:00: RTC can wake from S4
[    0.154074] rtc_cmos 00:00: registered as rtc0
[    0.154440] rtc_cmos 00:00: setting system clock to 2026-07-07T11:17:36 UTC (1783423056)
[    0.154829] rtc_cmos 00:00: alarms up to one month, 114 bytes nvram
[    0.154993] device-mapper: core: CONFIG_IMA_DISABLE_HTABLE is disabled. Duplicate IMA measurements will not be recorded in the IMA log.
[    0.155225] device-mapper: uevent: version 1.0.3
[    0.155456] device-mapper: ioctl: 4.48.0-ioctl (2023-03-01) initialised: dm-devel@redhat.com
[    0.155804] intel_pstate: CPU model not supported
[    0.156028] hv_utils: Registering HyperV Utility Driver
[    0.156153] hv_vmbus: registering driver hv_utils
[    0.156279] hv_vmbus: registering driver hv_balloon
[    0.156455] hv_vmbus: registering driver dxgkrnl
[    0.156529] hv_utils: TimeSync IC version 4.0
[    0.156856] hv_balloon: Using Dynamic Memory protocol version 2.0
[    0.157478] Free page reporting enabled
[    0.157594] hv_balloon: Cold memory discard hint enabled with order 9
[    0.158139] drop_monitor: Initializing network drop monitor service
[    0.168620] NET: Registered PF_INET6 protocol family
[    0.169094] Segment Routing with IPv6
[    0.169201] In-situ OAM (IOAM) with IPv6
[    0.169282] NET: Registered PF_PACKET protocol family
[    0.169480] 9pnet: Installing 9P2000 support
[    0.169682] NET: Registered PF_VSOCK protocol family
[    0.169812] hv_vmbus: registering driver hv_sock
[    0.174784] IPI shorthand broadcast: enabled
[    0.174962] AVX2 version of gcm_enc/dec engaged.
[    0.176222] AES CTR mode by8 optimization enabled
[    0.176640] scsi 0:0:0:0: Direct-Access     Msft     Virtual Disk     1.0  PQ: 0 ANSI: 5
[    0.177283] sched_clock: Marking stable (173110824, 1644147)->(187635022, -12880051)
[    0.177992] registered taskstats version 1
[    0.178032] scsi 0:0:0:1: Direct-Access     Msft     Virtual Disk     1.0  PQ: 0 ANSI: 5
[    0.178264] Loading compiled-in X.509 certificates
[    0.179619] ima: No TPM chip found, activating TPM-bypass!
[    0.179904] ima: Allocated hash algorithm: sha256
[    0.180199] ima: No architecture policies found
[    0.181299] sd 0:0:0:0: Attached scsi generic sg0 type 0
[    0.181401] sd 0:0:0:0: [sda] 747064 512-byte logical blocks: (382 MB/365 MiB)
[    0.181512] sd 0:0:0:1: Attached scsi generic sg1 type 0
[    0.181602] sd 0:0:0:1: [sdb] 295872 512-byte logical blocks: (151 MB/144 MiB)
[    0.181643] sd 0:0:0:1: [sdb] Write Protect is on
[    0.181770] sd 0:0:0:0: [sda] Write Protect is on
[    0.181943] sd 0:0:0:1: [sdb] Mode Sense: 0f 00 80 00
[    0.182044] sd 0:0:0:0: [sda] Mode Sense: 0f 00 80 00
[    0.182263] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[    0.182476] sd 0:0:0:1: [sdb] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[    0.183468] sd 0:0:0:0: [sda] Attached SCSI disk
[    0.183677] sd 0:0:0:1: [sdb] Attached SCSI disk
[    0.215738] RAS: Correctable Errors collector initialized.
[    0.215946] clk: Disabling unused clocks
[    0.219675] Freeing unused decrypted memory: 2028K
[    0.220325] Freeing unused kernel image (initmem) memory: 4480K
[    0.220495] Write protecting the kernel read-only data: 34816k
[    0.221180] Freeing unused kernel image (rodata/data gap) memory: 740K
[    0.221355] Run /init as init process
[    0.221426]   with arguments:
[    0.221501]     /init
[    0.221552]   with environment:
[    0.221632]     HOME=/
[    0.221739]     TERM=linux
[    0.221787]     WSL_ROOT_INIT=1
[    0.221849]     WSL_ENABLE_CRASH_DUMP=1
[    0.222128] WSL (1 - ): WSL version 2.7.3.0
[    0.239723] scsi 0:0:0:2: Direct-Access     Msft     Virtual Disk     1.0  PQ: 0 ANSI: 5
[    0.242745] sd 0:0:0:2: Attached scsi generic sg2 type 0
[    0.242832] sd 0:0:0:2: [sdc] 8388616 512-byte logical blocks: (4.29 GB/4.00 GiB)
[    0.243063] sd 0:0:0:2: [sdc] 4096-byte physical blocks
[    0.243226] sd 0:0:0:2: [sdc] Write Protect is off
[    0.243328] sd 0:0:0:2: [sdc] Mode Sense: 0f 00 00 00
[    0.243507] sd 0:0:0:2: [sdc] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    0.245321] sd 0:0:0:2: [sdc] Attached SCSI disk
[    0.274515] EXT4-fs (sda): mounted filesystem 00000000-0000-0000-0000-000000000000 ro without journal. Quota mode: none.
[    0.276052] EXT4-fs (sdb): mounted filesystem 00000000-0000-0000-0000-000000000000 ro without journal. Quota mode: none.
[    0.286808] tun: Universal TUN/TAP device driver, 1.6
[    0.305794] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[    0.307189] Bridge firewalling registered
[    0.307689] Adding 4194304k swap on /dev/sdc.  Priority:-2 extents:1 across:4194304k 
[    0.559343] hv_pci b7c981f1-2faf-4c3a-bdc0-c0f30f47bea8: PCI VMBus probing: Using version 0x10004
[    0.560041] hv_pci b7c981f1-2faf-4c3a-bdc0-c0f30f47bea8: PCI host bridge to bus 2faf:00
[    0.560234] pci_bus 2faf:00: root bus resource [mem 0xc00000000-0xe00001fff window]
[    0.560374] pci_bus 2faf:00: No busn resource found for root bus, will use [bus 00-ff]
[    0.561762] pci 2faf:00:00.0: [1af4:105a] type 00 class 0x088000
[    0.562391] pci 2faf:00:00.0: reg 0x10: [mem 0xe00000000-0xe00000fff 64bit]
[    0.562722] pci 2faf:00:00.0: reg 0x18: [mem 0xe00001000-0xe00001fff 64bit]
[    0.563026] pci 2faf:00:00.0: reg 0x20: [mem 0xc00000000-0xdffffffff 64bit]
[    0.564401] pci_bus 2faf:00: busn_res: [bus 00-ff] end is updated to 00
[    0.564559] pci 2faf:00:00.0: BAR 4: assigned [mem 0xc00000000-0xdffffffff 64bit]
[    0.564835] pci 2faf:00:00.0: BAR 0: assigned [mem 0xe00000000-0xe00000fff 64bit]
[    0.565112] pci 2faf:00:00.0: BAR 2: assigned [mem 0xe00001000-0xe00001fff 64bit]
[    0.565447] virtio-pci 2faf:00:00.0: enabling device (0000 -> 0002)
[    0.571771] virtiofs virtio1: Cache len: 0x200000000 @ 0xc00000000
[    0.664216] scsi 0:0:0:3: Direct-Access     Msft     Virtual Disk     1.0  PQ: 0 ANSI: 5
[    0.667464] sd 0:0:0:3: Attached scsi generic sg3 type 0
[    0.667523] sd 0:0:0:3: [sdd] 2147483648 512-byte logical blocks: (1.10 TB/1.00 TiB)
[    0.667773] sd 0:0:0:3: [sdd] 4096-byte physical blocks
[    0.667914] sd 0:0:0:3: [sdd] Write Protect is off
[    0.668014] sd 0:0:0:3: [sdd] Mode Sense: 0f 00 00 00
[    0.668181] sd 0:0:0:3: [sdd] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    0.669276] sd 0:0:0:3: [sdd] Attached SCSI disk
[    0.719514] EXT4-fs (sdd): mounted filesystem 5edb8e9a-ea42-4197-8114-c9a57228c71b r/w with ordered data mode. Quota mode: none.
[    0.985788] misc dxg: dxgk: dxgkio_is_feature_enabled: Ioctl failed: -22
[    0.988424] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -22
[    0.988582] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -22
[    0.988740] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -22
[    0.988969] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.107519] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.110465] systemd[375]: memfd_create() called without MFD_EXEC or MFD_NOEXEC_SEAL set
[    1.199773] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.200073] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.200314] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.200514] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.200707] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.200964] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.201193] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.201445] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.201676] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.201915] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.202133] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.202353] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.202583] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.202838] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.203073] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.203320] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.241609] misc dxg: dxgk: dxgkio_query_adapter_info: Ioctl failed: -2
[    1.297931] systemd-journald[60]: Received client request to flush runtime journal.
[    1.308383] systemd-journald[60]: File /var/log/journal/676250bf847f4105b1bc8feb55f2652a/system.journal corrupted or uncleanly shut down, renaming and replacing.
[    1.597389] kvm_intel: Using Hyper-V Enlightened VMCS
[    1.736512] intel_rapl_msr: PL4 support detected.
[    2.051619] systemd-journald[60]: File /var/log/journal/676250bf847f4105b1bc8feb55f2652a/user-1000.journal corrupted or uncleanly shut down, renaming and replacing.
w s l :   �hKm0R  l o c a l h o s t   �NtM�n�FO*g\��P0R  W S L 0N A T   !j_N�v  W S L   N/ec  l o c a l h o s t   �Nt0 
 
```

oom_evidence: NO
segfault_evidence: NO
