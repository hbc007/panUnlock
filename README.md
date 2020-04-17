# 使用方法

------

## 直接运行已编译的 windows 和 linux 的64位版本

| 文件名                     | 系统环境 | 使用的端口号 |
| -------------------------- | -------- | ------------ |
| `panunlock80_amd64.exe`    | windows  | 80           |
| `panunlock20415_amd64.exe` | windows  | 20415        |
| `panunlock80_amd64`        | linux    | 80           |
| `panunlock20415_amd64`     | linux    | 20415        |

* 在本机（默认 windows）运行（不支持安卓）

  1. 直接双击 `panunlock80_amd64.exe` (windows) 

  2. 在 `hosts文件` 末尾添加

     ```typescript
     127.0.0.1 pandownload.com
     ```

  3. 正常启动 `pandownload`

* 在服务器（默认 linux）运行（支持有root权限的安卓）

  1. 服务器上的配置

     * 如服务器已安装如 nginx、apache 之类的 httpd，建议使用 20415 端口版本的程序 `panunlock20415_amd64` 避免端口冲突，使用 httpd 创建域名为 `pandownload.com` 和 ` pandownw.linesoft.top` 的网站，并配置配置反向代理到 `http://127.0.0.1:20415` 。

     * 如 80 端口未被占用可使用 `panunlock80_amd64`

     * 使用 `screen`终端，或进程守护程序如 `supervisor` ，或配置成系统服务保证程序的持久运行。

     * （既然有服务器运维能力以上的详细配置不多说了，不懂的请多多百毒）

  2. （电脑）在 `hosts文件` 末尾添加

     ```typescript
     你的服务器IP pandownload.com
     ```

     （安卓）在 `/etc/hosts` 文件末尾添加

     ```
     你的服务器IP pandownw.linesoft.top
     ```

  3. 正常启动 `pandownload`

------

## 配置有 python3 环境的电脑可直接运行 `python panunlock.py` 

* 既然有编程能力无需多言详细的配置