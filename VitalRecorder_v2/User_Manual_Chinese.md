# VitalRecorder 用户手册 (Chinese)

VitalRecorder 是一款适用于 Windows、Raspberry Pi 和 Ubuntu 的实时生命体征记录应用程序。它能从 80 多种医疗设备采集数据，并以 `.vital` 文件格式存储。

---

## 目录

1. [安装](#安装)
2. [快速入门](#快速入门)
3. [用户界面](#用户界面)
4. [添加设备](#添加设备)
5. [连接方式](#连接方式)
6. [端口过滤](#端口过滤)
7. [录制](#录制)
8. [服务器上传](#服务器上传)
9. [配置文件 (vr.conf)](#配置文件-vrconf)
10. [命令行选项](#命令行选项)
11. [支持的设备](#支持的设备)
12. [故障排除](#故障排除)

---

## 安装

### Windows

从 Microsoft Store 下载安装：
- Store URL: https://apps.microsoft.com/detail/9MVBQL8R0TFL

或从发布页面下载 MSI 安装程序或 MSIX 安装包。

### Raspberry Pi / Ubuntu

从发布页面下载对应平台的二进制文件（`pivr64` 或 `ubuntu64`），直接运行即可。

---

## 快速入门

1. 启动 VitalRecorder。
2. 点击 **添加设备** 按钮添加医疗设备。
3. 选择设备类型（例如：`Medtronic : BIS`、`Philips : Intellivue`）。
4. 选择连接端口（COM 端口、IP 地址或端口号）。
5. 点击 **确定**。VitalRecorder 将开始与设备通信。
6. 点击 **录制** 开始记录数据。

---

## 用户界面

VitalRecorder 采用选项卡式界面。每个选项卡代表一个"房间"或"床位"，一个选项卡可以连接多个设备。

- **轨道**：每个设备生成一个或多个轨道（例如：HR、SpO2、BIS）。轨道以波形或数值形式显示。
- **事件**：录制过程中可以添加事件标记。
- **监视器**：可配置的监视器面板以大字体显示所选参数。

### 床位名称

每个选项卡可以指定一个 **床位名称**。其用途包括：
- 上传数据到服务器时用于标识房间。
- 分离 HL7 网关设备的多床位数据。

---

## 添加设备

在 **添加设备** 中选择设备分组：

| 分组 | 示例 |
|------|------|
| VitalDB 设备 | SNUADC, SNUADCM, BUTTON, VitalBOLUS |
| 模数转换器 | DataQ DI-149, DI-155, DI-245, DI-1100, DI-1120 |
| 患者监护仪 | Philips Intellivue, GE Solar/Dash/Bx50, Nihon Kohden, Mindray HL7, MEKICS |
| 多功能监护仪 | Masimo Radical-7/Root, Sentec SDM |
| 麻醉机 | Draeger Primus/Zeus/Fabius, GE Datex-Ohmeda Aisys/Avance |
| 呼吸机 | Maquet SERVO-i/s/U, Hamilton MR1/C2/C6/T1 |
| 药物注射泵 | Fresenius Agilia/Primea/PCBM, BBraun SpaceCom/HL7, Daiwha, Pion |
| 脑监护仪 | Medtronic BIS/VISTA/INVOS, Fresenius Conox, OBELAB NirsitON |
| 肌松监测仪 | TwitchView, TOFScan, TOFcuff |
| 液体加温器 | Belmont FMS 2000 |
| 心输出量监护仪 | Edwards Hemosphere/Vigilance/EV1000/Vigileo, Getinge PulsioFlex |
| 胎儿监护仪 | GE Corometrics 250cx |

---

## 连接方式

### RS-232（串口 / COM 端口）

大多数设备通过物理 COM 端口或 USB-to-Serial 适配器进行 RS-232 串口通信。

- 选择 COM 端口号（例如：`COM3`）。
- 波特率和其他串口参数会根据设备类型自动配置。
- 连接前请先安装 USB-to-Serial 驱动程序。

### TCP（网络）

用于网络连接的设备。VitalRecorder 可以作为 TCP **客户端**或**服务器**。

- **客户端模式**：输入设备的 IP 地址和端口，格式为 `IP:PORT`（例如：`192.168.1.100:9001`）。
- **服务器模式**：仅输入端口号（例如：`2575`）。VitalRecorder 监听并等待设备连接。

HL7 设备（Mindray HL7、Nihon Kohden HL7GW、BBraun HL7）通常使用带有 MLLP 帧封装的服务器模式。

### UDP（网络）

部分设备通过 UDP 广播数据。

- 输入要监听的端口号。

### BLE (Bluetooth Low Energy)

用于 Movesense 等无线传感器。

- 需要 Windows 10 及以上系统，并配备 Bluetooth 4.0 适配器。
- 设备必须处于配对模式。

---

## 端口过滤

连接 TCP/UDP 设备时，可以在端口字符串中添加过滤器，以选择性地接受连接或消息。仅在基于分隔符的帧通信（如 HL7）中有效。

### 格式

```
PORT#KEYWORD@IP_ADDRESS
```

除端口外，所有部分均为可选。

### 关键字过滤（`#`）

通过在消息内容中搜索关键字字符串进行过滤。不包含该关键字的消息将被静默丢弃。

```
2575#BED-001
```

在端口 2575 上监听，仅处理包含 `BED-001` 的消息。当单个 HL7 网关（例如 DoseLink、Mindray Gateway）通过一个连接发送多个床位的数据时非常有用。

#### 多关键字

- **AND 条件**：关键字之间用空格分隔，仅处理包含所有关键字的消息。
  ```
  2575#BED-001 Propofol
  ```
- **OR 条件**：使用多个 `#`，处理包含任一关键字的消息。
  ```
  2575#BED-001#BED-002
  ```

### IP 过滤（`@`）

按源 IP 地址过滤传入的 TCP 连接。来自其他 IP 地址的连接将在 TCP accept 阶段被拒绝。IP 过滤仅在 UDP 和 TCP 服务器模式下有效。

```
2575@192.168.100.22
```

在端口 2575 上监听，仅接受来自 `192.168.100.22` 的连接。

#### 后缀匹配

支持以点（`.`）为分隔符的后缀匹配。无需输入完整 IP 地址，只需指定后半部分即可。

```
2575@.100.22
```

此设置允许来自 `xxx.xxx.100.22` 格式的所有 IP 的连接。

### 组合使用

```
2575#BED-001@192.168.100.22
```

在端口 2575 上监听，仅接受来自 `192.168.100.22` 的连接，且仅处理包含 `BED-001` 的消息。

### 使用场景

- **BBraun DoseLink**：当 DoseLink 的 Endpoint Filtering 启用时，使用 `#` 按泵序列号或床位标识符进行过滤。
- **Mindray HL7 Gateway**：共享同一网关端口的多个床位可通过床位名称关键字进行分离。
- **多台 DoseLink 服务器**：使用 `@` 区分哪台 DoseLink 服务器连接到哪个 VitalRecorder 选项卡。

### 多床位 HL7 网关路由

当单个 HL7 网关（Mindray eGateway、BBraun DoseLink、Nihon Kohden HL7GW）通过一条 TCP 连接传送多个床位的数据时，VitalRecorder 会自动将每帧数据路由到正确的选项卡：

1. **只有一个选项卡绑定** TCP 端口（主选项卡），使用同一端口和同一设备类型的其他选项卡会自动成为被动订阅者。这从根本上消除了之前重启时需要手动点击 "Add device" 的 Windows `SO_REUSEADDR` 竞争问题。

2. **基于床位名称的路由（推荐，优先级高于关键字过滤）** — 将每个选项卡的床位名称设置为与网关发送的**任一**标识符完全一致，无需端口过滤设置：
   - **Mindray**：`PV1-3` 床位 ID（例如 `SU-1`、`BED-001`）
   - **Nihon Kohden**：`deviceId` JSON 字段或 12 字节 MFER 前缀
   - **BBraun**：`MDC_ATTR_LOCATION` OBX 中 `~` 分隔的**任一**非空令牌（例如 `Forskning`、`Bord4`、`Anilab`、`Operasjon`）

   如果同一帧可匹配多个选项卡（例如同时存在 `Forskning` 和 `Bord4` 选项卡，帧的 LOCATION 为 `Forskning~Operasjon~Bord4~Anilab~~~~~Bord4`），**更具体的令牌优先**。令牌按倒序检测，因此 `Bord4`（LOCATION 末尾的显示短名）优先于 `Forskning`（前面的部门名）。同一帧只会被一个选项卡接收。

3. **关键字过滤路由（备用）** — 当床位名称无法直接匹配网关标识符时，使用上述 `端口#关键字` 语法。仅在床位名称路由未命中时生效。

4. **自动创建选项卡** — 若没有选项卡匹配且帧中含床位标识符，则以**最具体的令牌**（最后一个非空）自动新建选项卡，以防止初始配置不全时的数据丢失。

5. **重启自动恢复** — 重启 VitalRecorder 后约 15 秒内，所有选项卡自动重新建立主/订阅者关系，无需手动点击 "Add device" 或 "Recording"。

对于 BBraun DoseLink，一个 HL7 帧代表一个 rack（即一个床位）；rack 内的多个泵以 VMD 块形式包含在帧中，并被记录到同一选项卡的不同轨道（PUMP1 … PUMP16）。

> **1.18.23 非英文 Windows 用户提示** — 旧版本在 `,` 作为小数点分隔符的地区（挪威语、德语、法语等）的 Windows 上，低于 1.0 mL/h 的注射速度会被记录为 0（C 运行时问题）。1.18.23 起强制数字解析始终使用 `.` 作为小数点分隔符，不受 Windows 区域设置影响。BBraun 每台设备的泵数量上限也从 8 提升至 16。

### 帧转发

当接收到与关键字过滤不匹配的消息时，VitalRecorder 会自动将其转发给在同一端口上监听的其他选项卡的设备。如果没有匹配的选项卡，且消息中包含床位标识符（例如 HL7 PV1 段），则会自动创建以该床位名称命名的新选项卡。

---

## 录制

### 自动录制

默认情况下，VitalRecorder 启动时自动开始录制（`RECORD_WHEN_START` 设置）。

### 文件格式

录制内容保存为 `.vital` 文件，这是一种基于轨道的压缩二进制格式。

### 保存目录

在设置中配置保存目录。默认为用户的"文档"文件夹。

### 文件名模板

文件名由模板生成。默认值：`%r_%y%m%d_%h%i%s`

| 代码 | 含义 |
|------|------|
| `%r` | 房间/床位名称 |
| `%y` | 年（4 位） |
| `%m` | 月（2 位） |
| `%d` | 日（2 位） |
| `%h` | 时（2 位） |
| `%i` | 分（2 位） |
| `%s` | 秒（2 位） |

---

## 服务器上传

VitalRecorder 可通过 WebSocket 实时上传数据到 VitalServer 实例。

### 设置

| 设置项 | 说明 |
|--------|------|
| `SERVER_IP` | VitalServer IP 地址或主机名 |
| `SEND_WEB` | 启用/禁用服务器上传（`1` 或 `0`） |
| `CLOUD_UPLOAD` | 启用/禁用云端上传（`1` 或 `0`） |
| `VRCODE` | 此 VitalRecorder 实例的唯一标识符 |

### 上传内容

- VitalRecorder 实例的 **版本、操作系统、架构**。
- **配置** 和 **支持的设备类型列表**（启动后首次成功上传时发送一次）。
- **房间数据**：每个选项卡的床位名称、设备列表、轨道值和波形。

数据在上传前使用 zlib 压缩。

### HL7 模式

当 `HL7` 设置启用时，VitalRecorder 以 HL7 格式而非 JSON 格式发送房间数据。

---

## 配置文件 (vr.conf)

VitalRecorder 将所有设置存储在名为 `vr.conf` 的单一配置文件中。该文件使用类似 INI 的格式，可手动编辑以用于无头部署或批量配置。

### 文件位置

| 平台 | 路径 |
|------|------|
| Windows | `%APPDATA%\VitalRecorder\vr.conf` |
| Linux | `./vr.conf` > `~/vr.conf` > `/boot/vr.conf`（按顺序搜索） |

- 编码：UTF-8
- 使用 `--conf <path>` 指定替代配置文件。

### 文件结构

```ini
# 全局设置（在任何节之前）
KEY=VALUE

# 床位（选项卡）定义
[BED/bedname]

# 此床位下的设备
[DEV/devicename]
type=DeviceType
port=PortSpec

# 此床位下的过滤器
[FILT/filter_module_name]
```

**规则：**
- 每行一个 `KEY=VALUE` 键值对。
- 节标题以 `[` 开头。
- 空行将被忽略。
- `[DEV/...]` 和 `[FILT/...]` 节属于其前面的 `[BED/...]`。
- 一个 `[BED/...]` 可以包含多个设备和过滤器。

### 全局设置

#### 常规

| 键 | 默认值 | 说明 |
|----|--------|------|
| `SAVEDIR` | （系统默认） | 录制文件保存目录 |
| `VRCODE` | （自动生成） | VitalRecorder 唯一识别码 |
| `FILENAME_TEMPLATE` | `%r_%y%m%d_%h%i%s` | 录制文件名模板 |

#### 录制

| 键 | 默认值 | 说明 |
|----|--------|------|
| `RECORD_WHEN_START` | 1 | 启动时自动录制（0：关闭，1：开启） |
| `CUT_FILE` | 1 | 在患者边界处分割文件（0：关闭，1：开启） |
| `CUT_HOURLY` | 0 | 每小时分割文件（0：关闭，1：开启） |
| `CUT_BY` | （无） | 文件分割触发信号（例如：`spo2`、`hr`、`any`） |
| `PT_WAITING_TIME` | 5 | 患者等待时间（分钟） |

#### 服务器

| 键 | 默认值 | 说明 |
|----|--------|------|
| `SERVER_IP` | （无） | VitalDB 服务器地址（IP:port） |
| `UPLOAD_SERVER_IP` | （无） | 文件上传服务器地址 |
| `MONITOR_SERVER_IP` | （无） | Web 监控服务器地址 |
| `SEND_WEB` | 1 | 向 Web 服务器发送数据（0：关闭，1：开启） |
| `CLOUD_UPLOAD` | 0 | 启用云端上传（0：关闭，1：开启） |

#### 窗口

| 键 | 默认值 | 说明 |
|----|--------|------|
| `START_MAXIMIZED` | 1 | 以最大化窗口启动 |
| `START_MINIMIZED` | 0 | 以最小化窗口启动 |
| `OPTION_MIN_TO_TRAY` | 0 | 最小化到系统托盘 |
| `OPTION_ALWAYS_ON_TOP` | 0 | 窗口始终置顶 |
| `PLAY_SOUND` | 1 | 播放报警声音 |

#### 事件预设

可通过 `EVT_TEXT_0` 至 `EVT_TEXT_29` 定义最多 30 个事件预设标签。

```ini
EVT_TEXT_0=Induction
EVT_TEXT_1=Intubation
EVT_TEXT_2=Incision
```

### 床位节

定义一个床位（选项卡）。一个配置文件中可以定义多个床位。

```ini
[BED/OR1]
```

- 床位名称位于 `BED/` 之后（例如：`OR1`、`ICU_BED3`）。
- 如果省略，将从 VRCODE 或 PC 主机名自动生成。

### 设备节

设备添加在 `[BED/...]` 节下。

```ini
[DEV/devicename]
type=DeviceType
port=PortSpec
```

| 键 | 必填 | 说明 |
|----|------|------|
| `type` | 是 | 设备类型（例如：`BIS`、`Intellivue`、`Solar8000`） |
| `port` | 是 | 连接端口（参见下方端口格式） |
| `company` | 否 | 制造商（例如：`Nihon Kohden`） |
| `readonly` | 否 | 只读模式（0：关闭，1：开启） |

#### 端口格式

| 格式 | 示例 | 说明 |
|------|------|------|
| COM 端口 | `COM1`、`COM3` | Windows 串口 |
| TCP/IP | `192.168.1.100:4343` | 网络设备（IP:port） |
| 端口号 | `4343` | TCP 服务器模式（localhost） |
| RPi 串口 | `F1`-`F4` | Raspberry Pi AMA 端口 |
| RPi USB | `LU`、`LU1`-`LU4` | USB 左上 |
| RPi USB | `RU`、`RU1`-`RU4` | USB 右上 |

#### 配置文件中的端口过滤

端口值支持关键字和 IP 过滤（语法与[端口过滤](#端口过滤)相同）：

```
port=PORT#keyword1 keyword2#keyword3@IP_SUFFIX
```

#### ADC 设备设置

ADC（模数转换器）设备有额外的通道级设置：

| 键 | 说明 |
|----|------|
| `srate` | 采样率（Hz） |
| `parname1`、`parname2`、... | 各通道的参数名称 |
| `gain1`、`gain2`、... | 各通道的电压到物理单位转换增益 |

```ini
[DEV/SNUADC]
type=SNUADC
port=COM3
srate=500
parname1=ECG
gain1=1.0
parname2=ART
gain2=100.0
```

### 过滤器节

添加实时信号处理过滤器。过滤器定义从过滤器服务器加载。

```ini
[FILT/filter_module_name]
```

- 模块名称必须与服务器上注册的过滤器的 `modname` 一致。
- 无需额外设置（过滤器参数由服务器提供）。

### 配置示例

#### 单个患者监护仪

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1
```

#### 多个设备

```ini
SAVEDIR=D:\VitalData
VRCODE=OR1_PC

[BED/OR1]

[DEV/Intellivue]
type=Intellivue
port=192.168.1.100:4343

[DEV/BIS]
type=BIS
port=COM3

[DEV/Primus]
type=Primus
port=COM4
```

#### 多个床位

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[BED/OR2]

[DEV/Philips]
type=Intellivue
port=192.168.1.101:4343
```

#### 调试 / 测试

```ini
SAVEDIR=C:\Users\lucid\Desktop

[BED/test]

[DEV/NK EGA]
type=EGA
company=Nihon Kohden
port=9001
```

#### 包含过滤器

```ini
[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[FILT/pleth_spi]
```

---

## 命令行选项

```
vital.exe [options] [filename]
```

| 选项 | 说明 |
|------|------|
| `--version`、`-v` | 显示版本号 |
| `--devtypes`、`-d` | 列出所有支持的设备类型 |
| `--console`、`-c` | 以控制台模式运行（无 GUI） |
| `--debug [conf]` | 以调试模式运行（包含控制台模式，可选择指定配置文件） |
| `--conf <path>` | 指定配置文件路径 |
| `--upgrade`、`-u` | 升级到最新版本 |
| `-u1.18.0` | 升级到指定版本 |
| `--help`、`-h` | 显示帮助信息 |
| `filename.vital` | 打开 `.vital` 文件进行回放 |

### 控制台模式

控制台模式（`--console` 或 `-c`）在无 GUI 的情况下运行 VitalRecorder。适用于 Raspberry Pi 或 Ubuntu 服务器的无头部署。设备从已保存的配置中加载。

### 调试模式

调试模式（`--debug`）包含控制台模式，并将设备打开/关闭、帧转发等详细日志输出到标准输出。在调试模式下不会生成实际的 `.vital` 文件。

```bash
# 使用默认配置运行调试模式
vital.exe --debug

# 使用指定配置文件运行调试模式
vital.exe --debug test_mindray.conf
```

---

## 支持的设备

有关支持设备的完整列表、连接详情和参数，请参阅 [Supported Devices](../VitalRecorder/Supported_Devices.md)。

### 常用设备速查

| 设备 | 连接方式 | 端口设置 |
|------|----------|----------|
| Philips Intellivue | RS-232 | COM 端口，115200 baud |
| GE Solar 8000 | RS-232 | COM 端口，9600 baud |
| Nihon Kohden（串口） | RS-232 | COM 端口，9600 baud |
| Nihon Kohden (HL7GW) | TCP 服务器 | 端口 9001 |
| Nihon Kohden (EGA) | UDP | 端口号 |
| Mindray (HL7) | TCP 服务器 | 端口 10000 |
| Draeger (Medibus) | RS-232 | COM 端口，9600 baud (8N2) |
| GE Datex-Ohmeda | RS-232 | COM 端口，19200 baud (7E1) |
| Medtronic BIS | RS-232 | COM 端口，57600 baud |
| BBraun SpaceCom | RS-232 | COM 端口，9600 baud |
| BBraun HL7 (DoseLink) | TCP 服务器 | 端口 2575 |
| Masimo Radical-7 | RS-232 | COM 端口，9600 baud |
| Edwards Hemosphere | RS-232 | COM 端口，9600 baud |
| Hamilton 呼吸机 | RS-232 | COM 端口，38400 baud |

---

## 故障排除

### 设备无法连接

1. **RS-232**：确认选择了正确的 COM 端口。在设备管理器中查看端口号。确认已安装 USB-to-Serial 驱动程序。
2. **TCP 服务器模式**：检查防火墙是否允许指定端口的传入连接。
3. **TCP 客户端模式**：确认设备 IP 地址可达（使用 `ping` 测试）。

### 无数据显示

- 部分设备需要在设备端进行特定配置（例如：在 Draeger 服务菜单中启用 RS-232 输出、在 Philips Intellivue 上激活 MIB 输出）。
- 检查波特率和串口参数是否与设备设置匹配。
- 使用 `--debug` 模式确认通信状态。

### 同一端口上的多个设备

对于共享单个网关端口的 HL7 设备，使用[端口过滤](#端口过滤)功能中的 `#` 关键字来分离床位。

### BBraun HL7 多泵

BBraun DoseLink 通过单个 TCP 连接发送多个泵的数据。VitalRecorder 使用 OBX-18（设备实例标识符）中的序列号自动识别每个泵，并将其映射到 PUMP1 至 PUMP8。

如果泵未被正确分离：
- 使用 `--debug` 模式查看日志。
- 检查原始 HL7 消息中的 OBX-18 值。
- 使用 DoseLink Endpoint Filtering 时，如有需要请使用 `#` 关键字过滤。

### 服务器上传不工作

- 确认 `SERVER_IP` 设置正确。
- 检查 `SEND_WEB` 是否设置为 `1`。
- 确认与服务器的网络连接正常。
- 配置和设备类型列表在启动后首次成功上传时发送。如果 VitalRecorder 在没有活动设备的情况下启动，初始上传可能会延迟到有设备连接时进行。
