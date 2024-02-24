SIXTEENHEX = "4e5154414a44545a" #一段16进制字符串 有什么用呢?
print(SIXTEENHEX)
import base64 #导入base64模块
bytes_data = bytes.fromhex(SIXTEENHEX)
#将16进制字符串转换为bytes
# base64_encoded_string = base64.b64encode(bytes_data).decode('utf-8')
#使用base64编码表示
#都提示到这里了 往下我也不知道了哦（〃｀ 3′〃）