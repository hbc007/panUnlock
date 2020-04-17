from flask import Flask, jsonify, render_template, send_file
import time
app = Flask(__name__)

# pandownw.linesoft.top


@app.route("/set/r/40")
def mobile():
    return jsonify({"stat": True, "message": "success", "code": 0, "data": {"notice": {"title": "LYHNMSL", "message": "What\'s your problem", "version": 23, "type": 1}, "stop": 0, "donate": True, "accelerate": {"type": 0, "min": 524288000, "max": 2147483648}}})

# pandownload.com


@app.route("/api/init")
def desktop_api_init():
    res = {"srecord": {"autoQuery": True}, "loginurl": {"url": "http:\/\/pandownload.com\/bdlogin.html"}, "wke": "http:\/\/dl.pandownload.club\/dl\/node-190312.dll", "pcscfg": {"appid": 250528, "ua": "", "ct": 0}, "flag": 1, "ad": {"url": "https:\/\/pandownload.com\/donate.html", "image": "http:\/\/pandownload.com\/images\/donate.png", "attribute": "width=\"88\" height=\"100\" padding=\"0,0,5,0\"", "rand": 100},
           "bdc": ["YlR4fWcffgt9A3N7fnxWQVJ0dXRQcXhhf1tFaGZbUVR8GWBja3pXW35zWnlkHlV9fXdiRm5BYGNmSHEdZlV8VmFaZ2pldFV9aFRGAmRkfXtSY3wdZlUCWGxKZ15\/fWhxYl5xZmNUcHZjH3dwfGF3D3t8dAxiZ3FyYmJ8CWNjd3djW3t8eXNeDGJncXJiYgwJY2N3cHxhdw97fHQMYmdxcmJiDAljY3dwfGF3D3t8dAxiZ3FyYmIMCWNjd3B8YXcPe3x0DGJncXJiYgwJY2N3cHxhdw97fHQMYmdxcmJiDAljY3dwfGF3D3t8dAxiZ3FyYmIMCWNjd3Bjd2dYa390A34ABGpRcHRTfUdzZmFxCnV4fAYHf1hgAn8NUR5oYXYDeXdmRncZYx9qZn1Zf1d0Vmtha1t5WlBBY1FeV35YVkR\/V2kcf3F6Bn5gd1V3Ynhba3ZhVH8NYx98HGZFeGBZVndBUR9+dltZf1AHBA=="], "timestamp": int(time.time()), "code": 0, "message": "success"}
    return jsonify(res)

# pandownload.com


@app.route("/dl/node-190312.dll")
def desktop_dl_node():
    return send_file("static/node-190312.dll")

# pandownload.com


@app.route("/api/script/list")
def desktop_api_script_list():
    res = {"scripts": [{"name": "search_pandown.lua", "remove": True}, {"name": "search_ncckl.lua", "remove": True}, {"name": "search_quzhuanpan.lua", "remove": True}, {"name": "anime_01.lua", "remove": True}, {"name": "anime_02.lua", "remove": True}, {"name": "anime_dilidili.lua", "remove": True}, {"name": "anime", "remove": True}, {"name": "s", "id": 2, "url": "http:\/\/pandownload.com\/static\/scripts\/s008",
                                                                                                                                                                                                                                                                                                                                                "md5": "8dfd9a6c08d06bec27ae358f315cca8f"}, {"name": "download_pcs.lua", "id": 1000, "url": "http:\/\/pandownload.com\/static\/scripts\/download_pcs.lua", "md5": "38770cd3e9bcd62f7212941b51ca1378"}, {"name": "default", "id": 0, "url": "http:\/\/pandownload.com\/static\/scripts\/default_0.6.7_3fee3733", "md5": "a1124f076924209d0322078000cdc882", "key": "568729a30cee34aec0e6fc7a6e303272"}], "code": 0, "message": "success"}
    return jsonify(res)

# pandownload.com


@app.route("/api/latest")
def desktop_api_latest():
    res = {"version": "2.2.2", "url": "https:\/\/dl1.cnponer.com\/files\/PanDownload_v2.2.2.zip", "web": "https:\/\/www.lanzous.com\/i8ua9na",
           "detail": "\u66f4\u65b0\u65f6\u95f4: 2020-01-24\n\u66f4\u65b0\u5185\u5bb9:\n1. \u754c\u9762\u4f18\u5316\n2. bug\u4fee\u590d", "md5": "13d3da755509afe3be8f7fc191a50cbd", "code": 0, "message": "success"}
    return jsonify(res)

# pandownload.com


@app.route("/bdlogin.html")
def bdlogin():
    return render_template("bdlogin.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 20415)
