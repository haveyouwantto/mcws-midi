import sys

loading = '加载中...'
welcome = "欢迎使用mcws midi模块"
welcome_info = "这里是一个midi点歌台，可以通过输入命令来控制音乐的播放。\n" + \
    "请使用 .midi -h 查看帮助信息."


search_error = '搜索内容不能为空'
empty_result = '未找到任何结果'
page_error = '页数无效'
file_not_exists = '文件不存在'
command_error = '语法错误'
pyversion = 'Python ' + sys.version
version = ''
unknown_command = '未知命令。'
invaild_id = 'ID 无效'
exception = '发生了一个错误。详情见服务端控制台。'
fatal_exception = '发生了严重错误'

list_format = '[§c{0}§r] - {1}'
pagenum_format = '第 {0} 页，共 {1} 页'


class module:
    reload = '文件列表已重新加载'
    help = {
        '--info': '显示信息    \u00a7c--info',
        '--help': '提供帮助/命令列表    \u00a7c--help',
        '--reload': '重新加载文件列表    \u00a7c--reload',
        '--list': '列出文件    \u00a7c--list [页码]',
        '--list-by-id':'根据文件id列出页面    \u00a7c--list-by-id [id]',
        '--search': '搜索文件    \u00a7c--search <内容>',
        '--list-config':'显示当前模块的配置信息    \u00a7c--list-config'
    }

class midiplayer:
    name = 'mcws midi模块'
    description = '在Minecraft中播放mid音乐'
    help = {
        '--play': '播放一个mid文件    \u00a7c--play <ID>',
        '--stop': '停止播放    \u00a7c--stop',
        '--playing': '显示正在播放的文件',
        '--loop': '设置播放模式    \u00a7c--loop <song|all>',
        '--list': '列出mid文件    \u00a7c--list [页码]',
        '--search': '搜索mid文件    \u00a7c--search <内容>',
        '--reload': '重新加载mid文件列表    \u00a7c--reload',
        '--from-url': '从互联网下载音乐进行播放    \u00a7c--from-url <URL>',
        '--keyboard': '设置是否显示键盘    \u00a7c--keyboard <0|1>',
        '--pan-by-pitch': '设置音高是否决定声音位置    \u00a7c--pan-by-pitch <0|1>'
    }
    info = '\u00a76mcws midi模块 \u00a7bby HYWT'
    midicount = "当前有 {0} 首 midi 音乐"
    stopping = "正在停止"
    stopped = '已停止'
    load_song = "正在加载 [\u00a7c{0}\u00a7r] - {1}... ({2})"
    reload = 'mid文件列表已重新加载'
    unknown_command = '未知命令。使用 .midi -h 查看可用命令列表。'
    keyboard_enable = '键盘显示: 开启'
    keyboard_disable = '键盘显示: 关闭'
    by_pitch_enable = '音高决定声音位置: 开启'
    by_pitch_disable = '音高决定声音位置: 关闭'
    playing = '正在播放: [\u00a7c{0}\u00a7r] - {1}'
