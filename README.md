# MidiPlayer for Minecraft

## 项目简介
MidiPlayer 是一个独立的程序，旨在为 Minecraft 中的联机玩家提供一个点歌台，让他们可以通过输入命令自由点歌。该程序是从原先的 Minecraft 控制项目 mcws 中分离出来的 MIDI 播放模块。

## 如何启动
1. 运行 `main.py` 来启动程序。
2. 在启动后，请按照提示进行操作。
3. 在 Minecraft 中输入命令：`/connect 127.0.0.1:26367`

### 支持的命令

以下是 MidiPlayer for Minecraft 支持的命令列表：

- `.midi search (-s, search) <query>`: 搜索文件
  - **参数**:
    - `<query>`: 必填，搜索查询关键词

- `.midi list (-ls, list) [page]`: 列出文件
  - **参数**:
    - `[page]`: 可选，指定要显示的页面编号

- `.midi reload (-re, reload)`: 重新加载文件列表

- `.midi list-by-id (-lsi) [id]`: 根据ID列出位于特定页的文件
  - **参数**:
    - `[id]`: 可选，指定文件的ID

- `.midi play (-p, play) <id>`: 播放文件
  - **参数**:
    - `<id>`: 必填，要播放文件的ID

- `.midi stop (-st, stop)`: 停止播放

- `.midi from-url (-u) <url>`: 从URL播放
  - **参数**:
    - `<url>`: 必填，指定要播放的音乐文件的URL

- `.midi keyboard (-k, keyboard) <0|1>`: 设置是否显示键盘
  - **参数**:
    - `<0|1>`: 必填，0表示不显示键盘，1表示显示键盘

- `.midi pan-by-pitch (-pp) <0|1>`: 设置音高是否决定声音位置
  - **参数**:
    - `<0|1>`: 必填，0表示音高不影响声音位置，1表示音高影响声音位置

- `.midi playing (-pl, playing)`: 显示正在播放的曲目

- `.midi loop (-l, loop) <song|all>`: 设置循环播放模式
  - **参数**:
    - `<song|all>`: 必填，选择 "song" 表示循环播放当前歌曲，选择 "all" 表示循环播放所有歌曲

以上是 MidiPlayer for Minecraft 支持的详细命令列表。请根据需要使用相应的命令来控制和管理 MIDI 文件的播放。祝您在 Minecraft 中享受美妙的音乐体验！

## 注意事项
- 确保在启动程序后按照提示进行操作。
- 确保在 Minecraft 中输入正确的连接命令以与程序建立连接。

通过 MidiPlayer，Minecraft 的联机玩家可以享受自由点歌的乐趣，轻松管理和播放 MIDI 文件。祝您使用愉快！