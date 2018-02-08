# 注意事项
# 1. jsonify 最后用json.dumps序列化字典，并且设置json的header,但是遇到bson格式的数据这个方法会报错
# 建议自定义返回数据的方法
from bson.json_util import dumps


def get_json_response(app, **kws):
    """[summary]
    Arguments:
        app {[flask app]} -- [用来生成response对象]
        **kws {[dict]} -- [返回的data与message]
    
    Returns:
        [response] -- [response]
    """
    resp = app.make_response(
        dumps({
            "code": 0,
            "data": kws.get('data'),
            "message": kws.get("message")
        }))
    resp.headers['Content-Type'] = 'application/json'
    return resp
